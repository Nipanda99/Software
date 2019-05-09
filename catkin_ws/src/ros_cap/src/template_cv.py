#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Image # importar mensajes de ROS tipo Image
import cv2 # importar libreria opencv
from cv_bridge import CvBridge # importar convertidor de formato de imagenes
import numpy as np # importar libreria numpy
from math import *

class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.sub=rospy.Subscriber("/duckiebot/camera_node/image/rect",Image,self.callback)
		self.pub=rospy.Publisher("/duckiebot/camera_node/image/procesada",Image,queue_size=1)


	#def publicar(self):

	def callback(self,img):

		bridge=CvBridge()
		image=bridge.imgmsg_to_cv2(img,"bgr8")
		self.fx=165.17295163624166
		self.fy=167.85490283721415
		
		
		# Cambiar espacio de color
                image_out=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		# Filtrar rango util
                mask=cv2.inRange(image_out,np.array([10,140,140]),np.array([60,255,255]))
		# Aplicar mascara
                image_out=cv2.bitwise_and(image_out,image_out,mask=mask)
		# Aplicar transformaciones morfologicas
                kernel=np.ones((5,5),np.uint8)
                img_out=cv2.erode(image,kernel,iterations=3)
                img_out=cv2.dilate(img_out,kernel,iterations=1)
		# Definir blobs
 		_, contours, hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		# Dibujar rectangulos de cada blob
		for cnt in contours:
			x,y,w,h=cv2.boundingRect(cnt)
			if w*h>300 and 0.5<h/w and h/w<1.5:    
				cv2.rectangle(image,(x,y),(x+w,y+h),(8,0,0),2)   
			
				# Calcular distancia
				dx=(self.fx*3.9)/w
				dy=(self.fy*3)/h
				print dy

				
				# Posicion
				#xpato=x+(w/2)
				#ypato=y+(h/2)
				#px=((xpato-154.921959034194)*d)/self.fx
				#py=((ypato-117.09155870869486)*d)/self.fy
				#pz=d
				
				
				# Publicar imagen final
		image=bridge.cv2_to_imgmsg(image,"bgr8")
		self.pub.publish(image) 

	
	
		


def main():
	rospy.init_node('tes') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()


