import string
from turtle import pos


class Cliente:
    def __init__(self, nombre):
        # Completar
        self.nombre = nombre
        self.siguiente = None
        pass


    def __str__(self):
        # NO MODIFICAR
        return self.nombre

class FilaPizza:
    def __init__(self):
        # Completar
        self.primero = None
        self.ultimo = None
        self.largo = 0    
        pass


    def llega_cliente(self, cliente: Cliente):
        #no hay nadie en la fila

        if self.primero is None: 
            self.primero = cliente
            self.ultimo = cliente
        else:
            # se agrega a ultimo 
            self.ultimo.siguiente = cliente
            self.ultimo = cliente

        self.largo += 1
        
        
    def alguien_se_cuela(self, cliente: Cliente, posicion: int):
        
        #siempre debemos partir del primero
        nodo_actual = self.primero

        if posicion == 0:
            self.llega_cliente(cliente)
            self.largo += 1
            return
        
        if posicion == self.largo:
            self.llega_cliente(cliente)
            return 
        
        for _ in range(posicion - 1): 
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente

        if nodo_actual is not None:
            cliente.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = cliente

            if nodo_actual.siguiente is None:
                self.ultimo = cliente

        self.largo += 1
        
        
    
    def cliente_atendido(self):
        # guardamos en una variable en nodo, porque si no perdemos la referencia
        nodo = self.primero
        
        if self.primero is not None: #  Solo si existe el nodo
            
            self.primero = self.primero.siguiente
            
            # caso que sea el ultimo de la fila            
            if self.largo == 1:
                self.primero = None
                self.ultimo = None
            
            self.largo -= 1

        return nodo

    def __str__(self):

        nodo_actual = self.primero
        lista = [nodo_actual]
 
        for _ in range(self.largo - 1):
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente
                # Si pasa esto es que se llego al final
                if nodo_actual is not None:
                    lista.append(nodo_actual)
                    break

        texto = ""

        for i in lista:
            texto += i.nombre + ", "

        return texto

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)