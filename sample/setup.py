#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=[''],
    package_dir={'': 'scripts'},
    requires=['std_msgs', 'rospy']
)

setup(**setup_args)

