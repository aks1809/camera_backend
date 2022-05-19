#!/bin/bash
yarn dev &
serve -s build &
cd /python_backend &
yarn dev
wait -n  
exit $?