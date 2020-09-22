
By default, it deploys for the cluster5 of dallas lab
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook create.yaml
```

In order to deploy for cluster6, add an additional parameter
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook create.yaml -e cluster_name=cluster6
```

In order to deploy images from quay.io registry, provide extra vars file
```
K8S_AUTH_KUBECONFIG=kubeconfig ansible-playbook create.yaml --extra-vars @quay-repo.yaml
```

In order to deploy TestPMD only from quay.io registry, provide extra vars file as
```
K8S_AUTH_KUBECONFIG=kubeconfig ansible-playbook create.yaml --extra-vars @quay-repo.yaml -e enable_trex=false
```
