import os

def file_name():
    """Get the name of the file to be executed"""
    return "command.wav"

def file_exists(file_name):
    """Check if the file exists"""
    return os.path.exists(file_name)

def delete_file(file_name):
    """Delete the file"""
    if file_exists(file_name):
        os.remove(file_name)
        print(f"{file_name} deleted to avoid re-triggering.")
    else:
        print(f"Error: File '{file_name}' not found.")