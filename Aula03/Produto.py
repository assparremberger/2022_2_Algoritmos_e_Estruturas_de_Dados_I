#from Categoria import Categoria

class Produto:

    def __init__(self, nome, preco, cat):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat

    def imprimir(self):
        print("Nome: " , self.nome )
        print("Preço: " , self.preco )
        print("Categoria: " , self.categoria.nome )
        print("-----------------------")

