from faker import Faker

fake = Faker()
db = []
def criar_pessoa():
    return {
        'nome': fake.name(),
        'fone': fake.phone_number(),
    }

def criar_pessoas(n):
    return [criar_pessoa() for _ in range(n)]

def buscar_pessoa(nome):
    for pessoa in db:
        if nome.lower() in pessoa['nome'].lower():
            return pessoa
    return None

def main():
    pessoas = criar_pessoas(100)
    for pessoa in pessoas:
        db.append(pessoa)
    
    for pessoa in db:
        print(pessoa)

    while True:
        nome = input('Digite o nome da pessoa que deseja buscar: ')
        pessoa = buscar_pessoa(nome)
        if pessoa:
            print('Nome:', pessoa['nome'])
            print('Fone:', pessoa['fone'])
        else:
            print('Pessoa não encontrada!')
        if input('Deseja sair? (s/n) ') == 's':
            break

if __name__ == '__main__':
    main()
    