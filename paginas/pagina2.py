import customtkinter as ctk

class Pagina2(ctk.CTkFrame):
    NOME = "pagina2"

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header.grid_rowconfigure(0, weight=1)

        
        self.titulo = ctk.CTkLabel(self.header, text="Concluídas", font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.grid(row=0, column=0, padx=(30,1), pady=(30, 10), sticky="w")


        self.frame_conteudo = ctk.CTkScrollableFrame(self)
        self.frame_conteudo.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")
        self.frame_conteudo.grid_columnconfigure(0,weight=1)

        
        for i in self.app.dados["concluidas"]:
            self._carregar_tarefa(tarefa=i)

    """
    ---
    def _popup(self): POPUP interessante
            popup = ctk.CTkFrame(self,width=500,height=300,border_color='white',border_width=1)
            popup.grid(row=1,column=0)
    ---        
    """
    
    def _carregar_tarefa(self,tarefa=None):

        def desfazer_tarefa(self, texto, frame):   
            self.app.dados["concluidas"].remove(texto.get("1.0","end").strip()) 
            self.app.dados["tarefas"].append(texto.get("1.0","end").strip())
            self.app._dados_salvar()

            frame.destroy()        

        def excluir_tarefa(self, texto, frame):   
            self.app.dados["concluidas"].remove(texto.get("1.0","end").strip()) 
            self.app._dados_salvar()

            frame.destroy()            

        linha = self.frame_conteudo.grid_size()[1]

        tarefa_frame = ctk.CTkFrame(self.frame_conteudo)
        tarefa_frame.grid(row=linha, column=0, padx=10, pady=5, sticky="ew")
        tarefa_frame.grid_columnconfigure(2,weight=1)

        texto = ctk.CTkTextbox(tarefa_frame,height=10)
        texto.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        texto.insert("0.0", tarefa)
        texto.configure(state="disabled")      

        btn = ctk.CTkButton(tarefa_frame,text="Desfazer",width=25,height=25, command=lambda: desfazer_tarefa(self,texto,tarefa_frame))
        btn.grid(row=0, column=0,padx=1,pady=5,sticky="w")

        btn_excluir = ctk.CTkButton(tarefa_frame,text="Excluir",width=25,height=25, command=lambda: excluir_tarefa(self,texto, tarefa_frame))
        btn_excluir.grid(row=0, column=1,padx=1,pady=5,sticky="w")
