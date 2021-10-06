"""
author : Ngô Văn Úc
date: 30/08/2021
program: 6. Add a command to this chapter’s case study program that allows the user to
view the contents of a file in the current working directory. When the command
is selected, the program should display a list of filenames and a prompt for the
name of the file to be viewed. Be sure to include error recovery.
solution:
    ...
"""

import os, os.path

menu = '''0. show this menu
1. show list of directory
2. move up
3. move down
4. getAdd
5. total number of file in a directory
6. total number of size in a directory
7. search name of file
8. show the text of a file in current working directory
9. exit'''

def main():
    request()

def request():
    number = (input("enter a number to choose a request: "))
    if number == "0":
        showmenu()
        line()
        main()
    elif number == "1":
        listsdir(os.getcwd())
        line()
        main()
    elif number == "2":
        moveup(os.getcwd())
        line()
        main()
    elif number == "3":
        movedown(os.getcwd())
        line()
        main()
    elif number == "4":
        addCWD()
        line()
        main()
    elif number == "5":
        print("total number of files: ", filesdir(os.getcwd()))
        line()
        main()
    elif number == "6":
        print("total number of size: ", filessize(os.getcwd()))
        line()
        main()
    elif number == "7":
        searchfile(os.getcwd())
        line()
        main()
    elif number == "8":
        showtext(os.getcwd())
        line()
        main()
    elif number == "9":
        pass
    else:
        print("les's enter a number around 0 and 9 to choose a request!")
        request()

def line():
    print("-" * 5)

def showmenu():
    "show the menu for users - 0"
    print(menu)

def listsdir(path):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(path)
    for element in lyst: print(element)

def moveup(path):
    "move up to parent directory - 2"
    os.chdir("..")
    print(os.getcwd())

def movedown(path):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(path + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")

def addCWD():
    "show address of CWD - 4"
    print("CWD: ", os.getcwd())

def filesdir(path):
    "count total files in a directory - 5"
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += filesdir(os.getcwd())
            os.chdir("..")
    return count

def filessize(path):
    "total size of directory - 6"
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += filessize(element)
            os.chdir("..")
    return count

def searchfile(path):
    "search a filename in a directory - 7"
    name = input("enter filename: ")
    lyst = os.listdir(path)
    if name in lyst:
        print(True)
    else:
        print("ERROR: no such filename")

def showtext(path):
    "print out the text of file in current working directory"
    name = input("enter a filename: ")
    lyst = os.listdir(path)
    if name in lyst:
        fr = open(name, "r")
        print(fr)
    else:
        print("ERROR: no such filename")

if __name__=="__main__":
    print(menu)
    main()

