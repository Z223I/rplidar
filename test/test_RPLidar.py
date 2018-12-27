#!/usr/bin/env python3

try:
    from builtins import object
except ImportError:
    pass

#import warnings
#import sys

import unittest
from unittest.mock import patch

#import queue
#import math

import sys
sys.path.append('/home/pi/pythondev/rplidar/RPLidar')
#print(sys.path)

from RPLidar import RPLidar
#import RPi.GPIO as GPIO


class TestRPLidar(unittest.TestCase):

    def setUp(self):
        self.test_rplidar = RPLidar('/dev/ttyUSB0')

    def tearDown(self):
        pass

    def test_class_constants(self):
        pass

    def test_class_variables(self):
        pass

    def test_velocity_check_A(self):
        pass


if __name__ == "__main__":

    unittest.main()
