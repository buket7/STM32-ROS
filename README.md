# STM32-ROS
Receiving IMU data with STM32F4 and transferring data to ROS based code via UART communication
# STM32F4 PART 
I performed the programming of the STM32F4 card through the Windows operating system. I used STM32CubeIDE for programming the STM32F4 board. We set the I2c pins and UART pins that we will use using the STM32CubeIDE. After making the pin adjustments, we move on to the coding part of our STM32F4 floor.
# CONNECTION PART
We used USB to TTL converter for UART communication. The connections of STM32F4 and USB to TTL converter should be as follows;
```apache
USB to TTL              STM32F4
TXD          ->           PA3
RXD          ->           PA2
5V           ->           5V
GND          ->           GND
```
We used MPU6050 as IMU. The connection of MPU6050 and STM32F4 is as follows;
```apache
MPU6050                 STM32F4
SCL          ->           PB6
SDA          ->           PB7
VCC          ->           3V
GND          ->           GND
```
You can see the processes done during programming in the video on Youtube.
Video->
# ROS PART 
The operations performed in this section were carried out on the Ubuntu 18.04 operating system. We can start by creating a ROS-based workspace.
```apache
$ source /opt/ros/melodic/setup.bash
$ mkdir -p ~/uart_ws/src
$ cd ~/uart_ws/
$ catkin_make
$ source devel/setup.bash
```
Let's create the ROS package we will use.

```apache
$ cd ~/uart_ws/src
$ catkin_create_pkg uart_pkg std_msgs rospy roscpp
$ cd ~/uart_ws
$ catkin_make
$ source ~/uart_ws/devel/setup.bash
```
After creating the ROS environment, we set our .xml and Cmake files according to the codes given above. We run the python files in the scripts folder as follows;

NOTE: Make sure you have UART communication before running the codes. Don't forget to connect the USB to TTL converter connected to the STM32F4 stage to the computer.

Use the following command to allow the USB port;

NOTE: The dev/ttyUSB0 part may differ for you.
```apache
$ sudo chmod 666 dev/ttyUSB0
```
Let's make python files executable.
```apache
$ cd ~/uart_ws/src/uart_pkg/src/scripts
$ sudo chmod +x uart_pub.py
$ sudo chmod +x uart_sub.py
```
Now we are ready to run our code

```apache
$ cd ~/uart_ws
$ source ~/uart_ws/devel/setup.bash
$ rosrun uart_pkg uart_pub.py
$ rosrun uart_pkg uart_sub.py
```
That's it.
