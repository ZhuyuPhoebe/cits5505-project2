from flask import Flask, request, jsonify
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/api/test')
def hello():
    return 'Hello World!'

@app.route('/api/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('cits.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        rows = cursor.fetchall()
        print(rows)
        conn.close()

        if len(rows):
            return jsonify(code=200,msg='success')
        else:
            return jsonify(code=400,msg='error')

@app.route('/api/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('cits.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = cursor.fetchall()

        if len(rows):
            conn.close()
            return jsonify(code=400,msg='username has exist')
        else:
            try:
                conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                print('register success')
                return jsonify(code=200,msg='success')
            except:
                return jsonify(code=400,msg='error')
            finally:
                conn.close()

if __name__ == '__main__':
    app.debug = True
    app.run()