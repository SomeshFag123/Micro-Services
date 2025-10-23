from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
courses = [
    {"id": 1, "code": "COMP605", "title": "Web Application Development"},
    {"id": 2, "code": "COMP642", "title": "Database Systems"}
]

@app.route('/')
def home():
    return jsonify({"message": "Course Catalogue Service is running!"})

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    if not data or "code" not in data or "title" not in data:
        return jsonify({"error": "Invalid course data"}), 400
    new_course = {
        "id": len(courses) + 1,
        "code": data["code"],
        "title": data["title"]
    }
    courses.append(new_course)
    return jsonify(new_course), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
