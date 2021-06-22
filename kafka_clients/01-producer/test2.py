
#! /usr/bin/env python3

import sys

def main(arg):
    print(arg)

if __name__ == '__main__':
    var = 0

    if len(sys.argv) != 2:
        var = 2
    else:
        var = sys.argv[1]

    main(var)