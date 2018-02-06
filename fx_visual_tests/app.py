# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from api.core import core
from api.helpers.general import general

import test_runner

class App(object):

    def __init__(self):
        print "app.py: This is our main app"

        # First we will create the core API,
        # on which our project is built

        self.core = core()

        # Helpers will be a library of commonly-used methods that
        # are written on top of our core API.
        # Eventually we'll have more categories of helpers outside
        # of just one ("general").

        self.helpers = general(self.core)


        test_runner.run(self)

