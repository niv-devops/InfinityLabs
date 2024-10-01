#!/bin/bash

ESXI_USER="devops"
ESXI_HOST="10.1.2.23"
ESXI_PSWD="Student2021!"
VMID="21"

sshpass -p "$ESXI_PSWD" ssh -o StrictHostKeyChecking=no "$ESXI_USER@$ESXI_HOST" << EOF
vm_m=\$(vim-cmd vmsvc/getallvms | awk 'NR>1{print \$1}')
stat1=\$(vim-cmd vmsvc/power.getstate "$VMID" | grep "Powered off")
if [ "\$stat1" == "Powered off" ]; then
    echo "Powering on machine $VMID..."
    vim-cmd vmsvc/power.on "$VMID"
else
    echo "Machine $VMID already running."
fi
EOF

# Add cronjob to execute this script every hour
# sudo crontab -e
# 0 * * * * /home/niv/InfinityLabs/DevOps/VMware_WS
