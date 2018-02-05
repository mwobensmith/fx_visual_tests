# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from sikuli import *


from test_case import base_test


class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test for hello world"


    def run (self):

        print ("hello_world.py: This is a test case")

        print "\nWe have various ways to create tests."

        print "We can access our own core classes: "
        print "\t" + str(self.core.get_screen())

        print "We can use our own helpers:"
        print "\t" + str(self.helpers.do_something())

        print "We can use high-level commands in our test case:"
        print "\t" + str(self.get_screen())

        print "We can even access Sikuli classes directly:"
        p = Pattern("foo")
        print "\tThis is a Pattern object: " + str(p)
