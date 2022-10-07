#!/usr/bin/env python

from ncclient import manager

HOST = "198.18.134.61"
NETCONF_PORT = "830"
USERNAME = "cisco"
PASSWORD = "cisco!123"

cfg_filter = '''
      <licensing xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-smart-license-cfg">
        <flex-consumption>
          <fcm-enable/>
        </flex-consumption>
      </licensing>
'''

def get_fcm_config():


    with manager.connect(
            host=HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False, device_params={"name":"iosxr"}) as device:
        
        print('\n***NETCONF FCM configuration for device {}***\n'.format(HOST))
        
        print(device.get_config(source="running", filter=("subtree", cfg_filter)))

if __name__ == '__main__':
    get_fcm_config()
