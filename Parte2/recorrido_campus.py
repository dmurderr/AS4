from Parte2.campus import Lugar
from collections import deque

def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    visitados = []

    queue = deque([inicio])

    vertice = inicio

    while len(queue) > 0 :
        vertice = queue.popleft()

        if vertice == final:
            
            return True
    
        if vertice in visitados:
            continue

        visitados.append(vertice)

        for vecino in vertice.vecinos:
            if vecino not in visitados:
                # si no hay chismosos agregamos ese camino
                if not comprobar_chismoso(vecino):
                    queue.append(vecino)
    else:
        # acabamos con la cola osea los vecinos y no encuentra el camino
        # entonces no es posible llegar
        return False

def dfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    pass

def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    visitados = []

    queue = deque([inicio])

    vertice = inicio
    recorrido = 0
    while len(queue) > 0 :

        vertice = queue.popleft()
        recorrido += 1

        if vertice == final:
            
            return recorrido
    
        if vertice in visitados:
            continue

        visitados.append(vertice)

        for vecino in vertice.vecinos:
            if vecino not in visitados:
                # si no hay chismosos agregamos ese camino
                if not comprobar_chismoso(vecino):
                    queue.append(vecino)
    else:
        # acabamos con la cola osea los vecinos y no encuentra el camino
        # entonces no es posible llegar
        return False

    # Completar 
    pass


def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar 
    pass


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    

def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    
    
def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQU?? EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
