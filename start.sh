#!/bin/bash
pm2-runtime "yarn dev"
wait -n  
exit $?