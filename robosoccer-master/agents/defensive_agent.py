#!/usr/bin/env python
import sys
sys.path.insert(0, '../soccerpy')
import 'agent'

class DefensiveAgent(Agent):

	def think(self):
        self.wm.ah.turn(self.wm.ball.direction / 2)
        return
