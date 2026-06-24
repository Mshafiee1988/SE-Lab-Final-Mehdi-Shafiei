students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

def get_student_by_id(student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None


# ---------------- TEST 1 ----------------
def test_get_student_success():
    result = get_student_by_id(1)
    assert result["name"] == "Ali"


# ---------------- TEST 2 ----------------
def test_get_student_not_found():
    result = get_student_by_id(999)
    assert result is None


# ---------------- TEST 3 ----------------
def test_student_id_match():
    result = get_student_by_id(2)
    assert result["id"] == 2
