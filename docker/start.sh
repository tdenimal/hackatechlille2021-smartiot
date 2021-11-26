#!/bin/bash

# Start the first process
source /root/.bashrc && jupyter server extension disable nbclassic &&  jupyter lab --allow-root --ip 0.0.0.0 &
  
# Start the second process
source /root/.bashrc && cd /app/pybridge && git checkout python && python server.py &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?
