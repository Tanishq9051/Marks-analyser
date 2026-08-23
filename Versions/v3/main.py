from database import (
    create_database,
    add_student,
    add_marks,
    get_all_students,
    get_student,
    search_students,
    get_student_exams,
    get_exam,
    update_exam,
    delete_exam,
    delete_student
)

from students_data import (
    get_student_name,
    get_exam_name,
    get_maximum_marks,
    get_marks
)

from input_validation import (
    get_yes_no,
    get_valid_integer
)

from analysis import (
    exam_percentage,
    generate_performance_summary,
    compare_exams
)


def choose_student():
    students = get_all_students()

    if not students:
        print("No students found.")
        return None

    print("\n===== STUDENTS =====")

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]}"
        )

    student_id = get_valid_integer(
        "\nEnter student ID: "
    )

    student = get_student(student_id)

    if student is None:
        print("Student not found.")
        return None

    return student


def add_new_student():
    print("\n===== ADD NEW STUDENT =====")

    name = get_student_name()

    student_id = add_student(name)

    print(
        f"\nStudent added successfully."
    )

    print(
        f"Student ID: {student_id}"
    )

    while True:

        print("\n===== ENTER EXAM DETAILS =====")

        exam_name = get_exam_name()

        (
            physics_max,
            chemistry_max,
            biology_max
        ) = get_maximum_marks()

        (
            physics,
            chemistry,
            biology
        ) = get_marks(
            physics_max,
            chemistry_max,
            biology_max
        )

        add_marks(
            student_id,
            exam_name,
            physics_max,
            chemistry_max,
            biology_max,
            physics,
            chemistry,
            biology
        )

        print(
            "Exam saved successfully."
        )

        another = get_yes_no(
            "Add another exam? (yes/no): "
        )

        if another == "no":
            break


def view_students():
    print("\n===== ALL STUDENTS =====")

    students = get_all_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]}"
        )


def search_student():
    print("\n===== SEARCH STUDENT =====")

    search_term = input(
        "Enter student name: "
    ).strip()

    if not search_term:
        print("Search cannot be empty.")
        return

    students = search_students(
        search_term
    )

    if not students:
        print("No matching students found.")
        return

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]}"
        )


def view_performance():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if not exams:
        print(
            "This student has no exams."
        )
        return

    print(
        f"\n===== PERFORMANCE: "
        f"{student[1]} ====="
    )

    generate_performance_summary(
        exams
    )


def view_exam_history():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if not exams:
        print(
            "This student has no exams."
        )
        return

    print(
        f"\n===== EXAM HISTORY: "
        f"{student[1]} ====="
    )

    for exam in exams:

        print("\n----------------------------")

        print(
            f"Exam ID: {exam[0]}"
        )

        print(
            f"Exam: {exam[2]}"
        )

        print(
            f"Physics: "
            f"{exam[6]}/{exam[3]}"
        )

        print(
            f"Chemistry: "
            f"{exam[7]}/{exam[4]}"
        )

        print(
            f"Biology: "
            f"{exam[8]}/{exam[5]}"
        )

        total_marks = (
            exam[6] +
            exam[7] +
            exam[8]
        )

        total_maximum = (
            exam[3] +
            exam[4] +
            exam[5]
        )

        print(
            f"Total: "
            f"{total_marks}/{total_maximum}"
        )

        print(
            f"Percentage: "
            f"{exam_percentage(exam):.2f}%"
        )


def compare_student_exams():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if len(exams) < 2:
        print(
            "At least two exams are "
            "required."
        )
        return

    print("\n===== EXAMS =====")

    for exam in exams:
        print(
            f"ID: {exam[0]} | "
            f"{exam[2]} | "
            f"{exam_percentage(exam):.2f}%"
        )

    first_id = get_valid_integer(
        "\nEnter first exam ID: "
    )

    second_id = get_valid_integer(
        "Enter second exam ID: "
    )

    first_exam = get_exam(first_id)
    second_exam = get_exam(second_id)

    if first_exam is None:
        print("First exam not found.")
        return

    if second_exam is None:
        print("Second exam not found.")
        return

    if first_exam[1] != student[0]:
        print(
            "First exam does not belong "
            "to this student."
        )
        return

    if second_exam[1] != student[0]:
        print(
            "Second exam does not belong "
            "to this student."
        )
        return

    (
        first_percentage,
        second_percentage,
        difference
    ) = compare_exams(
        first_exam,
        second_exam
    )

    print("\n===== COMPARISON =====")

    print(
        f"{first_exam[2]}: "
        f"{first_percentage:.2f}%"
    )

    print(
        f"{second_exam[2]}: "
        f"{second_percentage:.2f}%"
    )

    if difference > 0:

        print(
            f"Improvement: "
            f"+{difference:.2f} "
            "percentage points"
        )

    elif difference < 0:

        print(
            f"Decline: "
            f"{difference:.2f} "
            "percentage points"
        )

    else:

        print("No change.")


