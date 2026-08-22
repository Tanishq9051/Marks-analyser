from input_validation import (
    get_non_empty_text,
    get_valid_maximum,
    get_valid_marks
)


def get_student_name():
    return get_non_empty_text(
        "Enter student name: "
    )


def get_exam_name():
    return get_non_empty_text(
        "Enter exam name: "
    )


def get_maximum_marks():
    physics_max = get_valid_maximum("Physics")
    chemistry_max = get_valid_maximum("Chemistry")
    biology_max = get_valid_maximum("Biology")

    return (
        physics_max,
        chemistry_max,
        biology_max
    )


def get_marks(
    physics_max,
    chemistry_max,
    biology_max
):
    physics = get_valid_marks(
        "Physics",
        physics_max
    )

    chemistry = get_valid_marks(
        "Chemistry",
        chemistry_max
    )

    biology = get_valid_marks(
        "Biology",
        biology_max
    )

    return (
        physics,
        chemistry,
        biology
    )