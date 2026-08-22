import matplotlib.pyplot as plt

from analysis import (
    exam_percentage,
    calculate_subject_averages
)


def show_student_performance_graph(
    student_name,
    exams
):
    if not exams:
        print("No exam data available.")
        return

    exam_names = [
        exam[2]
        for exam in exams
    ]

    percentages = [
        exam_percentage(exam)
        for exam in exams
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(
        exam_names,
        percentages,
        marker="o"
    )

    plt.title(
        f"Performance Trend - {student_name}"
    )

    plt.xlabel("Exam")
    plt.ylabel("Percentage")

    plt.ylim(0, 100)

    plt.grid(True)

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


def show_subject_comparison(
    student_name,
    exams
):
    if not exams:
        print("No exam data available.")
        return

    averages = calculate_subject_averages(
        exams
    )

    subjects = [
        "Physics",
        "Chemistry",
        "Biology"
    ]

    plt.figure(figsize=(8, 6))

    plt.bar(
        subjects,
        averages
    )

    plt.title(
        f"Subject Performance - {student_name}"
    )

    plt.xlabel("Subject")
    plt.ylabel("Average Percentage")

    plt.ylim(0, 100)

    plt.grid(
        axis="y"
    )

    plt.tight_layout()

    plt.show()


def show_ranking_graph(rankings):
    if not rankings:
        print("No ranking data available.")
        return

    names = [
        student["name"]
        for student in rankings
    ]

    averages = [
        student["average"]
        for student in rankings
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(
        names,
        averages
    )

    plt.title(
        "Student Rankings"
    )

    plt.xlabel("Student")
    plt.ylabel("Average Percentage")

    plt.ylim(0, 100)

    plt.xticks(rotation=30)

    plt.grid(
        axis="y"
    )

    plt.tight_layout()

    plt.show()


def show_subject_trends(
    student_name,
    exams
):
    if len(exams) < 2:
        print(
            "At least two exams are "
            "required for a trend graph."
        )
        return

    exam_names = [
        exam[2]
        for exam in exams
    ]

    physics = []
    chemistry = []
    biology = []

    for exam in exams:
        percentages = []

        physics_max = exam[3]
        chemistry_max = exam[4]
        biology_max = exam[5]

        physics.append(
            (exam[6] / physics_max) * 100
        )

        chemistry.append(
            (exam[7] / chemistry_max) * 100
        )

        biology.append(
            (exam[8] / biology_max) * 100
        )

    plt.figure(figsize=(10, 6))

    plt.plot(
        exam_names,
        physics,
        marker="o",
        label="Physics"
    )

    plt.plot(
        exam_names,
        chemistry,
        marker="o",
        label="Chemistry"
    )

    plt.plot(
        exam_names,
        biology,
        marker="o",
        label="Biology"
    )

    plt.title(
        f"Subject Trends - {student_name}"
    )

    plt.xlabel("Exam")
    plt.ylabel("Percentage")

    plt.ylim(0, 100)

    plt.legend()

    plt.grid(True)

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()