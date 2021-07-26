import sys

def prime_factors(n):
	i = 2
	if(int((n-1)/6)==(n-1)/6 or int((n+1)/6)==(n+1)/6):
		print (n)
		return;
	while n>1 :
		if n%i == 0:
			n=n/i
			print(i)
		else:
			i+=1

def qualquercoisa ():
	imp=input()
	prime_factors(int(imp))
qualquercoisa()