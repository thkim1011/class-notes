#!/bin/python3
"""
My notes generation system! The idea is that when the semester
starts, I call `notes init` in whatever directory I'm using
for the class e.g. math202a or cs270. This will prompt me for
when the class meets (e.g. TTh, MW, MWT, etc), the first day
of class, and last day of class. This is sufficient for generating
on `lecxx.tex` file for each lecture and the directory structure 
somewhat as described in the init() function.

Some other ideas I have for this is for it to sync with my 
google drive, and my personal website which runs on flask.
The idea is that calling `notes upload` will upload each file
to my google drive and also create a json file which maps
each file `lecxx` to the link to the google drive. Having this
json file allows me to easily create a <ul> within my 
jinja-based website. 

Most of these docstrings are very rough ideas of how the project 
should be, so that I have a better idea of what I'm doing 
before I program this. 
"""

import sys
import os
from collections import OrderedDict

VERSION = 0.1

def init():
    """
    Initializes a new set of notes for a class.
    The directory structure which is currently planned
    is the following:
    |-notes
        |-lec01.tex
        |-lec02.tex
        |-...
        |-lec32.tex (e.g.)
    |-outputs
        |-lec01.pdf
        |-lec02.pdf
        |-notes.pdf
    |-.notes
        |-lectures.json
        |-0.tex
        |-1.tex
        |-...
        |-notes.tex
    The .notes folder contains a JSON file which keeps a list of 
    each of the dates. Each of the x.tex file within `.notes`
    has a structure roughly 

        \setcounter to lecture number
        \section{DATE} 
        \input{../notes/lecx.tex}`.

    The reason for this is to make it easy to modify the DATE. The 
    file notes.tex should simply coalesce all of these somehow. 

    Should be called when `python3 notes.py init` or `notes init` 
    is run.
    """
    if os.path.exists("./.notes"):
        print("Notes already exist in this project!")
        return
    os.mkdir('.notes')

def import_notes():
    """
    Imports a set of already written notes
    """
    if os.path.exists("./.notes"):
        print("Notes already exist in this project!")
        return
    os.mkdir('.notes')

def modify():
    """
    Modify the current structure e.g. remove a certain date
    for a lecture and refractor.

    Should be called when `python3 notes.py modify` or `notes modify`
    is run. 
    """

def make():
    """
    Makes all outputs. 
    """
    pass

def upload():
    """
    Uploads the compiled notes to google drive. Requires
    Drive Python3 API. (I think it's called REST? Ideally,
    I want this project finished before next semester starts.) 
    """
    pass

def help():
    """
    Prints out the help text. 
    """
    version()
    print("USAGE: python3 notes.py [COMMAND]")
    print("COMMAND:")
    help_dict = {
        "help": "Prints out the help text.",
        "version": "Prints out the version.",
        "init": "Initializes a new set of notes.",
        "modify": "Modify the current set of notes.",
    }
    help_dict = OrderedDict(sorted(help_dict.items()))
    for entry in help_dict:
        print(("  " + entry).ljust(10), help_dict[entry])

def version():
    print("class-notes v{0}".format(VERSION))

def main():
    """
    Main function for the module. The module has three
    primary functions.
    """
    if len(sys.argv) == 1:
        help()
    elif len(sys.argv) > 2:
        help()
    elif sys.argv[1] == "version":
        version()
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "init":
        init()
    elif sys.argv[1] == "modify":
        pass
    elif sys.argv[1] == "upload":
        pass

if __name__ == "__main__":
    main()
