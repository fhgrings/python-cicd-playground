import pytest
from app.app import add, divide

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -4) == -66

def test_divide_normal_case():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "Cannot divide by zero" in str(exc_info.value)
