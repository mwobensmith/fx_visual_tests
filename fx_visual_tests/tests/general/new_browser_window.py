# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.



from test_case import *

import os



class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of a new browser window"


    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)


    def run(self):

        # helper function
        launch_firefox()

        # custom function to construct the correct image path
        fx_ui = self.make_pattern("1517869118302.png")

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

