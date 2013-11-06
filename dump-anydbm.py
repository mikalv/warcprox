#!/usr/bin/python
# vim:set sw=4 et:
#

"""
Dump contents of database to stdout. Database can be any file that the anydbm
module can read. Included with warcprox because it's useful for inspecting a
deduplication database or a playback index database, but it is a generic tool.
"""

import anydbm
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: {} DBM_FILE\n".format(sys.argv[0]))
        exit(1)

    # import whichdb
    # which = whichdb.whichdb(sys.argv[1])
    # print('{} is a {} db'.format(sys.argv[1], which))

    db = anydbm.open(sys.argv[1])

    for key in db.keys():
        print("{}:{}".format(key, db[key]))
