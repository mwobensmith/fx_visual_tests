# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from test_case import *



class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.assets = os.path.join(os.path.split(__file__)[0], "assets")
        self.meta = "This is a test of a new browser window"


    def run(self):

        # helper function
        launch_firefox(profile="new_window_test", url="about:blank")

        fx_ui = "1517869118302.png"

        # core api function
        wait(fx_ui, 10)

        # helper function
        new_tab()

        # custom high-level function
        self.launch_ten_tabs()

        # core api function
        if exists(fx_ui, 5):
            result = "PASS"
        else:
            result = "FAIL"

        # write the result to file
        resultMessage = self.meta + ':' + result
        append_results_file(resultMessage)

        # helper function
        quit_firefox()
