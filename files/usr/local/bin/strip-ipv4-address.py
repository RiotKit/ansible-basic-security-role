#!/usr/bin/env python3

import re
import sys

line = sys.stdin.read()

try:
    ip_addr_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    replaced = re.sub(ip_addr_regex, '1.3.1.2', line)
except UnicodeDecodeError:
    print(line)
    sys.exit(1)

print(replaced)
