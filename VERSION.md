Operator vs Application Version Mapping
=======================================

| Operator 	| App 		| Deploy Script 	|
|-------- --|-------|----------------|
| v0.1.0	| v0.1.3	| v0.1		   |
| v0.2.0	| v0.2.0	| v0.2  	  |
| v0.2.1	| v0.2.0	| v0.2-1	  |
| v0.2.2	| v0.2.1	| v0.2-2  	|
| v0.2.2	| v0.2.1	| v0.2-3  	|


Deploy Scripts Highlighs
------------------------
This repository which hosts the ansible roles and playbooks required to deploy Example CNF test methodology. This sections highlights major changes with versions:

* v0.2-3
  * CNF app is now based on the OpenShift's default dpdk-base image, instead of a custom image. testpmd-operator has been updated in v0.2.2 version to support this deployment
  * Upgrade roles and playbooks are added to demonsrate example cnf methodology with OCP upgrade

* v0.2-2 (tag)
  * Earlier mac fetch is done as part of the CNF application. Inorder to reduce the CNF app functionality, mac fetch is removed from CNF app and exectued externally whenever a CNF app pod is created
  * TRex profile is configurable via new crd TRexApp, with which an existing TRex repo's profile can be used or a provifile py file can be provided as input via configmap
  * Multiple TRex apps can be created for each test scenario, as long as the duration is a finite value, the test will complete and move on to the next one

* v0.2-1 (tag)
  * Explicit labels removed and using of podAffinity and podAnitAffinity

* v0.2 (branch)
  * LB (packet distributor) is added to support multiple CNF applications
