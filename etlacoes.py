

import pandas as pd
import yfinance as yf
import pyodbc

tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'MGLU3.SA', '^BVSP']
data_inicio = '2023-01-01'
data_fim = '2024-12-31'


lista_de_dataframes = []
print("Baixando todos os dados de uma vez...")
dados_brutos = yf.download(tickers=tickers, start=data_inicio, end=data_fim)

print("Reorganizando a estrutura da tabela...")
df_final = dados_brutos.stack().reset_index()
df_final.rename(columns={'level_1': 'Ticker'}, inplace=True)
print("\nETL finalizado com sucesso! O DataFrame final está pronto.")
print("Dimensões do DataFrame final:", df_final.shape)
print("\nVerificando o início dos dados:")
print(df_final.head())
print("\nVerificando o final dos dados:")
print(df_final.tail())



# ==============================================================================
# 2. CARGA DE DADOS NO SQL SERVER
# ==============================================================================


server_name = 'MATHEUSNASC\SQLEXPRESS' 
database_name = 'dbacoesb3'
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server_name};'
    f'DATABASE={database_name};'
    f'Trusted_Connection=yes;'
)

try:
    print("\nConectando ao SQL Server...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

    print("Limpando a tabela HistoricoAcoes...")
    cursor.execute("TRUNCATE TABLE HistoricoAcoes")
    
    print("Iniciando a carga dos dados...")
    sql_insert = """
    INSERT INTO HistoricoAcoes (Date, Ticker, [Close], [High], [Low], [Open], Volume)
    VALUES (?, ?, ?, ?, ?, ?, ?); 
"""

    #Converte o DataFrame para o formato correto para inserção
  
    dados_para_inserir = [tuple(row) for row in df_final.itertuples(index=False)]

    # Executa a inserção de forma eficiente
    cursor.executemany(sql_insert, dados_para_inserir)
    
    # Confirma a transação
    conn.commit()

    print(f"\nCarga finalizada com sucesso! {len(dados_para_inserir)} linhas foram inseridas na tabela.")

except Exception as e:
    print(f"\nOcorreu um erro ao conectar ou inserir os dados: {e}")

finally:
   
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
        print("Conexão com o SQL Server fechada.")

print("Script finalizado.")

 