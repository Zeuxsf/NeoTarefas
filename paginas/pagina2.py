import customtkinter as ctk

class Pagina2(ctk.CTkFrame):
    NOME = "pagina2"

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(self, text="Página 2", font=ctk.CTkFont(size=24, weight="bold"))
        titulo.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        # Área de texto + entrada de exemplo
        frame = ctk.CTkFrame(self)
        frame.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text="Digite algo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entrada = ctk.CTkEntry(frame, placeholder_text="Texto de entrada...")
        self.entrada.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.texto = ctk.CTkTextbox(frame, height=200)
        self.texto.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.texto.insert("end", "Área de texto livre para o seu projeto.\n")

        ctk.CTkButton(frame, text="Adicionar", command=self._adicionar).grid(
            row=3, column=0, padx=10, pady=10, sticky="e"
        )

    def _adicionar(self):
        valor = self.entrada.get().strip()
        if valor:
            self.texto.insert("end", f"→ {valor}\n")
            self.entrada.delete(0, "end")
