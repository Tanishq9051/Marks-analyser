import sqlite3
import os


DATABASE_NAME = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "school.db"
)


def connect_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_key = ON")
    return connection


def create_database():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            exam_name TEXT NOT NULL,

            physics_max REAL NOT NULL,
            chemistry_max REAL NOT NULL,
            biology_max REAL NOT NULL,

            physics REAL NOT NULL,
            chemistry REAL NOT NULL,
            biology REAL NOT NULL,

            FOREIGN KEY (student_id)
            REFERENCES students(id)
            ON DELETE CASCADE
        )
    """)

    connection.commit()
    connection.close()


def add_student(name):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name)
        VALUES (?)
        """,
        (name,)
    )

    student_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return student_id


def get_all_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name
        FROM students
        ORDER BY id
        """
    )

    students = cursor.fetchall()

    connection.close()

    return students


def get_student(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    return student


def search_students(search_term):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name
        FROM students
        WHERE name LIKE ?
        ORDER BY name
        """,
        (f"%{search_term}%",)
    )

    students = cursor.fetchall()

    connection.close()

    return students


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
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO marks (
            student_id,
            exam_name,
            physics_max,
            chemistry_max,
            biology_max,
            physics,
            chemistry,
            biology
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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

    connection.commit()
    connection.close()


def get_student_exams(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            student_id,
            exam_name,
            physics_max,
            chemistry_max,
            biology_max,
            physics,
            chemistry,
            biology
        FROM marks
        WHERE student_id = ?
        ORDER BY id
        """,
        (student_id,)
    )

    exams = cursor.fetchall()

    connection.close()

    return exams


def get_exam(exam_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            student_id,
            exam_name,
            physics_max,
            chemistry_max,
            biology_max,
            physics,
            chemistry,
            biology
        FROM marks
        WHERE id = ?
        """,
        (exam_id,)
    )

    exam = cursor.fetchone()

    connection.close()

    return exam


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
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE marks
        SET
            exam_name = ?,
            physics_max = ?,
            chemistry_max = ?,
            biology_max = ?,
            physics = ?,
            chemistry = ?,
            biology = ?
        WHERE id = ?
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

    connection.commit()
    connection.close()


def delete_exam(exam_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM marks
        WHERE id = ?
        """,
        (exam_id,)
    )

    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM marks
        WHERE student_id = ?
        """,
        (student_id,)
    )

    cursor.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    connection.commit()
    connection.close()