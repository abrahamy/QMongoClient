__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

buildOptions = dict(
    includes = ["atexit",],
    compressed = True
    #icon = ":/Images/icon.png" pls import ui.resources_rc first!
)

setup(
        name = "QMongoClient",
        version = "0.1",
        description = "A simple GUI client to the mongodb database which copies most of its UI appearance from MongoVUE.",
        options = dict(build_exe=buildOptions),
        executables = [Executable("main.py", base = base)])
