import os


directory = "Directory_name"

file_extensions = ['.jpg', '.png', '.jpeg']

# Get a list of all image files in the directory with the allowed extensions
files = [f for f in os.listdir(directory) if f.endswith(tuple(file_extensions))]

# Rename each file with a new name that includes the index and file extension
for i, old_name in enumerate(files):
    # Split the file name and extension
    file_name, file_extension = os.path.splitext(old_name)
    
    new_name = f"photo{i+1:02d}{file_extension}"
    
    os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))


print("Files renamed successfully")
