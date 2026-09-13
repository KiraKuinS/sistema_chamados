from datetime import datetime

class Chamado:
    def __init__(self, id_chamado: int, titulo: str, prioridade: str):
        self.id = id_chamado
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = "Pendente"
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_criacao": self.data_criacao
        }