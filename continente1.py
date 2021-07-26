import sys
t=[]
valor=0;
def parseGrafo():
    
    for l in sys.stdin:
        l=l.strip('\n')
        l=l.split(' ')
     
        for s in l:
            if s not in t:
               t.append(s)
               for x in l:
                if x != s and x not in l:
                    t.append(s)
    print (len(t));

parseGrafo()
            
