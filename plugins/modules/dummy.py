#!/usr/bin/python

DOCUMENTATION = r'''
---
module: dummy

short_description: This is a simply dummy module

version_added: "0.0.1"

description: This is a simply dummy module for demostrative puropses only. 
  The module doesn't do anything, except check if a value is greater than 50.
  If the value is greater than 50, then the module reports a change. If the
  value is below 50, no change is reported.

options:
    number:
        description: The value to check if it's greater than 50.
        required: true
        type: int

author:
    - Jack-Benny Persson (jack-benny@cyberinfo.se)
'''

EXAMPLES = r'''
# Pass in a number
- name: Test a number
  jackbenny.demo.dummy:
    number: 55
'''

RETURN = r'''
number:
    description: The original number passed to the module.
    type: int
    returned: always
    sample: 55
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define arguments to the module
    module_args = dict(
        number=dict(type='int', required=True),
    )

    # create a dict for the result
    result = dict(
        changed=False,
        number=0,
    )
    
    # settings for the module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # the logic for the module
    result['number'] = module.params['number']
    if result['number'] > 50:
        result['changed']=True
    
    # return the result as json
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
