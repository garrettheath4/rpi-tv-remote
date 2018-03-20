#!/usr/bin/env python3
# env_properties.py

"""
This module reads the properties stored in the Java .properties-style file
located at /etc/catalist/${DEPLOYMENT_ENV}/env.properties

This file was stolen from the api-status project:
http://stash.datawarehousellc.com:7990/projects/API/repos/api-status/browse/apistatus/env_properties.py
Perhaps it should be its own project?
"""

import sys
import os
import textwrap

try:
    import javaproperties
except ImportError:
    try:
        import pip
    except ImportError:
        print("ERROR: pip3 is not installed on this system.")
        sys.exit(1)
    pip_exit = pip.main(['install', 'javaproperties'])
    if pip_exit != 0:
        print(textwrap.dedent(
            """\
            ERROR: Unable to automatically install 'javaproperties' module.
            Install it with:
            > pip3 install javaproperties \
            """))
        sys.exit(1)
    try:
        import javaproperties
    except ImportError:
        print(textwrap.dedent(
            """\
            ERROR: The 'javaproperties' module is not installed on this system.
            Install it with:
            > pip3 install javaproperties \
            """))
        sys.exit(1)


def load_environment_properties(properties_prefix=''):
    """
    Loads the env.properties file that corresponds with the environment type
    defined in the system's environment variable DEPLOYMENT_ENV.

    :param str properties_prefix: A property key prefix to filter by,
                                  like: 'api-status.'
    :return: dict containing the properties from the system's configured env
             file, or None if DEPLOYMENT_ENV is not set correctly
    :rtype: dict or None
    """
    curr_env = get_current_environment()
    if curr_env:
        return _load_specific_env_properties(curr_env, properties_prefix)
    else:
        # DEPLOYMENT_ENV must not have a valid value
        return None


def get_environment_property(property_key):
    """
    Fetches the given property key *property_key* from the env.properties file
    that corresponds with the environment type defined in the system's
    environment type defined in the system's environment variable
    DEPLOYMENT_ENV.

    :param str property_key: The desired property key to fetch
    :return: Value of the given property key, or None if it does not exist
             or if DEPLOYMENT_ENV is not set correctly
    :rtype: str or None
    """
    props = load_environment_properties(property_key)
    if props is None:
        # DEPLOYMENT_ENV must not have a valid value
        return None
    if property_key in props:
        return props[property_key]
    else:
        return None


def get_current_environment():
    """
    Returns the 3-4 character string code of the current system's environment
    as defined in the system's environment variable DEPLOYMENT_ENV.

    :return: 3 or 4 character string code of the current environment, or None
             if DEPLOYMENT_ENV is not set correctly
    :rtype: str or None
    """
    valid_envs = {'dev', 'test', 'stag', 'prod'}
    curr_env = os.environ['DEPLOYMENT_ENV'].lower()
    if curr_env in valid_envs:
        return curr_env
    else:
        print(("Warning: %s is not a valid environment. "
               "Valid environments include: %s") % (curr_env, str(valid_envs)))
        return None


def _load_specific_env_properties(env, prop_prefix=None):
    """
    Loads the env.properties file that corresponds with the given *env* str.
    :param str env: A valid environment, such as: dev, test, stag, prod
    :param str prop_prefix: A key prefix to filter by, like: 'api-status.'
    :return: dict containing the properties from the specified env file
    :rtype: dict
    """
    filename = '/etc/catalist/%s/env.properties' % env.strip().lower()
    prop_file = open(filename)
    return javaproperties.load(prop_file,
                               object_pairs_hook=_filter_generator(
                                   prop_prefix))


def _filter_generator(prefix_filter_str=None):
    """
    Returns a function that accepts an iterable object and returns a dict that
    does not contain any keys that begin with prefix_filter_str.

    :param str prefix_filter_str: The prefix string to filter dict items by
    :return: Function that filters an iterable and stores the items in a dict
    :rtype: function
    """
    def __dict_filter(iterable):
        """
        Accepts an iterable and returns a dict that only contains items whose
        key begins with a pre-defined prefix.

        :param iter iterable: Iterable object to filter and make into a dict
        :return: dict containing only the filtered items
        :rtype: dict
        """
        iterable_is_empty = True
        d = {}
        for (k, v) in iterable:
            iterable_is_empty = False
            if not prefix_filter_str or k.startswith(prefix_filter_str):
                d[k] = v
        if not d:
            if iterable_is_empty:
                print("Warning: No properties found on system")
            else:
                print(("Warning: Properties found but none match the prefix "
                       "'%s'") % prefix_filter_str)
        return d
    return __dict_filter
