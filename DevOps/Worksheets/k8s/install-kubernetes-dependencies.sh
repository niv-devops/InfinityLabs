# Install - kubeadm
# Install depedencies
sudo apt -y install curl apt-transport-https
# Get repository key
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
# Install kubectl kubeadm kubelet + dependencies
sudo apt -y install vim git curl wget kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
# Check version
kubectl version --client && kubeadm version
# Disable swap
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo swapoff -a
sudo mount -a
# Enable kernel modules
sudo modprobe overlay
sudo modprobe br_netfilter
# Add some settings to sysctl and reload sysctl
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
sudo sysctl --system


# Install container runtime - Containerd
# Configure persistent loading of modules
sudo tee /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF
# Load at runtime
sudo modprobe overlay
sudo modprobe br_netfilter
# Ensure sysctl params are set
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
# Reload configs
sudo sysctl --system
# Install required packages
sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates
# Add Docker repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# Install containerd
sudo apt update
sudo apt install -y containerd.io
# Configure containerd and start service
mkdir -p /etc/containerd
# reconfigure


#sudo chmod 777 /etc/containerd
sudo containerd config default > /temp
sudo rm -rf /etc/containerd/config.toml
sudo mv /temp /etc/containerd/config.toml
# restart containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
sudo systemctl enable kubelet.service

# install nfs dependencies
sudo apt install nfs-kernel-server

sudo systemctl enable kubelet
