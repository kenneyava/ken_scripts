#!/usr/bin/python

import os
import stat

CHECK_CONDITIONS = [stat.S_IWGRP, stat.S_IXGRP, stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH]


def walk_dir():
    for root, dirs, files in os.walk('/var/log', topdown=False):
        # print("files")
        for name in files:
            filename = os.path.join(root, name)
            if not (os.path.islink(filename)):
                stats = os.stat(filename)
                check_result = False
                for cond in CHECK_CONDITIONS:
                    if (stats.st_mode & cond):
                        check_result = True

                if check_result:
                    print( filename + " " + oct(stats.st_mode))


walk_dir()



