[![Build Status](https://travis-ci.com/fiaasco/chrony.svg?branch=master)](https://travis-ci.com/fiaasco/chrony)

# Ansible Role: chrony

This role will install and configure chrony.
In the event 'ntp' is still found, it will be stopped and removed.

## Requirements



## Role Variables


Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies


## Examples

Include the role in your playbook:

```
    - hosts: servers
      roles:
         - { role: chrony }
```

## Tags

No tags available.

## License

MIT

## Further Reading



## Author Information

Dieter Verhelst
