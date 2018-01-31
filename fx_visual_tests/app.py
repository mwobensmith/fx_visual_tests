# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import test_runner

class App(object):

    def __init__(self,sikuli):
        print "app.py: This is our main app"
        self._screen = sikuli["screen"]
        self._key = sikuli["key"]
        self._pattern = sikuli["pattern"]
        test_runner.run(self)

    # We can create friendly wrapper methods around Sikuli
    def get_screen(self):
        return self._screen