#class to define all inputs into the model based on step function for 1st order model in figure 7 of the following article:

#J.-Emeterio Navarro-Barrientos , Daniel E. Rivera & Linda M. Collins (2011):
#A dynamical model for describing behavioural interventions for weight loss and body composition
#change, Mathematical and Computer Modelling of Dynamical Systems: Methods, Tools and
#Applications in Engineering and Related Sciences, 17:2, 183-203


from pylab import array
from math import floor

# given belief step function
def belief(data,t):
	#TODO: add cache using given data list
	return squareWave(t, 3, 1, 1) 

# given outcome evaluation step function
def outcomeEval(data,t):
	return 1;

# xi = [ attitude, social norm, planned behavioral control ]
def xi(data,t, belief, outcomeEval):
	return array([belief*outcomeEval,
	              1,
	              1]);	#xi_2 & xi_3 are const here...
#	xi = array([[b1[t]*e1[t] for t in range(timeToRun)],	
#		    [1           for t in range(timeToRun)],
#		    [1           for t in range(timeToRun)]]);

#defines a step function at stepTime
def step(t, stepTime, beforeStep, afterStep):
	if t < stepTime:
		return beforeStep;
	else: # t > stepTime
		return afterStep;

#defines square wave starting (high) at t=0 with given high and low and frequency in 1/t units
# NOTE: 'high' is not required to be lower than 'low', changing this changes intial behavior i.e. highstart:|-_-_-| vs lowstart:|_-_-_|
def squareWave(t, high, low, frequency):
	if ( (floor(t/frequency)) % 2 == 0 ):
		return low
	else:
		return high

