# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.



class base_test(object):


    def __init__(self, app):
        self._app = app
        self.helpers = app.helpers
        self.core = app.core


    def run (self):
        # Empty for now
        return


    # Another possibility: wrap core and helper methods here
    def get_screen(self):
        s = self._app.core.get_screen()()
        return "This is a screen object: " + str(s)
