# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import os
import subprocess


# this is the main entry point defined in setup.py

def main(argv=None):
    print "main.py: main"

    # set up communication for headless mode
    os.environ["DISPLAY"] = ":99"

    # invoke the Sikuli jar in order to load a .sikuli package
    # which will in turn load our main app

    module_dir = os.path.split(__file__)[0]
    jar_path = os.path.join(module_dir, "lib/sikuli/sikuli-script.jar")
    init_path = os.path.join(module_dir, "lib/sikuli/import.sikuli")

    cmd = ['java', '-jar', jar_path, "-l", init_path]
    p = subprocess.Popen(cmd).communicate()
