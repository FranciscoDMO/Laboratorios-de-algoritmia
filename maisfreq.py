import sys
import collections
l={}

def maisfreq():
	i=0
	e=[]
	q=[]
	for s in sys.stdin:
		s=s.strip('\n')
		s=s.split(' ')
		for t in s:
			if t in l:
				l[t]+=1
			else:
				l[t]=1
	
	for key in l:
		q.append((l[key],key))
	
	for s in q:
		e.append(s[0])	
	e=sorted(e, reverse=True)		
	
	q = sorted(q, key=lambda q: q[1])

	for s in e:
		for t in q:
			if(s==t[0]):
				print(str(t[1])+':'+' '+str(t[0]))
				q.remove(t)
				break;

	 




	#b = sorted(l, key=lambda x: ((l[x]), x))
	#b=list(reversed(b))
	

	#for key in b:
	#	print (str(key)+':'+' '+str(l[key]))
	
maisfreq()
