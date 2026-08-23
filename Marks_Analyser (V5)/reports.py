from analysis import (
    exam_percentage,
    calculate_subject_averages,
    calculate_student_average,
    find_strongest_weakest_subject,
    classify_performance
)


def export_student_report(student, exams, filename):
    if not exams:
        return False

    physics, chemistry, biology = calculate_subject_averages(exams)
    average = calculate_student_average(exams)
    strongest, weakest = find_strongest_weakest_subject(exams)
    level = classify_performance(average)

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 40 + "\n")
        file.write("      MARKS ANALYSER REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Student : {student[1]}\n")
        file.write(f"ID      : {student[0]}\n\n")

        file.write("OVERALL PERFORMANCE\n")
        file.write("-" * 25 + "\n")
        file.write(f"Average : {average:.2f}%\n")
        file.write(f"Level   : {level}\n")
        file.write(f"Strongest Subject : {strongest}\n")
        file.write(f"Weakest Subject   : {weakest}\n\n")

        file.write("SUBJECT AVERAGES\n")
        file.write("-" * 25 + "\n")
        file.write(f"Physics   : {physics:.2f}%\n")
        file.write(f"Chemistry : {chemistry:.2f}%\n")
        file.write(f"Biology   : {biology:.2f}%\n\n")

        file.write("EXAM HISTORY\n")
        file.write("-" * 25 + "\n")

        for exam in exams:
            file.write(f"\n{exam[2]}\n")
            file.write(f"Physics   : {exam[6]}/{exam[3]}\n")
            file.write(f"Chemistry : {exam[7]}/{exam[4]}\n")
            file.write(f"Biology   : {exam[8]}/{exam[5]}\n")
            file.write(
                f"Percentage : {exam_percentage(exam):.2f}%\n"
            )

    return True