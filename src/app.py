from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data from the analysis notebooks
def load_data():
    # Example of loading data from CSV files generated in the notebooks
    natureza_juridica_data = pd.read_csv('data/raw/arrecadacao_natureza_juridica.csv')
    cnae_data = pd.read_csv('data/raw/arrecadacao_cnae.csv')
    ir_ipi_data = pd.read_csv('data/raw/arrecadacao_ir_ipi.csv')
    return natureza_juridica_data, cnae_data, ir_ipi_data

@app.route('/')
def index():
    natureza_juridica_data, cnae_data, ir_ipi_data = load_data()
    return render_template('index.html', 
                           natureza_juridica=natureza_juridica_data,
                           cnae=cnae_data,
                           ir_ipi=ir_ipi_data)

if __name__ == '__main__':
    app.run(debug=True)