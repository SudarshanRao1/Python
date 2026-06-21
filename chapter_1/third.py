import os

# Specify the directory path (use '.' for current directory)
directory_path = "/" 

# Get the list of contents
contents = os.listdir(directory_path)

# Print each item
for item in contents:
    print(item)   