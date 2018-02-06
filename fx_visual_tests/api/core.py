# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


# This class is used to wrap methods around the Sikuli API

from sikuli import *


def get_screen():
    return Sikuli.Screen


def get_key():
    return Sikuli.Key


def wait(pattern, timeout):
    return Sikuli.Screen().wait(pattern, timeout)


def exists(pattern, timeout):
    return Sikuli.Screen().exists(pattern, timeout)


def click(pattern):
    return Sikuli.Screen().click(pattern)


def type(pattern=None, text=None, modifier=None):
    if pattern is None:
        if modifier is None:
            return Sikuli.Screen().type(text)
        else:
            return Sikuli.Screen().type(text, modifier)
    else:
        if modifier is None:
            if text is None:
                return Sikuli.Screen().type(pattern)
            else:
                return Sikuli.Screen().type(pattern, text)
        else:
            if text is None:
                return Sikuli.Screen().type(pattern, modifier)
            else:
                return Sikuli.Screen().type(pattern, text, modifier)


def Key():
    return Sikuli.Key()


def Pattern(path):
    return Sikuli.Pattern(path)

def Screen():
    return Sikuli.Screen()