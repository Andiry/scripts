#!/usr/bin/python

import re
import sys
import os

def main():
	if len(sys.argv) < 2:
		print "paramemter error"
		sys.exit(0)
	filename = sys.argv[1]
	print "processing", filename, "..."
	length = len(filename)
	dir = filename[0 : length - 2]
	print "dir:", dir
	
	threads = [1, 2, 4, 8, 16, 100, 1000]
#	sizes = ["16k", "32k", "128k", "512k", "2m", "4m"]
	sizes = ["8m"]

	for thread in threads:
		for size in sizes:
			new_file = dir + '/' + dir + '_' + str(thread) + '_' + size + '.f'
			print "Formatting",  new_file + "..."
			fd = open(filename, 'r')
			fd1 = open(new_file, 'w')
			lines = fd.readlines()
			for line in lines:
				header = line[0 : 13] 
				if (cmp(header, "set $nthreads") == 0):
					line = header + '=' + str(thread) + '\n'
				if (cmp(header, "set $meanfile") == 0):
					line = line[0 : 17] + '=' + size + '\n'
				fd1.write(line)
			fd.close()
			fd1.close()

	print "done."
	return

main()
