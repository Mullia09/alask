import random
from getpass import getpass

from .db import connect, init_db, DB_PATH


def generate_otp() -> str:
    return f"{random.randint(100000, 999999)}"


def register():
    conn = connect()
    cur = conn.cursor()
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    age = input("Age: ").strip()
    location = input("Location: ").strip()
    community = input("Community: ").strip()

    otp = generate_otp()
    print(f"OTP sent (simulated): {otp}")
    user_input = getpass("Enter OTP: ")
    if user_input != otp:
        print("OTP mismatch. Registration aborted.")
        return

    cur.execute(
        """
        INSERT INTO users (name, email, phone, age, location, community, verified)
        VALUES (?, ?, ?, ?, ?, ?, 1)
        """,
        (name, email, phone, age, location, community),
    )
    conn.commit()
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (cur.lastrowid, "register"),
    )
    conn.commit()
    conn.close()
    print("Registration successful.")


def login(role="participant"):
    conn = connect()
    cur = conn.cursor()
    email = input("Email: ").strip()
    cur.execute("SELECT id FROM users WHERE email=? AND role=?", (email, role))
    row = cur.fetchone()
    if not row:
        print("User not found or role mismatch.")
        return None
    user_id = row[0]
    otp = generate_otp()
    print(f"OTP sent (simulated): {otp}")
    user_input = getpass("Enter OTP: ")
    if user_input != otp:
        print("OTP mismatch.")
        return None
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)", (user_id, "login")
    )
    conn.commit()
    conn.close()
    return user_id


def list_programs():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM programs")
    programs = cur.fetchall()
    conn.close()
    if not programs:
        print("No programs available.")
        return []
    for p in programs:
        print(f"{p[0]}. {p[1]} - {p[2]}")
    return programs


def join_program(user_id: int):
    programs = list_programs()
    if not programs:
        return
    choice = input("Program ID to join: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (user_id, program_id) VALUES (?, ?)", (user_id, choice)
    )
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (user_id, f"join_program:{choice}"),
    )
    conn.commit()
    conn.close()
    print("Attendance recorded.")


def add_reflection(user_id: int):
    programs = list_programs()
    if not programs:
        return
    choice = input("Program ID for reflection: ").strip()
    text = input("Reflection text: ")
    sentiment = "positive" if "good" in text.lower() else "neutral"
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO reflections (user_id, program_id, text, sentiment) VALUES (?, ?, ?, ?)",
        (user_id, choice, text, sentiment),
    )
    cur.execute(
        "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
        (user_id, f"reflect:{choice}"),
    )
    conn.commit()
    conn.close()
    print("Reflection saved.")


def participant_menu(user_id: int):
    while True:
        print("\nParticipant Menu")
        print("1. View programs")
        print("2. Join program")
        print("3. Add reflection")
        print("4. Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            list_programs()
        elif choice == "2":
            join_program(user_id)
        elif choice == "3":
            add_reflection(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


def admin_menu(user_id: int):
    conn = connect()
    cur = conn.cursor()
    while True:
        print("\nAdmin Menu")
        print("1. Add program")
        print("2. List participants")
        print("3. Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Program name: ")
            desc = input("Description: ")
            cur.execute(
                "INSERT INTO programs (name, description) VALUES (?, ?)", (name, desc)
            )
            cur.execute(
                "INSERT INTO audit_trail (user_id, action) VALUES (?, ?)",
                (user_id, f"add_program:{name}"),
            )
            conn.commit()
        elif choice == "2":
            cur.execute("SELECT id, name, email FROM users WHERE role='participant'")
            for row in cur.fetchall():
                print(f"{row[0]} {row[1]} - {row[2]}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
    conn.close()


def main():
    init_db()
    while True:
        print("\nWelcome")
        print("1. Register participant")
        print("2. Participant login")
        print("3. Admin login")
        print("4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user_id = login("participant")
            if user_id:
                participant_menu(user_id)
        elif choice == "3":
            user_id = login("admin")
            if user_id:
                admin_menu(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
