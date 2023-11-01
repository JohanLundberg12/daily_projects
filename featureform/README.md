
Today I am learning about AWS, Kubernetes (K8s), docker, ssh, minikube and maybe featureform. I am also setting up some neovim config files for future documentation (lua).

### What is x:

* Minikube: Create virtual machine on your local machine.
* Container runtime: Docker (default choice of k8s) and included in the minikube distribution.
* Today I set up my AWS account and went through some initial guides. This is to set up kubernetes in the future. However, for now I'm using Minikube, which does not require AWS. 
* Featureform: A store for your features (duh).


### Useful Commands

As always (tldr for quick explanations).

minikube start: Start your local cluster

minikube status: Obvious.

minikube dashboard: UI to manage clusters and deploy applications. Gives an overview of cluster operations and make it easier to modify resources. 

minikube ssh: To ssh into the minikube VM.

kubectl: Kubernetes' CLT to interact with the cluster.


### In depth explanations

* Minikube: Utility to run k8s on local machine. Creates a single node cluster in a VM. We can demo k8s operations without the time and resources of a real k8s installation.

* Kubernetes Concepts:
** Deployment: Configured and operational resources. The overall processes that enable us to orchestrate resources. 
** ReplicaSet: Set of pods which provide resources for my services.
** Pod: A unit containing one or more containers + storage resources and config defitions. Grouped together in replica sets. All pods in a set run the same container images. 
** Node Cluster: Control plane and worker nodes, containing 1 or more pods. Control plane orchestrates the workers, the workers run my workloads. This is created by Minikube. 
** Node Processes: Various components used to connect and manage Kubernetes. 
** Container: The image told to hold my applications. 

: Various components used to connect and manage Kubernetes. 
** Container: The image told to hold my applications. 


### nvim configs

Additions to the vim file include the use of:
* Making " " a mapleader "<leader>" and pv an alias for vim.cmd.Ex
** vim.cmd.Ex takes us to the default vim file tree
* Pluging manager: Packer
* Fuzzy finder: Telescope 
* <leader>pf -> file search
* <leader>ps -> word search
* rose-pine color scheme
* Treesitter -> highlighting


### nvim commands
(in command mode)
* shift=+enter -> align text
* so: Shout it out (source)
* PackerSync -> run this when you make changes to plugin configurations
* <leader>pf -> builtin.find_files() search
* <C-p> -> builtin.git_files search
* <leader>ps -> grep_string search = vim.fn.input("Grep > ") (search for words in files from vim

