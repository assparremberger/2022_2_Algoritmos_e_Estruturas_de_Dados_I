class Veiculo:

	def __init__(self, marcaVei, anoVei):
		self.marca = marcaVei
		self.ano = anoVei
	
	def imprimir(self):
		print( self.marca , " constuído" )