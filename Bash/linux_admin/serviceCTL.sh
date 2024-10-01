#!/bin/bash

read -p "Enter service name: " service

state=$(sudo systemctl status $service | grep Active | awk '{print $2}')

if [[ -z "$state" ]]; then
    echo "Invalid service name."
    exit 1
fi

echo "Service '$service' state: $state."

PS3="Select an option for '$service' service: "
options=("Start/restart" "Stop" "Leave at current state")
select opt in "${options[@]}"; do
	case $REPLY in
		1)
			if [[ "$state" == "active" ]]; then
				echo "Starting service '$service'..."
				systemctl start $service
			else
				echo "Restarting service '$service'..."
				systemctl restart $service
			fi
			break
			;;
		2)
			echo "Stopping service '$service'..."
			systemctl stop $service
			break
			;;
		3)
			echo "Leaving process '$service' at current state."
			break
			;;
		*)
			echo "Invalid option."
			;;
	esac
done
