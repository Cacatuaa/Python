#Na classe:
class Exemplo:
    def __init__(self, identidade, nome):
        self.identidade = identidade
        self.nome = nome

	# getter
    @property
    def nome(self):
        return self._nome

    # setter
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

#No programa:
def main():
    objeto = Exemplo(1, "cacatua")
    print(objeto)
    print(objeto.nome)
    objeto.nome = "pedro"
    print(objeto.nome)


if __name__ == "__main__":
    main()