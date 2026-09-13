import json
import os
from src.models import Chamado

class GerenciadorChamados:
    def __init__(self, arquivo_json: str = os.path.join("data", "chamados.json")):
        self.arquivo = arquivo_json
        
        # Garante que a pasta 'data' existe
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        self.chamados = self.carregar_dados()

    def carregar_dados(self) -> list:
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_dados(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.chamados, f, indent=4, ensure_ascii=False)

    def criar_chamado(self, titulo: str, prioridade: str):
        novo_id = len(self.chamados) + 1
        novo_chamado = Chamado(novo_id, titulo, prioridade)
        self.chamados.append(novo_chamado.to_dict())
        self.salvar_dados()
        print(f"\n✅ Chamado #{novo_id} ('{titulo}') criado com sucesso!")

    def listar_chamados(self):
        if not self.chamados:
            print("\n⚠️ Nenhum chamado registrado.")
            return

        print("\n" + "="*55)
        print(f"{'ID':<4} | {'TÍTULO':<20} | {'PRIORIDADE':<10} | {'STATUS':<10}")
        print("="*55)
        for c in self.chamados:
            print(f"{c['id']:<4} | {c['titulo']:<20} | {c['prioridade']:<10} | {c['status']:<10}")
        print("="*55)

    def atualizar_status(self, id_chamado: int, novo_status: str):
        for c in self.chamados:
            if int(c["id"]) == int(id_chamado):
                c["status"] = novo_status
                self.salvar_dados()
                print(f"\n✅ Status do chamado #{id_chamado} alterado para '{novo_status}'.")
                return
        print(f"\n❌ Chamado #{id_chamado} não encontrado.")
        
    def deletar_chamado (self,id_chamado: int) -> bool:
        for c in self.chamados:
            if int(c["id"]) == int(id_chamado):
                self.chamados.remove(c)
                self.salvar_dados()
                print(f"\n🗑️ Chamado #{id_chamado} removido com sucesso!")
                return True
        print(f"\n❌ Chamado #{id_chamado} não encontrado.")
        return False
    
    def buscar_chamados(self, termo:str):
        termo_lc = termo.lower()
        resultados = [
            c for c in self.chamados
            if termo_lc in c["titulo"].lower()
        ]

        if not resultados:
            print(f"\n⚠️ Nenhum chamado encontrado para o termo '{termo}'.")
            return

        print("\n" + "="*55)
        print(f"{'ID':<4} | {'TÍTULO':<20} | {'PRIORIDADE':<10} | {'STATUS':<10}")
        print("="*55)
        for c in resultados:
            print(f"{c['id']:<4} | {c['titulo']:<20} | {c['prioridade']:<10} | {c['status']:<10}")
        print("="*55)