#!/usr/bin/env python3

__author__ = "Matthew Carbone"
__maintainer__ = "Matthew Carbone"
__email__ = "x94carbone@gmail.com"
__status__ = "Prototype"


import os
import yaml
import sys
import subprocess

from paragon import core


class Initializer:
    """Initializes directories for unit testing.

    Attributes
    ----------
    default_path : str


    Notes
    -----
        See __init__ for details on attributes.

    """

    def __init__(self, default_path=os.getcwd()):
        """Initializes the Initializer class.

        Parameters
        ----------
        default_path : str
            Path to which testing directories and files will be saved, and
            later deleted. Default is the current working directory.

        """

        self.default_path = os.path.join(default_path, 'temp_testing')

    def initialize(self):
        """Uses os to make the directories used during unit testing.

        """

        try:
            os.makedirs(self.default_path)
        except FileExistsError:  # noqa
            self.delete()  # If the path exists, remove it
            self.initialize()  # Then re-initialize

    def delete(self):
        """Uses subprocess to make the directories used during unit testing.

        """

        subprocess.call('rm -r %s' % self.default_path, shell=True)


class TestCore(Initializer):
    """Controlled environment to run unit checks on classes and functions in
    paragon/core.py.

    """

    def __init__(self):
        """Initializes TestCore. Note that each of the TestCore classes should
        be initialized separately for each unit check. Inherits properties of
        the Initializer class so that unique environments may be created
        each time TestCore is called.

        Parameters
        ----------
        p : dict
            Pythonic dictionary of the parameters used during the test.
        path : str
            Absolute path to the desired parameter location.

        """

        super(TestCore, self).__init__()
        self.p = {
            'test_float': 9.12345,
            'test_int': 12345,
            'test_bool': True,
            'test_string': 'string_test',
            'test_list': ['I', 'Am', 'A', 'List']
        }
        self.initialize()

    def test_save_load(self):
        """Ensures that saving a parameter set works as intended."""

        p_set = core.SingleParameterSet(self.p, self.default_path)

        # Ensure the loaded parameters are equivalent to the saved ones
        extension = '.yml'
        name = 'parameters'
        p_set.save(extension=extension, name=name)
        _path = os.path.join(self.default_path, name + extension)
        with open(_path) as file:
            p_set_loaded = yaml.safe_load(file)
        for key, value in self.p.items():
            entry1 = self.p[key]
            entry2 = p_set_loaded[key]
            assert entry1 == entry2


if __name__ == '__main__':

    # Run checks
    TestCore(default_path=sys.argv[1]).test_save_load()

    print("hello world")
