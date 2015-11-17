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

# Team Name Constant
TEAM_NAME = 'DummyTeam'

# Number of Soccer Agents
PLAYER_COUNT = 11

def spawn_agent(team_name):
    """
    Used to run an agent in a seperate physical process.
    """

    a = Agent()
    a.connect("localhost", 6000, team_name)
    a.play()

    # we wait until we're killed
    while 1:
        # we sleep for a good while since we can only exit if terminated.
        time.sleep(1)

if __name__ == "__main__":
    
    agentthreads = []
    for agent in xrange(min(11, PLAYER_COUNT)):
        print "  Spawning agent %d..." % agent

        at = mp.Process(target=spawn_agent, args=(TEAM_NAME,))
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
        
