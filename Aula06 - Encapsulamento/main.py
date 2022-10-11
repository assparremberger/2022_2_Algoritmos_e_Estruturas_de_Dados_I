from Conta import Conta

c1 = Conta()
c1.setSaldo( 1000 )
print( c1.getSaldo() )

c1.saldo = 2000
print("Novo: ", c1.saldo )

c1.depositar( 10 )
print("Novo: ", c1.saldo )

c1.sacar( 2008 )
print("Novo: ", c1.saldo )

c1.tarifa  = 1.0
c1.sacar( 100 )
print("Novo: ", c1.saldo )