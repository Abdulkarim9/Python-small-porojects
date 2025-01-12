import subprocess


# Getting profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
# Decoding data
data = data.decode("ISO-8859-1").split("\n")

# creating a list to store profiles
profiles = []

for profile in data:
    if "All User Profile" in profile:
        profile = profile.split(":")
        profile = profile[1]
        profile = profile[1:-1]
        profiles.append(profile)

profiles.pop(0)

# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print(f"{'Wi-Fi Name':<30}| {'Password':<}")
print("----------------------------------------------")
# print(profiles)
for profile in profiles:
    try:
        meta_data_password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = meta_data_password.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(profile, results[0]))

            # else it will print blank in front of pass word
        except IndexError:
            print("{:<30}| {:<}".format(profile, ""))

        # called when this process get failed
    except subprocess.CalledProcessError:
        print("Encoding Error Occurred")






