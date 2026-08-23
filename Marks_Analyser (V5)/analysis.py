from statistics import mean


# -------------------------------
# BASIC CALCULATIONS
# -------------------------------

def subject_percentages(exam):
    return (
        (exam[6] / exam[3]) * 100,
        (exam[7] / exam[4]) * 100,
        (exam[8] / exam[5]) * 100
    )


def exam_percentage(exam):
    obtained = exam[6] + exam[7] + exam[8]
    maximum = exam[3] + exam[4] + exam[5]
    return (obtained / maximum) * 100


# -------------------------------
# STUDENT ANALYSIS
# -------------------------------

def calculate_subject_averages(exams):
    if not exams:
        return 0, 0, 0

    physics = []
    chemistry = []
    biology = []

    for exam in exams:
        p, c, b = subject_percentages(exam)
        physics.append(p)
        chemistry.append(c)
        biology.append(b)

    return (
        mean(physics),
        mean(chemistry),
        mean(biology)
    )


def calculate_overall_average(exams):
    if not exams:
        return 0

    return mean([exam_percentage(exam) for exam in exams])


def calculate_student_average(exams):
    return calculate_overall_average(exams)


def find_strongest_weakest_subject(exams):
    physics, chemistry, biology = calculate_subject_averages(exams)

    subjects = {
        "Physics": physics,
        "Chemistry": chemistry,
        "Biology": biology
    }

    strongest = max(subjects, key=subjects.get)
    weakest = min(subjects, key=subjects.get)

    return strongest, weakest


# -------------------------------
# EXAM COMPARISON
# -------------------------------

def compare_exams(first_exam, second_exam):
    first = exam_percentage(first_exam)
    second = exam_percentage(second_exam)

    return first, second, second - first


# -------------------------------
# PERFORMANCE LEVEL
# -------------------------------

def classify_performance(percentage):
    if percentage >= 90:
        return "Excellent"

    if percentage >= 75:
        return "Good"

    if percentage >= 60:
        return "Average"

    return "Needs Improvement"


# -------------------------------
# RANKINGS
# -------------------------------

def calculate_student_rankings(students_with_exams):
    rankings = []

    for student, exams in students_with_exams:

        if not exams:
            continue

        average = calculate_student_average(exams)

        rankings.append({
            "id": student[0],
            "name": student[1],
            "average": average,
            "classification": classify_performance(average)
        })

    rankings.sort(
        key=lambda x: x["average"],
        reverse=True
    )

    for rank, student in enumerate(rankings, start=1):
        student["rank"] = rank

    return rankings


def calculate_class_statistics(rankings):
    if not rankings:
        return {}

    averages = [student["average"] for student in rankings]

    return {
        "students": len(rankings),
        "class_average": mean(averages),
        "highest": max(averages),
        "lowest": min(averages)
    }