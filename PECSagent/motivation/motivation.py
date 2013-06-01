# this file contains all information pertaining to the 'motivation variables' AKA 'hidden variables' described in the PECS reference model

# === additions you might make are described in headers ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# and encapsulated in arrows
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# === 1 import desired classes to define parts of input here ===
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from .baseInfo.death  import oldAger  as mortalityGetter

# from CSEL model
from .CSEL.behaviorTankValue import xiFive as will_PAGetter


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class motivation:
	# constructor
	def __init__(self,theStates):
		self.state = theStates
		# === define ALL raw data structures ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		# from package baseInfo:
		self.__mortality=list()
		# from package CSEL:
		self.__will_PA=list()
		
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# returns ALL data for given time t as a dict 
	def __call__(self,t):
		# === 3 return ALL info for that time as a dict ===
		# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
		return dict(mortality=self.mortality(t),\
		            will_PA=self.will_PA(t))
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# === 4 define ALL getters using external functions ===
	# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# note: 'getters' are not true getters here; they also set.

	# describes the agent's physiological succeptibility to death. 
	# from package baseInfo
	def mortality(self,t):
		return mortalityGetter(self.__mortality,t,self.state.age)

	# represents the will of the agent to be physically active
	# from package CSEL 
	def will_PA(self,t):
		return will_PAGetter(self.__will_PA,t,self.state.eta)
	
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

