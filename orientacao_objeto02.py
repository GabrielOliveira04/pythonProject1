from flask import Flask, render_template
app= Flask(__name__)



class Pessoa():
    """
        Classe que representa uma pessoa.

        Atributos:
        - nome: str com o nome da pessoa
        - idade: int com a idade da pessoa
        - email: str com o endereço de e-mail da pessoa
        """
    def __init__(self, nome, idade =0, email=""):
        self.nome = nome
        self.idade = idade
        self.email = email

    def set_idade(self, idade):
        self.idade = idade

    def set_email(self, email):
        self.email = email

#Criar uma lista de pessoa
pessoas = [
Pessoa('gabriel',30,'email1232GMAIL.COM'),
Pessoa('Emmylly',25,'email321@gmail.com'),
Pessoa('Luis',80,'email@324@gmail.com')
]

@app.route('/')
def index():
    return render_template('index.html',pessoas=pessoas)




if __name__ =='__main__':
    app.run()