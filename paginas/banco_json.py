import os
import json

def carregar_json():
    if os.path.exists("TarefasSalvas/salvos.json"):
        print("existe")
        with open("TarefasSalvas/salvos.json","r") as file:
            dados = json.load(file)
    else:
        print("nao_existe")
        dados = {"tarefas": [], "concluidas": []}
    
    return dados

def salvar_json(dados):    
    with open("TarefasSalvas/salvos.json","w") as file:
        json.dump(dados,file)