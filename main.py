import sys
import json
import os
import subprocess

from Janela.Janela import Janela
from tkinter import messagebox

#obijetivos:
"""

Verificar a versao do python e se necessario atualizar                 -ture
Verificar as bibilhotecas necessarias e se necessario instalar         -false
Verficar a versao do codigo e se necessario atualizarusando o guit web -false

"""

def btn_erro_notificaçao(text):
    if (text == "Python desatualizado"):
        messagebox.showinfo("Python", "Python desatualizado ou nao encontrado, atualize o Python para a versão 3.12.5 ou superior")
    elif (text == "Bibliotecas desatualizadas"):
        messagebox.showinfo("Bibliotecas", "Bibliotecas desatualizadas ou nao encontradas, atualize as bibliotecas necessarias")
    elif (text == "ok"):
        messagebox.showinfo("OK", "Esta tudo OK por aqui :)")

def verificar_versao_python():
    # Captura a versão atual do Python
    versao_atual = tuple(map(int, sys.version.split()[0].split(".")))
    versao_requerida = (3, 12, 5)
    
    # Compara as versões
    if versao_atual > versao_requerida:
        return False
    else:
        return True

def verificar_bibliotecas():
    
    FILE = "Infor.json"
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
            instalado = data["Dependencias"].get("instaldo", False)
            if (instalado == False):
                infor = listar_bibliotecas()
                if infor:
                    data["Dependencias"]["instaldo"] = True
                    with open(FILE, "w") as file:
                        json.dump(data, file, indent=4)
                    return True
                else:
                    return False
            else:
                return True
    except:
        janela = Janela("600x500", "Instalador de bibliotecas")
        janela.label("Erro ao abrir o arquivo Infor.json", 10, 10, 20)
        janela.botao_config("Fechar", 10, 50, janela.fechar, "red")


def listar_bibliotecas():
    FILE = "Infor.json"
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
            instalado = data["Dependencias"].get("instaldo", False)
            messagebox.showinfo("Bibliotecas", "Bibliotecas desatualizadas ou nao encontradas, Aguarde enquanto as bibliotecas necessarias sao instaladas")
            if not instalado:
                try:
                    for _, biblioteca in data["Dependencias"]["instalacao"].items():
                        comando = biblioteca["Comando"]
                        os.system(comando)  # Executa o comando de instalação
                        result = subprocess.run(comando, shell=True, capture_output=True, text=True)
                        if result.returncode != 0:  # Verifica se houve erro
                            messagebox.showerror("Erro", f"Erro ao instalar a biblioteca: {result.stderr}")
                            return False
                    return True
                except Exception as e:
                    janela = Janela("600x500", "Instalador de bibliotecas")
                    janela.label("Erro ao instalar as Bibliotecas necessárias!", 10, 10, 20)
                    janela.botao_config("Fechar", 10, 50, janela.fechar, "red")
                    return False
            else:
                return True
    except Exception as e:
        janela = Janela("600x500", "Instalador de bibliotecas")
        janela.label("Erro ao abrir o arquivo Infor.json", 10, 10, 20)
        janela.botao_config("Fechar", 10, 50, janela.fechar, "red")
        return False


def verificar_versao_codigo():
    pass

def main():
    janela = Janela(geometria="600x500", titulo="Verificador de atualizações")
    Labeis = ["Python", "Bibliotecas", "Codigo"]
    
    for i in range(3):
        janela.label(Labeis[i], 10, 10 + i*50, 20)
    
    verson = verificar_versao_python()
    if verson:
        janela.botao_config("Python atualizado", 400, 20, lambda: btn_erro_notificaçao("ok"), "green")
    else:
        janela.botao_config("Python desatualizado", 400, 20, lambda: btn_erro_notificaçao("Python desatualizado"), "red")
    
    infor = verificar_bibliotecas()
    if infor:
        janela.botao_config("Bibliotecas atualizadas", 400, 70, lambda: btn_erro_notificaçao("ok"), "green")
    else:
        janela.botao_config("Bibliotecas desatualizadas", 400, 70, lambda: btn_erro_notificaçao("Bibliotecas desatualizadas"), "red")
    
    janela.iniciar()

if __name__ == "__main__":
    main()