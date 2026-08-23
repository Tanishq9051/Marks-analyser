from analysis import (
    exam_percentage,
    calculate_subject_averages,
    calculate_statistics,
    find_strongest_weakest_subject,
    calculate_subject_trends,
    classify_performance,
    calculate_student_average
)


def export_student_report(
    student,
    exams,
    filename
):
    if not exams:
        return False

    (
        physics_average,
        chemistry_average,
        biology_average
    ) = calculate_subject_averages(exams)

    overall_average = calculate_student_average(
        exams
    )

    strongest, weakest = (
        find_strongest_weakest_subject(exams)
    )

    statistics = calculate_statistics(
        exams
    )

    trends = calculate_subject_trends(
        exams
    )

    classification = classify_performance(
        overall_average
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "====================================\n"
        )

        file.write(
            "       MARKS ANALYSER REPORT\n"
        )

        file.write(
            "====================================\n\n"
        )

        file.write(
            f"Student: {student[1]}\n"
        )

        file.write(
            f"Student ID: {student[0]}\n\n"
        )

        file.write(
            "===== OVERALL PERFORMANCE =====\n"
        )

        file.write(
            f"Average: "
            f"{overall_average:.2f}%\n"
        )

        file.write(
            f"Classification: "
            f"{classification}\n"
        )

        file.write(
            f"Strongest subject: "
            f"{strongest}\n"
        )

        file.write(
            f"Weakest subject: "
            f"{weakest}\n\n"
        )

        file.write(
            "===== SUBJECT AVERAGES =====\n"
        )

        file.write(
            f"Physics: "
            f"{physics_average:.2f}%\n"
        )

        file.write(
            f"Chemistry: "
            f"{chemistry_average:.2f}%\n"
        )

        file.write(
            f"Biology: "
            f"{biology_average:.2f}%\n\n"
        )

        file.write(
            "===== STATISTICS =====\n"
        )

        file.write(
            f"Median: "
            f"{statistics['median']:.2f}%\n"
        )

        file.write(
            f"Highest: "
            f"{statistics['highest']:.2f}%\n"
        )

        file.write(
            f"Lowest: "
            f"{statistics['lowest']:.2f}%\n"
        )

        file.write(
            f"Range: "
            f"{statistics['range']:.2f}\n"
        )

        file.write(
            f"Standard deviation: "
            f"{statistics['standard_deviation']:.2f}\n\n"
        )

        file.write(
            "===== EXAM HISTORY =====\n"
        )

        for exam in exams:

            file.write(
                f"\nExam: {exam[2]}\n"
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
                f"{exam_percentage(exam):.2f}%\n"
            )

        if trends:

            file.write(
                "\n===== SUBJECT TRENDS =====\n"
            )

            for subject, difference in trends.items():

                if difference > 0:
                    status = "Improving"

                elif difference < 0:
                    status = "Declining"

                else:
                    status = "Stable"

                file.write(
                    f"{subject}: "
                    f"{status} "
                    f"({difference:+.2f} percentage points)\n"
                )

    return True