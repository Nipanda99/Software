#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped




class Control(object):
	def __init__(self, args):
		super(Control, self).__init__()
		self.args = args
                self.subscriber=rospy.Subscriber("/duckiebot/joy",Joy,self.callback)
                self.publisher=rospy.Publisher("/duckiebot/possible_cmd/duckietown_msgs/Twist2DStamped",Twist2DStamped,queue_size=10)

	def callback(self,msg):
            comando=Twist2DStamped()
	    comando.v=-msg.axes[1]
            comando.omega=13*msg.axes[3]
            botonEmergencia=msg.buttons[1]
            if botonEmergencia==1:
               comando.v=0
               comando.omega=0
	    print 1
            self.publisher.publish(comando)  
            
	

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Control('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
