import tkinter as tk

class Janela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Janela')
        self.janela.geometry('300x300')
        self.widgets = []

    def adicionar_botao(self, texto, comando):
        botao = tk.Button(self.janela, text=texto, command=comando)
        botao.pack()
        self.widgets.append(botao)

    def adicionar_label(self, texto):
        label = tk.Label(self.janela, text=texto)
        label.pack()
        self.widgets.append(label)

    def fechar(self):
        self.janela.destroy()

    def iniciar(self):
        self.janela.mainloop()   