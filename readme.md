# Análise de Performance de Ações da B3

## Descrição
Projeto de portfólio de análise de dados de ponta a ponta (end-to-end) que explora a performance diária de um conjunto de ações da bolsa de valores brasileira (B3), utilizando dados públicos do mercado financeiro.

## Objetivo
O objetivo deste projeto foi construir um pipeline de dados completo para extrair, transformar, carregar e visualizar dados históricos de cotações e volumes de negociação, permitindo a análise comparativa de performance entre diferentes ativos.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas Principais:** Pandas, yfinance, pyodbc
- **Banco de Dados:** Microsoft SQL Server
- **Ferramenta de BI:** Power BI
- **Versionamento:** Git e GitHub

## Estrutura do Pipeline
O script `etlacoes.py` automatiza todo o processo de ETL:

1.  **Extração:** Conecta-se à API do Yahoo Finance através da biblioteca `yfinance` para buscar as séries históricas de cotações das ações selecionadas.
2.  **Transformação:** Utiliza a biblioteca Pandas para limpar, estruturar e reorganizar os dados em um formato analítico.
3.  **Carga:** Carrega os dados tratados em uma tabela no banco de dados SQL Server, deixando-os prontos para o consumo.

O dashboard desenvolvido no Power BI conecta-se a este banco de dados para a análise visual interativa.

## Dashboard Final
Uma prévia do dashboard finalizado, que permite a análise de KPIs, evolução de preços e participação no volume de negociação:

![Imagem do WhatsApp de 2025-09-01 à(s) 12 48 56_0bc65d28](https://github.com/user-attachments/assets/a945a32a-d5d3-4319-a108-7194b7e8144a)

