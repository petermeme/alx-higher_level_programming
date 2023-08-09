#!/usr/bin/python3
for num in range(0, 8):
    for num2 in range(num + 1, 10):
         print("{}{}".format(num, num2), end=", ") 
print("{}{}".format(num + 1, num2))
