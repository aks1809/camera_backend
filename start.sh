#!/bin/bash
yarn dev &
serve -s build &
wait -n  
exit $?