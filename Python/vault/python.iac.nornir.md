---
id: RdVFFQgV8VpVXWfgqUea7
title: Nornir
desc: ''
updated: 1644253701645
created: 1644251922377
---

<sum>These are all the notes regarding the python framework Nornir.</sum>

### Nornir is a python framework for network automation. It takes preexsisiting automation packages such as netmiko and ncclient and structures it for larger enviroments. ###

## When comparing Nornir and Ansible the differences include: ##
    - Speed
        - Nornir has the ability to specify the amount of workers in the configuration. This number can scale along side network requirements.
    - Pythonic
        - Nornir is python so we also have the ability to leverage the entire Python library making Nornir more flexible.
        - Can be integrated into other python frameworks such as Flask or Django

## Commonalities include: ##
    - Inventory
        - Nornir and Ansible both can recieve dynamic inventories from various Sources Of Truth (SoT).
        - Nornir can use an inventory from Nautobot or even an anbile Host/Group files.
    - Playbooks/Runbooks
        - Ansible and Nornir both use task based scripts. While Ansible playbooks are written in YAML, Nornir runbooks are Python functions.
    - Clientless
        - Both solutions are clientless and depend on SSH sessions.
    
