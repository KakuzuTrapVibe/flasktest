from flask import Flask, jsonify
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
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * from Pets""")
    rv = cur.fetchall()
    return jsonify(rv)

if __name__ == '__main__':
    app.run(debug=True)
    