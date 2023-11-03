#!/bin/bash

# not parallel
# xargs: execute a command with piped arguments coming from another command, a file etc.
# i.e. arguments source | xargs command

seq 10 | xargs -n 1 python parallel.py

# parallel: run commands on multiple CPU cores
# parallel: 4 at a time
seq 10 | parallel -j 4 python parallel.py

#command: htop: display dynamic real-time information about running processes