import customtkinter as ctk

"""
==============================================================================
                    COLINHA DE SOBREVIVÊNCIA - CUSTOMTKINTER
==============================================================================
"""

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MinhaJanela(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- ID INCREMENTAL ---
        self.proximo_id = 1  # Inicia o contador de ID

        # Configurações básicas da tela
        self.title("Título da Janela")
        self.geometry("600x400")
        self.resizable(True, True)

        # --- WIDGETS ---
        self.meu_texto = ctk.CTkLabel(
            self, 
            text="Texto de Exemplo", 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.meu_texto.pack(pady=10)

        self.minha_entrada = ctk.CTkEntry(
            self, 
            placeholder_text="Digite algo aqui...", 
            width=250
        )
        self.minha_entrada.pack(pady=10)

        self.meu_dropdown = ctk.CTkOptionMenu(
            self, 
            values=["Baixa", "Média", "Alta"]
        )
        self.meu_dropdown.pack(pady=10)

        self.meu_botao = ctk.CTkButton(
            self, 
            text="Executar Ação", 
            command=self.minha_funcao_ao_clicar
        )
        self.meu_botao.pack(pady=10)

        self.minha_caixa_texto = ctk.CTkTextbox(
            self, 
            width=500, 
            height=150, 
            font=ctk.CTkFont(family="Consolas", size=12)
        )
        self.minha_caixa_texto.pack(pady=10)

    def minha_funcao_ao_clicar(self):
        texto_digitado = self.minha_entrada.get().strip()
        opcao_selecionada = self.meu_dropdown.get()

        if texto_digitado:
            # Pega o ID atual do contador
            id_chamado = self.proximo_id

            self.meu_texto.configure(text=f"Recebido: {texto_digitado}")
            self.minha_entrada.delete(0, "end")

            # Escreve a linha formatada com o ID correto
            self.minha_caixa_texto.insert(
                "end", 
                f"ID: {id_chamado:<3} | Item: {texto_digitado:<20} | Prioridade: {opcao_selecionada}\n"
            )

            # Incrementa +1 no ID para o próximo clique
            self.proximo_id += 1
        else:
            self.minha_caixa_texto.delete("1.0", "end")


if __name__ == "__main__":
    app = MinhaJanela()
    app.mainloop()