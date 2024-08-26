import tkinter as tk

class Janela:
    def __init__(self,geometria,titulo):
        self.janela = tk.Tk()
        self.janela.title(titulo)
        self.janela.geometry(geometria)

    def label(self, texto, x, y,tamanho):
        fonte = ("Fonte/NerkoOne-Regular.ttf",tamanho)
        label = tk.Label(self.janela, text=texto, font=fonte)
        label.place(x=x, y=y)

    def botao(self, texto, x, y, comando):
        botao = tk.Button(self.janela, text=texto, command=comando)
        botao.place(x=x, y=y)
    
    def botao_config(self, texto, x, y, comando, cor):
        botao = tk.Button(self.janela, text=texto, command=comando, bg=cor)
        botao.place(x=x, y=y)

    def fechar(self):
        self.janela.destroy()

    def iniciar(self):
        self.janela.mainloop()   