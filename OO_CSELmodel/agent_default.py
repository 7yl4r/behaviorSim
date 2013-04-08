# this file is used to specify constants for CSEL model which effect the agent's (participant's) 'personality'

from pylab import array

class agent:
	theta = array([0,0,0, 2,2,2,2,2]);	#time delays
	tau   = array([1,1,1, 2, 4]);		#time constants

	# exogenous inflow resistances:
	gamma = array([[1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1],\
		       [1,1,1]]);

	# outflow resistances (depletion constants)
	beta  = array([[0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5],\
		       [0.5,0.5,0.5,0.5,0.5]]);

	# disturbances
	zeta= array([0,\
	       0,\
	       0,\
	       0,\
	       0]);

