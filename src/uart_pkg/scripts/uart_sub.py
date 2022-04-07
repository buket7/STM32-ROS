#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from uart_pkg.msg import uart
import serial
import time


def func(uart):
    if (uart.x == ''):
       print("~~~")
    else:
        rospy.loginfo('alinan veriler x: (%s)', uart.x)
    if (uart.y == ''):
       print("~~~")
    else:
        rospy.loginfo('alinan veriler y: (%s)', uart.y)


rospy.init_node('subscriber',anonymous=True)
rospy.Subscriber('drone_topic',uart,func)
rospy.spin()
