
By default, it deploys for the cluster5 of dallas lab
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook playbook.yaml
```

In order to deploy for cluster6, add an additional parameter
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook playbook.yaml -e cluster_name=cluster6
```
