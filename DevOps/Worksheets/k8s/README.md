# install kubeadm cluster + weave-net CNI on a number of nodes
## install on control plain
- run install-kubernetes-dependencies.sh
- To use the systemd cgroup driver, set plugins.cri.systemd_cgroup = true in /etc/containerd/config.toml.
- use kubeadm init command to initialize the cluster: ( make sure to choose the right subnet, weavenet is preconfigured with 10.244.0.0/16)
```
    sudo kubeadm init \
    --pod-network-cidr=10.244.0.0/16 \
    --cri-socket unix:///run/containerd/containerd.sock \
    --upload-certs 
```
- follow instructions of the init command output
    - copy join command
    - add kubeconfig file to the right path
     
- apply weave.yaml to the cluster:
    - if you changed the init subnet you should change it in weave.yaml in two different places, under: 
    ```
    - name: IPALLOC_RANGE
    value: 10.244.0.0/16
    ```
    ```
    kubectl apply -f weave.yaml
    ```
- execute:
``` 
fix-networking.sh
``` 
    - this script sets up iptables firewall rules to allow communication between a weave internal network interface and an eno1 external network interface in a secure manner. 
    - The script sets up NAT masquerading to hide the internal network topology and allows only authorized traffic between the two interfaces.

  ## install on workers:
- execute:
```
install-kubernetes-dependencies.sh
```
- execute join command
- execute:
```
fix-networking.sh
```

### install ingress-nginx-controller (control plain): 
install ingress-nginx-controller object on cluster by running the command:
```
kubectl apply -f ingress-nginx-controller.yaml
```
install ingress service ( nodeport or loadbalancer ) 
```
kubectl apply -f nodeport.ingress.yaml
or 
kubectl apply -f loadbalancer.ingress.yaml
```

### test ingress:
apply solitaire & 2048 apps, and ingress:
  ```
  kubectl apply -f example-working-apps/solitaire.yaml
  kubectl apply -f example-working-apps/2048.yaml
  kubectl apply -f example-working-apps/ingress-rules.yaml
  ```


##### nodes have ubuntu 20.04 installed
##### guide used to configure this build:
  - https://computingforgeeks.com/deploy-kubernetes-cluster-on-ubuntu-with-kubeadm/
