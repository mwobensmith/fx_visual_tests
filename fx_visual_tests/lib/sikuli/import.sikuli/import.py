# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import sys
module_dir = os.path.join(os.getcwd(), "fx_visual_tests")
sys.path.append(module_dir)
from app import App

# This script runs in java/jython/Sikuli land,
# so we will just invoke our app from here

print "import.py: Starting from Sikuli"
App()
