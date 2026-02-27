import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

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
        #self._criar_area_principal()

    def _criar_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0,column=0,rowspan=2,sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)

        titulo = ctk.CTkLabel(self.sidebar, text="NeoTarefas", font=ctk.CTkFont(size=20,weight="bold"))
        titulo.grid(row=0,column=0,padx=20,pady=(20,10))

        self.btn_pagina1 = ctk.CTkButton(self.sidebar, text="Tarefas", command=lambda: self._trocar_pagina("pagina1"))
        self.btn_pagina1.grid(row=1,column=0,padx=20,pady=5,sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()