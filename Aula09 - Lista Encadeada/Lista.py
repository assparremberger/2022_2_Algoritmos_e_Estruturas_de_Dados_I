from No import No

class Lista:

    def __init__(self):
        self.inicio = None


    def adicionarNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio
            self.inicio = nodo
        self.imprimir()


    def adicionarNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while ( aux.proximo ):
                aux = aux.proximo
            aux.proximo = nodo
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia!\n--------- ")
        else:
            print("----------------\n")
            aux = self.inicio
            while( aux ):
                print(aux.dado , "\n")
                aux = aux.proximo
            
    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista vazia!\n--------- ")
        elif self.inicio.proximo == None:
            self.inicio = None
        else: 
            self.inicio = self.inicio.proximo
        self.imprimir()
        
    def removerDoFim(self):
        if self.inicio == None:
            print("Lista vazia!\n--------- ")
        elif self.inicio.proximo == None:
            self.inicio = None
        else: 
            ant = self.inicio
            aux = self.inicio.proximo
            while ( aux.proximo ):
                ant = aux
                aux = aux.proximo
            ant.proximo = None
            
        self.imprimir()

    

