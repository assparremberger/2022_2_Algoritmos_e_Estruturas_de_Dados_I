from Veiculo import Veiculo

class Carro( Veiculo ):

	def __init__(self, marcaCar, anoCar, portas):
		super().__init__(marcaCar, anoCar)
		self.qtdPortas = portas
		print("Carro Construído")