def update_exam_record():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if not exams:
        print("No exams found.")
        return

    print("\n===== EXAMS =====")

    for exam in exams:
        print(
            f"ID: {exam[0]} | "
            f"{exam[2]}"
        )

    exam_id = get_valid_integer(
        "\nEnter exam ID to update: "
    )

    exam = get_exam(exam_id)

    if exam is None:
        print("Exam not found.")
        return

    if exam[1] != student[0]:
        print(
            "That exam does not belong "
            "to this student."
        )
        return

    print("\nEnter new exam information.")

    exam_name = get_exam_name()

    (
        physics_max,
        chemistry_max,
        biology_max
    ) = get_maximum_marks()

    (
        physics,
        chemistry,
        biology
    ) = get_marks(
        physics_max,
        chemistry_max,
        biology_max
    )

    update_exam(
        exam_id,
        exam_name,
        physics_max,
        chemistry_max,
        biology_max,
        physics,
        chemistry,
        biology
    )

    print(
        "Exam updated successfully."
    )


def delete_exam_record():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if not exams:
        print("No exams found.")
        return

    print("\n===== EXAMS =====")

    for exam in exams:
        print(
            f"ID: {exam[0]} | "
            f"{exam[2]}"
        )

    exam_id = get_valid_integer(
        "\nEnter exam ID to delete: "
    )

    exam = get_exam(exam_id)

    if exam is None:
        print("Exam not found.")
        return

    if exam[1] != student[0]:
        print(
            "That exam does not belong "
            "to this student."
        )
        return

    confirmation = get_yes_no(
        "Delete this exam? (yes/no): "
    )

    if confirmation == "yes":

        delete_exam(exam_id)

        print(
            "Exam deleted successfully."
        )

    else:

        print("Deletion cancelled.")


def delete_student_record():
    student = choose_student()

    if student is None:
        return

    confirmation = get_yes_no(
        f"Delete {student[1]} and "
        "all their exams? (yes/no): "
    )

    if confirmation == "yes":

        delete_student(student[0])

        print(
            "Student and exams deleted."
        )

    else:

        print("Deletion cancelled.")


def export_report():
    student = choose_student()

    if student is None:
        return

    exams = get_student_exams(
        student[0]
    )

    if not exams:
        print(
            "This student has no exams."
        )
        return

    filename = (
        f"student_{student[0]}_report.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            f"MARKS ANALYSER REPORT\n"
        )

        file.write(
            f"Student: {student[1]}\n"
        )

        file.write(
            f"Student ID: {student[0]}\n\n"
        )

        for exam in exams:

            file.write(
                f"Exam: {exam[2]}\n"
            )

            file.write(
                f"Physics: "
                f"{exam[6]}/{exam[3]}\n"
            )

            file.write(
                f"Chemistry: "
                f"{exam[7]}/{exam[4]}\n"
            )

            file.write(
                f"Biology: "
                f"{exam[8]}/{exam[5]}\n"
            )

            file.write(
                f"Percentage: "
                f"{exam_percentage(exam):.2f}%\n\n"
            )

    print(
        f"Report saved as {filename}"
    )


def show_menu():
    while True:

        print("\n")
        print("======================================")
        print("           MARKS ANALYSER")
        print("======================================")

        print("1.  Add new student")
        print("2.  View students")
        print("3.  Search students")
        print("4.  View performance analysis")
        print("5.  View exam history")
        print("6.  Compare exams")
        print("7.  Update exam")
        print("8.  Delete exam")
        print("9.  Delete student")
        print("10. Export report")
        print("11. Exit")

        print("======================================")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_new_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            view_performance()

        elif choice == "5":

            view_exam_history()

        elif choice == "6":

            compare_student_exams()

        elif choice == "7":

            update_exam_record()

        elif choice == "8":

            delete_exam_record()

        elif choice == "9":

            delete_student_record()

        elif choice == "10":

            export_report()

        elif choice == "11":

            print("Goodbye!")

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-11."
            )


def main():
    create_database()

    show_menu()


if __name__ == "__main__":
    main()