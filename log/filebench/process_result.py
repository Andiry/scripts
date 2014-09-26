#!/usr/bin/python

import re
import sys
import os

def main():
	if len(sys.argv) < 2:
		print "paramemter error"
		sys.exit(0)
	dir = sys.argv[1]
	print "processing", dir, "..."
	length = len(dir)
	if dir[length - 1] == '/':
		dir = dir[0 : length - 1]
	
	workloads = ["fileserver", "varmail", "webproxy", "webserver", "videoserver"]
	threads = [1, 2, 4, 8, 16, 100, 1000]
	sizes = ["16k", "32k", "128k", "512k", "2m", "4m", "8m"]
	cycle = '1'

	output = dir + ".csv"
	fd1 = open(output, 'w')
	title = "system, workload, thread, size, IOPS\n"
	fd1.write(title)

	for workload in workloads:
	    for thread in threads:
		for size in sizes:
			filename = dir + '/' + workload + '_' + str(thread) + '_' + size + '_' + cycle
			if os.path.isfile(filename) == False:
				continue
			print "processing",  filename + "..."
			fd = open(filename, 'r')
			lines = fd.readlines()
			for line in lines:
				parts = line.split(' ')
				if (len(parts) > 7 and parts[2] == 'IO' and parts[3] == 'Summary:'):
					print line
					print parts[6]
					result = dir + ', ' + workload + ', ' + str(thread) + ', ' + size + ', ' + parts[6] + '\n'
					fd1.write(result)
				if (len(parts) > 7 and parts[3] == 'IO' and parts[4] == 'Summary:'):
					print line
					print parts[7]
					result = dir + ', ' + workload + ', ' + str(thread) + ', ' + size + ', ' + parts[7] + '\n'
					fd1.write(result)
			fd.close()

	fd1.close()
	print "done."
	return

main()
