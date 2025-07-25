from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('ticket_db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_us')
def about():
    return render_template('about_us.html')

@app.route('/history')
def history():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM complaints').fetchall()
    conn.close()
    return render_template('history.html', data=data)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        complaint = request.form['complaint']
        rating = request.form['rating']
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO feedback (complaint, rating) VALUES (?, ?)', (complaint, rating)
        )
        conn.commit()
        conn.close()
        return render_template('feedback.html', submitted=True)
    return render_template('feedback.html', submitted=False)


@app.route('/problems')
def problems():
    return render_template('problems.html')

if __name__ == '__main__':
    app.run(debug=True)
