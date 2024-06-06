#!/usr/bin/env python3
import rospy
from ar_week8_test.msg import cubic_traj_params,cubic_traj_coeffs
from ar_week8_test.srv import compute_cubic_traj
def comp_publish(data):
    try:
    	#service to compute coefficients from parameters     
        compute=rospy.ServiceProxy('compute_cubic_traj',compute_cubic_traj)
        r=compute(data)
        #publish the computed coefficients
        msg=cubic_traj_coeffs(a0=r.a0,a1=r.a1, a2=r.a2,a3=r.a3,t0=data.t0,tf=data.tf)
        pub.publish(msg)
    except rospy.ServiceException as e:
        rospy.logwarn("service failed: %s",e)
#setup subscriber to receive parameters and publisher for coefficients
def cubic_traj_planner():
    global pub
    rospy.init_node('cubic_traj_planner',anonymous=True)
    rospy.wait_for_service('compute_cubic_traj')
    pub = rospy.Publisher('coeffs',cubic_traj_coeffs,queue_size=10)
    rospy.Subscriber('params',cubic_traj_params,comp_publish)
    rospy.spin()
if __name__ == "__main__":
    cubic_traj_planner()
