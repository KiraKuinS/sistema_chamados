# 🎫 Sistema de Gestão de Chamados (CLI)

Aplicação em linha de comando desenvolvida em Python para gerenciamento de chamados técnicos, aplicando conceitos de **Programação Orientada a Objetos (POO)**, **modularização de código (SOC)** e **persistência de dados em JSON**.

---

## 🚀 Funcionalidades

- **Criação de Chamados:** Cadastro de novos tickets com título e prioridade.
- **Listagem Geral:** Exibição organizada de todos os chamados registrados.
- **Atualização de Status:** Alteração de status (Pendente, Em Andamento, Concluído).
- **Busca Flexível:** Filtro por palavra-chave em título, prioridade ou status.
- **Exclusão de Chamados:** Remoção de tickets da base de dados.
- **Persistência de Dados:** Armazenamento automático no arquivo `data/chamados.json`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+**
- Módulos Nativos: `json`, `os`

---

## 📁 Estrutura do Projeto

```text
sistema_chamados/
│
├── data/
│   └── chamados.json
│
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── manager.py
│   └── cli.py
│
├── main.py
├── .gitignore
└── README.md