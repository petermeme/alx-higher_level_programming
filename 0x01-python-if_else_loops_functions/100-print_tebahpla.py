#!/usr/bin/python3

# Print the alphabet in lowercase, not followed by a new line.

for alphabet in(reversed (range(97, 123))):
    if alphabet % 2 != 0:
        alphabet = alphabet - 32
    print("{:c}".format(alphabet), end="")
