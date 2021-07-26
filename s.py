import sys

def adj(mapa, v):
	""" devolve a lista de adjacentes de v(destino e custo)"""
	adjs = [(v[0]-1,v[1]-2), (v[0]+1,v[1]-2), (v[0]+2,v[1]-1), (v[0]+2,v[1]+1), (v[0]+1,v[1]+2), (v[0]-1,v[1]+2), (v[0]-2,v[1]+1), (v[0]-2,v[1]-1)] #norte, sul, este, oeste, vou ver de qual dos 4 está livre, qual deles for, retorna
	res = []
	for (x,y) in adjs:
		if x>=0 and x < len(mapa) and y>=0 and y<len(mapa[x]):
			if mapa[x][y]==' ':
				res.append(((x,y),1))
	return (res)

def dijkstra(mapa,o,dim): #qual o vertice e qual é o custo usando o caminho mais curto
	queue = []
	dist = {}
	dist[o] = 0
	queue.append(o)
	while queue:
		u = min(queue,key=lambda x : dist[x])
		queue.remove(u)
		for (v,w) in adj(mapa,u):
			alt = dist[u] + w #novo custo
			if v in dist:
				if alt < dist[v]:
					dist[v] = alt
			else :
				dist[v] = alt
				queue.append(v)	
	return dist[(dim[0], dim[1])]
"""

def bfs(adj,o):
    count = 0
    discovered = []
    queue = []
    discovered.append(o)
    queue.append(o)
    while queue:
        c = queue.pop(0)
        for n in adj[c]:
            if n not in discovered:
                discovered.append(n)
                count +=1
                queue.append(n)
    return count

"""

def main():
	#Parsing do input
	x = 0
	y = 0
	t = 0
	mapa = [] 
	o = []
	for l in sys.stdin:
		if t == 0:
			dim = int(l)
			t = 1
		else:
			pos = l.split(" ")
			while (x < dim):
				while(y<dim):
					o.append(' ')
					y+=1
				mapa.append(o)
				x+=1
			dist = dijkstra(mapa,(int(pos[0]), int(pos[1])), (int(pos[2]),int(pos[3])))
			print(dist)

main()