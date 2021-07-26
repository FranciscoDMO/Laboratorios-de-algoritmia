#8 certas

import sys

for s in sys.stdin:
	l = s.split(" ") 
num1=int(l[0])
num2=int(l[1])
resto =None;
if(num2 != 0):
	while resto !=0 :
		resto = int(num1%num2)
		num1=num2
		num2=resto

print(num1)



	






