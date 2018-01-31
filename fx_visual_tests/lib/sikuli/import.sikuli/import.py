# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import sys
module_dir = os.path.join(os.getcwd(), "fx_visual_tests")
sys.path.append(module_dir)
from app import App

# This script runs in java/jython/Sikuli land, so it
# already has the Sikuli classes imported

# We will create an object to hold all Sikuli classes
# that we'd like to access in our project

print "import.py: Getting Sikuli classes"
obj = {
    # TBD: add more Sikuli classes and methods
    "screen": Screen,
    "key": Key,
    "pattern": Pattern
}

# pass it to our app
a = App(obj)
