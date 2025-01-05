# EKS Cluster Module

This module creates an Amazon EKS (Elastic Kubernetes Service) cluster to manage and orchestrate containerized applications using Kubernetes.

## Features

- Creates an EKS cluster with configurable settings.
- Supports node group creation.
- Configurable IAM roles for cluster and node group access.
- Outputs the cluster name, endpoint, and kubeconfig details.

### Inputs

| Name                           | Description                                              | Type             | Default  |
|--------------------------------|----------------------------------------------------------|------------------|----------|
| `cluster_name`                 | Name of the EKS cluster                                  | `string`         | `null`   |
| `subnet_ids`                   | List of subnet IDs for EKS cluster nodes                | `list(string)`   | `[]`     |
| `desired_capacity`             | Desired number of nodes in the node group               | `number`         | `1`      |
| `max_capacity`                 | Maximum number of nodes in the node group                | `number`         | `5`      |
| `min_capacity`                 | Minimum number of nodes in the node group                | `number`         | `1`      |

### Outputs

| Name                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `cluster_name`           | The name of the EKS cluster                      |
| `cluster_endpoint`       | The endpoint of the EKS cluster                  |
| `kubeconfig`             | Kubeconfig file for accessing the cluster       |

## Usage

Include this module in your Terraform configuration, edit the cluster's name, subnets IDs, desired and min/max capacities for node group in `variables.tf`.
