# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

# Temporarily hard-coded for just one test
from tests.general import hello_world


# The test runner will be written so that it can iterate through the "tests"
# directory and dynamically import what it finds.
#
# Additionally, we can create a file that can exclude tests from running,
# and/or create logic to only run certain tests.

def run(app):
    print "test_runner.py: Running tests"
    # then we'd dynamically call test() and run on this list of test cases
    hello_world.test(app).run()
