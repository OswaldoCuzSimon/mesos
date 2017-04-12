import sys

for i in range(1,10):
	print(str(i)+" hello mesos")
	sys.stderr.write(str(i)+" hello stderr\n")