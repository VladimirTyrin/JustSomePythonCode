#!/usr/bin/python


from sys import argv


def main():
    if len(argv) > 1:
        print "These are my args: %s" % " ".join([arg for arg in argv[1:]])
    else:
        print "No args, sorry :("  


if __name__ == '__main__':
    main()

