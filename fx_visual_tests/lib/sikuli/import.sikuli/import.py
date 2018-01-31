# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
module_dir = os.path.join(os.getcwd(), "fx_visual_tests")
sys.path.append(module_dir)
from app import App

print "import.py: getting Sikuli classes"
# set up all Sikuli classes that we'd like to access
obj = {
    "screen": Screen,
    "key": Key,
    "pattern": Pattern
}

# pass them to our app
a = App(obj)


