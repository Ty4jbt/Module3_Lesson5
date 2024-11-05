# Task 1
# Objective: Create a Python script that lists all files and subdirectories in a directory. Your script should prompt the user for the directory path and the display its contents.

import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories
        entries = os.listdir(path)
        
        # States the directory path in a user-friendly way
        print(f"\nContents of directory '{path}':")
        print("-----------------------------")
        
        # Separate files and directories
        files = []
        directories = []
        
        # Loop through each item in the directory
        for entry in entries:

            # Get the full path of the entry and the item in the directory
            full_path = os.path.join(path, entry)

            # Check if the entry is a file or a directory and append it to the appropriate list
            if os.path.isfile(full_path):
                files.append(entry)
            elif os.path.isdir(full_path):
                directories.append(entry)
        
        # Print directories
        if directories:
            print("\nDirectories:")
            for directory in directories:
                print(f"  - {directory}")
        else:
            print("\nNo subdirectories found.")
        
        # Print files
        if files:
            print("\nFiles:")
            for file in files:
                print(f"  - {file}")
        else:
            print("\nNo files found.")
    
    # Handle exceptions
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except IOError:
        print(f"Error: An I/O error occurred while accessing '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for directory path
user_path = input("Enter the directory path: ")

# Call the function with the user-provided path
list_directory_contents(user_path)