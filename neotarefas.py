#Imports
import customtkinter as ctk
import json
import os
from pathlib import Path

#O código cria uma pasta para salvar o arquivo json contendo todas as tarefas salvas
pastasaves = Path('TarefasSalvas')
pastasaves.mkdir(parents=True,exist_ok=True)
#Aí toda tarefa criada vai diretamente pra esse arquivo dentro dessa pasta
SavesCaminho = pastasaves / 'salvos.json'
arquivojson = 'salvos.json'

#Uma função pra carregar o arquivo json, pra facilitar o código
def carregarjson():
    with open(SavesCaminho, 'r') as arquivo:
        return json.load(arquivo)

#Criando a janela principal
janela = ctk.CTk(fg_color='darkgoldenrod1')
janela.geometry('700x500')
janela.title('Neo Tarefas')
janela.iconbitmap('./ico.ico')
janela.resizable(False, False)
#Criando um frame usado pra decoração/customização do programa
jnl = ctk.CTkFrame(janela,fg_color='saddle brown',width=680,height=480,border_color='darkgoldenrod2',border_width=5)
jnl.place(x=10,y=10)
#É o rosto do 'NeoByte', pra deixar o programa carismático
expressão = ctk.CTkLabel(jnl,text='█ ‿ █',font=('bold',202),text_color='white')
expressão.place(x=93,y=90)

