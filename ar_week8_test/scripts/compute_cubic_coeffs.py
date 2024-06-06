#!/usr/bin/env python3
import rospy
import numpy as np
from ar_week8_test.srv import compute_cubic_traj, compute_cubic_trajResponse
#computes trajectory coefficients.
def compute_coeffs(req):
    a = np.array([
        [1,req.par.t0, req.par.t0**2,req.par.t0**3],
        [0,1,2*req.par.t0,3*(req.par.t0**2)],
        [1,req.par.tf, req.par.tf**2,req.par.tf**3],
        [0,1, 2*req.par.tf,3*(req.par.tf**2)]])
    #set initial and final positions and velocities
    c =np.array([req.par.p0, req.par.v0, req.par.pf, req.par.vf])
    # solve the equation for coefficients
    coeffs= np.linalg.solve(a, c) if np.linalg.cond(a)<1/np.finfo(a.dtype).eps else np.zeros(4)
    return compute_cubic_trajResponse(*coeffs)
#initialize service to compute coefficients
def compute_coeffs_s():
    rospy.init_node("compute_cubic_coeffs")
    rospy.Service("compute_cubic_traj",compute_cubic_traj,compute_coeffs)
    rospy.spin()
if __name__ == "__main__":
    compute_coeffs_s()
