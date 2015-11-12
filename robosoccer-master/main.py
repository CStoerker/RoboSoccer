#!/usr/bin/env python

import sys
import multiprocessing as mp
import threading
import time
import random
import signal

from soccerpy import sock
from soccerpy import sp_exceptions
from soccerpy import handler
from soccerpy.agent import Agent
from soccerpy.world_model import WorldModel
from soccerpy.offensive_agent import OffensiveAgent

# Team Name Constant
TEAM_NAME = 'Mannynator'

# Variables
# number of forward agents
num_forwards = 3

# Number of midfield Agents
num_midfields = 4

# Number of defenders Agents
num_defenders = 4

def spawn_agent(team_name, agent_position):
    """
    Used to run an agent in a seperate physical process.
    """

    a = agent_position()
    a.connect("localhost", 6000, team_name)
    a.play()

    # we wait until we're killed
    while 1:
        # we sleep for a good while since we can only exit if terminated.
        time.sleep(1)

if __name__ == "__main__":
    
    agentthreads = []

	#create goalie
	#create goalie

	#Create the forward positon players
    for agent in range(0, num_forwards):
        print "  Spawning num_forward agent %d..." % (agent + 1)

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME, OffensiveAgent))
        at.daemon = True
        at.start()

        agentthreads.append(at)

	#Create the defensive positon players
    for agent in range(0, num_defenders):
        print "  Spawning num_forward agent %d..." % (agent +1)

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME, OffensiveAgent))
        at.daemon = True
        at.start()

        agentthreads.append(at)

	#Create the defensive positon players
    for agent in range(0, num_midfields):
        print "  Spawning num_forward agent %d..." % (agent +1)

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME, OffensiveAgent))
        at.daemon = True
        at.start()

        agentthreads.append(at)

    print "Spawned %d agents." % len(agentthreads)
    print
    print "Playing soccer..."

    def quit_gracefully(*args):
        print
        print "Killing agent threads..."

        # terminate all agent processes
        count = 0
        for at in agentthreads:
            print "  Terminating agent %d..." % (count + 1)
            at.terminate()
            count += 1
        print "Killed %d agent threads." % (count)

        print
        print "Exiting."
        sys.exit()
        
    # handle SIGINT exit from bash
    signal.signal(signal.SIGINT, quit_gracefully)

    # wait until killed to terminate agent processes
    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        quit_gracefully()
        
