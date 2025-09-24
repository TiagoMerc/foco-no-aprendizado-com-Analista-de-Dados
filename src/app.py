# Estrutura básica do app Flask para servir páginas HTML
# que exibem os resultados das análises feitas nos notebooks.

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__) # Inicializando a aplicação Flask

# Carregando dados dos cadernos de análise
def load_data(): # Função para carregar os dados
    # Exemplo de carregamento de dados a partir de arquivos CSV gerados nos notebooks
    natureza_juridica_data = pd.read_csv('data/raw/arrecadacao_natureza_juridica.csv')
    cnae_data = pd.read_csv('data/raw/arrecadacao_cnae.csv')
    ir_ipi_data = pd.read_csv('data/raw/arrecadacao_ir_ipi.csv')
    return natureza_juridica_data, cnae_data, ir_ipi_data

@app.route('/') # Rota principal que renderiza a página inicial
def index(): # Função para renderizar a página inicial
    natureza_juridica_data, cnae_data, ir_ipi_data = load_data() # Carregando os dados
    return render_template('index.html',   # Renderizando o template HTML com os dados
                           natureza_juridica=natureza_juridica_data,
                           cnae=cnae_data, # Passando os dados para o template
                           ir_ipi=ir_ipi_data)

if __name__ == '__main__':
    app.run(debug=True) # Rodando o servidor em modo debug