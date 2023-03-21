class Vendedor ():
    def __init__(self,nome):
        self.nome=nome
        self.vendas = 0

    def vendeu(self,vendas):
        self.vendas = vendas

    def bateu_meta(self,meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu meta')
        else:
            print(self.nome, 'Não bateu meta')

vendedor1 = Vendedor('Gabriel')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)
