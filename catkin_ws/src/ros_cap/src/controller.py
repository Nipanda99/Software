#!/usr/bin/env python
import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Image # importar mensajes de ROS tipo Image
import cv2 # importar libreria opencv
from cv_bridge import CvBridge # importar convertidor de formato de imagenes
import numpy as np # importar libreria numpy
from math import *
import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped
from template_cv import *
from geometry_msgs.msg import Point

class Controller(object):
	def __init__(self, args):
		super(Controller, self).__init__()
		self.sub=rospy.Subscriber("/duckiebot/possible_cmd/duckietown_msgs/Twist2DStamped",Joy,self.controlador)
		self.sub2=rospy.Publisher("/duckiebot/posicionPato/geometry_msgs/Point",Point,self.controlador)
		self.pub=rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd",Twist2DStamped,queue_size=10)


	def controlador(self,msg):
		if dy<10:
		comando.v=0
               	comando.omega=0
		self.publisher.publish(comando) 
		#if coordenada.x>160: #el pato esta a la derecha
				#self.publisher.publish(comando) #se mueve a la
				#comando.v=10
			#else: #esta a la izquierda	
				#comando.omega=	
				#comando.v=	

		else: 
			self.publisher.publish(comando) 

