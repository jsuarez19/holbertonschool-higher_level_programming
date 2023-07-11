#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    argc = len(argv)
    inf_add = 0
    for i in range(1,argc):
        inf_add += int(argv[i])
    print("{:d}".format(inf_add))
