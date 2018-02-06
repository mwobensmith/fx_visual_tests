import helperAwesomebar
import os

from test_case import base_test


class test(base_test):
    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of basic URL navigation via awesomebar"

    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)

    def run(self):

        self.helpers.launch_firefox(profile="new_profile")

        url = "www.google.com"
        helperAwesomebar.navigate(url)

        image = self.make_pattern("1516891870986.png")
        if self.core.exists(image, 5):
            print "PASS"
        else:
            print "FAIL"

        self.helpers.quit_firefox()