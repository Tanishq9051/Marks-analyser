from statistics import median, mean, stdev


def subject_percentages(exam):
    physics_max = exam[3]
    chemistry_max = exam[4]
    biology_max = exam[5]

    physics = exam[6]
    chemistry = exam[7]
    biology = exam[8]

    physics_percentage = (
        physics / physics_max
    ) * 100

    chemistry_percentage = (
        chemistry / chemistry_max
    ) * 100

    biology_percentage = (
        biology / biology_max
    ) * 100

    return (
        physics_percentage,
        chemistry_percentage,
        biology_percentage
    )


def exam_percentage(exam):
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

    return (
        total_marks /
        total_maximum
    ) * 100


def calculate_subject_averages(exams):
    if not exams:
        return 0, 0, 0

    physics = []
    chemistry = []
    biology = []

    for exam in exams:
        percentages = subject_percentages(exam)

        physics.append(percentages[0])
        chemistry.append(percentages[1])
        biology.append(percentages[2])

    return (
        sum(physics) / len(physics),
        sum(chemistry) / len(chemistry),
        sum(biology) / len(biology)
    )


def calculate_overall_average(exams):
    if not exams:
        return 0

    percentages = []

    for exam in exams:
        percentages.append(
            exam_percentage(exam)
        )

    return sum(percentages) / len(percentages)


def calculate_student_average(exams):
    return calculate_overall_average(exams)


def find_strongest_weakest_subject(exams):
    averages = calculate_subject_averages(exams)

    subjects = {
        "Physics": averages[0],
        "Chemistry": averages[1],
        "Biology": averages[2]
    }

    strongest = max(
        subjects,
        key=subjects.get
    )

    weakest = min(
        subjects,
        key=subjects.get
    )

    return strongest, weakest


def calculate_subject_high_low(exams):
    if not exams:
        return {}

    physics = []
    chemistry = []
    biology = []

    for exam in exams:
        percentages = subject_percentages(exam)

        physics.append(percentages[0])
        chemistry.append(percentages[1])
        biology.append(percentages[2])

    return {
        "Physics": {
            "highest": max(physics),
            "lowest": min(physics)
        },
        "Chemistry": {
            "highest": max(chemistry),
            "lowest": min(chemistry)
        },
        "Biology": {
            "highest": max(biology),
            "lowest": min(biology)
        }
    }


def calculate_subject_trends(exams):
    if len(exams) < 2:
        return {}

    first = subject_percentages(exams[0])
    last = subject_percentages(exams[-1])

    subjects = [
        "Physics",
        "Chemistry",
        "Biology"
    ]

    trends = {}

    for index, subject in enumerate(subjects):
        difference = (
            last[index] -
            first[index]
        )

        trends[subject] = difference

    return trends


def get_best_exam(exams):
    if not exams:
        return None

    return max(
        exams,
        key=exam_percentage
    )


def get_worst_exam(exams):
    if not exams:
        return None

    return min(
        exams,
        key=exam_percentage
    )


def compare_exams(first_exam, second_exam):
    first_percentage = exam_percentage(
        first_exam
    )

    second_percentage = exam_percentage(
        second_exam
    )

    difference = (
        second_percentage -
        first_percentage
    )

    return (
        first_percentage,
        second_percentage,
        difference
    )


def classify_performance(percentage):
    if percentage >= 90:
        return "Excellent"

    if percentage >= 75:
        return "Good"

    if percentage >= 60:
        return "Average"

    return "Needs Improvement"


def calculate_statistics(exams):
    if not exams:
        return {}

    percentages = [
        exam_percentage(exam)
        for exam in exams
    ]

    statistics = {
        "mean": mean(percentages),
        "median": median(percentages),
        "highest": max(percentages),
        "lowest": min(percentages),
        "range": max(percentages) - min(percentages)
    }

    if len(percentages) >= 2:
        statistics["standard_deviation"] = stdev(
            percentages
        )
    else:
        statistics["standard_deviation"] = 0

    return statistics


