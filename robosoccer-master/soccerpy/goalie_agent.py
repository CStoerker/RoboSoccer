from agent import *

class GoalieAgent(Agent):
    """
    TODO Describe ME...
    """

    def __init__(self):
        """
        TODO
        """
        Agent.__init__(self)

        self.catch_distance = 5

    def calc_kickoff_pos(self):
        """
        Calculate the kickoff position of the GolaieAgent. The goalie should
        be centered in front of his own team's goal.
        """

        if self.wm.side == WorldModel.SIDE_R:
            return (50, 0)
        return (-50, 0)

    def setup_environment(self):
        """
        TODO describe me...
        """
        self.in_kick_off_formation = False

    def think(self):
        """
        TODO Describe me...
        """
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