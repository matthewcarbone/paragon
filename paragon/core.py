#!/usr/bin/env python3

__author__ = "Matthew Carbone"
__maintainer__ = "Matthew Carbone"
__email__ = "x94carbone@gmail.com"
__status__ = "Prototype"

import yaml
import os


class SingleParameterSet:
    """Core class for the module. Parameters for some single run, meaning a job
    to be run on one core, or perhaps one machine on multiple cores. In
    general, these jobs (meaning these classes) will be assigned a unique hash.
    A map between hashes and parameters is generated at a higher depth level.
    Note that this class may be considered the lowest depth level, meaning
    there will be no more sub-directories saved in directories containing
    information from this class.

    Attributes
    ----------
    p : dict
    path : str

    Notes
    -----
        See __init__ for details on attributes.

    """

    def __init__(self, p, path):
        """Initialize the SingleParameterSet class.

        Parameters
        ----------
        p : dict
            Pythonic dictionary containing the parameters to save to the path.
            Note that at this level each dictionary key should correspond to
            a single value (this value can be a list as long as the list is
            the 'single' parameter to be passed to the current run).
        path : str
            Absolute path to desired parameter location. Note that the path
            should point to the directory location, not specify the absolute
            path of the file + extension, which will be added during saving.

        """

        self.p = p
        self.path = path

    def save(self, extension='.yml', name='parameters'):
        """Saves the parameter file into the path using the indicated
        extension.

        Parameters
        ----------
        extension : {'.yml'}
            The protocol used to save the parameter file to the path. Default
            (and recommended format) is '.yml'.

        name : str
            Name of the parameter file to be saved. Default is 'parameters'.

        Raises
        ------
        RuntimeError
            If extension is not allowed.

        """

        if extension == '.yml':
            _path = os.path.join(self.path, name + extension)
            with open(_path, 'w') as outfile:
                yaml.dump(self.p, outfile)
        else:
            raise RuntimeError(
                "Unsupported extension %s for saving parameters." % extension)

