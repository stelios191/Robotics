#!/usr/bin/env python3
import rospy
from ar_week8_test.msg import cubic_traj_coeffs
import numpy as np
from std_msgs.msg import Float64
#callback to publish trahectory data points.
def traj_callback(data):
    #calculate and publish trajectory points over time			
    t = np.linspace(data.t0, data.tf, num=100)
    for pos,vel,accel in zip(data.a0 + data.a1*t + data.a2*t**2 + data.a3*t**3,
                               data.a1 + 2*data.a2*t + 3*data.a3*t**2,
                               2*data.a2 + 6*data.a3*t):
        position_pub.publish(Float64(data=pos))
        velocity_pub.publish(Float64(data=vel))
        acceleration_pub.publish(Float64(data=accel))
        #publish rate
        rospy.sleep(0.05)  
#setup plublishers for trajectory data and subscribe to coefficients
rospy.init_node("plot_cubic_traj", anonymous=True)
position_pub=rospy.Publisher("position_traj",Float64,queue_size=10)
velocity_pub=rospy.Publisher("velocity_traj",Float64,queue_size=10)
acceleration_pub=rospy.Publisher("acceleration_traj",Float64,queue_size=10)
rospy.Subscriber('coeffs',cubic_traj_coeffs,traj_callback)
if __name__ == "__main__":
    rospy.spin()
