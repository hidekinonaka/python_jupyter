class ControleRemoto:
    def __init__(self, cor, altura, largura):
        self.cor = cor
        self.altura = altura
        self.largura = largura


controle_remoto = ControleRemoto("Preto", "10cm", "5cm")
print(controle_remoto.largura)
print(controle_remoto.cor)
