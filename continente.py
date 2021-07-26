'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta. 
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa sequência de linhas, onde cada linha lista uma sequência de países que são vizinhos entre si. 
O programa deverá devolver o tamanho do maior continente do planeta.
Exemplo de entrada:

portugal espanha
espanha franca
franca belgica alemanha 
franca suica italia
belgica holanda alemanha
inglaterra irelanda
suica austria italia
alemanha polonia
brasil uruguai paraguai
brasil peru paraguai 
brasil colombia venezuela
colombia equador peru
islandia

Saída correspondente:

10
'''

import sys
adj = {}

def parseGrafo():
    
    for l in sys.stdin:
        l=l.strip('\n')
        l=l.split(' ')
     
        for s in l:
            if s not in adj:
               adj[s] = []
            for t in l:
                if t != s and t not in adj[s]:
                    adj[s].append(t)

def bfs(adj,o):
    count = 1
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
    return(count)


def main():
    valor=0;

    for s in adj:
        x=bfs(adj,s)
        if x > valor :
            valor=x
    print(valor)





parseGrafo()
main()

