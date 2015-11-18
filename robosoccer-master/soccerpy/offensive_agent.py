#!/usr/bin/env python

"""@OffensiveAgent
    Documentation for this module.
    General Agent for all the agents 
    controls all agents not assigned to a specific
    task
"""

# imports
from agent import Agent


# start of class
class OffensiveAgent (Agent):

	#variables
	goal_pos = (55, 0)
	#enemy_pos = (-55,0)

#Start of methods
#############################################################################################

	"""@_init_ 
		initializes the notion of self
	"""
	def _init_(self):
		#recognize agent self
		Agent._init_(self)
	 #end of method

	"""@think
		makes the decision for the player
		If player has ball make ball decisions, otherwise make positioning based 			decisions
	"""
	def think(self):

		# check the conditions of the field
		self.check_values()

		# if statement for after kick off
		if not self.wm.is_before_kick_off():
		
			# if statement for when player does not have the ball
			if self.wm.ball is None or self.wm.ball.direction is None:
				self.wm.ah.turn(30)
				return

			# if statement for when a player does have the ball
			if True: 
			    if self.shoot():
				return
			    if self.pass_ball():
				return
			    if self.dribble():
				return
			else:
			    if self.receive_pass():
				return
			    if self.open_space():
				return
		else:
			# if it is before kick off then use the normal agent for setup
		     self.general()
		return
		 #end of method

	"""@check_values
		Sets values used in the think loop and checks to see
		if thread is still running
		sets the conditions of the field
		ex. the side to take 
	"""
	def check_values(self):
	# DEBUG:  tells us if a thread dies
	#if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
	   # raise Exception("A thread died.")

		#check which side we are playing in
		if self.wm.side == self.wm.SIDE_R:
		    self.goal_pos = (-55, 0)
		    #self.enemy_pos = (55,0)
		else:
		    self.goal_pos = (55, 0)
		    #self.enemy_pos = (-55,0)
		return
		 #end of method

	"""@general
		Does what the normal agent does if no other cases appear,
		should not be called 			
		unless needs to no task assigned
	"""
	def general(self):
		
		#normal agent
		Agent.think(self)
		return
		 #end of method

	"""@shoot
		Determine if it should try to shoot, 
		if so shoot and return true else return false
	"""
	def shoot(self):
	
		# figure out how far the goal is and if there is someone in front of the 			player. If not, shoot
		# kick it at the enemy goal if agent is within range of goal
		if self.wm.is_ball_kickable() and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 15:

			self.wm.kick_to(self.goal_pos, .1)
			return True

		else:	
			return False
		#end of method

	"""@pass
		Determine if the ball should be passed, if so pass and return true else return false
	"""
	def pass_ball(self):
	
		#determine when to pass the ball

		return False
	#end of method

	"""@dribble
		Determine if the ball should be carried up the field, if so dribble else 			return false
	"""
	def dribble(self):
		
		#determine if the agent has the ball
		if self.wm.is_ball_kickable():
			#Dribble towards the opponets goalpost
			self.wm.kick_to(self.goal_pos, 0.1)
			return True
		else:
		    # move towards ball
		    if -7 <= self.wm.ball.direction <= 7 and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 60:

			self.wm.ah.dash(65)
			return True
		    else:
			# face ball
			self.wm.ah.turn(self.wm.ball.direction / 2)
			return True 
		return False
		 #end of method

	"""@receive_pass
		Determine if the player should move into position to accept a pass
	"""
	def receive_pass(self):
	
		#determine when to catch/intercept the ball

		return False
		 #end of method

	"""@open_space
		Determine if player should move to open space
		how to move without the ball
	"""
	def open_space(self):

		#figure out how to move when we dont have the ball or for interception

		return False
		 #end of method

#end of OffensiveAgent Class
#############################################################################################

