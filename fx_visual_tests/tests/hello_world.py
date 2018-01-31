# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


def run(app):
    print ("hello_world.py: This is a test case")
    print "\tCan access Sikuli classes: "
    print "\t" + str(app.get_screen())
