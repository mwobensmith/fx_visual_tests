# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


# This class is used to wrap methods around the Sikuli API

from sikuli import *

class core(object):

    def __init__(self):
        self.meta = "core"


    def get_screen(self):
        return Sikuli.Screen


    def get_key(self):
        return Sikuli.Key


    def wait(self, pattern, timeout):
        return wait(pattern, timeout)


    def exists(self, pattern, timeout):
        return exists(pattern, timeout)


    def type(self, pattern=None, text=None, modifier=None):
        if pattern is None:
            if modifier is None:
                return type(text)
            else:
                return type(text, modifier)
        else:
            if modifier is None:
                if text is None:
                    return type(pattern)
                else:
                    return type(pattern, text)
            else:
                if text is None:
                    return type(pattern, modifier)
                else:
                    return type(pattern, text, modifier)


    def Key(self):
        return Key