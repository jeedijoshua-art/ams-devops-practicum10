
"""
AMS - Attendance Management System
Attendance Status Validation Module
"""

VALID_STATUSES = {
    "present": "Present",
    "absent": "Absent",
    "late": "Late",
    "excused": "Excused",
}


def attendance_status(raw_status):
    """
    Validate and normalize student attendance status.

    Accepted statuses:
    present, absent, late, excused
    """

    if not isinstance(raw_status, str):
        raise TypeError("Attendance status must be a string.")

    normalized = raw_status.strip().lower()

    if not normalized:
        raise ValueError("Attendance status cannot be empty.")

    if normalized not in VALID_STATUSES:
        raise ValueError("Unsupported attendance status.")

    return VALID_STATUSES[normalized]
