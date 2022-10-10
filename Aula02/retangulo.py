class Retangulo:
    def __init__(self, altura, largura):
        self.alt = altura
        self.larg = largura

    def calcular_area(self):
        return self.alt * self.larg

    def imprimir_atributos(self) -> None:
        print(f"""Altura: {self.alt} m,
Largura: {self.larg} m.""")


retangulo = Retangulo(10, 20)
print(retangulo)
print(f"Area: {retangulo.calcular_area()} m².")
retangulo.imprimir_atributos()
