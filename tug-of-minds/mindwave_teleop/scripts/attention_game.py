#!/usr/bin/env python

import rospy
import roslib

from geometry_msgs.msg import Twist
from mindwave_msgs.msg import Mindwave

M_PI = 3.1415116

class Turtlebot:
    """
    This class allows to teleoperate the turtlebot with
    the Mindwave headset.
    """

    def __init__(self):
        """Init method
        
        This Subscribes to rostopic mindwave and create a publisher
        of Twist message.

        """

        rospy.init_node('turtle_teleop_mindwave', anonymous=True)
        
        self.speed = 0.1 # 0.1 m/s
        self.turn = 1
        self.meditation_threshold = 50
        self.attention_threshold = 50
	self.distance = 0
	self.max_distance = 5

        self.loop_rate = rospy.Rate(10) # T = 1/10
        
        self.lastvel = Twist()        
        self.sub = rospy.Subscriber('/mindwave', Mindwave, 		self.mindwaveCallback, queue_size=100)
	#changed from ~/cmd_vel        
	self.pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)    

    def mindwaveCallback(self, msg):
        """
        This method publishes a rostopic Twist with angular and lineal velocities 
        to move the turtlebot. 

        When the user concentrate the robot goes fordward over x axes and
        turn to left over z axes when the person meditates. You need to 
        concentrate or meditate more higher than the threshold param in 
        the launch file.

        Param:
            msg : ROS message with meditation and attention values  

        """  
        twist = Twist()

        # Go fordward
        if msg.attention >= self.attention_threshold:
            twist.linear.x = 0.1 # if the attention level is above the threshold move forward
	    self.distance += 0.1
        else:
            twist.linear.x = 0 # otherwise stop

        twist.linear.y = 0 
        twist.linear.z = 0
   
        
        self.lastvel = twist

    def run(self):
        while not rospy.is_shutdown() and self.distance < self.max_distance:
            self.pub.publish(self.lastvel)
            self.loop_rate.sleep()

if __name__=="__main__":
    try:
        turtle = Turtlebot()
        turtle.run()
        rospy.spin()        
    except rospy.ROSInterruptException, e:
        print str(e)
        pass
