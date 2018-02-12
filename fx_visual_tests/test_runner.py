# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from api.helpers.general import *

# Temporarily hard-coded for just a few tests
from tests.general import hello_world, new_browser_window, empty
from tests.tracy import test_BasicURL, test_BackForward
from api.helpers.results import  *



# The test runner will be written so that it can iterate through the "tests"
# directory and dynamically import what it finds.
#
# Additionally, we can create a file that can exclude tests from running,
# and/or create logic to only run certain tests.

def run(app):
    print "test_runner.py: Running tests"
    # let's print results to file, this line calls begins that .txt file
    begin_results_file()

    # start with no saved profiles
    clean_profiles()

    # then we'd dynamically call test() and run on this list of test cases
    #hello_world.test(app).run()
    #new_browser_window.test(app).run()
    test_BasicURL.test(app).run()
    test_BackForward.test(app).run()
    #empty.test(app).run()

    clean_profiles()

    # this line finishes use of the results text file
    conclude_results_file()
