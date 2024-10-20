import os

def list_contents(folder_path):
    # List all items in the specified folder
    items = os.listdir(folder_path)
    
    # Print each item (files and directories)
    for item in items:
        print(item)

# Replace 'your_folder_path' with the path of the folder you want to check
folder_path = r"C:\Users\Asmir Alam\Desktop\Python Courses\Python Tutorial For Beginners in Hindi"
list_contents(folder_path)
