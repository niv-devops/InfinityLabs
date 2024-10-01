#!/bin/bash

netstat -lpx | awk '{print $8, $9, $10}' | column -t
