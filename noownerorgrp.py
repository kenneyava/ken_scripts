#!/usr/bin/python

import os
import re
import pwd

PATTERN = re.compile(r'^/proc|^/var|^/sys|^/dev|^/run|^/tmp')

def walk_dir():
    for root, dirs, files in os.walk('/', topdown=False):
        # print("files")
        for name in files:
            filename = os.path.join(root, name)
            if (not (os.path.islink(filename))) and (not PATTERN.findall(root)):  
                stats = os.stat(filename)
                try:
                    uid = pwd.getpwuid(stats.st_uid).pw_name
                except Exception as e:
                    print( filename + " " + stats.st_uid)


walk_dir()