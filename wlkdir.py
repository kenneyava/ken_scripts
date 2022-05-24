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

    # print("dirs")
    # for name in dirs:
    #     print(os.path.join(root, name))

# 0100640

# print(oct( os.stat('/var/log/messages').st_mode & stat.S_IRUSR & stat.S_IWUSR ))

# if os.stat('/var/log/messages').st_mode & stat.S_IRUSR & stat.S_IWUSR:
#     print("true")
# else:
#     print("false")

"""
https://www.tutorialspoint.com/python/os_walk.htm

https://www.deepanseeralan.com/tech/checking-file-permissions-in-python/
https://www.devdungeon.com/content/working-files-and-directories-python#toc-9
https://stackoverflow.com/questions/5337070/how-can-i-get-the-unix-permission-mask-from-a-file/5337329#5337329

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

& and | works like and and or
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
2 & 1 = 0
3 & 1 = 1
2 | 1 = 3

"""