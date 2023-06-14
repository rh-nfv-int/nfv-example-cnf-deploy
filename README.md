Prerequisites
=============
OpenShift 4 Cluster should be deployed with  additional operators:
 * SR-IOV operator should be deployed and necessary resources for
   `SriovNetworkNodePolicy` and `SriovNetwork` should be created with
   target namespace (default namespace used to deploy example cnf
   is `example-cnf`).

 * Performance Addon operator should be deployed and a `PerformanceProfile`
   should be created.

Application Version
===================
The versions of the different parts of example-cnf (trex-app, trex-server, testpmd containers...) are dynamically extracted from the nfv-example-cnf-catalog. To run properly some tests, make sure you are using a dedicated catalog containing the versions fo the images you want to test.


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
