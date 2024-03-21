import time
import random
import sys
import os
import platform

def is_file_empty(filename):
    try:
        return os.path.exists(filename) and os.stat(filename).st_size == 0
    except FileNotFoundError:
        return False


def create_file(filename):
    try:
        with open(filename, 'x'):
            print()
    except FileExistsError:
        print()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print()

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    
def remove_single_quotes(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Remove single quotes from the content
    new_content = content.replace("'", "")

    with open(filename, 'w') as file:
        file.write(new_content)

def register():
    print("Welcome to npcldOS!")
    print("Please Create a account")
    name = input("Username: ")
    passw = input("Password: ")
    namefile = "name.txt"
    passfile = "password.txt"
    create_file(namefile)
    create_file(passfile)
    write_to_file(namefile, f"'{name}'")
    write_to_file(passfile, f"'{passw}'")
    remove_single_quotes(namefile)
    remove_single_quotes(passfile)
    login()

def login():
    namefile = "name.txt"
    passfile = "password.txt"
    with open(namefile, 'r') as file:
        name = file.read()
    print("Hello", name)
    pw = input("Please type password: ")
    content = read_file(passfile)
    if content == pw:
        osstart()
    else:
        print("Incorrect password. Please try again")
        login()

def osstart():
    print("Welcome to npcldOS!")
    print(f"  Operating System: npcldOS 2.0")
    print(f"  Processor: {platform.processor()}")
    print(f"  Machine: {platform.machine()}")
    cmdd()

def cmdd():
    cmd = input("> ")
    if cmd.startswith("dir "):
            directory = cmd[4:]
            try:
                dir_list = os.listdir(directory)
                for item in dir_list:
                    print(item)
                cmdd()
            except OSError as e:
                print(f"Error listing directory '{directory}': {e}")
                cmdd()
    elif cmd.startswith("exit"):
        print("")
    elif cmd.startswith("read "):
        file_path = cmd[5:]
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                print(file.read())
        else:
            print(f"Error listing directory '{file_path}'")
            cmdd()
    elif cmd.startswith("create "):
        file_path = cmd[5:]
        try:
            with open(file_path, 'x'):
                print(f'Created {file_path} file')
        except FileExistsError:
            print("File Already Exist")
        cmdd()
    else:
        print("Command not recognized. Type help to look at the list of commands")
        cmdd()

def welcome():
    print("Welcome to npcldOS!")
    register()

def systemdownload():
    directorysys = input()
    if directorysys == "C:":
        download()
    elif directorysys == "D:":
        download()
    else:
        print("Error. Wrong directory")
        systemdownload()

def download():
    for i in range(101):
        print(f"\rCopying System Files... {i}%", end="")
        time.sleep(random.uniform(0.1,0.2))
    print("")
    for i in range(101):
        print(f"\rPasting System Files... {i}%", end="")
        time.sleep(random.uniform(0.1,0.2))
    register()

def osstart():
    print("Welcome to npcldOS!")
    print(f"  Operating System: npcldOS 1.0")
    print(f"  Processor: {platform.processor()}")
    print(f"  Machine: {platform.machine()}")
    cmdd()


if is_file_empty("name.txt") and is_file_empty("password.txt"):
    welcome()
else:
    login()
