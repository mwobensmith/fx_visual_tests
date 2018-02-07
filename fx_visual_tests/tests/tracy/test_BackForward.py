# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from api.helpers.awesome_bar import *
from test_case import *



class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.meta = "This is a test of browser back/forward"


    def run(self):

        # helper function from "general"
        launch_firefox(profile="back_forward")

        url = "about:home"
        # helper function from "awesome_bar"
        navigate(url)

        if exists("1517515751124.png", 5):
            url = "www.google.com"

            # helper function from "awesome_bar"
            navigate(url)

            # core api function
            if exists("1516891870986-1.png", 2):

                # helper function from "awesome_bar"
                back_in_history()

                # core api function
                if exists("1517515751124.png", 2):

                    # helper function from "awesome_bar"
                    forward_in_history()

                    # core api function
                    if exists("1516891870986-1.png", 2):
                        print "PASS"
                    else:
                        print "FAIL"
                else:
                    print "FAIL"
            else:
                print "FAIL"
        else:
            print "FAIL"

        # helper function from "general"
        quit_firefox()
