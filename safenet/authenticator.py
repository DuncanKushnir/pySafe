########################################################################################################################
#
# pySafe - Authenticator
#
# This file encapsulates the interface for the authenticator library.
#
# The authenticator is a critical component of any app, and is required for many tasks. Later, it may be a design
# decision access this through another abstraction (e.g. session or connection)
#
# The implementations for the various functions should be the last place in the library you will see ffi.
#  Higher level abstractions should be able to use the public methods with pure python objects
#
########################################################################################################################

import safenet.base_classes as base
import getpass
import queue

class Authenticator(base.FullAuthenticator):
    '''
    A python interface to the SAFE authenticator object
    At present, introspection fails because of the auto-binding.  For further reference on methods:
    https://github.com/maidsafe/safe_client_libs/wiki
    safenet/safe_auth_defs.py
    '''

    def __init__(self):
        self.is_setup=False
        self.queue = queue.Queue()  # Each object has it's own queue for ffi calls
        self._setup()

    def _setup(self):
        '''
        Does the basic priming of the authenticator and libraries.  Really only needs be done once per connection
        session
        '''
        self.bind_ffi_methods()
        self.auth_set_additional_search_path(self.global_config.GLOBAL_BINPATH, None)
        self.auth_exe_file_stem(None, None)
        self.is_setup=True

    # Public methods of this class override the auto bound ffi methods and are generally necessary where simple
    # string and null pointer conversion of python objects are not sufficient.  Default functionality is equivalent to:
    #  def login(self, secret, password, userdata=None, o_cb=None):
    #     self._login(*self.ensure_correct_form(secret, password, userdata, self.login_cb))
    # A full listing of the class methods automatically bound can be found in safe_auth_defs.py



    # Callback methods

    @staticmethod
    def login_cb(result):
        print('login result', result)


# now there is only one
#Authenticator=Authenticator()

if __name__ == '__main__':
    A = Authenticator()

    def printfilestem(one,two,stem):
        print(A.ffi_auth.string(stem))
    # Note again that these methods were never defined, and can be called with regular strings and python objects:)
    A.login('secret','password', None, None)
