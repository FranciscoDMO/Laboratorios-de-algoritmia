'''
Podemos usar um (multi) grafo pesado para representar um mapa de uma cidade: cada nó representa um cruzamento e cada aresta uma rua 
(etiquetada com o respectivo comprimento). O objectivo deste problema é determinar o tamanho de uma cidade: a distância entre os seus cruzamentos 
mais afastados.
A entrada consistirá numa sequência (não vazia) de nomes de ruas de uma única palavra, com no máximo 100 minúsculas. 
Os identificadores dos cruzamentos correspondem a uma letra do alfabeto, e cada rua começa (e acaba) no cruzamento identificado pelo primeiro 
(e último) caracter do respectivo nome. O comprimento de uma rua é o tamanho do seu nome. A saída deverá consistir no tamanho do maior caminho 
mais curto entre quaisquer dois cruzamentos da cidade.

Exemplo de entrada:

raio
central
liberdade
chaos
saovictor
saovicente
saodomingos
souto
capelistas
anjo
taxa

Saída correspondente:
25

Este resultado corresponde ao tamanho do caminho
taxa
anjo
souto
chaos
central

Relembramos que determinar todos os caminhos mais curtos é um problema clássico de programação dinâmica: considere a generalização que consiste em determinar o caminho mais curto entre os nós i e j usando apenas como nós intermédios os primeiros k nós do grafo.
'''
import sys

def parse(adj):
	for l in sys.stdin:
		l=l.strip('\n')
		w=len(l)
		o=l[0]
		d=l[w-1]

		if o not in adj:
			adj[o] = []
		if d not in adj:
			adj[d] = []
		adj[o].append((d,int(w)))
		adj[d].append((o,int(w)))


def dijkstra(adj,o):
    q = []
    parent = {}
    dist = {}
    for v in adj:
        dist[v] = float("inf")
        q.append(v)
    dist[o] = 0
    while q:
        u = q[0]
        for w in q:
            if dist[w] < dist[u]:
                u = w
        q.remove(u)
        for (v,w) in adj[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                parent[v] = u
    return dist[u]

adj = {}
parse(adj)
r=0
for v in adj:
	dist = dijkstra(adj,v)
	r=max(r,dist)
print (r)