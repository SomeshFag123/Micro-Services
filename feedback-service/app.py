from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# In-memory store for feedback
feedback_list = [
    {"id": 1, "student": "Alex Johnson", "course": "COMP605", "comment": "Great course!", "date": "2025-10-22"}
]

@app.route('/')
def home():
    return jsonify({"message": "Feedback Service is running!"})

@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_list)

@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    if not data or "student" not in data or "course" not in data or "comment" not in data:
        return jsonify({"error": "Missing feedback data"}), 400

    new_feedback = {
        "id": len(feedback_list) + 1,
        "student": data["student"],
        "course": data["course"],
        "comment": data["comment"],
        "date": datetime.datetime.now().strftime("%Y-%m-%d")
    }

    feedback_list.append(new_feedback)

    # Simulate notification (print to console log)
    print(f"Notification sent to admin: New feedback from {data['student']} on {data['course']}")

    return jsonify(new_feedback), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
