#!/usr/bin/env python

from ncclient import manager
import xmltodict


NETCONF_PORT = "830"
USERNAME = "cisco"
PASSWORD = "cisco!123"
HOSTS = ["198.18.134.60", "198.18.134.61"]


get_filter_auth = '''
      <smart-agent xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-smartlicense-oper">
        <licensing>
          <state>
            <state-info>
              <authorization>
                <authorization-state/>
              </authorization>
            </state-info>
          </state>
        </licensing>
      </smart-agent>
'''

get_filter_registration = '''
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

def fcm_report(HOST):


    with manager.connect(
            host=HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False, device_params={"name":"iosxr"}) as device:
            
        
          reply = device.get(filter=("subtree", get_filter_registration)).data_xml
          xml_dict = xmltodict.parse(reply)
          register_state = xml_dict["data"]["smart-agent"]["licensing"]["state"]["state-info"]["registration"]["registration-state"]

          reply = device.get(filter=("subtree", get_filter_auth)).data_xml
          xml_dict = xmltodict.parse(reply)
          auth_state = xml_dict["data"]["smart-agent"]["licensing"]["state"]["state-info"]["authorization"]["authorization-state"]

          print(f"{HOST:<15} | {register_state :<25} | {auth_state:<40}")


if __name__ == '__main__':
  print(f"{'Device':<15} | {'FCM Registration':<25} | {'FCM Status':<40}")
  print("----------------------------------------------------------------")
  for h in HOSTS:
    fcm_report(h)
