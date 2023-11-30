#!/bin/bash
# Bash script that makes a request
curl -LX PUT -H "origin:HolbertonSchool" -d "user_id=98" -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
