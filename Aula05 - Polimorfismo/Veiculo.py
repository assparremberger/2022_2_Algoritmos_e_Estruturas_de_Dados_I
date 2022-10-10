class Veiculo:
	def __init__(self, modelo = "Auto"):
		self.modelo = modelo
	def imprimir(self):
		print("Modelo: ", self.modelo)

	def __str__(self) -> str:
		return "Modelo: " + self.modelo
		