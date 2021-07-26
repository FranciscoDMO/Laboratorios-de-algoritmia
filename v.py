'''
O objectivo deste problema é determinar o preço mais barato para voar entre 2 aeroportos. 
Irá receber o código de 2 aeroportos entre os quais pretende viajar, seguida de uma sequência de itinerários disponíveis. 
Cada itinerário consiste nos códigos dos aeroportos e do respectivo preço. Assuma que o preço é o mesmo nos dois sentidos. 
Deverá imprimir o custo da viagem mais barata entre os 2 aeroportos pretendidos. Em todas os testes essa viagem será sempre possível.

Exemplo de entrada:

FRA NRT
OPO LIS 100
OPO FAO 70
LIS FAO 100
MAD OPO 200
LIS LON 300
FRA OPO 300
LIS NRT 1200
LON NRT 800
LON FRA 200
LIS FRA 300

Saída correspondente:

1000

'''
import sys

def parse(txt):
	adj = {}
	for l in txt:
		o, d, w = l.split()
		if o not in adj:
			adj[o] = []
		if d not in adj:
			adj[d] = []
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

def short(txt,way):
	if way[0] not in txt:
		return 0
	if way[1] not in txt:
		return 0
	return txt[way[0]][way[1]]

txt=[]
for l in sys.stdin.readlines():
	if len(l.split())==2:
		way = l.split()
	else:
		txt.append(l)

fin = fw(parse(txt))
print(short(fin, way))