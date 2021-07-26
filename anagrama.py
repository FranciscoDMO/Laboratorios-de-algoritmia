import sys
import itertools
def ana ():
	n=input()
	n=n[0:len(n)]
	t=[]
	l = list(itertools.permutations(n)) 
	
	for s in l:
		str = ''.join(s)
		if str not in t:
			t.append(str)
	t.sort()
	for s in t:
		print (s)

ana()