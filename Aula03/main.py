from Categoria import Categoria
from Produto import Produto


cat01 = Categoria("Bebidas")
p1 = Produto( "Coca-Cola", 7.29 , cat01 )
p2 = Produto( "Pepsi", 5.99 , cat01 )

p3 = Produto( "X-Tudo", 25.00 , Categoria("Lanches") )
p4 = Produto( "X-Acebolado", 20.00 , p3.categoria )


p1.imprimir()
p3.imprimir()
p4.imprimir()