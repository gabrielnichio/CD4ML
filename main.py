from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv")

df = df[['tamanho', 'preco']]

x = df.drop('preco', axis=1)
y = df['preco']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Minha primeira API.'

@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = model.predict([[tamanho]])
    return str(preco)


app.run()