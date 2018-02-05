import os
import sys
module_dir = os.path.join(os.getcwd(), "fx_visual_tests")
sys.path.append(module_dir)


class base_test(object):


    def __init__(self, app):
        self._app = app
        self.helpers = app.helpers
        self.core = app.core


    def run (self):
        # Empty for now
        return


    # Another possibility: wrap core methods here
    def get_screen(self):
        return self._app.core.get_screen()
