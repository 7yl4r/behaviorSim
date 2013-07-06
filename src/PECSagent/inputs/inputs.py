# the inputs class describes the context of the agent
#	dependencies:
#		environment = the environment which the agent is in

from ..settings import settings
from ...__util.agentData import dataObject

### import default functions ###
from .baseInfo.debugInfo  import currentTime as __DFLT_FUNC__initTime
from .baseInfo.timePassed import timePassed  as __DFLT_FUNC__time

from .CSEL.fromEnvironment import pa         as __DFLT_FUNC__attitudeChange_PA
#TODO: from .CSEL.fromEnvironment import eb         as __DFLT_FUNC__attitudeChange_EB
from .CSEL.xi              import xi         as __DFLT_FUNC__xi

#TODO: xi not needed, since it is determined from attitudeChange values?


class inputs:	#can't use 'input' as the name b/c of built-in 'input()'
	# constructor
	def __init__(self,envir):
		self.environment = envir

		### create dataObjects ###

		# real-world time of calculation for each sim-world calculation of inputs
		self.initTime = dataObject(__DFLT_FUNC__initTime)

		# sim-world time of calculation
		self.time = dataObject(__DFLT_FUNC__time,settings.simStartTime,settings.deltaTime)

		#inflow to attitude about physical activity from theory of planned behavior
		self.attitudeChange_PA = dataObject(__DFLT_FUNC__attitudeChange_PA,self.environment)

#TODO:
	#	#inflow to attitude about eating behaviors from theory of planned behavior
	#	self.attitudeChange_EB = dataObject(__DFLT_FUNC__attitudeChange_EB,self.environment)

		#exogenous flow variables from package CSEL
		self.xi = dataObject(__DFLT_FUNC__xi,self.attitudeChange_PA)
		

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		### return ALL input info for that time as a dict ###
		return dict(initTime=self.initTime(t), \
		            time    =str(self.time(t)),\
		            attitudeChange_PA_behavioralBelief=str(self.attitudeChange_PA(t).behavioralBelief),\
		            attitudeChange_PA_behaviorAttitude=str(self.attitudeChange_PA(t).behaviorAttitude),\
		            attitudeChange_PA_normativeBelief=str(self.attitudeChange_PA(t).normativeBelief),\
		            attitudeChange_PA_subjectiveNorm=str(self.attitudeChange_PA(t).subjectiveNorm),\
		            attitudeChange_PA_PBC=str(self.attitudeChange_PA(t).PBC),\
		            attitudeChange_PA_controlBelief=str(self.attitudeChange_PA(t).controlBelief),\
		            xi           =str(self.xi(t)))

