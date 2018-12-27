#!/usr/bin/env python3

import sys
import numpy as np
from rplidar import RPLidar


PORT_NAME = '/dev/ttyUSB0'


def run():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    run()
