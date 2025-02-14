from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pickle

colunas = ['tamanho', 'ano', 'garagem']

with open('model.sav', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'gabriel'
app.config['BASIC_AUTH_PASSWORD'] = 'nichio'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return 'Minha primeira API.'

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = model.predict([dados_input])
    return jsonify(preco=preco[0])


app.run(debug=True)