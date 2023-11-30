#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -o /dev/null -sw "You got me!" -L -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
