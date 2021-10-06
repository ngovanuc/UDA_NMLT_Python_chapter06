"""
author : Ngô Văn Úc
date: 30/08/2021
program: Gathering Information from a File System
solution:
    ...
"""

import os, os.path

menu = """0. show this menu
1. list the current working directory
2. move up
3. move down
4. total number of size in a directory
5. total number of files in a directory
6. search a filename
7. quit the program"""

def main():
    print(os.getcwd())
    print(menu)
    while True:
        number = request()
        if number == 7:
            break
        else:
            print(os.getcwd())
            compare(number)
def request():
    answer = int(input("enter your number: "))
    if answer >= 0 and answer <= 7:
        return answer
    else:
        print("error: number must be between 1 and 7")
        return request()

def compare(request):
    if request == 1:
        # list the files in directory
        listfilecwd(os.getcwd())
    elif request == 0:
        print(menu)
    elif request == 2:
        # move up to the directory
        moveupdir()
    elif request == 3:
        # move down to the directory
        movedowndir(os.getcwd())
    elif request == 4:
        # total number of file in a directory
        print(totalfiledir(os.getcwd()))
    elif request == 5:
        # total number of size in a directory
        print(totalsizedir(os.getcwd()))
    elif request == 6:
        # search a filename
        searchname(os.getcwd())
    else:
        pass
def listfilecwd(path):
    lists = os.listdir(path)
    for element in lists: print(element)

def moveupdir():
    "move up to the directory"
    os.chdir("..") # move up to the parent directory
    print(os.getcwd())

def movedowndir(currentcwd):
    "move down to the directory"
    print("choose a file or directory to move down.")
    print(os.listdir(os.getcwd()))
    newdir = input("enter the name new directory to move down: ")
    if os.path.exists(currentcwd + os.sep + newdir) and os.path.isdir(newdir):
        os.chdir(newdir)
        print("currentcwd is: ", os.getcwd())
    else:
        print("error: no such the name of directory")

def totalfiledir(path):
    print("the number of file in this directory is: ", end='')
    lists = os.listdir(path)
    count = 0
    for element in lists:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += totalfiledir(os.getcwd())
            os.chdir("..") # comeback to the current directory
    return count

def totalsizedir(path):
    print("the total number of bytes size in this directory is: ", end='')
    lists = os.listdir(path)
    sum = 0
    for element in lists:
        if os.path.isfile(element):
            sum += os.path.getsize(element)
        else:
            os.chdir(element)
            sum += totalfiledir(os.getcwd())
            os.chdir("..")
    return sum

def searchname(path):
    pass

if __name__ == "__main__":
    main()
