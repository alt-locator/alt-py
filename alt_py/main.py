import sys


def main():
    """Command line interface for Address Location Tool.

    arguments:
        run method
        environment variable
    """

    run = None
    env = None

    if sys.argv.__len__() >= 2:
        run = sys.argv[1]
        print 'run: ' + run

    if sys.argv.__len__() >= 3:
        env = sys.argv[2]
        print 'env: ' + env


if __name__ == '__main__':
    main()
