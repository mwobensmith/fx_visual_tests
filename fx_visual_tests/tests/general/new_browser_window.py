
import os


from test_case import base_test


class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of a new browser window"


    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)


    def run(self):

        self.helpers.launch_firefox()
        fx_ui = self.make_pattern("1517869118302.png")
        self.core.wait(fx_ui, 10)
        self.helpers.new_tab()
        self.launch_ten_tabs()

        if self.core.exists(fx_ui, 5):
            print "PASS"
        else:
            print "FAIL"

        self.helpers.quit_firefox()

