#!/usr/bin/env python3

import os
import sys


def find_files(files, dirs: list = []):
    new_dirs = []
    for d in dirs:
        try:
            new_dirs += [ os.path.join(d, f) for f in os.listdir(d) ]
        except OSError:
            files.append(d)

    if new_dirs:
        find_files(files, new_dirs)


logs_files = []
find_files(logs_files, dirs=['/var/log'])

for file_path in logs_files:
    print("Processing " + file_path)

    if os.access(file_path, os.W_OK) is not True:
        print(file_path + ' needs to be writable')
        sys.exit(1)

    if file_path.endswith('.gz'):
        os.system(
            'zcat "{file_path}" | strip-ipv4-address.py | gzip -f > /tmp/.log.cleanup && mv /tmp/.log.cleanup "{file_path}"'
            .format(file_path=file_path)
        )
        continue

    if file_path.endswith('.xz'):
        os.system(
            'xzcat "{file_path}" | strip-ipv4-address.py | xz -f > /tmp/.log.cleanup && mv /tmp/.log.cleanup "{file_path}"'
            .format(file_path=file_path)
        )
        continue

    os.system(
        'cat "{file_path}" | strip-ipv4-address.py > /tmp/.log.cleanup && mv /tmp/.log.cleanup "{file_path}"'
        .format(file_path=file_path)
    )
