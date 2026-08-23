# ---------- BASIC VALIDATION ----------

def validate_name(name):
    if not isinstance(name, str):
        return False

    name = name.strip()

    if not name:
        return False

    if len(name) > 100:
        return False

    return True


def validate_exam_name(name):
    if not isinstance(name, str):
        return False

    name = name.strip()

    if not name:
        return False

    if len(name) > 100:
        return False

    return True


# ---------- MARKS VALIDATION ----------

def validate_max_marks(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return False

    return value > 0


def validate_marks(obtained, maximum):
    try:
        obtained = float(obtained)
        maximum = float(maximum)
    except (ValueError, TypeError):
        return False

    return 0 <= obtained <= maximum


# ---------- ID VALIDATION ----------

def validate_id(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return False

    return value > 0