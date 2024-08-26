import os

#verifica se tem um arquivo com o nome main.py uma pasta acima
if os.path.isfile(f"../main.py"):
    #o exlui
    os.remove(f"../main.py")
    #sobe o arquivo main.py para a pasta raiz para ser executado
    os.rename("main.py", "../main.py")
    #executa o arquivo main.py
    os.system("python ../main.py")
else:
    print("Erro: O arquivo main.py não foi encontrado.")
    exit(1)    