#!/usr/bin/env python
import os

i=0
for i in range(10):

    print("Hi there. time number %s" % i)
    i = i+1
    if i == 5:
        print("Halfway there!")
        f = open("./Izzy.txt", "w")
        f.write("Bonjour")

exit(0)

