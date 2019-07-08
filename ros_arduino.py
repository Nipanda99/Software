#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Point

class Control(object):
	def __init__(self, args):
		super(Control, self).__init__()
		self.args = args
                self.subscriber=rospy.Subscriber("/joy",Joy,self.callback)
		self.publisher=rospy.Publisher("test",Int32,queue_size=10)
		#self.publisher1=rospy.Publisher("toserv1",Int32,queue_size=10)
		self.publisher2=rospy.Publisher("toserv2",Int32,queue_size=10)
		self.publisher3=rospy.Publisher("tomotor",Int32,queue_size=10)


	def callback(self,msg):
		arduino_servo1=msg.buttons[2]
		arduino_servo2=msg.buttons[3]
		arduino_motor=msg.buttons[4]
		if arduino_servo1==1:
			arduino_msg=2
			self.publisher.publish(arduino_msg)
		if arduino_servo2==1:
			arduino_msg=3
			self.publisher2.publish(arduino_msg)
		if arduino_motor==1:
			arduino_msg=4
			self.publisher3.publish(arduino_msg)



def main():
	rospy.init_node('controles') #creacion y registro del nodo!
	obj = Control('args')
	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
