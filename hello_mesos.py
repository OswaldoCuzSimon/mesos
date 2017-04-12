import sys,time
for i in range(1,21):
	print("echo \""+str(i)+" hello mesos\"")
	sys.stderr.write("echo \""+str(i)+" hello mesos\"\n")
	time.sleep(1)