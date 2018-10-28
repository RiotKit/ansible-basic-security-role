Basic Security
==============

Just another security role for Ansible.

Allows to improve security of:
- SSH
- logs (IPv4 anonymization)
- firewall (blocking incoming connections on unknown ports)
- change root password

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
    ssh_port: "6420"
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

    #
    # Firewall
    #
    configure_firewall: true
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
