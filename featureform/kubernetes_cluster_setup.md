### How to being with AWS & Kubernetes with EKSCTL

Here I retrace my steps of how to setup a cluster and get started with it. 
This is based on following the guide: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
& https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html

It is better to follow those guiden rather than I could make. 

Things you need to to:

1. Start your journey with AWS: https://aws.amazon.com/getting-started/?ref=docs_gateway
    - Learn best practices: https://aws.amazon.com/getting-started/guides/setup-environment/
    - Get to know the AWS Management Console: https://aws.amazon.com/getting-started/hands-on/getting-started-with-aws-management-console/
2. Now to setup AWS CLI on your machine: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
    - See prerequisites: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html
    - Install: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
3. Now follow this to configure the AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
4. Authenticate access: https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html
    - Do: aws configure sso
    - You need Command line programmatic access 

At this point you should be able to run:
```
aws --version
```
You should also have a config file in ~/.aws/config and credentials in ~/.aws/credentials.

5. Install kubectl: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
6. Install eksctl: https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
7. To check current user, run:
```
aws sts get-caller-identity
```

8: Before we create the cluster, we also need to ensure that this command works: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
```
aws-iam-authenticator
```


9. Create cluster (replace "region-code" with other, i.e. eu-north-1) (this takes a few minutes, grab a coffee):
```
eksctl create cluster --name my-cluster --region region-code
```
Note: A file in ~/.kube/config is created which have information about the cluster. 

10. Once it's done, check it on aws: https://console.aws.amazon.com/cloudformation

11. Sanity check, run from your command line:
```
kubectl get nodes
```

Final note: Consider installing kubectl using brew. And if there is trouble using kubectl, try specifying the absolute path when executing commands such as "kubectl get nodes". In my case, it was in /home/linuxbrew/.linuxbrew/bin/kubectl.  







