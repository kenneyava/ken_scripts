#!/usr/bin/python

import os
import re
import pwd
import grp

PATTERN = re.compile(r'^/boot|^/etc|^/proc|^/usr|^/var|^/sys|^/dev|^/run|^/tmp|^/opt')

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
                    print( filename + " uid: " + str(stats.st_uid))

                try:
                    gid = grp.getgrgid(stats.st_gid).gr_name
                except Exception as e:
                    print( filename + " gid: " + str(stats.st_gid))                


walk_dir()