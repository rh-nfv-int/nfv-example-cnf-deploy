#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: parse_trex_logs 

short_description: Organize packet missing logs

version_added: "2.9"

description:
    - Organize the packet missing and recovery logs to find packet loss

options:
    path:
        description:
            - TRex Applications log file path where PacketMated and PacketDrop are captured
        required: true
        type: str
    strict:
        description:
            - Whether to uset strict checking on events or ignore short differences
        required: false
        type: boolean
        default: false

author:
    - Saravanan KR (@krsacme)
'''

EXAMPLES = '''
# Parse event list
- name: prase trex log file
  parse_trex_log:
    path: run-trex.log
    strict: no

'''

RETURN = '''
message:
    description: The output message that the test module generates
    type: str
    returned: always
missing:
    description: List of instances where the packet missing is observed
    type list
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from dateutil.parser import parse

def get_missing_list(module, result):
    log_path = module.params['path']
    strict = module.params['strict']
    combine = []
    with open(log_path) as f:
        for line in f:
            if "PacketMatched" in line:
                obj = {}
                obj['reason'] = 'PacketMatched'
                obj['eventTime'] = line.split(' at ')[1].rstrip()
                combine.append(obj)
            elif "PacketDrop" in line:
                obj = {}
                obj['reason'] = 'PacketDropped'
                obj['eventTime'] = line.split(' at ')[1].rstrip()
                combine.append(obj)
    if combine[0]['reason'] == 'PacketMatched':
        del combine[0]
    if combine[0]['reason'] != 'PacketDropped':
        result['message'] = "First event should be dropped"
        return False

    missing = []
    for i in range(0, len(combine), 2):
        if combine[i]['reason'] != 'PacketDropped':
            result['message'] = ("Resson %s is not valid" % combine[i]['reason'])
            return False

        # Handle when the last event is PacketDropped (no recovery event)
        if len(combine) == (i + 1):
            missing.append({'start': combine[i]['eventTime'], 'duration': -1})
            result['warning'] = "Last event is dropped"
            break

        if combine[i + 1]['reason'] != 'PacketMatched':
            result['message'] = ("Reason %s is not valid for followed event" % combine[i + 1]['reason'])
            return False

        dropped_time = parse(combine[i]['eventTime'])
        matched_time = parse(combine[i + 1]['eventTime'])
        diff = matched_time - dropped_time
        diff_seconds = diff.total_seconds()
        if not strict and int(diff_seconds) <= 1:
            continue
        obj = {}
        obj['start'] = combine[i]['eventTime']
        obj['duration'] = diff_seconds
        missing.append(obj)

    result['missing'] = missing
    if missing:
        result['message'] = "Packet miss found"
    elif not strict and missing:
        result['message'] = "No packet miss during migration"
    else:
        result["message"] = "No packet miss"
    return True


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        strict=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        missing=[],
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )


    result['strict'] = module.params['strict']
    response = get_missing_list(module, result)
    if response:
        result['changed'] = True
    else:
        result['failed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

