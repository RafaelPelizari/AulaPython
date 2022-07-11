class Livro:
    def __init__(self,nome,qtdpaginas, autor, preco):
        self.nome = str(nome)
        self.qtdpaginas = int(qtdpaginas)
        self.autor = str(autor)
        self.preco = float(preco)
        print(nome,qtdpaginas, autor, preco)

    def getpreco (self):
        print ("O preco original do liro é", self.preco)
    #metodo para alterar o preÇo do livro
    def setPreco(self, precoNovo):
        self.preco = precoNovo
        print("O novo preço do livro é", self.preco)

    mostrarlivro = property(getpreco, setPreco)
livro = Livro("Livro A", 320, "Luis Peixoto", 25)
livro.getpreco()
livro.setPreco(15)
print(vars(livro))
