from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '../static')
)

def get_db():
    conn = sqlite3.connect('feedback.db')
    return conn

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', feedback=data)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, message TEXT)")
    conn.close()
    app.run(host='0.0.0.0', port=5000)