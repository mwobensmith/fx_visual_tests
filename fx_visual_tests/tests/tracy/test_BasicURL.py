# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import os
from test_case import *
from api.helpers.awesome_bar import *


class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.meta = "This is a test of basic URL navigation via awesomebar"


    def run(self):

        # helper function from "general"
        launch_firefox(profile="new_profile")

        url = "www.google.com"
        # helper function from "awesome_bar"
        navigate(url)

        image = "1516891870986.png"

        # core api function
        if exists(image, 5):
            print "PASS"
        else:
            print "FAIL"

        # helper function from "general"
        quit_firefox()