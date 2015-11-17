#!/bin/sh

#create a directory for log files
mkdir -p log
pushd log

# list of spawned processes
pidlist=()

# start robocup server
rcsoccersim &

# add robocup server to pidlist
pidlist+=($!)
echo "SOCCERSIM $!"

# wait before spawning clients 
sleep 1

# spawn our client
python ../main.py &
echo "CLIENT $!"

# add main client to pidlist
pidlist+=($!)

# spawn an opponent
case $1 in
    # run simulator with full team of 'dumb' opponents
    dummy)
    python ../opponent.py &
    # add opponent client to pidlist
    pidlist+=($!)
    ;;

    # run simulator with no opponents
    *) 
    #do nothing
    ;;
esac

echo "Waiting for RoboCup Server to exit..."
wait ${pidlist[0]}

echo "Sending SIGINT to RoboCup Clients..."
unset pidlist[0]
for pid in ${pidlist[@]}; do
    echo "  SIGINT: $pid"
    kill -2 $pid
done 

popd

sleep 1
