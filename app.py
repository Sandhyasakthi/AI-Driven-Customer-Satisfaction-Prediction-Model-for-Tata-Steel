from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "tata_secret_key"

DATABASE = "database.db"


# ---------------- DATABASE ---------------- #

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- HOME ---------------- #

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


# ---------------- LOGIN ---------------- #

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['email'] = user['email']
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", error="Invalid Email or Password")

    return render_template("login.html")


# ---------------- SIGNUP ---------------- #

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password)
            )

            conn.commit()
            conn.close()

            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            return render_template("signup.html", error="Email already registered")

    return render_template("signup.html")


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):  # safer than 'user_id' in session
        return redirect(url_for('login'))

    return render_template("dashboard.html", email=session['email'])



# ---------------- ANALYTICS ---------------- #

@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    result = None
    confidence = None

    if request.method == 'POST':
        operational = int(request.form['operational'])
        raw_material = int(request.form['raw_material'])
        customer = int(request.form['customer'])
        sustainability = int(request.form['sustainability'])

        score = (operational + raw_material + customer + sustainability) / 4

        if score >= 7:
            result = "Highly Satisfied"
            confidence = 92
        elif score >= 5:
            result = "Moderate Satisfaction"
            confidence = 80
        else:
            result = "At Risk"
            confidence = 70

    return render_template("analytics.html", result=result, confidence=confidence)


# ---------------- LOGOUT ---------------- #

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
