from Janela.Janela import Janela

def main():
    janela = Janela()
    janela.adicionar_botao('Fechar', janela.fechar)
    janela.adicionar_label('Hello, World!')
    janela.iniciar()

if __name__ == "__main__":
    main()