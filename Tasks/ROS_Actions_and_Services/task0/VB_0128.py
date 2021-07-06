
"""
Team-id : 128
Task : Rotation of turtle in a circle
"""

#!/usr/bin/env python

#Importing the required libraries
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#defining global variables
X = 0
Y = 0
THETA = 0


def rotate():
    """
    This function is used to rotate the turtle in circle
    """

    #Declare a Twist message to send velocity commands

    vel_msg = Twist()

    #global THETA
    angle_covered = 0.0
    total_angle_covered = 5.3568   #This is the total angle covered by the turtle in one revolution

    rate = rospy.Rate(10)          # 10hz
    #velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Moving in a circle")
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        vel_msg.linear.x = 2.5
        vel_msg.angular.z = 1.5
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()

        if THETA > 0:
            angle = THETA
            print angle

        if THETA < 0:
            theta = abs(THETA)
            angle_covered = angle + (angle - theta)
            print angle_covered

        if  angle_covered > total_angle_covered:
            vel_msg.linear.x = 0.555
            vel_msg.angular.z = 1.3899
            VELOCITY_PUBLISHER.publish(vel_msg)
            rospy.loginfo("goal reached")
            break
        rate.sleep()


    rospy.loginfo("The END")
    rospy.signal_shutdown(0)



def pose_callback(msg):
    """
    Callback function
    """

    global X
    global Y
    global THETA
    X = msg.X
    Y = msg.Y
    THETA = msg.THETA

#Main Function
if __name__ == '__main__':
    try:
        rospy.init_node('node_turtle_revolve', anonymous=True)

        VELOCITY_PUBLISHER = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        POSE_PUBLISHER = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        time.sleep(2)

        rotate()

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
