
"""
AMS - Automated Attendance Testing
19 test cases using pytest.
"""

import pytest

from attendance import attendance_status


# TEST CASES 1-11: Valid attendance statuses

@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("present", "Present"),
        ("absent", "Absent"),
        ("late", "Late"),
        ("excused", "Excused"),
        ("PRESENT", "Present"),
        ("Absent", "Absent"),
        ("LaTe", "Late"),
        (" present ", "Present"),
        ("  absent  ", "Absent"),
        ("late ", "Late"),
        ("excused\n", "Excused"),
    ],
)
def test_valid_statuses(value, expected):
    assert attendance_status(value) == expected


# TEST CASES 12-17: Invalid attendance statuses

@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
        "holiday",
        "unknown",
        "P",
        "presented",
    ],
)
def test_invalid_status_values(value):
    with pytest.raises(ValueError):
        attendance_status(value)


# TEST CASES 18-19: Invalid data types

@pytest.mark.parametrize(
    "value",
    [
        None,
        123,
    ],
)
def test_non_string_status_values(value):
    with pytest.raises(TypeError):
        attendance_status(value)
