#! /usr/bin/python
import rospy

from turtlesim.srv import Spawn, Kill

def turtlespawn(x,y,theta,name):
	rospy.wait_for_service('/spawn')
	spawn_func = rospy.ServiceProxy('/spawn', Spawn)
	spawn_func(x,y,theta,name)

def turtlekill(name):
	rospy.wait_for_service('/kill')
	kill_func = rospy.ServiceProxy('/kill', Kill)
	kill_func(name)

class spawner:
	def __init__(self,x,y,theta,name):
		rospy.init_node('publisher')
		try:
			turtlespawn(x,y,theta,name)
		except rospy.service.ServiceException: 
			turtlekill(name)
			turtlespawn(x,y,theta,name)

if __name__== '__main__':
	s = spawner(4.0, 8.0, 0.0, 'isobu')
