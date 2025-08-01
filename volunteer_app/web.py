from flask import Flask, request, redirect, url_for, session, render_template_string
import random
from .db import init_db, connect

app = Flask(__name__)
app.secret_key = 'change-me'


def generate_otp():
    return f"{random.randint(100000, 999999)}"


@app.before_first_request
def setup_db():
    init_db()


@app.route('/')
def index():
    return render_template_string(
        """
        <h1>Volunteer System</h1>
        <p><a href='{{ url_for('register') }}'>Register</a></p>
        <p><a href='{{ url_for('login') }}'>Login as Participant</a></p>
        <p><a href='{{ url_for('login', role="admin") }}'>Login as Admin</a></p>
        """
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # save data in session until OTP verified
        session['reg'] = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'age': request.form['age'],
            'location': request.form['location'],
            'community': request.form['community'],
        }
        otp = generate_otp()
        session['otp'] = otp
        return render_template_string(
            """
            <p>OTP sent (simulated): {{otp}}</p>
            <form method='post' action='{{ url_for('verify_register') }}'>
              <input type='text' name='otp' placeholder='Enter OTP'/>
              <input type='submit' value='Verify'/>
            </form>
            """,
            otp=otp,
        )
    return render_template_string(
        """
        <h2>Register</h2>
        <form method='post'>
          <input name='name' placeholder='Name'><br>
          <input name='email' placeholder='Email'><br>
          <input name='phone' placeholder='Phone'><br>
          <input name='age' placeholder='Age'><br>
          <input name='location' placeholder='Location'><br>
          <input name='community' placeholder='Community'><br>
          <input type='submit' value='Submit'>
        </form>
        """
    )


@app.route('/verify_register', methods=['POST'])
def verify_register():
    if request.form['otp'] != session.get('otp'):
        return 'OTP mismatch', 400
    data = session.pop('reg', None)
    session.pop('otp', None)
    if not data:
        return redirect(url_for('register'))
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO users (name, email, phone, age, location, community, verified)
        VALUES (?, ?, ?, ?, ?, ?, 1)
        """,
        (
            data['name'],
            data['email'],
            data['phone'],
            data['age'],
            data['location'],
            data['community'],
        ),
    )
    user_id = cur.lastrowid
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (user_id, 'register'),
    )
    conn.commit()
    conn.close()
    return 'Registration successful. <a href="/">Home</a>'


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<role>', methods=['GET', 'POST'])
def login(role='participant'):
    if request.method == 'POST':
        email = request.form['email']
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE email=? AND role=?", (email, role))
        row = cur.fetchone()
        if not row:
            conn.close()
            return 'User not found or role mismatch', 404
        user_id = row[0]
        otp = generate_otp()
        session['login_user'] = user_id
        session['otp'] = otp
        conn.close()
        return render_template_string(
            """
            <p>OTP sent (simulated): {{otp}}</p>
            <form method='post' action='{{ url_for('verify_login', role=role) }}'>
              <input type='text' name='otp' placeholder='Enter OTP'/>
              <input type='submit' value='Verify'/>
            </form>
            """,
            otp=otp,
            role=role,
        )
    return render_template_string(
        """
        <h2>Login as {{ role }}</h2>
        <form method='post'>
          <input name='email' placeholder='Email'><br>
          <input type='submit' value='Send OTP'>
        </form>
        """,
        role=role,
    )


@app.route('/verify_login/<role>', methods=['POST'])
def verify_login(role):
    if request.form['otp'] != session.get('otp'):
        return 'OTP mismatch', 400
    user_id = session.pop('login_user', None)
    session.pop('otp', None)
    if not user_id:
        return redirect(url_for('login', role=role))
    session['user_id'] = user_id
    session['role'] = role
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (user_id, 'login'),
    )
    conn.commit()
    conn.close()
    if role == 'admin':
        return redirect(url_for('admin_home'))
    return redirect(url_for('participant_home'))


@app.route('/participant')
def participant_home():
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'participant':
        return redirect(url_for('login'))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM programs")
    programs = cur.fetchall()
    conn.close()
    prog_list = ''.join(
        f"<li>{p[1]} - {p[2]} <a href='/join/{p[0]}'>Join</a></li>" for p in programs
    )
    return render_template_string(
        """
        <h2>Participant Dashboard</h2>
        <ul>{{prog_list|safe}}</ul>
        <p><a href='/reflect'>Add Reflection</a></p>
        <p><a href='/logout'>Logout</a></p>
        """,
        prog_list=prog_list,
    )


@app.route('/join/<int:pid>')
def join_program(pid):
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'participant':
        return redirect(url_for('login'))
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (user_id, program_id) VALUES (?, ?)",
        (user_id, pid),
    )
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (user_id, f'join_program:{pid}'),
    )
    conn.commit()
    conn.close()
    return redirect(url_for('participant_home'))


@app.route('/reflect', methods=['GET', 'POST'])
def reflect():
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'participant':
        return redirect(url_for('login'))
    conn = connect()
    cur = conn.cursor()
    if request.method == 'POST':
        program_id = request.form['program_id']
        text = request.form['text']
        sentiment = 'positive' if 'good' in text.lower() else 'neutral'
        cur.execute(
            "INSERT INTO reflections (user_id, program_id, text, sentiment) VALUES (?, ?, ?, ?)",
            (user_id, program_id, text, sentiment),
        )
        cur.execute(
            "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
            (user_id, f'reflect:{program_id}'),
        )
        conn.commit()
        conn.close()
        return redirect(url_for('participant_home'))
    cur.execute("SELECT id, name FROM programs")
    programs = cur.fetchall()
    conn.close()
    options = ''.join(
        f"<option value='{p[0]}'>{p[1]}</option>" for p in programs
    )
    return render_template_string(
        """
        <h2>Add Reflection</h2>
        <form method='post'>
          <select name='program_id'>{{ options|safe }}</select><br>
          <textarea name='text'></textarea><br>
          <input type='submit' value='Save'>
        </form>
        """,
        options=options,
    )


@app.route('/admin')
def admin_home():
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'admin':
        return redirect(url_for('login', role='admin'))
    return render_template_string(
        """
        <h2>Admin Dashboard</h2>
        <p><a href='/add_program'>Add Program</a></p>
        <p><a href='/list_participants'>List Participants</a></p>
        <p><a href='/logout'>Logout</a></p>
        """
    )


@app.route('/add_program', methods=['GET', 'POST'])
def add_program():
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'admin':
        return redirect(url_for('login', role='admin'))
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['description']
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO programs (name, description) VALUES (?, ?)",
            (name, desc),
        )
        cur.execute(
            "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
            (user_id, f'add_program:{name}'),
        )
        conn.commit()
        conn.close()
        return redirect(url_for('admin_home'))
    return render_template_string(
        """
        <h2>Add Program</h2>
        <form method='post'>
          <input name='name' placeholder='Name'><br>
          <input name='description' placeholder='Description'><br>
          <input type='submit' value='Add'>
        </form>
        """
    )


@app.route('/list_participants')
def list_participants():
    user_id = session.get('user_id')
    role = session.get('role')
    if not user_id or role != 'admin':
        return redirect(url_for('login', role='admin'))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name, email FROM users WHERE role='participant'")
    rows = cur.fetchall()
    conn.close()
    items = ''.join(f"<li>{r[0]} - {r[1]}</li>" for r in rows)
    return render_template_string(
        """
        <h2>Participants</h2>
        <ul>{{ items|safe }}</ul>
        <p><a href='/admin'>Back</a></p>
        """,
        items=items,
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
