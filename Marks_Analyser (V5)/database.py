import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("school.db")


def connect():
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ---------- DATABASE ----------

def create_database():
    with connect() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS marks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                exam_name TEXT NOT NULL,
                physics_max REAL NOT NULL,
                chemistry_max REAL NOT NULL,
                biology_max REAL NOT NULL,
                physics REAL NOT NULL,
                chemistry REAL NOT NULL,
                biology REAL NOT NULL,
                FOREIGN KEY(student_id)
                REFERENCES students(id)
                ON DELETE CASCADE
            )
        """)


# ---------- STUDENTS ----------

def add_student(name):
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students(name) VALUES(?)",
            (name,)
        )
        return cur.lastrowid


def get_all_students():
    with connect() as conn:
        return conn.execute(
            "SELECT id, name FROM students ORDER BY id"
        ).fetchall()


def get_student(student_id):
    with connect() as conn:
        return conn.execute(
            "SELECT id, name FROM students WHERE id=?",
            (student_id,)
        ).fetchone()


def search_students(text):
    with connect() as conn:
        return conn.execute(
            """
            SELECT id, name
            FROM students
            WHERE name LIKE ?
            ORDER BY name
            """,
            (f"%{text}%",)
        ).fetchall()


def delete_student(student_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )


# ---------- EXAMS ----------

def add_marks(
    student_id,
    exam_name,
    physics_max,
    chemistry_max,
    biology_max,
    physics,
    chemistry,
    biology
):
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO marks(
                student_id,
                exam_name,
                physics_max,
                chemistry_max,
                biology_max,
                physics,
                chemistry,
                biology
            )
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                student_id,
                exam_name,
                physics_max,
                chemistry_max,
                biology_max,
                physics,
                chemistry,
                biology
            )
        )


def get_student_exams(student_id):
    with connect() as conn:
        return conn.execute(
            """
            SELECT *
            FROM marks
            WHERE student_id=?
            ORDER BY id
            """,
            (student_id,)
        ).fetchall()


def get_exam(exam_id):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM marks WHERE id=?",
            (exam_id,)
        ).fetchone()


def update_exam(
    exam_id,
    exam_name,
    physics_max,
    chemistry_max,
    biology_max,
    physics,
    chemistry,
    biology
):
    with connect() as conn:
        conn.execute(
            """
            UPDATE marks
            SET exam_name=?,
                physics_max=?,
                chemistry_max=?,
                biology_max=?,
                physics=?,
                chemistry=?,
                biology=?
            WHERE id=?
            """,
            (
                exam_name,
                physics_max,
                chemistry_max,
                biology_max,
                physics,
                chemistry,
                biology,
                exam_id
            )
        )


def delete_exam(exam_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM marks WHERE id=?",
            (exam_id,)
        )