
import sys


file_out = sys.argv[1]
file_in = sys.argv[2]

f= open(file_out,"w+")

for i in range(10000):
     f.write("%d\n" % (i+1))