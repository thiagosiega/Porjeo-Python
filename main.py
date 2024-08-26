import sys
import json
import subprocess
import os
import shutil
from tkinter import messagebox
from Janela.Janela import Janela

def btn_erro_notificaçao(text):
    if text == "Python desatualizado":
        messagebox.showinfo("Python", "Python desatualizado ou não encontrado, atualize o Python para a versão 3.12.5 ou superior.")
    elif text == "Bibliotecas desatualizadas":
        messagebox.showinfo("Bibliotecas", "Bibliotecas desatualizadas ou não encontradas, atualize as bibliotecas necessárias.")
    elif text == "Codigo desatualizado":
        messagebox.showinfo("Código", "Código desatualizado, atualize o código para a versão mais recente.")
        resposta = messagebox.askyesno("Atualizar", "Deseja atualizar o código?")
        if resposta:
            atualizar_codigo()
            messagebox.showinfo("Atualizado", "Código atualizado com sucesso!")
        else:
            messagebox.showinfo("Atualizado", "Código não atualizado!")
    elif text == "ok":
        messagebox.showinfo("OK", "Está tudo OK por aqui :)")
    elif text == "Erro no código":
        messagebox.showinfo("Erro", "Versao atual e superior a disponivel!")
        

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
    import requests
    WEB = "https://raw.githubusercontent.com/thiagosiega/Porjeo-Python/main/Infor.json"
    try:
        # Baixar o arquivo JSON da web
        resposta = requests.get(WEB)
        resposta.raise_for_status()
        dados_web = resposta.json()
        versao_web = dados_web["Codigo"]["Versao"]
        versao_web = tuple(map(int, versao_web.split(".")))
        
        # Ler o arquivo JSON local
        with open("Infor.json", "r") as file:
            dados_local = json.load(file)
            versao_atual = dados_local["Codigo"]["Versao"]
            versao_atual = tuple(map(int, versao_atual.split(".")))

        print(f"Versão atual: {versao_atual}")
        print(f"Versão web: {versao_web}")
        
        # Comparar as versões
        if versao_atual < versao_web:
            res = "Código desatualizado"
            return res
        elif versao_atual > versao_web:
            res = "Código mais recente"
            return res
        else:
            res = "Código atualizado"
            return res

    except requests.RequestException as e:
        print(f"Erro ao acessar a versão online do código: {e}")
        return False
    
    except FileNotFoundError:
        print("Erro: O arquivo Infor.json local não foi encontrado.")
        return False
    
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Verifique o formato do arquivo.")
        return False
    
    except KeyError as e:
        print(f"Erro no formato do arquivo JSON: Chave ausente {e}")
        return False

def atualizar_codigo():
    WEB = "https://github.com/thiagosiega/Porjeo-Python.git"
    comando = f"git clone {WEB}"
    pasta = "Porjeo-Python"
    try:
        subprocess.run(comando, shell=True, check=True)
        excluir = ["Infor.json", "Janela"]
        for arquivo in excluir:
            subprocess.run(f"rm -rf {pasta}/{arquivo}", shell=True, check=True)
        FILE = "Porjeo-Python"
        py = ["main.py", "Update.py"]
        #sobe todos os arquivos da pasta para a pasta raiz exeto a pasta main.py
        for i in os.listdir(FILE):
            if i != py:
                shutil.move(f"{FILE}/{i}", i)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o código: {e}")
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
    if codigo_atualizado == "Código atualizado":
        janela.botao_config("Código atualizado", 400, 120, lambda: btn_erro_notificaçao("ok"), "green")
    elif codigo_atualizado == "Código desatualizado":
        janela.botao_config("Código desatualizado", 400, 120, lambda: btn_erro_notificaçao("Codigo desatualizado"), "red")
    else:
        janela.botao_config("Erro no código", 400, 120, lambda: btn_erro_notificaçao("Erro no código"), "red")
    
    janela.iniciar()

if __name__ == "__main__":
    main()
