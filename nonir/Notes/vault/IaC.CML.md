---
id: fVxbyNVkcymgyk9yib3BT
title: CML
desc: ''
updated: 1644804288064
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
    
## Tool Familiarization

- **Dashboard**
    The Dashboard shows you all the labs that exsist on the CML Controller. You can add as well as import lab files here.

- **Add nodes**
    While in a lab, there is a tab on the right side that will allow you to add nodes. CML comes pre-loaded with all kinds of Cisco Products from CSRs to ASAs to Nexus products.

- **Lab toolbar**
    If you aren't currently in a node, there are a few options for the lab:
    - **Lab Info:** Gives you a high-level view of the lab including Lab Description, total nodes, total interfaces, and current number of links in lab.
    - **Simulate:** You can Start/Stop the lab, Download the lab.yml file, and wipe the lab from here.
    - **Nodes:** From the nodes tab you get a health check of the nodes. You can also select which nodes you want to include in the lab.yml file and export them. You can Start/Stop/Wipe individual nodes from here as well.
    - **Design:** You can set default bootstrap parameters here for supports devices.
    - **Logs:** Yep, Logs.
    - **Lab Notes:** NOTES! And yes, it's in MARKDOWN!

- **Breakout**
    The breakout tool is what allows us to reach out programmatically to devices within the lab. It will take the ip where the breakout executable exsists and attaches a different port depedning on the device.
    
    The breakout tool allows you to use putty, SecureCRT, blah blah blah. But we want it for Ansible and Python!

    Once you open a CML, go to Tools -> Breakout Tool. In the documentation theres a download section with the breakout section. Along with [ this ](https://oznetnerd.com/2020/06/26/network-automation-with-cml2/) to help configure your workstation.

    After its all said and done, heres a code snippit using netmiko to interface with CML:
    ```python
    from netmiko import ConnectHandler

    breakout_host_ip = "192.168.20.3"
    cmd = "show ip int brief"

    iosv_1 = {
        "device_type": "cisco_ios_telnet",
        "host": breakout_host_ip,
        "port": 9000,
        "global_delay_factor": 2,
    }

    print(f"Connecting to: {host_ip}...")
    net_connect = ConnectHandler(**iosv_1)
    print("Connected!")
    print(f"Executing command:\n{cmd}")
    sh = net_connect.send_command(cmd)
    print(sh)
    ```