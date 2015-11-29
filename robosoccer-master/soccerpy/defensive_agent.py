#!/usr/bin/env python

"""@DefensiveAgent
    Documentation for this module.
    General Agent for all the agents 
    controls all agents not assigned to a specific
    task
"""

# imports
from agent import Agent


# start of class
class DefensiveAgent (Agent):

	#variables
	goal_pos = (55, 0)
	original_place = (0.0,0.0)
	at_original_place = True

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
		
		#if self.at_original_place is True:
			#self.original_place = self.wm.abs_coords
			#self.at_original_place = False
			#return

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
		else:
		    self.goal_pos = (55, 0)
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
	
		# figure out how far the goal is and if there is someone in front of the player. If not, shoot

		return False
	 #end of method

	"""@pass
		Determine if the ball should be passed, if so pass and return true else return 	false
	"""
	def pass_ball(self):
	
		#determine when to pass the ball

		#determine if the agent has the ball
		if self.wm.is_ball_kickable():
			#kick towards the closest teammate
			
			mypos = self.wm.abs_coords
			
			coords = self.wm.get_nearest_teammate_to_point(mypos)
			
			#coords = self.wm.get_object_absolute_coords(closest_mate)
			
			#coords = (55,0)
			run_speed = 75
			
			#self.wm.turn_body_to_point(mate_coords)
			angle = self.wm.angle_between_points(mypos, coords)
			
			if(angle > 180):
				angle = angle - 360
			elif(angle < -180):
				angle = angle + 360
			
			print "angle: %d" % (angle)
			print "passing to %s" % (coords,)
			self.wm.ah.turn(angle)
			
			if(self.wm.ball.distance <=7):
				run_speed = 55
			#self.wm.ah.dash(run_speed)
			
			#self.wm.ah.turn_neck(angle)
			if self.wm.is_ball_kickable():
				self.wm.ah.kick(30, angle)
			#self.wm.ah.turn_neck(-angle)
			#self.wm.kick_to(coords, 0.0)

			return True
		else:
		    return False

		return False
	#end of method pass_ball

	"""@dribble
		Determine if the ball should be carried up the field, if so dribble else return false
	"""
	def dribble(self):
		
		#determine if the agent has the ball
		if self.wm.is_ball_kickable():
			#kick towards the opponets goalpost
			self.wm.kick_to(self.goal_pos, 0.0)
			return True
		else:
		    # move towards ball
		    if -7 <= self.wm.ball.direction <= 7 and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 100 and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) >= 80 and self.wm.ball.distance < 20:
			self.wm.ah.dash(65)
			return True
		   # elif -7 <= self.wm.ball.direction <= 7 and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) <= 100 and self.wm.euclidean_distance(self.wm.abs_coords,self.goal_pos) >= 80 and self.wm.ball.distance > 20:
			#self.wm.turn_body_to_point(self.goal_pos)
			#self.wm.ah.dash(65)
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
		if self.wm.is_ball_kickable():
			return False
			
		ball_coords = self.wm.get_object_absolute_coords(self.wm.ball)
		ball_dist = self.wm.euclidean_distance(self.wm.abs_coords, ball_coords)
		
		if(ball_coords[1]<self.wm.abs_coords[1]):#ball is above player y
			if self.wm.ball.direction>=0:#ball to right of player x
				self.wm.ah.turn(self.wm.ball.direction / 2 )
			elif self.wm.ball.direction<=0:# ball to left of player x
				self.wm.ah.turn(self.wm.ball.direction / 2 )
		if(ball_coords[1]>self.wm.abs_coords[1]):#ball is below player y
			if self.wm.ball.direction>=0:#ball to right of player x
				self.wm.ah.turn(self.wm.ball.direction / 2 )
			elif self.wm.ball.direction<=0:#ball to left of player x
				self.wm.ah.turn(self.wm.ball.direction / 2 )
			
			if (ball_dist <= 8):
				self.wm.ah.dash(100)
			if (ball_dist <= 4):
				self.wm.ah.catch(self.wm.ball.direction / 2)
		#else:
			#if(ball_coords[1]<self.wm.abs_coords[1]):
			#if(ball_coords[1]>self.wm.abs_coords[1]):
			#self.wm.ah.turn(self.wm.ball.direction / 2)
		
		return True
		
		
		 #end of method

	"""@open_space
		Determine if player should move to open space
		how to move without the ball
	"""
	def open_space(self):

		#figure out how to move when we dont have the ball or for interception

		return False
		 #end of method

#end of MidfieldAgent Class
#############################################################################################
