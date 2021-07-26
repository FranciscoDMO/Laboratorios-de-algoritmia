
import sys

def adj(mapa, v):
	""" devolve a lista de adjacentes de v(destino e custo)"""
	adjs = [(v[0]-1,v[1]), (v[0],v[1]+1), (v[0]+1,v[1]), (v[0],v[1]-1)] #norte, sul, este, oeste, vou ver de qual dos 4 está livre, qual deles for, retorna
	res = []
	for (x,y) in adjs:
		if x>=0 and x < len(mapa) and y>=0 and y<len(mapa[x]):
			if mapa[x][y]==' ':
				res.append(((x,y),1))
			if mapa[x][y]=='.':
				res.append(((x,y),2))

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
	return dist[(dim[0]-1, dim[1]-1)]




def main():
	#Parsing do input
	txt = sys.stdin.readlines()
	pos=txt[0].split()
	dim = (int(pos[0]),int(pos[1])) #vai dar um inteiro, so tenho um inteiro na 1ª linha
	mapa = txt[1:]
	dist = dijkstra(mapa,(0,0),dim)
	print(dist)
main()


