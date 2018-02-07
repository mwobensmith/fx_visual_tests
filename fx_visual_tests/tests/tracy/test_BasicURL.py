# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import os
from test_case import *

from api.helpers.awesome_bar import *


class test(base_test):
    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of basic URL navigation via awesomebar"

    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)

    def run(self):

        launch_firefox(profile="new_profile")

        url = "www.google.com"
        navigate(url)

        image = self.make_pattern("1516891870986.png")
        if exists(image, 5):
            print "PASS"
        else:
            print "FAIL"

        quit_firefox()