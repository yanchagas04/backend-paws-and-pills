# 📡 Backend - Paws and Pills

Backend da aplicação Paws and Pills, focada no monitoramento de medicamentos de cães e gatos.

## 🚀 Tecnologias Utilizadas
- FastAPI
- Prisma (ORM)
- PostgreSQL

## 📁 Estrutura do Projeto

```bash
.
├── src/
│   ├── routers/        # Define as rotas da aplicação
│   ├── schemas/        # Modelos de dados usados na API (Pydantic)
│   ├── services/       # Funções responsáveis por acesso e manipulação de dados
│   └── utils/          # Utilitários e estruturas auxiliares
├── dependencies.py     # Arquivo de definição das dependências
├── main.py             # Arquivo principal (ponto de entrada da aplicação)
├── requirements.txt    # Lista de dependências do projeto
├── .gitignore          # Arquivos/pastas ignorados pelo Git
```
## 📌 Descrição das Pastas
**routers/**: Contém os endpoints da API organizados por funcionalidades.

**schemas/**: Define os modelos de dados utilizados na entrada e saída da API com Pydantic.

**services/**: Contém a lógica de negócio e acesso a banco de dados ou outras fontes externas.

**utils/**: Funções auxiliares, helpers e classes reutilizáveis.

## ▶️ Como rodar a API
### 1. Instalação das bibliotecas
```python
pip install -r requirements.txt
```
### 2. Migrate e Generate do Prisma 
```bash
prisma migrate dev
prisma generate
```
### 3. Rodar o servidor Uvicorn
```bash
uvicorn main:app --host HOST_DESEJADO --port PORTA_DESEJADA
```