def calculate_subject_statistics(exams):
    if not exams:
        return {}

    subjects = {
        "Physics": [],
        "Chemistry": [],
        "Biology": []
    }

    for exam in exams:
        percentages = subject_percentages(exam)

        subjects["Physics"].append(
            percentages[0]
        )

        subjects["Chemistry"].append(
            percentages[1]
        )

        subjects["Biology"].append(
            percentages[2]
        )

    result = {}

    for subject, values in subjects.items():
        result[subject] = {
            "average": mean(values),
            "highest": max(values),
            "lowest": min(values),
            "median": median(values)
        }

    return result


def calculate_overall_change(exams):
    if len(exams) < 2:
        return 0

    first = exam_percentage(exams[0])
    last = exam_percentage(exams[-1])

    return last - first


def generate_performance_summary(exams):
    if not exams:
        print("No exam data available.")
        return

    physics_average, chemistry_average, biology_average = (
        calculate_subject_averages(exams)
    )

    overall_average = calculate_overall_average(
        exams
    )

    strongest, weakest = (
        find_strongest_weakest_subject(exams)
    )

    best_exam = get_best_exam(exams)
    worst_exam = get_worst_exam(exams)

    high_low = calculate_subject_high_low(
        exams
    )

    trends = calculate_subject_trends(
        exams
    )

    statistics = calculate_statistics(
        exams
    )

    classification = classify_performance(
        overall_average
    )

    print("\n===== PERFORMANCE ANALYSIS =====")

    print(
        f"Overall average: "
        f"{overall_average:.2f}%"
    )

    print(
        f"Performance level: "
        f"{classification}"
    )

    print(
        f"Physics average: "
        f"{physics_average:.2f}%"
    )

    print(
        f"Chemistry average: "
        f"{chemistry_average:.2f}%"
    )

    print(
        f"Biology average: "
        f"{biology_average:.2f}%"
    )

    print(
        f"\nStrongest subject: {strongest}"
    )

    print(
        f"Weakest subject: {weakest}"
    )

    print("\n===== STATISTICS =====")

    print(
        f"Median: "
        f"{statistics['median']:.2f}%"
    )

    print(
        f"Highest: "
        f"{statistics['highest']:.2f}%"
    )

    print(
        f"Lowest: "
        f"{statistics['lowest']:.2f}%"
    )

    print(
        f"Range: "
        f"{statistics['range']:.2f}"
    )

    print(
        f"Standard deviation: "
        f"{statistics['standard_deviation']:.2f}"
    )

    print("\n===== HIGH / LOW =====")

    for subject, values in high_low.items():
        print(
            f"{subject}: "
            f"Highest {values['highest']:.2f}% | "
            f"Lowest {values['lowest']:.2f}%"
        )

    print("\n===== BEST / WORST EXAM =====")

    print(
        f"Best exam: {best_exam[2]} "
        f"({exam_percentage(best_exam):.2f}%)"
    )

    print(
        f"Worst exam: {worst_exam[2]} "
        f"({exam_percentage(worst_exam):.2f}%)"
    )

    if trends:
        print("\n===== SUBJECT TRENDS =====")

        for subject, difference in trends.items():

            if difference > 0:
                word = "Improving"

            elif difference < 0:
                word = "Declining"

            else:
                word = "Stable"

            print(
                f"{subject}: "
                f"{word} "
                f"({difference:+.2f} percentage points)"
            )

    overall_change = calculate_overall_change(
        exams
    )

    if len(exams) >= 2:
        print(
            "\nOverall change from first "
            "exam to latest exam: "
            f"{overall_change:+.2f} percentage points"
        )


def calculate_student_rankings(students_with_exams):
    rankings = []

    for student, exams in students_with_exams:

        if not exams:
            continue

        average = calculate_student_average(
            exams
        )

        rankings.append({
            "id": student[0],
            "name": student[1],
            "average": average,
            "classification": classify_performance(
                average
            )
        })

    rankings.sort(
        key=lambda student: student["average"],
        reverse=True
    )

    for rank, student in enumerate(
        rankings,
        start=1
    ):
        student["rank"] = rank

    return rankings


def calculate_class_statistics(rankings):
    if not rankings:
        return {}

    averages = [
        student["average"]
        for student in rankings
    ]

    return {
        "students": len(rankings),
        "class_average": mean(averages),
        "median": median(averages),
        "highest": max(averages),
        "lowest": min(averages),
        "range": max(averages) - min(averages)
    }