# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from api.core import *
from api.helpers.general import *
import os


class base_test(object):

    def __init__(self, app):
        self._app = app
        self.isolate = True


    def set_image_path(self, path):
        add_image_path(os.path.join(path, "images", self._app.os))


    def setup (self):
        """
        this might be a good place to declare variables or clean up Fx state
        """
        return


    def run (self):
        """
        This is your test logic
        """
        return


    def teardown(self):
        """
        this might be a good place to close windows and clean up what was done
        """
        return


    # One possibility: wrap core and helper methods here as well
    # This might be things that directly apply to test cases, like
    # restoring app state or restoring Fx state

    def close_all_windows(self):
        """
        Get rid of all stray windows generated from a test case
        """
        return


    def remove_all_bookmarks(self):
        """
        Get rid of all bookmarks generated from a test case
        """
        return


    # Just some useless examples of class methods
    def launch_ten_tabs(self):
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()


    def get_screen(self):
        s = Screen()
        return "This is a screen object: " + str(s)
