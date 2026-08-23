from database import create_database
from students_data import (
    create_student,
    list_students,
    find_students,
    remove_student,
    create_exam,
    list_exams,
    remove_exam
)
from analysis import (
    exam_percentage,
    calculate_student_average,
    classify_performance,
    find_strongest_weakest_subject
)


def show_students():
    students = list_students()

    if not students:
        print("\nNo students found.")
        return

    print("\nSTUDENTS")
    print("-" * 35)

    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]}")


def add_new_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student_id = create_student(name)

    print(f"Student added successfully. ID: {student_id}")


def search_student():
    name = input("Enter name to search: ").strip()

    results = find_students(name)

    if not results:
        print("No matching students found.")
        return

    print("\nSEARCH RESULTS")
    print("-" * 35)

    for student in results:
        print(f"ID: {student[0]} | Name: {student[1]}")


def add_new_exam():
    try:
        student_id = int(input("Student ID: "))
        exam_name = input("Exam name: ").strip()

        physics_max = float(input("Physics maximum marks: "))
        chemistry_max = float(input("Chemistry maximum marks: "))
        biology_max = float(input("Biology maximum marks: "))

        physics = float(input("Physics marks: "))
        chemistry = float(input("Chemistry marks: "))
        biology = float(input("Biology marks: "))

        if min(
            physics_max,
            chemistry_max,
            biology_max
        ) <= 0:
            print("Maximum marks must be greater than zero.")
            return

        if not (
            0 <= physics <= physics_max
            and 0 <= chemistry <= chemistry_max
            and 0 <= biology <= biology_max
        ):
            print("Obtained marks must be between 0 and maximum marks.")
            return

        create_exam(
            student_id,
            exam_name,
            physics_max,
            chemistry_max,
            biology_max,
            physics,
            chemistry,
            biology
        )

        print("Exam added successfully.")

    except ValueError:
        print("Please enter valid numeric values.")


def show_student_analysis():
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Invalid student ID.")
        return

    exams = list_exams(student_id)

    if not exams:
        print("No exams found for this student.")
        return

    average = calculate_student_average(exams)
    strongest, weakest = find_strongest_weakest_subject(exams)

    print("\nSTUDENT ANALYSIS")
    print("-" * 35)
    print(f"Average   : {average:.2f}%")
    print(f"Level     : {classify_performance(average)}")
    print(f"Strongest : {strongest}")
    print(f"Weakest   : {weakest}")

    print("\nEXAM HISTORY")
    print("-" * 35)

    for exam in exams:
        print(
            f"{exam[2]} : "
            f"{exam_percentage(exam):.2f}%"
        )


def delete_student():
    try:
        student_id = int(input("Student ID to delete: "))
    except ValueError:
        print("Invalid student ID.")
        return

    confirm = input(
        "Delete this student and all their exams? (y/n): "
    ).lower()

    if confirm == "y":
        remove_student(student_id)
        print("Student deleted.")
    else:
        print("Operation cancelled.")


def delete_exam():
    try:
        exam_id = int(input("Exam ID to delete: "))
    except ValueError:
        print("Invalid exam ID.")
        return

    confirm = input("Delete this exam? (y/n): ").lower()

    if confirm == "y":
        remove_exam(exam_id)
        print("Exam deleted.")
    else:
        print("Operation cancelled.")


def menu():
    create_database()

    while True:
        print("\n" + "=" * 40)
        print("          MARKS ANALYSER")
        print("=" * 40)

        print("1. Show students")
        print("2. Add student")
        print("3. Search student")
        print("4. Add exam")
        print("5. Student analysis")
        print("6. Delete student")
        print("7. Delete exam")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            show_students()

        elif choice == "2":
            add_new_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            add_new_exam()

        elif choice == "5":
            show_student_analysis()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            delete_exam()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()