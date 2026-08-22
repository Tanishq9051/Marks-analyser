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


def generate_performance_summary(exams):
    if not exams:
        return "No exam data available."

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

    print("\n===== PERFORMANCE ANALYSIS =====")

    print(
        f"Overall average: "
        f"{overall_average:.2f}%"
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

    if len(exams) >= 2:

        first_percentage = exam_percentage(
            exams[0]
        )

        last_percentage = exam_percentage(
            exams[-1]
        )

        difference = (
            last_percentage -
            first_percentage
        )

        print(
            "\nOverall change from first "
            "exam to latest exam: "
            f"{difference:+.2f} percentage points"
        )