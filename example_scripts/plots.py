import pylab

# === === === === === === AGENT SETUP === === === === === ===
from behaviorSim.environment.environment import environment
envmt = environment()	#load default environment

from behaviorSim.PECSagent.agent import agent
agent1 = agent(envmt)	#load default agent

# === === === === === === PLOTS === === === === === ===
from behaviorSim.PECSplotter.plot import plotAll, plotInputs, plotState 	#load the plotter

print 'plot using plotAll? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	plotAll(agent1,0,10)
	# and show the plots:
	pylab.show()	

print 'plot using individual plotters? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	#using the built-in plotters:
	plotInputs(agent1,0,10)	#plot inputs t={0->10}
	plotState(agent1,0,10)
	# and show the plots:
	pylab.show()		

print 'plot using custom plot? (y/n)'
choice = raw_input()
while choice != 'n' and choice != 'y':
	print choice + '? please enter y or n.'
	choice = raw_input()
if choice == 'y':
	#to make custom plots, we must get an array of the desired data:
	timeArray = [agent1.inputs.time(t) for t in range(0,10)]
	ageArray  = [agent1.state.age(t).total_seconds()/(60*60*24*365.242) for t in range(0,10)]

	# then set up the figure:
	pylab.figure('agent age[yrs] v time of subject born '+str(agent1.state.birthday))

	# plot the data:
	pylab.plot(timeArray,ageArray)
	# force yticks to be in years (and not deci-years):
	locs,labels = pylab.yticks()
	pylab.yticks(locs, map(lambda ageArray: "%g" % ageArray, locs))
	# and show the plot:
	pylab.show()

