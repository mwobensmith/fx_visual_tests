


class general(object):

    def __init__(self, core):
        self.core = core


    def do_something(self):
        print "I can access APIs:"
        print self.core.get_key()


    def launch_firefox(self, args):
        # launch the app with optional args for profile, windows, URI, etc.
        return


    def restart_firefox(self, args):
        # just as it says, with options
        return


    def navigate (self, uri, window):
        # general purpose function
        return


