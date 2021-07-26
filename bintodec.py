import sys
import math	

def bintodec ():
	for s in sys.stdin:
		s=s.strip("\n")
		s = list(reversed(s))
		i=1
		t=0
		for x in s:
				t+=int(x)*i
				i*=2

		print(t)
	


bintodec()

