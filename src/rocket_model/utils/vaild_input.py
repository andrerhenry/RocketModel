
def validate_positive_number(input: int | float):
    try:
        if not isinstance(input, (int, float)):
            raise TypeError("Input must be an integer or float")
        if input <= 0:
            raise ValueError("Input must be a positive number")
        return input
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return e

if __name__ == "__main__":
    validate_positive_number(-1)