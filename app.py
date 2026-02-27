import customtkinter as ctk
from paginas.pagina1 import Pagina1
from paginas.pagina2 import Pagina2


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NeoTarefas")

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        largura_janela = max(800, min(int(largura_tela * 0.80), 1400))
        altura_janela = max(500, min(int(altura_tela * 0.80), 900))

        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        self.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        self.minsize(800, 500)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._criar_sidebar()
        self._criar_area_principal()

    def _criar_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0,column=0,rowspan=2,sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)

        titulo = ctk.CTkLabel(self.sidebar, text="NeoTarefas", font=ctk.CTkFont(size=20,weight="bold"))
        titulo.grid(row=0,column=0,padx=20,pady=(20,10))

        self.btn_pagina1 = ctk.CTkButton(self.sidebar, text="Tarefas", command=lambda: self._trocar_pagina("pagina1"))
        self.btn_pagina1.grid(row=1,column=0,padx=20,pady=5,sticky="ew")

        self.btn_pagina2 = ctk.CTkButton(self.sidebar, text="Concluídas", command=lambda: self._trocar_pagina("pagina2"))
        self.btn_pagina2.grid(row=5,column=0,padx=20,pady=5,sticky="ew")

    def _criar_area_principal(self):
        self.caixa = ctk.CTkFrame(self)
        self.caixa.grid(row=0, column=1,padx=20,pady=20,sticky="nsew")
        self.caixa.grid_rowconfigure(0,weight=1)
        self.caixa.grid_columnconfigure(0,weight=1)

        self.paginas: dict[str, ctk.CTkFrame] = {}

        for PaginaClasse in (Pagina1, Pagina2):
            pagina = PaginaClasse(self.caixa)
            self.paginas[pagina.NOME] = pagina
            pagina.grid(row=0,column=0,sticky="nsew")

        self._trocar_pagina("pagina1")

    def _trocar_pagina(self, nome: str):
        pagina = self.paginas.get(nome)
        if pagina:
            pagina.tkraise()            

if __name__ == "__main__":
    app = App()
    app.mainloop()