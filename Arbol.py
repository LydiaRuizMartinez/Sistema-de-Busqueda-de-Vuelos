class Arbol():
    def __init__(self,orden):
        self.raiz = None
        self.orden = orden
    def insertar_vuelo():
        pass

class Nodo():
    def __init__(self):
        pass

class Nodo2():
    
    def __init__(self, clave):
        self.clave = clave
        self.padre = None
        self.izq = None
        self.der = None

# Clase Arbol

class Arbol2():
    def __init__(self):
        self.raiz = None

    def InsertarArbolBin(self,nodo):
        padre = None
        x = self.raiz
        while x != None:
            padre = x
            if nodo.clave < x.clave:
                x=x.izq
            else:
                x=x.der
        nodo.padre = padre
        if padre == None:
            self.raiz = nodo
        else:
            if nodo.clave < padre.clave:
                padre.izq = nodo
            else:
                padre.der = nodo
        
    def Buscar(self,clave):
        x = self.raiz
        while x != None and clave != x.clave:
            if clave < x.clave:
                x = x.izq
            else:
                x = x.der
        if x == None:
            print("No existe un nodo con esa clave.")
        return x
    
    def MinimoArbolBin(self,n):
        if n != None:
            while n.izq != None:
                n = n.izq
        return n 
    
    def SucesorArbolBin(self,n):
        if n != None:
            if n.der != None:
                p = self.MinimoArbolBin(n.der)
            else:
                p = n.padre
                while p != None and n==p.der:
                    n=p
                    p=p.padre
        return p
    
    def Eliminar(self,clave):
        n = self.Buscar(clave)
        if n == None:
            print("No se puede eliminar el nodo porque no existe.")
        else:
            if n.izq == None or n.der == None:
                y = n
            else:
                y = self.SucesorArbolBin(n)
                
            if y.izq != None:
                x = y.izq
            else:
                x = y.der
            if x != None:
                x.padre = y.padre
            if y.padre == None:
                self.raiz = x
            else:
                if y == y.padre.izq:
                    y.padre.izq = x
                else:
                    y.padre.der = x
            if y != n:
                 n.clave = y.clave
                 n.izq.padre = y
                 n.der.padre = y
                 y.izq = n.izq
                 y.der = n.der
                 
        return y
    
    
    def mostrar(self):
            if self.raiz is None:
                print("El árbol está vacío")
                return
            pila = [(self.raiz, 0)]
            while pila:
                nodo, nivel = pila.pop()
                print("   " * nivel + "->", nodo.clave)
                if nodo.der:
                    pila.append((nodo.der, nivel + 1))
                if nodo.izq:
                    pila.append((nodo.izq, nivel + 1))