'''
All credits go to this chad: https://github.com/davidbombal/red-python-scripts/blob/main/windows10-wifi.py

This scripts is deviated from this script above
'''

import re
import subprocess

print('Getting all the wifi ssid....')

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

#print(command_output)

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

#print(profile_names)

wifi_info_list = []

if(len(profile_names) != 0):
    for name in profile_names:
        wifi_info = {}

        #profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        pass_info = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
        password_info = re.search("Key Content            : (.*)\r", pass_info)
        
        #print(type(password_info))
        if(password_info is not None):
            wifi_info["ssid"] = name
            wifi_info["password"] = password_info[1]
            
        wifi_info_list.append(wifi_info)

print(wifi_info_list)
	