#!/usr/bin/env python

import os
import sys


def find_files(files, dirs=[], extensions=[]):
    new_dirs = []
    for d in dirs:
        try:
            new_dirs += [ os.path.join(d, f) for f in os.listdir(d) ]
        except OSError:
            if os.path.splitext(d)[1] in extensions:
                files.append(d)

    if new_dirs:
        find_files(files, new_dirs, extensions )


logs_files = []
find_files(logs_files, dirs=['/var/log'], extensions=['.log', '.gz'])

for file_path in logs_files:
    print("Processing " + file_path)

    if os.access(file_path, os.W_OK) is not True:
        print(file_path + ' needs to be writable')
        sys.exit(1)

    if ".gz" in file_path:
        os.system("cat " + file_path + " | gunzip | strip-ipv4-address.py | gzip -f > /tmp/.log.cleanup && mv /tmp/.log.cleanup " + file_path)
        continue

    os.system("cat " + file_path + " | strip-ipv4-address.py > /tmp/.log.cleanup && mv /tmp/.log.cleanup " + file_path)
