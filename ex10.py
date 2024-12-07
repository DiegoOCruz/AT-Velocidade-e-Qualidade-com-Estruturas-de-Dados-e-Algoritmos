class Pilha:
    def __init__(self):
        self.data = [
            'www.google.com',
            'www.facebook.com',
            'www.twitter.com',
            'www.linkedin.com',
            'www.instagram.com'
        ]
        self.index = 0
       
    def voltar(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            return None
        
    def avancar(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return self.data[self.index]
        else:
            return None
                
def main():
    navegador = Pilha()

    print(navegador.avancar())
    print(navegador.avancar())
    print(navegador.avancar())
    print(navegador.voltar())
    print(navegador.voltar())

if __name__ == '__main__':
    main()