import customtkinter as ctk
import json
import os
from pathlib import Path

pastasaves = Path('TarefasSalvas')
pastasaves.mkdir(parents=True,exist_ok=True)

SavesCaminho = pastasaves / 'salvos.json'

janela = ctk.CTk(fg_color='darkgoldenrod1')
janela.geometry('700x500')
janela.title('Neo Tarefas')
janela.iconbitmap('./ico.ico')
janela.resizable(False, False)

jnl = ctk.CTkFrame(janela,fg_color='saddle brown',width=680,height=480,border_color='darkgoldenrod2',border_width=5)
jnl.place(x=10,y=10)

expressão = ctk.CTkLabel(jnl,text='█ ‿ █',font=('bold',202),text_color='white')
expressão.place(x=93,y=90)

def cmç():
    expressão.destroy()
    começa.destroy()

    ctk.CTkLabel(janela,text='TAREFAS',font=('Arial Black',20),text_color='white',bg_color='saddle brown').place(x=25,y=18)

    #Colar abaixo
    jnl2 = ctk.CTkFrame(janela,fg_color='saddle brown',bg_color='saddle brown',border_color='white',border_width=3,width=660,height=430)
    jnl2.place(x=20,y=53)

    jnl3 = ctk.CTkScrollableFrame(janela,fg_color='saddle brown',bg_color='saddle brown',width=612,height=407,scrollbar_button_color='white',scrollbar_button_hover_color='snow3')
    jnl3.place(x=35,y=59)

    #Funçãp ADICIONAR
    def adicionar():
        add = ctk.CTkToplevel(janela,fg_color='darkgoldenrod1')
        add.geometry('400x100')
        add.title('ADICIONAR Tarefa')
        add.resizable(False,False)
        
        addd = ctk.CTkFrame(add,390,97,fg_color='saddle brown',border_color='darkgoldenrod2',border_width=3)
        addd.place(x=5,y=3)

        tarefa = ctk.CTkEntry(add,365,50,bg_color='saddle brown',fg_color='saddle brown',border_color='white',border_width=2,text_color='white',placeholder_text='Nome da Tarefa...',placeholder_text_color='snow2')
        tarefa.place(x=17,y=13)

        #Função ADD
        def passar():
            def feito():
                taframe.destroy()

            check = ctk.StringVar(value='')    
            def retorne():
                comando = check.get()
                if comando == 'Feito':
                    deletaf.configure(state = 'normal')
                if comando == 'Desfeito':
                    deletaf.configure(state = 'disabled')

                return comando        
    

            nometaf = tarefa.get().strip()
            if nometaf == '':
                print('None')
            else:
                #Código Do Frame onde a Tarefa se encontra        
                taframe = ctk.CTkFrame(jnl3,fg_color='saddle brown',bg_color='saddle brown',border_color='white',border_width=3,width=500,height=70)
                taframe.pack()

                #Código Do CheckBox
                checktaf = ctk.CTkCheckBox(taframe,20,20,text=nometaf,onvalue='Feito', offvalue='Desfeito',variable=check,command=retorne,hover_color='white',fg_color='white',text_color='white',checkmark_color='saddle brown',border_color='white',font=('Arial Black', 20))
                checktaf.place(x=10,y=25)

                #Código Do Botão de Feito
                deletaf = ctk.CTkButton(taframe,30,50,text='FEITO', command=feito,state='disabled',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,text_color_disabled='snow3')  
                deletaf.place(x=440,y=10)

                #Salvando em um arquivo json

                with open(SavesCaminho,'a') as arquivo:
                    json.dump(nometaf,arquivo,indent=4)


            add.destroy()

        #Botão de adicionar a tarefa
        btn_tarefa = ctk.CTkButton(add,width=20,text='ADICIONAR',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,command=passar)
        btn_tarefa.place(x=158,y=66)


    #Função SALVAR
    def salvar():
        pass

    btn_add = ctk.CTkButton(janela,width=20,text='ADICIONAR',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,command=adicionar)
    btn_add.place(x=535,y=18)


    btn_salvar = ctk.CTkButton(janela,width=20,text='SALVAR',font=('Arial Black',10),text_color='white',bg_color='saddle brown',fg_color='saddle brown',hover_color='white',border_color='white',border_width=2,command=salvar)
    btn_salvar.place(x=620,y=18)


#O main termina aqui
começa = ctk.CTkButton(janela,1,1,text='TAREFAS',command=cmç,border_color='white',border_width=1,fg_color='saddle brown', hover_color='white',font=('Arial Black',10),text_color='white')
começa.place(x=317,y=430)

janela.mainloop()