class HashTable:
    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def cadastro(self, key, value):
        index = hash(key) % self.size
        self.data[index] = value

    def busca(self, key):
        index = hash(key) % self.size
        if self.data[index]:
            return self.data[index]
        else:
            print('Usuário não encontrado!')
            return None
    
def main():
    facebook = HashTable()
    facebook.cadastro("diego.cruz", {"nome": "Diego", "idade": 35, "email": "diego@email.com"})
    facebook.cadastro("ana.silva", {"nome": "Ana", "idade": 28, "email": "ana.silva@email.com"})
    facebook.cadastro("lucas.moura", {"nome": "Lucas", "idade": 40, "email": "lucas.moura@email.com"})
    facebook.cadastro("juliana.almeida", {"nome": "Juliana", "idade": 22, "email": "juliana.almeida@email.com"})
    facebook.cadastro("carlos.santos", {"nome": "Carlos", "idade": 50, "email": "carlos.santos@email.com"})
    facebook.cadastro("fernanda.lima", {"nome": "Fernanda", "idade": 30, "email": "fernanda.lima@email.com"})
    facebook.cadastro("marcelo.rocha", {"nome": "Marcelo", "idade": 27, "email": "marcelo.rocha@email.com"})
    facebook.cadastro("priscila.gomes", {"nome": "Priscila", "idade": 33, "email": "priscila.gomes@email.com"})
    facebook.cadastro("roberto.oliveira", {"nome": "Roberto", "idade": 45, "email": "roberto.oliveira@email.com"})
    facebook.cadastro("laura.souza", {"nome": "Laura", "idade": 19, "email": "laura.souza@email.com"})

                        
    print(facebook.busca('alice123'))
    print(facebook.busca('laura.souza'))

if __name__ == '__main__':
    main()