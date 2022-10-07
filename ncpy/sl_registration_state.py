#!/usr/bin/env python

from ncclient import manager

HOST = "198.18.134.61"
NETCONF_PORT = "830"
USERNAME = "cisco"
PASSWORD = "cisco!123"

get_filter = '''
      <smart-agent xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-smartlicense-oper">
        <licensing>
          <state>
            <state-info>
              <registration>
                <registration-state/>
              </registration>
            </state-info>
          </state>
        </licensing>
      </smart-agent>

'''

def get_fcm_config():


    with manager.connect(
            host=HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False, device_params={"name":"iosxr"}) as device:
        
        print('\n***NETCONF FCM Registration {}***\n'.format(HOST))
        print(device.get(filter=("subtree", get_filter)))

if __name__ == '__main__':
    get_fcm_config()
