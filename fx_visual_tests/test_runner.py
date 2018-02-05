# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from tests import hello_world

# can we iterate through the file system and dynamically import?
# can we save a list of those imported files?

def run(app):
    print "test_runner.py: Running tests"
    # then we'd dynamically call test() and run on this list of test cases
    hello_world.test(app).run()
    # obj = hello_world(app).run()