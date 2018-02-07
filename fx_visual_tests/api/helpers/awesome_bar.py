# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from api.core import *
from general import *

import os


def make_pattern(file_name):
    current_dir = os.path.split(__file__)[0]
    return Pattern(os.path.join(current_dir, "images", file_name))

def navigate(url):
    wait(make_pattern("1516888289228.png"), 10)
    type((make_pattern("1516888289228.png").targetOffset(221, 0)), url + Key.ENTER)
    return


def back_in_history():
    wait(make_pattern("1517514241697.png"), 5)
    click(make_pattern("1517514241697.png"))
    return


def forward_in_history():
    wait(make_pattern("1517514418304.png"), 5)
    click(make_pattern("1517514418304.png"))
    return