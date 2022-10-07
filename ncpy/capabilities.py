#!/usr/bin/env python

from ncclient import manager

HOST = "198.18.134.61"
NETCONF_PORT = "830"
USERNAME = "cisco"
PASSWORD = "cisco!123"

# create a get_capabilities() method
def get_capabilities():


    with manager.connect(
            host=HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False, device_params={"name":"iosxr"}) as device:
        
        # print NETCONF capabilities
        print('\n***NETCONF Capabilities for device {}***\n'.format(HOST))
        
        for capability in device.server_capabilities:
            print(capability)

if __name__ == '__main__':
    get_capabilities()
