#!/usr/bin/env python
#

#
# Converts text file with plain text file to hashed format
#
#
# (c) 2019  Danwand N S <Titanium Hitler>
# co-created by Abhinand N S <> github.com/abhi-nvr-quits
import hashlib
import os

from optparse import OptionParser


def main():
	with open('a.txt', 'r') as afile:
		fo = open("b.txt","w")
		c=0
		for i in afile:
			#print(i,j)
			result = hashlib.md5(str.encode(i))
			#print(result.hexdigest())
			fo.write(result.hexdigest())
			fo.write("\n")
			c = c+ 1
			print("count : " + str(c))

		fo.close()

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]... ")

    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
		
        exit(1)


    for arg in args:
        if os.path.isfile(arg):
            main()




