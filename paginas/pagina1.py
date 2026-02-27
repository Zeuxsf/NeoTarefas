import customtkinter as ctk

class Pagina1(ctk.CTkFrame):
    NOME = "pagina1"

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Cabeçalho
        titulo = ctk.CTkLabel(self, text="Página 1", font=ctk.CTkFont(size=24, weight="bold"))
        titulo.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        # Conteúdo de exemplo
        frame_conteudo = ctk.CTkScrollableFrame(self, label_text="Conteúdo")
        frame_conteudo.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

        for i in range(1, 6):
            ctk.CTkLabel(frame_conteudo, text=f"Item de exemplo {i}").pack(
                padx=10, pady=5, anchor="w"
            )

        # Botão de ação
        btn = ctk.CTkButton(self, text="Executar Ação", command=self._acao)
        btn.grid(row=2, column=0, padx=30, pady=20, sticky="e")

    def _acao(self):
        print("Ação da Página 1 executada!")

# ───────────────────────────────────────────────────────────────────────────