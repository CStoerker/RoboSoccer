#!/usr/bin/env python
from agent import Agent



class OffensiveAgent (Agent):

    goal_pos = (55, 0)

    def _init_(self):
	Agent._init_(self)

    # If player has ball make ball decisions, otherwise make positioning based decisions
    def think(self):
        self.check_values()
	if not self.wm.is_before_kick_off():
		if self.wm.ball is None or self.wm.ball.direction is None:
			self.wm.ah.turn(30)
			return

		if True: #self.wm.is_ball_kickable()
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
       	     self.general()
        return

    # Sets values used in the think loop and checks to see if thread is still running
    def check_values(self):
        # DEBUG:  tells us if a thread dies
        #if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
           # raise Exception("A thread died.")

        if self.wm.side == self.wm.SIDE_R:
            self.goal_pos = (-55, 0)
        else:
            self.goal_pos = (55, 0)
        return

    # Does what the normal agent does if no other cases appear, should not be called unless needs to defend or something
    def general(self):
        Agent.think(self)
        return

    # Determine if it should try to shoot, if so shoot and return true else return false
    def shoot(self):
        # figure out how far the goal is and if there is someone in front of the player. If not, shoot
        return False

    # Determine if the ball should be passed, if so pass and return true else return false
    def pass_ball(self):
        return False

    # Determine if the ball should be carried up the field, if so dribble else return false
    def dribble(self):
        if self.wm.is_ball_kickable():
                self.wm.kick_to(self.goal_pos, 0.3)
                return True
        else:
            # move towards ball
            if -7 <= self.wm.ball.direction <= 7:
                self.wm.ah.dash(65)
                return True
            else:
                # face ball
                self.wm.ah.turn(self.wm.ball.direction / 2)
                return True
        return False

    # Determine if the player should move into position to accept a pass
    def receive_pass(self):
        return False

    # Determine if player should move to open space
    def open_space(self):
        return False

