#!/usr/bin/python
from subprocess import *
import re
import shlex
import sys
import os

def find_dscan():
        p1 = Popen(['tail', '-n', '5000', '/var/log/apache2/other_vhosts_access.log'], stdout=PIPE)
        p2 = Popen(['grep', '-E', 'sql|SQL|myadmin|phpMy|jenkins|hudson|jmx|manager|msd|blackcat|pma|dump|w00t|script|qq.com|proxy|Survey|scan|cgi-bin|spider|wp-|radar'], stdin=p1.stdout, stdout=PIPE)
        output = p2.communicate()[0].split('\n')

        ip_list = []
        for i in output:
                result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", i)
                if len(result):
			"""Add your IP(s) below to avoid being blacklisted"""
			if result[0] != 'xxx.xxx.xxx.xxx':
				ip_list.append(result[0])

	return set(ip_list)

print "Forcing IP banning..."
for ip in find_dscan():
        input = "iptables -A INPUT -s " + ip + " -j DROP"
        wrtng = 'echo "' + ip + '" >> bannedips'
        os.system(wrtng)
	wrtng = 'echo "$(sort -u bannedips)" > bannedips'
	os.system(wrtng)
        Popen(shlex.split(input))
sys.exit(0)
