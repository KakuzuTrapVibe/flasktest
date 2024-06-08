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
    cur.execute("""SELECT Nome_pet from pet WHERE IDdono_pet='""" + str(IDdono) + """'""")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/enviarLoc', methods=['GET', 'POST'])
def enviarLoc():
    idPet = request.args.get('idPet')
    lat = request.args.get('lat')
    long = request.args.get('long')
    vel = request.args.get('vel')
    
    try:
        cur = mysql.connection.cursor()
        query = "INSERT INTO localiza VALUES (NULL, %s, %s, %s, %s, CURRENT_TIMESTAMP)"
        cur.execute(query, (idPet, lat, long, vel))
        mysql.connection.commit()
        return jsonify({'status': 'Success', 'message': 'Cadastro concluído'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    senha = request.args.get('senha')

    if not email or not senha:
        return jsonify({'status': 'error', 'message': 'Email and password are required'}), 400

    cur = mysql.connection.cursor()
    query = "SELECT * FROM usuario WHERE email=%s AND senha=%s"
    cur.execute(query, (email, senha))
    user = cur.fetchone()

    if user:
        return jsonify({'status': 'Success', 'user': user})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid email or password'}), 401

@app.route('/cadastroPet', methods=['POST'])
def cadastroPet():
    data = request.get_json()
    idDono = data.get('idDono')
    Nome_pet = data.get('Nome_pet ')
    Animal = data.get('Animal')
    Raio_seguranca = data.get('Raio_seguranca')
    
    if not all([idDono, Nome_pet, Animal, Raio_seguranca]):
        return jsonify({'status': 'error', 'message': 'All fields are required'}), 400
    
    try:
        cur = mysql.connection.cursor()
        query = "INSERT INTO usuario (IDdono_pet, Nome_pet, Animal, Raio_seguranca) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (idDono, Nome_pet, Animal, Raio_seguranca))
        mysql.connection.commit()
        return jsonify({'status': 'Success', 'message': 'Cadastro do pet concluído'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    nome = data.get('nome')
    raio = data.get('raio')
    notifica = data.get('notifica')
    email = data.get('email')
    senha = data.get('senha')
    
    if not all([nome, raio, notifica, email, senha]):
        return jsonify({'status': 'error', 'message': 'All fields are required'}), 400
    
    try:
        cur = mysql.connection.cursor()
        query = "INSERT INTO usuario (nome, email, senha, raio, notifica) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (nome, email, senha, raio, notifica))
        mysql.connection.commit()
        return jsonify({'status': 'Success', 'message': 'Cadastro concluído'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/historico', methods=['GET'])
def Historico():
    idPet = request.args.get('idPet')
    data = request.args.get('data')

    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from localiza WHERE IDpet_local='""" + str(idPet) + """' AND DATE(Data_hora)='"""+ str(data) +"""'""")
    historyData = cur.fetchall()
    return jsonify(historyData)

if __name__ == '__main__':
    app.run(debug=True)
