import matplotlib.pyplot as plt

from analysis import (
    subject_percentages,
    exam_percentage
)


def show_subject_averages(exams):
    if not exams:
        return

    subjects = ["Physics", "Chemistry", "Biology"]
    values = [[], [], []]

    for exam in exams:
        percentages = subject_percentages(exam)

        for i in range(3):
            values[i].append(percentages[i])

    averages = [
        sum(subject) / len(subject)
        for subject in values
    ]

    plt.figure(figsize=(7, 5))
    plt.bar(subjects, averages)

    plt.title("Subject Performance")
    plt.ylabel("Average Percentage")
    plt.ylim(0, 100)

    for i, value in enumerate(averages):
        plt.text(i, value + 2, f"{value:.1f}%", ha="center")

    plt.tight_layout()
    plt.show()


def show_exam_progress(exams):
    if not exams:
        return

    names = [exam[2] for exam in exams]
    percentages = [
        exam_percentage(exam)
        for exam in exams
    ]

    plt.figure(figsize=(8, 5))
    plt.plot(
        names,
        percentages,
        marker="o"
    )

    plt.title("Exam Performance Progress")
    plt.xlabel("Exam")
    plt.ylabel("Percentage")
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)

    for i, value in enumerate(percentages):
        plt.text(
            i,
            value + 2,
            f"{value:.1f}%",
            ha="center"
        )

    plt.tight_layout()
    plt.show()


def show_exam_comparison(first_exam, second_exam):
    if not first_exam or not second_exam:
        return

    subjects = ["Physics", "Chemistry", "Biology"]

    first = subject_percentages(first_exam)
    second = subject_percentages(second_exam)

    x = range(len(subjects))
    width = 0.35

    plt.figure(figsize=(8, 5))

    first_positions = [
        value - width / 2
        for value in x
    ]

    second_positions = [
        value + width / 2
        for value in x
    ]

    plt.bar(
        first_positions,
        first,
        width,
        label=first_exam[2]
    )

    plt.bar(
        second_positions,
        second,
        width,
        label=second_exam[2]
    )

    plt.xticks(x, subjects)
    plt.ylabel("Percentage")
    plt.title("Exam Comparison")
    plt.ylim(0, 100)
    plt.legend()

    plt.tight_layout()
    plt.show()