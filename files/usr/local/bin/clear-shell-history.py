#!/usr/bin/env python3

#
# Clears history files (from Bash, ZSH, PostgreSQL psql, Python, etc.)
# ====================================================================
#   Prevents from leaking passwords typed in shell
#   Should be running as ROOT
#

import os
import sys
import pwd
import subprocess

HISTORY_FILES = ['.bash_history', '.sqlite_history', '.python_history',
                 '.config/psysh/psysh_history', '.psql_history', '.zsh_history']
exit_status = True

for p in pwd.getpwall():
    username = p.pw_name
    homedir = p.pw_dir

    for history_file in HISTORY_FILES:
        path = homedir + '/' + history_file

        if os.path.isfile(path):
            print(' >> Clearing {path}'.format(path=path))

            try:
                with open(path, 'w') as f:
                    f.write('')
            except Exception as exc:
                print(exc)
                exit_status = False

        subprocess.call(['rm', path + '-*.tmp'], stderr=subprocess.DEVNULL)


sys.exit(0 if exit_status else 1)
