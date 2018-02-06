# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from api.helpers.general import *

# Temporarily hard-coded for just a few tests
from tests.general import hello_world, new_browser_window
from tests.tracy import test_BasicURL, test_BackForward


# The test runner will be written so that it can iterate through the "tests"
# directory and dynamically import what it finds.
#
# Additionally, we can create a file that can exclude tests from running,
# and/or create logic to only run certain tests.

def run(app):
    print "test_runner.py: Running tests"

    # start with no saved profiles
    clean_profiles()

    # then we'd dynamically call test() and run on this list of test cases
    hello_world.test(app).run()
    new_browser_window.test(app).run()
    test_BasicURL.test(app).run()
    test_BackForward.test(app).run()

    clean_profiles()