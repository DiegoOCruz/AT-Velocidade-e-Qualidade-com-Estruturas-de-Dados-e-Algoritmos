class Fila:
    def __init__(self):
        self.fila = []
    def inserir(self, item):
        self.fila.append(item)
    def remover(self):
        if len(self.fila) > 0:
            self.fila.pop(0)
        else:
            print("Fila vazia")
    def imprimir(self):
        print(self.fila)

def main():
    fila = Fila()
    fila.inserir('Chamado 1')
    fila.inserir('Chamado 2')
    fila.inserir('Chamado 3')
    fila.inserir('Chamado 4')
    fila.inserir('Chamado 5')
    fila.imprimir()
    fila.remover()
    fila.imprimir()
    fila.remover()
    fila.imprimir()

if __name__ == '__main__':
    main()