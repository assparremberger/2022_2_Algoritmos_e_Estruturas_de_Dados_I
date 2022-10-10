from Veiculo import Veiculo

class Moto( Veiculo ):

	def __init__(self, marcaMoto, anoMoto, partida):
		super().__init__(marcaMoto, anoMoto)
		self.partidaEletrica = partida
		print("Moto Construída")