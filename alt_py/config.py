import os
import platform


class Config(object):
    """Configuration with default values."""

    def __init__(self):
        if os.environ.has_key('ALT_NAME'):
            self.location_name = os.environ.get('ALT_NAME')
        else:
            self.location_name = platform.node()

        # The firebase host name. For example this could be: 'foo-baz.firebaseio.com'. The value of
        # the firebaseHost can be overriden by environment variable 'ALT_FIREBASE_HOST'. The default
        # value is 'alt-github.firebaseio.com'.
        if os.environ.has_key('ALT_FIREBASE_HOST'):
            self.firebase_host = os.environ.get('ALT_FIREBASE_HOST')
        else:
            self.firebase_host = 'alt-github.firebaseio.com'

        # The initial path to save everything. So for example, if the path is '/foobaz', the items
        # stored would be at 'foo-baz.firebase.io/foobaz'. The value of the firebasePath can be
        # overriden by the environment variable 'ALT_FIREBASE_PATH'. The default value is '/hosts'.
        if os.environ.has_key('ALT_FIREBASE_PATH'):
            self.firebase_path = os.environ.get('ALT_FIREBASE_PATH')
        else:
            self.firebase_path = '/test'

        # The file name to store data. This value can be overriden by the environment
        # variable 'ALT_FILENAME'. The default value is 'file.json'.
        if os.environ.has_key('ALT_FILENAME'):
            self.file_name = os.environ.get('ALT_FILENAME')
        else:
            self.file_name = 'file.json'

    def to_json(self):
        """to json"""
        pass

    def to_string(self):
        """to string"""
        pass
