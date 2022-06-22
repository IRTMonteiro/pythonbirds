"""
Aula sobre Métodos
"""

class Pessoa:#classe
    olhos = 2

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

    luciano.sobrenome = "Ramalho"

    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    '''.
    __dict__ é um atributo python  que revela todos
    os atribuitos de instância de uma função
    '''
    print(Pessoa.olhos) 
    print(luciano.olhos) 
    print(renzo.olhos) 
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))