import pytest
from rocket_model.utils.vaild_input import validate_positive_number

def test_validate_positive_number():
    assert validate_positive_number(0.5)
    assert validate_positive_number(100)

    with pytest.raises(TypeError,match = "Input must be an integer or float"):
        validate_positive_number("hello")
    with pytest.raises(ValueError):
       validate_positive_number(-1)


