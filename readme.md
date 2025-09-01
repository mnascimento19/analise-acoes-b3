# Projeto: Análise de Performance de Ações da B3

## Descrição
Este projeto consiste em um pipeline de dados completo para a análise de ações da bolsa de valores brasileira (B3). Os dados são extraídos diariamente, processados com Python, armazenados em um banco de dados SQL Server e visualizados em um dashboard interativo no Power BI.

## Arquitetura do Projeto
Fonte de Dados (Yahoo Finance) -> ETL em Python -> Banco de Dados (SQL Server) -> Dashboard (Power BI)

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Bibliotecas Python:** Pandas, yfinance, pyodbc
- **Banco de Dados:** Microsoft SQL Server
- **Visualização:** Power BI
- **Versionamento:** Git e GitHub

## Como Executar o Projeto
1. **Pré-requisitos:** Ter Python 3, SQL Server e Power BI Desktop instalados.
2. Clone este repositório: `git clone https://github.com/seu-usuario/nome-do-repositorio.git`
3. Navegue até a pasta do projeto: `cd nome-do-repositorio`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure sua string de conexão com o banco de dados no script `etl_acoes.py`.
6. Execute o script para carregar os dados: `python etl_acoes.py`
7. Abra o arquivo do Power BI para visualizar o dashboard.