from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'apprastreador.mysql.uhserver.com'
app.config['MYSQL_USER'] = 'marcaralho'
app.config['MYSQL_PASSWORD'] = 'pickup-2007'
app.config['MYSQL_DB'] = 'apprastreador'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getPets', methods=['GET'])
def getPets():
    IDdono = request.args.get('IDdono')
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from pet WHERE IDdono_pet='""" + str(IDdono) + """'""")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/login', methods=['GET'])
def Login():
    email = request.args.get('email')
    senha = request.args.get('senha')
    
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from usuario WHERE email='""" + str(email) + """' AND  senha='""" + str(senha) + """'""")
    user = cur.fetchone()
    return jsonify(user)

@app.route('/cadastro', methods=['POST'])
def Cadastro():
    nome = request.args.get('nome')
    Raio = request.args.get('raio')
    Notifica = request.args.get('notf')
    Email = request.args.get('email')
    senha = request.args.get('senha')
    
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO usuario VALUES ('null""" + str(nome) + """','""" + str(Email) + """','""" + str(senha) + """','""" + str(Raio)+ """','""" + str(Notifica)+ """')""")
    return jsonify("Cadastro concluído")

@app.route('/historico', methods=['GET'])
def Historico():
    idPet = request.args.get('idPet')
    data = request.args.get('data')

    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from localiza WHERE IDpet_local='""" + str(idPet) + """AND DATE(Data_hora)='"""+ str(data) +"""'""")
    historyData = cur.fetchall()
    return jsonify(historyData)

if __name__ == '__main__':
    app.run(debug=True)
