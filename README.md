Basic Security
==============

Just another security role for Ansible.

**Features:**
- SSH security improvements
- IPv4 addresses anonymization in logs (scheduled every X hours, so the fail2ban can have time to block attackers on time)
- Firewall configuration (blocking incoming connections on unknown ports)
- Change root password
- Scheduled bash, zsh, python (and others) history cleaning, so your passwords will not stay in a history

Does not include fail2ban configuration, as it has a good dedicated role.

```bash
ansible-galaxy install blackandred.server_basic_security
```

Configuration reference
-----------------------

```yamlex
    #
    # SSH
    #
    configure_ssh: true
    ssh_listen: "0.0.0.0"
    ssh_input_port: "6420"
    ssh_gateway_ports: no
    ssh_permit_tunnel: yes
    ssh_password_auth: yes
    ssh_permit_root_login: no
    ssh_host_title: "International Workers Association server"
    ssh_allow_only_specific_users: ""   # type user names here, separated by [space] character
    ssh_idle_time: "1800"

    #
    # Logs IP addresses anonymization
    #
    anonymize_logs: true
    anonymize_logs_schedule:
        minute: 30
        hour: "*"
        day: "*"
        weekday: "*"
        month: "*"
    
    #
    # Clear bash history
    #
    clear_shell_history: false
    clear_shell_history_schedule:
        minute: 30
        hour: "*"
        day: "*"
        weekday: "*"
        month: "*"

    #
    # Firewall
    #
    configure_firewall: true
    # Allow to access 192.168.0.0/16, 172.16.0.0/12 and 10.0.0.0/8 to all {{ firewall_allowed_outgoing_ports }} ports
    firewall_whitelist_local_network_addresses: true 
    firewall_allowed_outgoing_ports:
        - 22
        - 6420
        - 80
        - 443

    #
    # Root password
    #
    change_root_password: true
    root_password: "xxx"
```
