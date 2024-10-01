#!/bin/bash

# Create deployment of pod for Nginx container
kubectl apply -f deployment.yaml
kubectl create deployment --image <image_name> weather -o yaml > deployment.yaml

# Display created deployment and existing pods
kubectl get deployments
kubectl get pods

# Expose app to outside of K8s network using service
kubectl apply -f service.yaml

# Connect to service via browser
kubectl get services
kubectl get nodes -o wide
http://192.168.49.2:31637/

# Open minikube dashboard
minikube dashboard

# Delete service
kubectl get services
kubectl delete service test-service

# Deploy weather app
kubectl create deployment weather-app --image devopsgoofy/weather-webapp:latest --replicas=2 -o yaml > webapp-weather.yaml
kubectl get pod
kubectl expose deployment weather-app --type=NodePort --port=5000
minikube service weather-app

# Delete one of the pods
kubectl get pods
kubectl delete pod <pod-name>

# Scale app to 3 replica sets
kubectl scale deployment weather-app --replicas=3

# Display info about the service
kubectl get service
kubectl describe service weather-app

# Restart minikube
minikube delete
minikube start

##################################################################################################################

# Install Kubeadm in EC2 instance and create cluster
sudo apt-get update -y
KUBERNETES_VERSION=v1.30
CRIO_VERSION=v1.30
sudo apt-get install -y software-properties-common curl apt-transport-https ca-certificates curl gpg

# Installing runtime - cri-o
curl -fsSL https://pkgs.k8s.io/addons:/cri-o:/stable:/$CRIO_VERSION/deb/Release.key |     sudo gpg --dearmor -o /etc/apt/keyrings/cri-o-apt-keyring.gpg
sudo apt-get update
sudo apt-get install -y cri-o
echo "deb [signed-by=/etc/apt/keyrings/cri-o-apt-keyring.gpg] https://pkgs.k8s.io/addons:/cri-o:/stable:/$CRIO_VERSION/deb/ /" | sudo tee /etc/apt/sources.list.d/cri-o.list
sudo apt-get update
sudo apt-get install -y cri-o
sudo systemctl start crio
sudo systemctl enable crio
sudo swapoff -a

# Load kernel models on boot
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

# Load modules now
sudo modprobe overlay
sudo modprobe br_netfilter

# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system

# Install kubeadm kubectl and kubelet
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet

# Initialize kubeadm and join nodes
sudo kubeadm init

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

sudo kubeadm join 172.31.47.169:6443 --token ixdek6.ykr8c82q83kr52xz \
	--discovery-token-ca-cert-hash sha256:26acb007a41859100a846eaab6f8246f972497c844b44463fd79d5ea5714b7e6 --cri-socket unix:///var/run/cri-dockerd.sock

# unset KUBECONFIG

kubectl get nodes

kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl edit deploy metrics-server -n kube-system

: <<'END_COMMENT'
    containers:
    	- --kubelet-insecure-tls
    
    spec:
      containers:
      - image: chimenesjr/solitaire:nginx
        imagePullPolicy: IfNotPresent
        name: solitaire
        resources:
          requests:
            cpu: 10m
            memory: 64Mi
END_COMMENT

kubectl get pods --all-namespaces

kubectl create deployment solitaire --image chimenesjr/solitaire:nginx --replicas=1 -o yaml > solitaire.yaml
kubectl autoscale deployment solitaire --cpu-percent=50 --min=1 --max=10
kubectl expose deployment solitaire --type=NodePort --port=80 -o yaml > service.yaml

kubectl get hpa -w

sudo apt install siege -y
sudo siege -c 50 -t1M http://172.31.47.169:6443


