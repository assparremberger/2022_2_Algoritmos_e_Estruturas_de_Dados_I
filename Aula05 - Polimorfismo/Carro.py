from Veiculo import Veiculo

class Carro(Veiculo):
	def __init__(self, modelo="Fusca", nPortas = 4):
		super().__init__(modelo)
		self.nPortas = nPortas
	def imprimir(self):
		super().imprimir()
		print("QTD portas: ", self.nPortas)

	def __str__(self) -> str:
		return super().__str__() + "\nQtd Portas: " + str(self.nPortas)


