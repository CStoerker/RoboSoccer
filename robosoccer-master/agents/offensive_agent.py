#!/usr/bin/env python
from ..soccerpy.agent import Agent
from ..soccerpy.world_model import WorldModel


class OffensiveAgent (Agent):

    goal_pos = (55, 0)

    # If player has ball make ball decisions, otherwise make positioning based decisions
    def think(self):
        self.check_values()
        if self.wm.is_ball_kickable():
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
        self.general()
        return

    # Sets values used in the think loop and checks to see if thread is still running
    def check_values(self):
        # DEBUG:  tells us if a thread dies
        if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
            raise Exception("A thread died.")

        if self.wm.side == WorldModel.SIDE_R:
            self.goal_pos = (-55, 0)
        else:
            self.goal_pos = (55, 0)
        return

    # Does what the normal agent does if no other cases appear, should not be called unless needs to defend or something
    def general(self):
        super(OffensiveAgent, self).think()
        return

    # Determine if it should try to shoot, if so shoot and return true else return false
    def shoot(self):
        # figure out how far the goal is and if there is someone in front of the player. If not, shoot
        return False

    # Determine if the ball should be passed, if so pass and return true else return false
    def pass_ball(self):
    	if self.wm.is_ball_kickable():
                self.wm.kick_to(self.wm.get_nearest_teammate_to_point(self,self.goal_pos), 0.7)
                return True
        else:
            # move towards ball
            if -7 <= self.wm.ball.direction <= 7:
                self.wm.ah.dash(65)
                return False
            else:
                # face ball
                self.wm.ah.turn(self.wm.ball.direction / 2)
                return False
        return False

    # Determine if the ball should be carried up the field, if so dribble else return false
    def dribble(self):
        if self.wm.is_ball_kickable():
                self.wm.kick_to(self.goal_pos, 0.1)
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
	if self.euclidean_distance(self.wm.get_nearest_teammate_to_point(self, abs_coords),abs_coords)) < 5:
		
		return True
	else:
        	return False

