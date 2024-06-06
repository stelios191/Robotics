#!/usr/bin/env python3
import rospy
import random
from ar_week8_test.msg import cubic_traj_params
#publish random trajectory parameters 
def generate_points():
    pub =rospy.Publisher("params", cubic_traj_params, queue_size=10)
    rospy.init_node("points_generator", anonymous=True)
    #once every 20 seconds
    rate= rospy.Rate(0.05) 
    while not rospy.is_shutdown():
    	#generate random parameters
        msg = cubic_traj_params(p0=random.uniform(-10, 10),pf=random.uniform(-10, 10),
                                v0=random.uniform(-10, 10),vf=random.uniform(-10, 10),
                                t0=0,tf=round(random.uniform(5, 10), 0))
        pub.publish(msg)
        rate.sleep()
if __name__ == "__main__":
    generate_points()

