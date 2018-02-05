# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


# This class is used to wrap methods around the Sikuli API

class sikuli(object):

    def __init__(self, s):
        self.pattern = s['pattern']
        self.screen = s['screen']
        self.key = s['key']


    def get_screen(self):
        return self.screen


    def get_key(self):
        return self.key


    def wait(self, arg):
        return self.screen.wait(arg)

