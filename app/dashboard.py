# Criando um dashboard interativo com Dash para visualização dos dados de arrecadação federal do Brasil
#  utilizando o framework Dash e Plotly.

# Fazendo importação das bibliotecas necessárias
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Caminhos dos arquivos de dados 
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
natureza_path = os.path.join(data_dir, 'arrecadacao-natureza.csv')
cnae_path = os.path.join(data_dir, 'arrecadacao-cnae.csv')
ir_ipi_path = os.path.join(data_dir, 'arrecadacao-ir-ipi.csv')

# Carregando dados
natureza_df = pd.read_csv(natureza_path, encoding='latin1', sep=';')
cnae_df = pd.read_csv(cnae_path, encoding='latin1', sep=';')
ir_ipi_df = pd.read_csv(ir_ipi_path, encoding='latin1', sep=';')

app = dash.Dash(__name__) # Inicializando a aplicação Dash

app.layout = html.Div([ # Definindo o layout do dashboard
    html.H1('Dashboard de Arrecadação Federal'), # Título do dashboard
    dcc.Tabs([   # Criando abas para diferentes visualizações
        dcc.Tab(label='Natureza Jurídica', children=[  # Aba para Natureza Jurídica
            dcc.Graph( # Gráfico de barras para Natureza Jurídica
                id='natureza-graph',  # Identificador do gráfico
                figure=px.bar(natureza_df, x=natureza_df.columns[0], y=natureza_df.columns[-1], # Definindo o gráfico
                              title='Arrecadação por Natureza Jurídica') # Título do gráfico
            )
        ]),
        dcc.Tab(label='CNAE', children=[
            dcc.Graph(
                id='cnae-graph',
                figure=px.bar(cnae_df, x=cnae_df.columns[0], y=cnae_df.columns[-1],
                              title='Arrecadação por CNAE')
            )
        ]),
        dcc.Tab(label='IR e IPI', children=[
            dcc.Graph(
                id='ir-ipi-graph',
                figure=px.line(ir_ipi_df, x=ir_ipi_df.columns[0], y=ir_ipi_df.columns[-1],
                               title='Arrecadação de IR e IPI detalhada')
            )
        ]),
    ])
])

if __name__ == '__main__': # Executando o servidor da aplicação
    app.run(debug=True) # Rodando o servidor em modo debug
