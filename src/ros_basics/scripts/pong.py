#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
	if data.data == 'ping':
	    pub.publish('pong')
	    rospy.loginfo('pong')
	else:
		pub.publish('Failed!')
		rospy.loginfo('Failed!')
	    
    
rospy.init_node('pong_node', anonymous=True)
sub = rospy.Subscriber('ping', String, callback)
pub = rospy.Publisher('pong',  String, queue_size=10)
rospy.spin()
