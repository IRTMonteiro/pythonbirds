"""
Aula sobre Métodos
"""

class Pessoa:#classe
    def __init__(self, *filhos, nome=None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):# método =  função que pertence a uma classe
        return f"Olá! {id(self)}"

if __name__ == '__main__': ##este é o teste da classe
    renzo = Pessoa(nome='Renzo') #objeto
    luciano = Pessoa(renzo, nome='Luciano',idade=50) #objeto
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
   