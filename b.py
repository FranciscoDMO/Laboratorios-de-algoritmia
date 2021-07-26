import sys
adj = {}
'''
Braga,	coimbra:170
viseu,coimbra:50
lisboa,coimbra:210
BRAGA LISBOA VISEU

	'''

def parse(txt):
	adj = {}
	for l in txt:
		o=l[0]
		d=l[1]
		w=l[2]
		if o not in adj:
			adj[o] = []
		if d not in adj:
			adj	[d] = []
		adj[o].append((d, int(w)))
		adj[d].append((o, int(w)))
	return adj



def fw(adj):
	dist = {}
	for o in adj:
		dist[o] = {}
		for d in adj:
			if o == d:
				dist[o][d] = 0
			else:
				dist[o][d] = float("inf")
		for (d,w) in adj[o]:
				dist[o][d] = w
	for k in adj:
		for o in adj:
			for d in adj:
				if dist[o][d] > dist[o][k] + dist[k][d]:
					dist[o][d] = dist[o][k] + dist[k][d]
	return dist


def bla(dist, pos, sitio):
	f=10000000
	for s in sitio: # todas as cidades 

		q=0
		for t in pos:
			x=int(dist[s][t])
			if x>q :
				q=x
			
		if q<f:
			f=x
	if(f==10000000): 
		f=0
	print(f)


def main():
	l=[]
	mapa1=[]
	txt = sys.stdin.readlines()
	pos=txt[0].strip('\n')
	pos=pos.split(',')
	mapa=txt[1:]
	for s in mapa:
		s=s.strip('\n')
		t=s.split(':')
		s=t[0].split(',')
		s.append(t[1])
		mapa1.append(s)
		if s[0] not in l:
			l.append(s[0])
		if s[1] not in l:
			l.append(s[1])
	bla(fw(parse(mapa1)), pos , l)
main()


