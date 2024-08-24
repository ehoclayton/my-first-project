from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Substitua pelo seu usuário do MySQL
    password="20@Fev91",  # Substitua pela sua senha do MySQL
    database="my_database"
)

@app.route('/users', methods=['GET'])
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
