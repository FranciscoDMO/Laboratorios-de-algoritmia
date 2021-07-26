import sys 
def robot():
	for t in sys.stdin:
		b=0
		f=('N','S','E','O')
		x=0
		y=0
		x_min = 0
		y_min = 0	
		x_max = 0
		y_max = 0
		t=t.split()
		for s in t :

			if(s=='E' and b==0):
				b=3
			elif(s=='E' and b==1):
				b=2
			elif(s=='E' and b==2):
				b=0
			elif(s=='E' and b==3):
				b=1
			elif(s=='D' and b==0):
				b=2
			elif(s=='D' and b==1):
				b=3
			elif(s=='D' and b==2):
				b=1
			elif(s=='D' and b==3):
				b=0
			if(s=='A'):
				if(f[b]=='E'):
					x+=1
					if(x>x_max):
						x_max=x
				elif(f[b]=='O'):
					x-=1
					if(x<x_min):
						x_min=x
				elif(f[b]=='N'):
					y+=1
					if(y>y_max):
						y_max=y
				elif(f[b]=='S'):
					y-=1
					if(y<y_min):
						y_min=y
			elif(s=='H'):
				print("(" + str(x_min) + "," + str(y_min) + ") (" + str(x_max) + "," + str(y_max) + ")")		
robot()