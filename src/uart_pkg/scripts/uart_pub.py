#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from uart_pkg.msg import my_uart
import serial
import time

pub = rospy.Publisher('drone_topic',my_uart,queue_size=10)

serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200,
                           bytesize=8, timeout=0)

rospy.init_node('publisher',anonymous= True)

rate = rospy.Rate(10)
a = 0
i = 0

while(not rospy.is_shutdown()):
    data = my_uart()
    uart_bilgi = serialPort.readline()
    uart_bilgi1 = uart_bilgi.decode('utf-8')
    time.sleep(0.1)
    if uart_bilgi1 == '$':
        i = i + 1
        continue
    elif a < i:
        if uart_bilgi1 == '':
            continue
        else:
          data.x = uart_bilgi1   
          print("X:", data.x )
          a = a + 1
       
    elif a == i:
        if uart_bilgi1 == '':
            continue
        else:
          data.y = uart_bilgi1  
          print("Y:", data.y ) 


    pub.publish(data)

    rate.sleep()
  
