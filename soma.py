import sys
import operator
import decimal

def soma():
	t=[]
	for s in sys.stdin:
		
		s=s.strip('\n')
		t.append(s)
	n1=int(t[0])
	n2=int(t[1])
	soma=n1+n2
	print(soma)

  
soma()
