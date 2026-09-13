# 🎫 Sistema de Gestão de Chamados

Aplicação desktop desenvolvida em Python para gerenciamento e acompanhamento de chamados de suporte técnico, utilizando interface gráfica moderna e persistência de dados em formato JSON.

---

## 🚀 Funcionalidades

- **Abertura de Chamados:** Cadastro simples com definição de título e nível de prioridade (Baixa, Média, Alta).
- **Interface Gráfica Intuitiva:** Desenvolvida com CustomTkinter para um visual moderno em modo escuro (Dark Mode).
- **Persistência de Dados:** Armazenamento automático e estruturado das informações no arquivo `chamados.json`.
- **Listagem Dinâmica:** Exibição imediata dos chamados cadastrados e seus respectivos status em tempo real.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **GUI Framework:** CustomTkinter
- **Persistência:** JSON

---

## 📂 Estrutura do Projeto

```text
sistema_chamados/
├── data/
│   └── chamados.json      # Banco de dados em formato JSON
├── src/
│   ├── gui.py             # Interface gráfica (CustomTkinter)
│   └── manager.py         # Regra de negócio e manipulação do JSON
├── .gitignore
├── main.py                # Ponto de entrada da aplicação
└── README.md              # Documentação do repositório
⚙️ Como Executar o Projeto
Clone o repositório:

Bash
git clone [https://github.com/KiraKuinS/sistema_chamados.git](https://github.com/KiraKuinS/sistema_chamados.git)
cd sistema_chamados
Instale a biblioteca CustomTkinter:

Bash
pip install customtkinter
Inicie a aplicação:

Bash
python main.py