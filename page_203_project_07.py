"""
author : Ngô Văn Úc
date: 30/08/2021
program: 7. Write a recursive function that expects a pathname as an argument. The pathname can be either the name
of a file or the name of a directory. If the pathname
refers to a file, its name is displayed, followed by its contents. Otherwise, if the
pathname refers to a directory, the function is applied to each name in the directory.
Test this function in a new program.
solution:
    ...
"""

import os, os.path

def main():
    print("enter double point (..) to move up directory")
    print("enter 'quit' to exit")
    refers(os.getcwd())

def refers(path):
    print(path)
    name = input("enter name to open file/directory: ")
    if os.path.exists(name) and name != "..":
        if os.path.isfile(name):
            if name.endswith(".txt"):
                fr = open(name, "r")
                for lines in fr:
                    print(lines)
                refers(os.getcwd())
            else:
                print("this file not endswith .txt")
                refers(os.getcwd())
        else:
            os.chdir(name)
            lyst = os.listdir(os.getcwd())
            for element in lyst:
                print(element)
            refers(os.getcwd())
    elif name == "..":
        os.chdir("..")
        refers(os.getcwd())
    elif name == "quit":
        pass
    else:
        print("ERROR: no such file or directory")
        refers(os.getcwd())

if __name__ == "__main__":
    main()

