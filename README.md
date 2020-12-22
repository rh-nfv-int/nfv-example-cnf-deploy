Prerequisites
=============
OpenShift 4 Cluster should be deployed with  additional operators:
 * SR-IOV operator should be deployed and necessary resources for
   `SriovNetworkNodePolicy` and `SriovNetwork` should be created with
   target namespace (default namespace used to deploy example cnf
   is `example-cnf`).

 * Performance Addon operator should be deployed and a `PerformanceProfile`
   should be created.

Label the nodes before deploying the example cnf:
```
oc label node worker-0 examplecnf.openshift.io/trex=""
oc label node worker-1 examplecnf.openshift.io/testpmd=""
oc label node worker-1 examplecnf.openshift.io/lb=""
```
NOTE: Role `example-cnf-labels` will label the nodes, if it needs to be automated.


Deploy
======

In order to deploy images from quay.io registry, provide extra vars file
```
K8S_AUTH_KUBECONFIG=kubeconfig ansible-playbook create.yaml --extra-vars @quay-repo-v2.yaml
```

Other Deploy Options
--------------------

By default, it deploys for the cluster5 of dallas lab
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook create.yaml
```

In order to deploy for cluster6, add an additional parameter
```
K8S_AUTH_KUBECONFIG=../kubeconfig ansible-playbook create.yaml -e cluster_name=cluster6
```

In order to deploy TestPMD only from quay.io registry, provide extra vars file as
```
K8S_AUTH_KUBECONFIG=kubeconfig ansible-playbook create.yaml --extra-vars @quay-repo-v0.2.yaml -e enable_trex=false -e enable_lb=false
```
