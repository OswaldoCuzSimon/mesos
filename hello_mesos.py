import sys,time
i=1
while True:
	print("echo \""+str(i)+" hello mesos\"")
	sys.stderr.write("echo \""+str(i)+" hello mesos\"\n")
	i=i+1
	time.sleep(1)