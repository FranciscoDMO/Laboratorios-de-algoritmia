import sys

def lol():
    i=0
    l=[]
  
    for s in sys.stdin:

        s=s.strip('\n')
        s=s.split(' ', 1)
        l.append(s)
        i+=1
    for s in l:
        print ("else if(x=="+s[0]+"){\n printf(Banco: "+s[1]+");\n}")
        
lol()