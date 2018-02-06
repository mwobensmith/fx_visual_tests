# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import subprocess

class general(object):

    def __init__(self, core):
        self.core = core


    def do_something(self):
        return "I am a helper function: " + str (self.core.get_key())


    def launch_firefox(self, profile='empty_profile', url='about:blank'):
        # launch the app with optional args for profile, windows, URI, etc.
        current_dir = os.path.split(__file__)[0]
        active_profile = os.path.join(current_dir, "test_profiles", profile)
        cmd = ['/Applications/Firefox.app/Contents/MacOS/firefox', '-profile',
               active_profile, '-url', url, '-foreground',]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def clean_profiles(self):
        path = os.path.join (os.path.split(__file__)[0], "test_profiles")
        cmd = ['rm', '-rf', path]
        p = subprocess.Popen(cmd)


    def new_tab(self):
        self.core.type(text=self.core.Key().F2, modifier=self.core.Key().CTRL)
        self.core.type(text="File")
        self.core.type(text=self.core.Key().DOWN)
        self.core.type(text="t", modifier=self.core.Key().CMD)
        self.core.type(text=self.core.Key().UP)


    def restart_firefox(self, args):
        # just as it says, with options
        return


    def quit_firefox(self):
        # just as it says, with options
        self.core.type(text=self.core.Key().F2, modifier=self.core.Key().CTRL)
        self.core.type(text="Firefox")
        self.core.type(text="q", modifier=self.core.Key().CMD)
        return


    def navigate (self, uri, window):
        # general purpose function
        return
