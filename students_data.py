from database import (
    add_student,
    get_all_students,
    get_student,
    search_students,
    delete_student,
    add_marks,
    get_student_exams,
    get_exam,
    update_exam,
    delete_exam
)


# ---------- STUDENT OPERATIONS ----------

def create_student(name):
    return add_student(name.strip())


def list_students():
    return get_all_students()


def find_student(student_id):
    return get_student(student_id)


def find_students(name):
    return search_students(name.strip())


def remove_student(student_id):
    delete_student(student_id)


# ---------- EXAM OPERATIONS ----------

def create_exam(
    student_id,
    exam_name,
    physics_max,
    chemistry_max,
    biology_max,
    physics,
    chemistry,
    biology
):
    add_marks(
        student_id,
        exam_name.strip(),
        physics_max,
        chemistry_max,
        biology_max,
        physics,
        chemistry,
        biology
    )


def list_exams(student_id):
    return get_student_exams(student_id)


def find_exam(exam_id):
    return get_exam(exam_id)


def edit_exam(
    exam_id,
    exam_name,
    physics_max,
    chemistry_max,
    biology_max,
    physics,
    chemistry,
    biology
):
    update_exam(
        exam_id,
        exam_name.strip(),
        physics_max,
        chemistry_max,
        biology_max,
        physics,
        chemistry,
        biology
    )


def remove_exam(exam_id):
    delete_exam(exam_id)