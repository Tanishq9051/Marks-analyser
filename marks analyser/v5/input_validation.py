def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_valid_maximum(subject):
    while True:
        try:
            maximum = float(
                input(f"Enter {subject} maximum marks: ")
            )

            if maximum > 0:
                return maximum

            print("Maximum marks must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_marks(subject, maximum):
    while True:
        try:
            marks = float(
                input(f"Enter {subject} marks: ")
            )

            if 0 <= marks <= maximum:
                return marks

            print(
                f"Marks must be between 0 and {maximum}."
            )

        except ValueError:
            print("Please enter a valid number.")


def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Please enter a whole number.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "no"):
            return answer

        print("Please enter yes or no.")