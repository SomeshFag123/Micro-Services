from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alex Johnson", "email": "alex.j@autuni.ac.nz", "programme": "BCompSci"}
]

@app.route('/')
def home():
    return jsonify({"message": "Student Profile Service is running!"})

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing student data"}), 400
    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "email": data.get("email", ""),
        "programme": data.get("programme", "")
    }
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
