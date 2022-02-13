---
id: fVxbyNVkcymgyk9yib3BT
title: CML
desc: ''
updated: 1644789802563
created: 1644771587177
---

## Cisco Modeling Labs
**Note:**
- CML Personal Allows 20 nodes

- CML Personal Plus Allows 30 nodes

**Additional info can be found here:**

[ _Cisco Modeling labs_ ](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html)

## Setting Up CML

When setting up CML you will need the Reference Platform ISO (refplat) and the Controller OVA for the VM.

The Controller ova will contain CML and the ISO will allow labs to be built.

**Heres a step-by-step deployment guide:**

[ Steps and requirements for deploying CML ](https://developer.cisco.com/docs/modeling-labs/#!deploying-the-ova-file-on-vmware-workstation-fusion)

Local CML Creds:

admin P@ssw0rd12

## Troubleshooting:
- Make sure VM has access to internet. I bridged my connection
- If having issues with registration, try:
    - $ curl https://tools.cisco.com/its/service/oddce/services/DDCEService
        - This should return output
    - Login to the Cockpit (https://n.n.n.n:9090)
        - -> CML2 -> Maintenance -> Restart Controller Services 
    