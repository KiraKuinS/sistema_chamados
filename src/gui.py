import customtkinter as ctk
from src.manager import GerenciadorChamados

ctk.set_appearance_mode("Dark")

class MinhaJanela(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.gerenciador = GerenciadorChamados()
        self.title("Sistema de Gestão de Chamados")
        self.geometry("600x520")

        # 1. Label de texto
        self.lbl_titulo = ctk.CTkLabel(self,
            text="🎫 Gestão de Chamados", 
            font=ctk.CTkFont(size=20, weight="bold")
        )

        # 2. Entrada de texto (Usamos placeholder_text para a dica)
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=10, padx=20, fill="x")

        self.entry_titulo = ctk.CTkEntry(
            self.frame_form, 
            placeholder_text="Título do chamado...", 
            width=220
        )
        self.entry_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.combo_prioridade = ctk.CTkOptionMenu(
            self.frame_form, 
            values=["Baixa", "Média", "Alta"]
        )
        self.combo_prioridade.grid(row=0, column=1, padx=10, pady=10)

        self.btn_criar = ctk.CTkButton(
            self.frame_form, 
            text="Criar Chamado", 
            command=self.criar_chamado
        )
        self.btn_criar.grid(row=0, column=2, padx=10, pady=10)
        
        self.textbox_chamados = ctk.CTkTextbox(
            self, 
            width=550, 
            height=300, 
            font=ctk.CTkFont(family="Consolas", size=12)
        )
        self.textbox_chamados.pack(pady=15, padx=20)
        self.atualizar_lista()
        
    def criar_chamado(self):
        titulo = self.entry_titulo.get().strip()
        prioridade = self.combo_prioridade.get()

        if titulo:
            self.gerenciador.criar_chamado(titulo, prioridade)
            self.entry_titulo.delete(0, "end")
            self.atualizar_lista()

    def atualizar_lista(self):
        self.textbox_chamados.delete("1.0", "end")

        if not self.gerenciador.chamados:
            self.textbox_chamados.insert("end", "Nenhum chamado registrado.")
            return

        header = f"{'ID':<5} | {'TÍTULO':<25} | {'PRIORIDADE':<10} | {'STATUS':<12}\n"
        divisor = "-" * 60 + "\n"
        self.textbox_chamados.insert("end", header + divisor)

        for c in self.gerenciador.chamados:
            linha = f"{c['id']:<5} | {c['titulo']:<25} | {c['prioridade']:<10} | {c['status']:<12}\n"
            self.textbox_chamados.insert("end", linha)


def iniciar_gui():
    app = MinhaJanela()
    app.mainloop()