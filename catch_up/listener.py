#! /usr/bin/python

import rospy

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

class my_class:
	def __init__(self):
		self.position = Pose()
        
		rospy.init_node('listener')
		
		self.pub = rospy.Publisher('isobu/cmd_vel', Twist, queue_size = 1)

		self.sub = rospy.Subscriber('isobu/pose', Pose, self.setPosition)
		self.subtarget = rospy.Subscriber('/turtle1/pose', Pose, self.setTargetPosition)
	    
	def setPosition(self, msg):		
		self.position = msg

	def setTargetPosition(self, msg):	
		twist = Twist()
        
		twist.linear.x = self.getLinearX(msg)
		twist.linear.y = 0
		twist.linear.z = 0

		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = self.getAngularZ(msg)

		self.pub.publish(twist)

	def getLinearX(self, targetPosition, constant = 0.375):
		return constant * sqrt(pow((targetPosition.x - self.position.x), 2) + pow((targetPosition.y - self.position.y), 2))
	
	def getAngularZ(self, targetPosition, constant = 5):
		return constant * (atan2(targetPosition.y - self.position.y, targetPosition.x - self.position.x) - self.position.theta)

if __name__== '__main__':
	m = my_class()
	while not rospy.is_shutdown():	
		rospy.spin()


	
