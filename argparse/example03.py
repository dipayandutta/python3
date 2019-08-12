import sys
from subprocess import run
def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <command>" %(argv[0]),)
        return 1

    else:
        print(argv[1])
        output = run(argv[1:])
        print (output)
if __name__ == '__main__':
    main(sys.argv)
