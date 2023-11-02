
Today I am learning about AWS, Kubernetes (K8s), docker, ssh, minikube and maybe featureform. I am also setting up some neovim config files for future documentation (lua).

### What is x:

* Minikube: Create virtual machine on your local machine.
* Container runtime: Docker (default choice of k8s) and included in the minikube distribution. It needs a linux system to run, therefore it needs a runtime like docker.
* Today I set up my AWS account and went through some initial guides. This is to set up kubernetes in the future. However, for now I'm using Minikube, which does not require AWS. 
* Featureform: A store for your features (duh).


### Useful Commands

As always (tldr for quick explanations).

minikube start: Start your local cluster

minikube status: The internal component status for every component of minikube and k8s. 

minikube dashboard: UI to manage clusters and deploy applications. Gives an overview of cluster operations and make it easier to modify resources. 

minikube ssh: To ssh into the minikube VM.

kubectl: Kubernetes' CLT to interact with the cluster.

minikube [COMMAND] [COMMAND] --help: Learn more about a command. 

minikube stop

minikube stop -all

minikube pause

minikube delete -all


### In depth explanations

* Minikube: Utility to run k8s on local machine. Creates a single node cluster in a VM. We can demo k8s operations without the time and resources of a real k8s installation.

- minikube profile list: Will list all the clusters created on the local machine. It will show the driver runtime type(docker etc.), IP, K8s version, number of nodes, active or no, port. 

* minikube profile list -o="table" or "json" etc.: Get output in various formats.

* minikube node add: Add another worker node to our cluster with the same settings as the other node (use --help to learn how to change settings).


* Kubernetes Concepts/Terminology:
** Container: The image told to hold my applications. 
** Pod: A group of containers (the smallest unit that Kubernetes administers). They have a single IP and share memory and resources, storage, configs. Thus is treated as a single application. Common to a 1 pod with 1 container, but multi-container pods ease deployment.
** ReplicaSet: Set of pods which provide resources for my services.

** Deployments: Defines the scale of an application through the details of how pods should be replicated on Kubernetes' nodes. Describe number of identical pod replicaas, preferrred update strategy, pod health.

** Services: An abstraction over the pods. Ensures that, to the outside network, everything appears to be unchanged. I.e. as pods are replaced (they are unreliable) their internal names and IPs might change, but only internally. A service is the interface over the pods whwich various application consumers interact with.

** Nodes: Manages and runs pods; it's the machine (virtual or physical). A node collects entire pods. We usually hand work over to a node whose pods are free to take it.

** Control Plane: main entry point for admins and users to manage various nodes. Operations are issued to it through HTTP or CLI scripts.

** Cluster: All above components put together.

Control Plane Components:
- API Server: exposes a REST interface to Kubernetes cluster. 
- Scheduler: Responsible for assigning work to the various nodes. 
- Controller Manager: Makes sure that the state of the cluster is operating as expected. I.e. oversees controllers which responds to events (e.g. a node goes down).


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

