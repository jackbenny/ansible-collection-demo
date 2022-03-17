# Ansible Collection - jackbenny.demo
This is a simple demonstration of what a collection looks like and works. The
collection is made as a part of my Swedish book about Ansible.

The `base` role installs some common package and sets the timezone according to
the `timezone`-variable. The default timezone is set to Europe/Stockholm. The
`base`-role uses the `update_cache`-role to update the package manager cache.

The `dummy` module demonstrates a simple module and doesn't do anything except
check if a value is greater than 50.

## Content
This collection contains the following:

* roles
  * base
  * update_cache

* modules
  * dummy

## Example usage

```
- hosts: ankeborg
  become: true
  vars:
    timezone: Europe/Stockholm

  tasks:
    - name: Test my dummy module
      jackbenny.demo.dummy:
        number: 51
      register: the_num
    
    - name: Print the return value
      debug:
        msg: "{{ the_num }}"

  roles:
    - jackbenny.demo.base

```

or, if your prefer to use the `collections` keyword:

```
- hosts: ankeborg
  become: true
  vars:
    timezone: Europe/Stockholm

  collections: 
    - jackbenny.demo

  tasks:
    - name: Test my dummy module
      dummy:
        number: 51
      register: the_num
    
    - name: Print the return value
      debug:
        msg: "{{ the_num }}"

  roles:
    - base

```
