#!/usr/bin/python

import os
import re
import stat

"""
stat.S_IRUSR # Read, user  256
stat.S_IWUSR # Write, user 128
stat.S_IXUSR # Execute, user 64

stat.S_IRGRP # Read, group  32
stat.S_IWGRP # Write, group 16
stat.S_IXGRP # Execute, group 8

stat.S_IROTH # Read, other  4
stat.S_IWOTH # Write, other  2
stat.S_IXOTH # Execute, other  1

stat.S_IRWXU # Read, write, and execute for user  448
stat.S_IRWXG # Read, write and execute for group   56
stat.S_IRWXO # Read, write, and execute for other   7

"""

CHECK_CONDITIONS = [stat.S_IWOTH]

PATTERN = re.compile(r'/proc|/var|/sys|/dev|/run|/tmp')

def walk_dir():
    for root, dirs, files in os.walk('/', topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            if (not (os.path.islink(filename))) and (not PATTERN.findall(root)):
                stats = os.stat(filename)
                check_result = False
                for cond in CHECK_CONDITIONS:
                    if (stats.st_mode & cond):
                        check_result = True

                if check_result:
                    print( filename + " " + oct(stats.st_mode))


walk_dir()


