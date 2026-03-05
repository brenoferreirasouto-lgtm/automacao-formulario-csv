# Automação de Cadastro via CSV (Google Forms) 🤖

Automação em **Python** que lê uma base de dados em **CSV** e realiza o preenchimento automático de um **Google Forms**, simulando ações humanas (cliques, digitação e navegação com TAB/ENTER).  
Projeto focado em praticar automação de tarefas repetitivas e manipulação de dados com `pandas`.

## 🎯 Problema que resolve
Cadastrar muitos registros manualmente em formulários é **lento** e sujeito a **erros**.  
Este script automatiza o processo a partir de uma planilha, reduzindo o trabalho manual e padronizando o preenchimento.

## ✅ O que o script faz
- Lê `dados.csv` com colunas `nome`, `idade`, `email`
- Abre o navegador e acessa o Google Forms
- Para cada registro do CSV:
  - Preenche os campos do formulário (nome, idade, email)
  - Envia o formulário
  - Clica em “Enviar outra resposta”
  - Repete até finalizar

## 🛠️ Tecnologias utilizadas
- **Python 3**
- **Pandas** (leitura/manipulação do CSV)
- **PyAutoGUI** (automação de mouse e teclado)
- **time** (controle de espera/sincronização)

## 📦 Pré-requisitos
- Python 3 instalado
- Repositório com os arquivos:
  - `main.py`
  - `dados.csv`

Instale as dependências:

```bash
pip install pandas pyautogui
