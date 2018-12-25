"""
This module is used to maintain global settings. 
"""

import json
import os


class Setting(object):
    """
    This Class maintains global settings. The Class uses singleton design.

    >>> x = Setting("settings.json")
    >>> x.val = 'sausage'
    >>> y = Setting("settings.json")
    >>> y.val = 'eggs'
    >>> z = Setting("settings.json")
    >>> z.val = 'spam'
    >>> z.val == x.val == z.val
    True
    """
    class __Setting:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + self.val
    instance = None

    def __init__(self, setting_file):
        """
        This function initialize the class. If there is no instance, we generate a instance using setting file path
        else if the setting file path is same as current instance we do nothing, else we raise error.

        Args:
            setting_file:
        """
        if not Setting.instance:
            Setting.__setting_file_path = os.path.abspath(setting_file)
            Setting.instance = Setting.__Setting()
        else:
            if os.path.abspath(setting_file) != Setting.__setting_file_path:
                raise Exception("Setting file name error")

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()