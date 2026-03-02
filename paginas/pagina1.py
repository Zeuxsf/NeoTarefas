import customtkinter as ctk
class Pagina1(ctk.CTkFrame):
    NOME = "pagina1"

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header.grid_rowconfigure(0, weight=1)

        
        self.titulo = ctk.CTkLabel(self.header, text="Tarefas", font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.grid(row=0, column=0, padx=(30,1), pady=(30, 10), sticky="w")

        
        self.btn_add = ctk.CTkButton(self.header, text="+",width=25,height=25, command=self._criar_tarefa)
        self.btn_add.grid(row=0, column=1, padx=(10,30), pady=(30, 10), sticky="e")

        
        self.frame_conteudo = ctk.CTkScrollableFrame(self)
        self.frame_conteudo.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")
        self.frame_conteudo.grid_columnconfigure(0,weight=1)

        
        for i in self.app.dados["tarefas"]:
            self._carregar_tarefa(tarefa=i)

    """
    ---
    def _popup(self): POPUP interessante
            popup = ctk.CTkFrame(self,width=500,height=300,border_color='white',border_width=1)
            popup.grid(row=1,column=0)
    ---        
    """
    
    def _carregar_tarefa(self,tarefa=None):

        def finalizar_tarefa(self, texto, frame): 
            self.app.dados["tarefas"].remove(texto.get("1.0","end").strip()) 
            self.app.dados["concluidas"].append(texto.get("1.0","end").strip())
            self.app._dados_salvar()

            frame.destroy()        

        linha = self.frame_conteudo.grid_size()[1]

        tarefa_frame = ctk.CTkFrame(self.frame_conteudo)
        tarefa_frame.grid(row=linha, column=0, padx=10, pady=5, sticky="ew")
        tarefa_frame.grid_columnconfigure(1,weight=1)

        texto = ctk.CTkTextbox(tarefa_frame,height=10)
        texto.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        texto.insert("0.0", tarefa)
        texto.configure(state="disabled")      

        btn = ctk.CTkButton(tarefa_frame,text="Feito",width=25,height=25, command=lambda: finalizar_tarefa(self,texto,tarefa_frame))
        btn.grid(row=0, column=0,padx=1,pady=5,sticky="w")
    
    def _criar_tarefa(self):
        
        def confirmar_nome_tarefa(self, texto, botao):
            self.app.dados["tarefas"].append(texto.get("1.0","end").strip())
            self.app._dados_salvar()

            texto.configure(state="disabled")
            botao.destroy()

        def finalizar_tarefa(self, texto, frame):
            self.app.dados["tarefas"].remove(texto.get("1.0","end").strip()) 
            self.app.dados["concluidas"].append(texto.get("1.0","end").strip())
            self.app._dados_salvar()

            frame.destroy()                    

        linha = self.frame_conteudo.grid_size()[1]

        tarefa_frame = ctk.CTkFrame(self.frame_conteudo)
        tarefa_frame.grid(row=linha, column=0, padx=10, pady=5, sticky="ew")
        tarefa_frame.grid_columnconfigure(1,weight=1)

        texto = ctk.CTkTextbox(tarefa_frame,height=10)
        texto.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        btn = ctk.CTkButton(tarefa_frame,text="Feito",width=25,height=25, command=lambda: finalizar_tarefa(self,texto, tarefa_frame))
        btn.grid(row=0, column=0,padx=1,pady=5,sticky="w")

        btn2 = ctk.CTkButton(tarefa_frame,text="Confirmar",width=25,height=25, command=lambda: confirmar_nome_tarefa(self,texto,btn2))
        btn2.grid(row=0, column=0,padx=1,pady=5,sticky="w")


    
