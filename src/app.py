from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

# ---------------- GET ALL STUDENTS ----------------
@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Get all students
    ---
    tags:
      - Students
    operationId: getStudents
    responses:
      200:
        description: List of all students
    """
    return jsonify(students)


# ---------------- GET STUDENT BY ID ----------------
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Get student by ID
    ---
    tags:
      - Students
    operationId: getStudentById
    parameters:
      - name: student_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Student found
      404:
        description: Student not found
    """
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


# ---------------- ADD STUDENT ----------------
@app.route('/api/students', methods=['POST'])
def add_student():
    """
    Add new student
    ---
    tags:
      - Students
    operationId: addStudent
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: Student created
    """
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


if __name__ == '__main__':
    app.run(debug=True)
