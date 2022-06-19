"""
Aula sobre Métodos
"""

class Pessoa:#classe
    def __init__(self, nome=None, idade=39):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):# método =  função que pertence a uma classe
        return f"Olá! {id(self)}"

if __name__ == '__main__': ##este é o teste da classe
    p = Pessoa() #objeto
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Igor"
    print(p.nome, p.idade)
    