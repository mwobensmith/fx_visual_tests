# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from test_case import *
import os



class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.meta = "This is a test of a new browser window"


    def run(self):

        # helper function
        launch_firefox()

        fx_ui = "1517869118302.png"

        # core api function
        wait(fx_ui, 10)

        # helper function
        new_tab()

        # custom high-level function
        self.launch_ten_tabs()

        # core api function
        if exists(fx_ui, 5):
            print "PASS"
        else:
            print "FAIL"

        # helper function
        quit_firefox()

