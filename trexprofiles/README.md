Run with TRex profile options
=============================

Related ansible variables:
```
trex_profile_path
trex_profile_name
trex_profile_cm_name
```

Default
------
Without providing any of these paramters, TRex app will run with the default profile.


Profile file
------------

```
trex_profile_path: trexprofiles/simple_3st.py
```

Choose one of trex-core repo profiles
-------------------------------------
TRex repo's default profile files can be used directly by specificing the `trex_profile_name`. Refer
to [trex-core](https://github.com/cisco-system-traffic-generator/trex-core/tree/v2.85/scripts/stl) for
list of available profiles.

```
trex_profile_name: simple_3st.py
```

Creating ConfigMap
------------------

```
oc create configmap cm-test --from-file trexprofiles/simple_3st.py
```

```
trex_profile_name: simple_3st.py
trex_profile_cm_name: cm-test
```
TRex Version
============
Supported with v0.85 TRex release
