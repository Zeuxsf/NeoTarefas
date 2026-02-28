import customtkinter as ctk

class Pagina1(ctk.CTkFrame):
    NOME = "pagina1"

    def __init__(self, parent):
        super().__init__(parent)
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

    """def _criar_tarefa(self): POPUP interessante
            popup = ctk.CTkFrame(self,width=500,height=300,border_color='white',border_width=1)
            popup.grid(row=1,column=0)
"""
    def _criar_tarefa(self):
        linha = self.frame_conteudo.grid_size()[1]

        tarefa = ctk.CTkFrame(self.frame_conteudo)
        tarefa.grid(row=linha, column=0, padx=10, pady=5, sticky="ew")
        tarefa.grid_columnconfigure(1,weight=1)

        btn = ctk.CTkButton(tarefa,text="Feito",width=25,height=25, command=lambda: tarefa.destroy())
        btn.grid(row=0, column=0,padx=1,pady=5,sticky="w")

        texto = ctk.CTkTextbox(tarefa,height=10)
        texto.grid(row=0, column=1, padx=5, pady=5, sticky="ew")



