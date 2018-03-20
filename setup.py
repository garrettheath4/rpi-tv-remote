"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tvserver',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.1',

    description='A web server that tests internal APIs and shows the results',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/garrettheath4/rpi-tv-remote',

    # Author details
    author='Garrett Koller',
    author_email='garrettheath4@gmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Categorize the type of software
        'Topic :: System :: Hardware',
        'Topic :: Multimedia',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: System :: Monitoring',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        # What is the target execution environment?
        'Environment :: Web Environment',
        'Environment :: Console',

        # What operating systems is this code written for?
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',

        # Specify the natural language the package uses
        'Natural Language :: English',
    ],

    # What does your project relate to?
    keywords='tv remote control webapp app web server',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=['tvserver'],

    # List additional files here that are needed by the project but are not
    # specific to any actual Python modules in this project
    # data_files=[
    #     ('static', [
    #         'static/favicon.ico',
    #         'static/default.css',
    #     ]),
    #     ('templates', [
    #         'templates/base.html',
    #         'templates/index.html',
    #         'templates/report.html',
    #     ]),
    # ],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'javaproperties',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'tvserver = tvserver.__main__:main',
        ],
    },
)
