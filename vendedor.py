import sys 

def ler (t):
	i =0
	for s in sys.stdin:
		l=s.split(" ")
		t.append(l)

def melhor (t):
	i=1
	x=int(t[0][0].strip("\n"))
	n=len(t)
	while(i<n):
		u=int((t[i][2]).strip())
		if(u<x)
		i+=1




def vendedor():
	t=[]
	ler(t)
	melhor(t)
vendedor()