#!/usr/bin/python3
def main():
    print('{} argument'.format(len(argv) - 1), end='')
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print("{:d} argument".format(len(argv) - 1), end="")
    else:
        print("s:")
    for i in range(1, len(argv)):
        print('{}: {}'.format(i, argv[i]))

if __name__ == "__main__":
    from sys import argv
    main()
