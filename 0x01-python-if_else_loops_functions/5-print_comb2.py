#!/usr/bin/python3
# 10-add.py

for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
