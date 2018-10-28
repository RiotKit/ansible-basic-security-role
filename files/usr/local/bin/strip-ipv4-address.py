#!/usr/bin/env python

import re
import sys

ip_addr_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
replaced = re.sub(ip_addr_regex, '1.3.1.2', sys.stdin.read())

print(replaced)
