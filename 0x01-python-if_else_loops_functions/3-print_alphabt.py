#!/usr/bin/python3

# Print the alphabet in lowercase, not followed by a new line
# print all letters except q and e

for alphabet in range(97, 123):
    if chr(alphabet) != 'q' and chr(alphabet) != 'e':
        print("{}".format(chr(alphabet)), end="")
