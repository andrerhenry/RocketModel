
def validate_positive_number(input: int | float):
    if not isinstance(input, (int, float)):
        raise TypeError("Input must be an integer or float")
    if input <= 0:
        raise ValueError("Input must be a positive number")
    return input


def check_positive_number(input: int | float):
    try:
        validate_positive_number(input)
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
