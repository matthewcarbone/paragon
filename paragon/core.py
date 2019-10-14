#!/usr/bin/env python3

__author__ = "Matthew Carbone"
__maintainer__ = "Matthew Carbone"
__email__ = "x94carbone@gmail.com"
__status__ = "Prototype"

import yaml
import os
import itertools


class GroupParameterSet:
    """Contains a set of SingleParameterSet classes. A set of lists are input
    to this class as various sets of parameters to be iterated over. Each
    combination constitutes a SingleParameterSet.

    Attributes
    ----------
    d: dict
    run_path : str

    Notes
    -----
        See __init__ for details on attributes.

    """

    def __init__(self, d, run_path):
        """Initializes the GroupParameterSet class. Each possible permutation
        of the parameter space is assigned a unique hash which can be cross
        referenced to the precise directory by a master parameter list.

        Parameters
        ----------
        d : dict
            Pythonic dictionary in the following form

            d = {
                'property_1' : [value_1, value_2, value_3, ..., value_N],
                'property_2' : [value_1', value_2', value_3', ..., value_M'],
                ...
            }

            The dictionary is structured as follows. Each key's value is a list
            of possible values for parameters corresponding to the key. The
            class settings determine whether or not a subset of the total
            parameter space is sampled, all permutations are sampled, or if
            the lists are meant to be read in a 1-1 correspondence (e.g.,
            value_1 corresponds to value_1', value_1'', value_1''', etc).

        run_path : str
            Absolute path pointing to where all data for this group of runs
            will be saved.

        >>> keys, values = zip(*config_overrides.items())
        >>> experiments = [dict(zip(keys, v)) for v in itertools.product(*values)]

        """

        self.d = d
        self.run_path = run_path

        # secrets.token_hex(nbytes=16)

    def parser(self, protocol='all_permutations'):
        """Parses the input dictionary in one of two ways. 1) Constructs all
        permutations or 2) constructs a 1-1 correspondence, which requires that
        each list is of the same length.

        Parameters
        ----------
        protocol : {'all_permutations', 'one_to_one'}
            Determines the parsing method, each of which is described in this
            docstring and in the doctring of __init__.

        """

        if protocol == 'all_permutations':




    def init_dataframe(sel):
        """
        Something like 

        jobs = pd.DataFrame(parse_all_jobs(p, args),
                        columns=['Atom', 'Sort', 'Cutoff', 'Displace'])
        dir_hashes = [secrets.token_hex(nbytes=8) for __ in range(len(jobs))]

        if len(set(dir_hashes)) != len(dir_hashes):
            raise RuntimeError("Hash conflict. Play the lottery!")

        dir_names = pd.DataFrame(dir_hashes, columns=['Hash'])
        jobs = pd.concat([dir_names, jobs], axis=1)
        create_all_directories(p, jobs, args.name)
        """

        pass


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
