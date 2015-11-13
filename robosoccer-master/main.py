#!/usr/bin/env python

"""@Main
    Documentation for this module.
    General Agent for all the agents 
    controls all agents not assigned to a specific
    task
"""
#import modules
import sys
import multiprocessing as mp
import threading
import time
import random
import signal

#import classes
from soccerpy import sock
from soccerpy import sp_exceptions
from soccerpy import handler
from soccerpy.agent import Agent
from soccerpy.world_model import WorldModel
from soccerpy.offensive_agent import OffensiveAgent
from soccerpy.midfield_agent import MidfieldAgent
from soccerpy.goalie_agent import GoalieAgent

# Team Name Constant
TEAM_NAME = 'Mannynator'

# Variables
# number of forward agents
num_forwards = 2

# Number of midfield Agents
num_midfields = 4

# Number of defenders Agents
num_defenders = 4

"""@spawn_agent
Used to run an agent in a seperate physical process.
"""
def spawn_agent(team_name, agent_position):

    a = agent_position()
    a.connect("localhost", 6000, team_name)
    a.play()

    # we wait until we're killed
    while 1:
        # we sleep for a good while since we can only exit if terminated.
        time.sleep(1)
	 #end of method

if __name__ == "__main__":

#Start of main
#############################################################################################

	#create array for agents    
    agentthreads = []

    #create goalie
    print "  Spawning GoalieAgent 1..."

    at = mp.Process(target=spawn_agent, args=(TEAM_NAME, GoalieAgent))
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

	#Create the midfield positon players
    for agent in range(0, num_midfields):
        print "  Spawning num_forward agent %d..." % (agent +1)

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME, OffensiveAgent))
        at.daemon = True
        at.start()

        agentthreads.append(at)

	#Create the forward positon players
    for agent in range(0, num_forwards):
        print "  Spawning num_forward agent %d..." % (agent + 1)

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME, OffensiveAgent))
        at.daemon = True
        at.start()

        agentthreads.append(at)

    #print the agents
    print "Spawned %d agents." % len(agentthreads)
    print
    print "Playing soccer..."

    """@quit_gracefully
		quits the program in a fashionable way
		no just quits
    """
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
        
#End of Main
#############################################################################################
