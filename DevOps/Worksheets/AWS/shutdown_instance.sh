#!/bin/bash

INSTANCE_IDS=$(aws ec2 describe-instances \
    --query "Reservations[*].Instances[*].InstanceId" \
    --filters Name=instance-state-name,Values=running,pending \
    --output text)

if [ -n "$INSTANCE_IDS" ]
then
    echo "Stopping instances: $INSTANCE_IDS"
    aws ec2 stop-instances --instance-ids $INSTANCE_IDS
else
    echo "No running instances found."
fi

####################################
#                                  #
#   Excute and add cronjob         #
#                                  #
####################################
chmod +x shutdown_instances.sh
crontab -e
25 18 * * * ~/InfinityLabs/DevOps/AWS_WS/shutdown_instances.sh

# Add to crontab:
aws ec2 stop-instances --instance-ids $(aws ec2 describe-instance-status --include-all-instances --filters "Name=instance-state-name,Values=running,pending" --query "InstanceStatuses[].[InstanceId]" --output text | tr '\n' ' ')
