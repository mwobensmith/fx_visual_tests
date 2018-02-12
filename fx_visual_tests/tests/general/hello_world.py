# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from test_case import *


class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.assets = os.path.join(os.path.split(__file__)[0], "assets")
        self.meta = "This is a test for hello world"


    def run (self):

        print ("hello_world.py: This is a test case")

        print "\nWe have various ways to create tests."

        print "We can access our own core classes and methods: "
        print "\t" + str(Key())
        print "\t" + str(exists)

        print "We can use our own helpers:"
        print "\t" + str(do_something())

        print "We can use high-level commands in our test case:"
        print "\t" + str(self.get_screen())

