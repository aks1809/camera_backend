#!/bin/bash
yarn dev &
serve -s build &
/python_backend/yarn dev &
wait -n  
exit $?