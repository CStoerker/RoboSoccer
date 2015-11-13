#!/usr/bin/env python

"""@Main
    Documentation for this module.
    General Agent for all the agents 
    controls all agents not assigned to a specific
    task
"""

#import 
from agent import *

class GoalieAgent(Agent):

#Start of methods
#############################################################################################

	"""@_init_self
		recognize yourself
	"""
	def __init__(self):

		Agent.__init__(self)

		self.catch_distance = 5
		 #end of method

	"""@calc_kickoff_pos
		Calculate the kickoff position of the GolaieAgent. The goalie should
		be centered in front of his own team's goal.
	"""
	def calc_kickoff_pos(self):

		#determine field side
		if self.wm.side == WorldModel.SIDE_R:
		    return (50, 0)

		#else
		return (-50, 0)
		 #end of method
	"""@setup_environment
		set
	"""
	def setup_environment(self):

		self.in_kick_off_formation = False
		 #end of method

	"""@think
		think for
	"""
	def think(self):

		# if it is possible to teleport, move into position
		# FIXME... sometimes goalie does not telport.
		# only fix I can come up with is keep doing it over and over
		if self.wm.is_before_kick_off:
		    self.goto_kickoff_position()
		    self.in_kick_off_formation = True
		    return

		# the game is being played, protect goal
		# locate the ball
		if (self.wm.ball is None) or (self.wm.ball.direction is None):
		    self.wm.ah.turn(30)
		    return

		elif self.wm.ball.distance < self.catch_distance:
		    self.catch(self.wm.ball.direction)
		    return

		else:
		   # face ball
		   self.wm.ah.turn(self.wm.ball.direction / 2)
		   return
		    #end of method

#End of methods
#############################################################################################
