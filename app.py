from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10701793'
app.config['MYSQL_PASSWORD'] = '8dt1R9KwG7'
app.config['MYSQL_DB'] = 'sql10701793'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getPets', methods=['GET'])
def getPets():
    idDono = request.args.get('idDono')
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from Pets WHERE idDono='""" + str(idDono) + """'""")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/login', methods=['GET'])
def Login():
    email = request.args.get('email')
    senha = request.args.get('senha')
    
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from Usuarios WHERE email='""" + str(email) + """' AND  senha='""" + str(senha) + """'""")
    user = cur.fetchone()
    return jsonify(user)

@app.route('/cadastro', methods=['POST'])
def Cadastro():
    nome = request.args.get('nome')
    endereco = request.args.get('endereco')
    cep = request.args.get('cep')
    email = request.args.get('email')
    senha = request.args.get('senha')
    
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO Usuarios VALUES ('""" + str(nome) + """','""" + str(endereco) + """','""" + str(cep) + """','""" + str(email)+ """','""" + str(senha)+ """')""")
    return jsonify("Cadastro concluído")

if __name__ == '__main__':
    app.run(debug=True)
    
