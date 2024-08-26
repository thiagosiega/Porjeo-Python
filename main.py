import sys
import json
import subprocess
from tkinter import messagebox
from Janela.Janela import Janela

def btn_erro_notificaçao(text):
    if text == "Python desatualizado":
        messagebox.showinfo("Python", "Python desatualizado ou não encontrado, atualize o Python para a versão 3.12.5 ou superior.")
    elif text == "Bibliotecas desatualizadas":
        messagebox.showinfo("Bibliotecas", "Bibliotecas desatualizadas ou não encontradas, atualize as bibliotecas necessárias.")
    elif text == "Codigo desatualizado":
        messagebox.showinfo("Código", "Código desatualizado, atualize o código para a versão mais recente.")
    elif text == "ok":
        messagebox.showinfo("OK", "Está tudo OK por aqui :)")

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
            bibliotecas = data["Dependencias"]["Bibilhotecas"]
            instalacao = data["Dependencias"]["instalacao"]
            
            for biblioteca_key, biblioteca in bibliotecas.items():
                if not biblioteca.get("instaldo", False):
                    try:
                        __import__(biblioteca["Nome"])
                    except ImportError:
                        janela = Janela("600x500", "Instalador de Bibliotecas")
                        janela.label(f"Biblioteca {biblioteca['Nome']} não encontrada", 10, 10, 20)
                        janela.label(f"Instalando a biblioteca {biblioteca['Nome']}", 10, 50, 20)
                        janela.botao_config("Fechar", 10, 90, janela.fechar, "red")
                        comando = instalacao[biblioteca_key]["Comando"]
                        subprocess.run(comando, shell=True, check=True)
                        return True
            return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        janela = Janela("600x500", "Instalador de Bibliotecas")
        janela.label(f"Erro ao abrir ou ler o arquivo Infor.json: {e}", 10, 10, 20)
        janela.botao_config("Fechar", 10, 50, janela.fechar, "red")
        return False
    except subprocess.CalledProcessError as e:
        janela = Janela("600x500", "Instalador de Bibliotecas")
        janela.label(f"Erro ao instalar a biblioteca: {e}", 10, 10, 20)
        janela.botao_config("Fechar", 10, 50, janela.fechar, "red")
        return False

def verificar_versao_codigo():
    WEB =  "https://github.com/thiagosiega/Porjeo-Python/blob/main/Infor.json"
    try:
        with open("Infor.json", "r") as file:
            data = json.load(file)
            versao_atual = data["Versao"]
            versao_atual = tuple(map(int, versao_atual.split(".")))
            versao_requerida = (0, 2, 0)
            if versao_atual == versao_requerida:
                return True
            else:
                return False
    except (FileNotFoundError, json.JSONDecodeError) as e:
        janela = Janela("600x500", "Instalador de Bibliotecas")
        janela.label(f"Erro ao abrir ou ler o arquivo Infor.json: {e}", 10, 10, 20)
        janela.botao_config("Fechar", 10, 50, janela.fechar, "red")
        return False


def main():
    janela = Janela(geometria="600x500", titulo="Verificador de Atualizações")
    Labeis = ["Python", "Bibliotecas", "Código"]
    
    for i in range(3):
        janela.label(Labeis[i], 10, 10 + i*50, 20)
    
    python_atualizado = verificar_versao_python()
    if python_atualizado:
        janela.botao_config("Python atualizado", 400, 20, lambda: btn_erro_notificaçao("ok"), "green")
    else:
        janela.botao_config("Python desatualizado", 400, 20, lambda: btn_erro_notificaçao("Python desatualizado"), "red")
    
    bibliotecas_atualizadas = verificar_bibliotecas()
    if bibliotecas_atualizadas:
        janela.botao_config("Bibliotecas atualizadas", 400, 70, lambda: btn_erro_notificaçao("ok"), "green")
    else:
        janela.botao_config("Bibliotecas desatualizadas", 400, 70, lambda: btn_erro_notificaçao("Bibliotecas desatualizadas"), "red")

    codigo_atualizado = verificar_versao_codigo()
    if codigo_atualizado:
        janela.botao_config("Código atualizado", 400, 120, lambda: btn_erro_notificaçao("ok"), "green")
    else:
        janela.botao_config("Código desatualizado", 400, 120, lambda: btn_erro_notificaçao("Codigo desatualizado"), "red")
    
    janela.iniciar()

if __name__ == "__main__":
    main()