#É aqui onde o programa vai começar de verdade, logo após um botão ser ativado
def cmç():
    #Vai apagar o botão e o 'rosto' do NeoByte pra dar espaço ao programa
    expressão.destroy()
    começa.destroy()
    #Título pra deixar o programa mais apresentável
    ctk.CTkLabel(janela,text='TAREFAS',font=('Arial Black',20),text_color='white',bg_color='saddle brown').place(x=25,y=18)

    #Vai criar um outro frame de decoração e definir os limites de onde as tarefas vão ficar
    jnl2 = ctk.CTkFrame(janela,fg_color='saddle brown',bg_color='saddle brown',border_color='white',border_width=2,width=660,height=430)
    jnl2.place(x=20,y=53)
    #É aqui que a mágica vai acontecer, os frames das tarefas vão ficar todos localizados aqui dentro, ele tem uma scrollbar pra não limitar o programa e o usuário colocar quantas tarefas quiser
    jnl3 = ctk.CTkScrollableFrame(janela,fg_color='saddle brown',bg_color='saddle brown',width=612,height=407,scrollbar_button_color='white',scrollbar_button_hover_color='snow3')
    jnl3.place(x=35,y=59)

    #Função CARREGAR. Vai Carregar todas as tarefas salvas no arquivo json. Vai recriar todos os frames e botões das tarefas, como se nunca tivesse fechado o programa
    def carregar(nometaf,state):
        dados = carregarjson()
        #Função pra apagar uma tarefa depois de concluída. Essa função vai ser usada em um botão mais pra frente
        def feito():
                taframe.destroy()
                dados = carregarjson()
                del dados[nometaf]
                with open(SavesCaminho,'w+') as arquivo:
                    json.dump(dados,arquivo,indent=4)  

        #Se a tarefa existir, ele vai recriar ela do zero, como se nunca tivesse saído do programa
        if nometaf in dados:
                #Código Do Frame onde a Tarefa se encontra, cada frame desse é uma tarefa        
                taframe = ctk.CTkFrame(jnl3,fg_color='saddle brown',bg_color='saddle brown',border_color='white',border_width=1,width=500,height=70)
                taframe.pack()

                #CheckBox: O código do checkbox ficou extenso porque ele precisa verificar se a caixinha está marcada ou não, pra carregar o programa exatamento como ele fechou
                
                #Aqui ele vai ver se o valor salvo é True ou Falso
                check = ctk.BooleanVar()
                #Aqui ele vai setar o valor: Tipo, se antes de fechar o programa, a tarefa se encontrava marcada, ela tinha o valor True. Esse código vai garantir que o valor continue True
                check.set(state)
                
                #Aqui é o código do botão de 'Feito', que vai excluir a tarefa. Vai verificar se o botão estava ligado ou desligado antes de fechar o programa
                feitostate = 'disabled'
                if state == True:
                    feitostate = 'normal'
                elif state == False:
                    feitostate = 'disabled'    

                #O nome da função não é muito autoexplicativo mas kkkkkk. Vai salvar o estado do check e salvar ele diretamente no arquivo json pra depois fazer a verificação
                def retorne():
                    dados = carregarjson()
                    comando = check.get()

                    #Se o check ficar ligado, ele vai receber True e vai ligar o botão de Feito. Salvando essas informações no arquivo json
                    if comando == True:
                        deletaf.configure(state = 'normal')

                        if nometaf in dados:
                            dados[nometaf]['state'] = True
                        with open(SavesCaminho,'w') as arquivo:
                            json.dump(dados,arquivo,indent=4)        

                    #Aqui é basicamente a mesma fórmula do True, oque diferencia é que o botão vai ficar desligado esperando o usuário terminar a tarefa
                    if comando == False:
                        deletaf.configure(state = 'disabled')

                        if nometaf in dados:
                            dados[nometaf]['state'] = False
                        with open(SavesCaminho,'w') as arquivo:
                            json.dump(dados,arquivo,indent=4)
     
                #Código Do CheckBox: Aqui vai gerar o botão do CheckBox, e com as configurações acima, ele vai iniciar marcado ou desmarcado dependendo do que foi salvo
                checktaf = ctk.CTkCheckBox(taframe,20,20,text=nometaf,onvalue=True, offvalue=False,variable=check,command=retorne,hover_color='white',fg_color='white',text_color='white',checkmark_color='saddle brown',border_color='white',font=('Arial Black', 20))
                checktaf.place(x=10,y=25)


                #Código Do Botão de Feito: O botão que vai excluir as tarefas concluídar
                deletaf = ctk.CTkButton(taframe,30,50,text='FEITO', command=feito,state=feitostate,font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,text_color_disabled='snow3')  
                deletaf.place(x=440,y=10)
    
    #Aqui, se o arquivo Json não existir, ele vai criar um novo Vazio
    if not SavesCaminho.exists():
        with open(SavesCaminho,'w') as arquivo:
            json.dump({},arquivo)

    dados = carregarjson()
    #Pra cada Tarefa salva no arquivo Json, vai carregar em um for
    for nome_tarefa, state in dados.items():

        #Esse aqui é um print que vai aparecer somente no Terminal. Não impacta em nada o programa, eu usei como teste e vou deixar como um 'easteregg'
        print(f'Tarefa: {nome_tarefa}, Estado: {state}')
        estado = state['state']

        #Foi preciso criar essa função pro programa não bugar e criar cada tarefa individualmente
        carregar(nome_tarefa,estado)
    

    #Função ADICIONAR: Vai criar uma Tarefa Nova

    #Essa função vai criar uma nova janela pro usuário poder adicionar sua tarefa. Essa nova janela não tem muitas funções, apenas escrever o nome da tarefas e um botão pra adicionar ela na janela principal
    def adicionar():
        add = ctk.CTkToplevel(janela,fg_color='darkgoldenrod1')
        add.geometry('400x100')
        add.title('ADICIONAR Tarefa')
        add.resizable(False,False)
        #Vai adicionar um frame de decoração
        addd = ctk.CTkFrame(add,390,97,fg_color='saddle brown',border_color='darkgoldenrod2',border_width=3)
        addd.place(x=5,y=3)

        #Esse entry vai receber o nome da tarefa
        tarefa = ctk.CTkEntry(add,365,50,bg_color='saddle brown',fg_color='saddle brown',border_color='white',border_width=2,text_color='white',placeholder_text='Nome da Tarefa...',placeholder_text_color='snow2')
        tarefa.place(x=17,y=13)

        #Função do botão que adiciona o arquivo á tela pricipal. É basicamente o código de Carregar os frames, Só que dessa vez é apenas pra criar tarefa por tarefa e ir salvando tudo no arquivo
        def passar():
            dados = carregarjson()
            #Função pra apagar uma tarefa depois de concluída. Essa função vai ser usada em um botão mais pra frente
            def feito():
                taframe.destroy()
                dados = carregarjson()
                del dados[nometaf]
                with open(SavesCaminho,'w+') as arquivo:
                    json.dump(dados,arquivo,indent=4)  

            #Aqui vai pegar o nome Dado á tarefa e depois vai retirar os espaços em branco pra não ter erros na hora de comparar
            nometaf = tarefa.get().strip()
            #Se não for dado um nome pra tarefa, o programa não vai fazer nada
            if nometaf == '':
                print('None')
            else:
             #Aqui vai verificar se a tarefa já existe no arquivo. Se ela não existir, caso contrário, o programa não vai fazer nada
             if nometaf not in dados:
                #Código Do Frame onde a Tarefa se encontra, cada frame desse é uma tarefa        
                taframe = ctk.CTkFrame(jnl3,fg_color='saddle brown',bg_color='saddle brown',border_color='white',border_width=3,width=500,height=70)
                taframe.pack()

                #CheckBox: Código que vai verificar se o check box está marcado ou não

                #Aqui eu usei string var porque eu fiz essa parte do programa antes de fazer a parte de carregar, eu preferi não refatorar pra não perder tempo, pois o funcionamento não atrapalha 
                check = ctk.StringVar(value='')    
                #Vai salvar o estado do check pra depois fazer a verificação no carregamento            
                def retorne():
                    dados = carregarjson()
                    comando = check.get()
                    
                    #Aqui, caso a caixinha esteja marcada, vai receber o comando 'Feito', então, vai salvar no arquivo json como True e ativar o botão de feito
                    if comando == 'Feito':
                        deletaf.configure(state = 'normal')

                        if nometaf in dados:
                            dados[nometaf]['state'] = True
                        with open(SavesCaminho,'w+') as arquivo:
                            json.dump(dados,arquivo,indent=4)        
                    
                    #Aqui, caso a caixinha esteja desmarcada, vai receber o comando 'Desfeito', então, vai salvar no arquivo json como False e desativar o botão de feito
                    if comando == 'Desfeito':
                        deletaf.configure(state = 'disabled')

                        if nometaf in dados:
                            dados[nometaf]['state'] = False
                        with open(SavesCaminho,'w+') as arquivo:
                            json.dump(dados,arquivo,indent=4)
     
                #Código Do CheckBox
                checktaf = ctk.CTkCheckBox(taframe,20,20,text=nometaf,onvalue='Feito', offvalue='Desfeito',variable=check,command=retorne,hover_color='white',fg_color='white',text_color='white',checkmark_color='saddle brown',border_color='white',font=('Arial Black', 20))
                checktaf.place(x=10,y=25)

                #Código Do Botão de Feito: Vai iniciar ele desativado, esperando o usuário concluir a tarefa
                deletaf = ctk.CTkButton(taframe,30,50,text='FEITO', command=feito,state='disabled',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,text_color_disabled='snow3')  
                deletaf.place(x=440,y=10)

                #Salvando em um arquivo json. Vai ler o arquivo, e caso ele não exista, vai criar um novo vazio
                if SavesCaminho.exists():
                    with open(SavesCaminho, 'r') as arquivo:
                        dados = json.load(arquivo)
                else:
                    dados = {}        
                
                #Vai Salvar a tarefa desse jeito no arquivo, O nome vai receber um dicionário contendo o estado da checkbox, que na criação da tarefa, vai ser salvo como False 
                dados[nometaf] = {'state': False}
                with open(SavesCaminho,'w') as arquivo:
                    json.dump(dados,arquivo,indent=4)
             
             #Caso o nome da tarefa ja exista, o programa não vai salvar nada e printar um 'Existe' no terminal
             else:
                 print('Existe')

            #Vai fechar a janela extra logo após criar a tarefa
            add.destroy()

        #Botão de adicionar a tarefa á janela principaç
        btn_tarefa = ctk.CTkButton(add,width=20,text='ADICIONAR',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,command=passar)
        btn_tarefa.place(x=158,y=66)

    #Esse Botão vai criar a Janela na Qual a Tarefa vai ser criada e depois enviada á Janela principal
    btn_add = ctk.CTkButton(janela,width=20,text='ADICIONAR',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,command=adicionar)
    btn_add.place(x=600,y=20)

#O botão que depois que clicado, começa o programa (oque é meio irônico pelo fato dele ficar no final do código kkkkk)
começa = ctk.CTkButton(janela,1,1,text='TAREFAS',command=cmç,border_color='white',border_width=1,fg_color='saddle brown', hover_color='white',font=('Arial Black',10),text_color='white')
começa.place(x=317,y=430)

janela.mainloop()

#END
#Programa NeoTarefas: Um gerenciador de Tarefas NeoByte!

#Criador: Alexandre, 19 anos
#Data em que o projeto foi finalizado: 02/05/2025