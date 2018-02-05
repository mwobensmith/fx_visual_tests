# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.



class general(object):

    def __init__(self, core):
        self.core = core


    def do_something(self):
        return "I am a helper function: " + str (self.core.get_key())


    def launch_firefox(self, args):
        # launch the app with optional args for profile, windows, URI, etc.
        return


    def restart_firefox(self, args):
        # just as it says, with options
        return


    def navigate (self, uri, window):
        # general purpose function
        return


