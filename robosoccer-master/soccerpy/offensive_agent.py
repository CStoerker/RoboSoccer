#!/usr/bin/env python

"""@OffensiveAgent
    Documentation for this module.
    General Agent for all the agents 
    controls all agents not assigned to a specific
    task
"""

# imports
from agent import Agent
import math

# start of class
class OffensiveAgent (Agent):

	#variables
	goal_pos = (55, 0)
	enemy_pos = (-55,0)
	catch_perimeter = 5

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
			if self.wm.is_ball_kickable(): 
			    #if self.shoot():
				#return
			    if self.pass_ball():
				return
			    if self.dribble():
				return
			else:
		            #if self.receive_pass():
				#return
			    if self.go_to_ball():
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
		    self.enemy_pos = (55,0)
		else:
		    self.goal_pos = (55, 0)
		    self.enemy_pos = (-55,0)
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

		#determine if the agent has the ball
		if self.wm.is_ball_kickable() and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 20:
			#Dribble towards the opponets goalpost

			print "About to shoot"
			pivot_angle = self.real_angle(self.wm.abs_coords, self.goal_pos)
			print "pivot = %d" % pivot_angle
            		self.wm.ah.kick(30, pivot_angle)
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

			print "About to dribble"
			pivot_angle = self.calcAngleToCoords(self.wm.abs_body_dir,self.wm.abs_coords, self.goal_pos)
			print "pivot = %d" % pivot_angle
			#self.wm.ah.turn(pivot_angle)

			if pivot_angle < -90:
				pivot_angle = -90
			if pivot_angle > 90:
				pivot_angle = 90
			self.wm.ah.turn(pivot_angle)
			print "pivot = %d" % pivot_angle
            		self.wm.ah.kick(15, pivot_angle)
			return True
		else:
		    # move towards ball
		    if -7 <= self.wm.ball.direction <= 7:# and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 60:

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
		#determine if the agent has the ball
		#print "in receiving ball"
		if self.wm.ball.distance <= self.catch_perimeter:

			#receive
			#print "receiving ball dis %d " % self.wm.ball.distance
			# face ball
			self.wm.ah.turn(self.wm.ball.direction / 2)
			self.wm.ah.dash(60)

			return True

		return False
		 #end of method

	"""@open_space
		Determine if player should move to open space
		how to move without the ball
	"""
	def go_to_ball(self):

		# move towards ball
		if -7 <= self.wm.ball.direction <= 7:

			if self.wm.ball.distance >= 10:
				 self.wm.ah.dash(85)
			else:
				self.wm.ah.dash(55)
			return True
		else:
			# face ball
			self.wm.ah.turn(self.wm.ball.direction / 2)
			return True 
		#end of method

	def open_space(self):

		#figure out how to move when we dont have the ball or for interception

		return False
		 #end of method
	"""@real_angle

	"""
	def real_angle(self, point1, point2):

		direction_point = 0
		angle = self.wm.angle_between_points(point1, point2)

		#see if the agent is in motion
		if self.wm.abs_body_dir is not None:

		    direction_point = self.wm.abs_body_dir - angle

		return direction_point

	def calcAngleToCoords(self, curAngle, curPosition, targPosition):
	   	retVal = False

		x_1, y_1 = curPosition
		x_2, y_2 = targPosition
		# Sets origin coordinate to zero
		x_2 = x_2 - x_1
		y_2 = y_2 - y_1
		angle = curAngle * (math.pi / 180)
		dx = math.cos(angle)
		dy = math.sin(angle)
		turnArc = math.atan2(x_2 * dy - y_2 * dx,  x_2 * dx + y_2 * dy ) * (180 / math.pi)
		retVal = turnArc

	        return(retVal)

#end of OffensiveAgent Class
#############################################################################################

