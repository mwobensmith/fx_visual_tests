# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import os
import struct
import subprocess
import sys


# this is the main entry point defined in setup.py

def main(argv=None):
    print "main.py: main"

    # set up communication for headless mode
    os.environ["DISPLAY"] = ":99"

    module_dir = os.path.split(__file__)[0]

    # if Windows, set environment variable for path
    # TODO: fix, not working
    # if detect_platform().startswith("win"):
    #    libs_path = os.path.join(module_dir, "lib\sikuli\libs")
    #    path_cmd = ['set', 'PATH=%PATH%;' + libs_path]
    #    p = subprocess.Popen(path_cmd).communicate()

    # invoke the Sikuli jar in order to load a .sikuli package
    # which will in turn load our main app
    jar_path = os.path.join(module_dir, "lib/sikuli/sikuli-script.jar")
    init_path = os.path.join(module_dir, "lib/sikuli/import.sikuli")

    cmd = ['java', '-jar', jar_path, "-l", init_path]
    p = subprocess.Popen(cmd).communicate()



def detect_platform():
    is_64bit = struct.calcsize('P') * 8 == 64
    platform = None
    if sys.platform.startswith("darwin"):
        platform = "osx"
    elif sys.platform.startswith("linux"):
        platform = "linux" if is_64bit else "linux32"
    elif sys.platform.startswith("win"):
        platform = "win" if is_64bit else "win32"
    return platform