
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Priya", "score": 92},
    {"name": "Amit", "score": 78},
    {"name": "Sneha", "score": 88},
    {"name": "Arjun", "score": 95}
]


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=False, port=5000)
