#!/usr/bin/env python
import os, sys, statvfs
container = '/path/to/container'
mount_point = '/path/to/mount/point'
#Charsets are
#range(48, 58)  --> [0-9]
#range(97, 123) --> [a-z]
#range(65, 91)  --> [A-Z]
#[n,n,n]	--> special chars
Chars = range(48, 58) + range(97, 123) + range(65, 91) + [39,45,58]

def checkPassword(password):
	result = os.system("truecrypt --text --non-interactive " + container + " " + mount_point + " -p" + password.replace("'", "\\'"))
	if result == 0:
		print "*** Found [" + password + "]"
		f = open('password.txt','w+')
		f.write(password)
		f.close()
		sys.exit()

def recurse(width, position, baseString):
	for char in Chars:
		if(position < width-1):
			recurse(width, position + 1, baseString + "%c" % char)
		checkPassword(baseString + "%c" % char)
def main():
	if len(sys.argv) != 2:
		print "usage :", sys.argv[0] , " maxlenght  "
		sys.exit(0)

	maxlength	= int(sys.argv[1])

	for baseWidth in range(1, maxlength + 1):
		print "* checking passwords width [" + `baseWidth` + "]"
		recurse(baseWidth, 0, "")

if __name__ == "__main__":
	main()
