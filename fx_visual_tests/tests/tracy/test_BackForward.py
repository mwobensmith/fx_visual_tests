# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from api.helpers.awesome_bar import *
from test_case import *
import os



class test(base_test):
    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of browser back/forward"

    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)

    def run(self):

        # helper function
        launch_firefox(profile="back_forward")

        url = "about:home"
        navigate(url)

        if exists(self.make_pattern("1517515751124.png"), 5):
            url = "www.google.com"
            navigate(url)
            if exists(self.make_pattern("1516891870986-1.png"), 2):
                back_in_history()
                if exists(self.make_pattern("1517515751124.png"), 2):
                    forward_in_history()
                    if exists(self.make_pattern("1516891870986-1.png"), 2):
                        print "PASS"
                    else:
                        print "FAIL"
                else:
                    print "FAIL"
            else:
                print "FAIL"
        else:
            print "FAIL"

        # helper function
        quit_firefox()
