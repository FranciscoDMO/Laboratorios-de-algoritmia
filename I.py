import sys
'''
O objectivo deste problema é determinar a área interna de uma figura desenhada com caracteres. 
A entrada consistirá nas coordenadas (horizontal e vertical, medidas a partir do canto superior esquerdo) de um ponto arbitrário dentro de uma figura. 
O limite da figura estará desenhado usando asteriscos. A área interna consiste no número de caracteres contidos dentro da figura. 
Assuma que a figura ocupa no máximo 100 por 100 caracteres.

Exemplo de entrada:
3 2
  ***
 *   *
*     *
 *   *
  ***

Note que neste caso o ponto inicial é coincidentemente o ponto central da imagem.

Saída correspondente:

11
'''
def bfs(mapa,o):
    count = 1
    discovered = []
    queue = []
    discovered.append(o)
    queue.append(o)
    while queue:
        c = queue.pop(0)
        for n in adj(mapa,c):
            
            if n not in discovered:
                discovered.append(n)
                count +=1                           # para tamanhos se nao isto : parent[n] = c
                queue.append(n)
    print(count)

def adj(mapa, v):
    """ devolve a lista de adjacentes de v """
    adjs = [(v[0]-1,v[1]), (v[0],v[1]+1), (v[0]+1,v[1]), (v[0],v[1]-1)]
    res = []
    for (x,y) in adjs:
        if x>=0 and x < len(mapa) and y>=0 and y<len(mapa[x]):
            if mapa[x][y]==' ':
                res.append((x,y))
    return res

def main():
    txt = sys.stdin.readlines()
    if(txt):
        vx, vy = txt[0].split()
        vx = int(vx)
        vy = int(vy)
        mapa = txt[1:]
        if not mapa:
            print(0)
            return
        else:
           bfs(mapa,(vx,vy))
    else: 
        print(0)
        return
    #print(mapa, vx, vy, adj(mapa,(vx,vy)))


main()
