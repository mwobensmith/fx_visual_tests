import helperAwesomebar
from test_case import *
import os



class test(base_test):
    def __init__(self, app):
        base_test.__init__(self, app)
        self.meta = "This is a test of browser back/forward"

    def make_pattern(self, file_name):
        current_dir = os.path.split(__file__)[0]
        return os.path.join(current_dir, "images", file_name)

    def run(self):

        # helper function
        launch_firefox(profile="back_forward")

        url = "about:home"
        helperAwesomebar.navigate(url)

        if exists(self.make_pattern("1517515751124.png"), 5):
            url = "www.google.com"
            helperAwesomebar.navigate(url)
            if exists(self.make_pattern("1516891870986-1.png"), 2):
                helperAwesomebar.back_in_history()
                if exists(self.make_pattern("1517515751124.png"), 2):
                    helperAwesomebar.forward_in_history()
                    if exists(self.make_pattern("1516891870986-1.png"), 2):
                        print "PASS"
                    else:
                        print "FAIL"
                else:
                    print "FAIL"
            else:
                print "FAIL"
        else:
            print "FAIL"

        # helper function
        quit_firefox()
