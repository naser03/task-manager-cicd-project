from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "title": "Learn Git", "completed": False},
    {"id": 2, "title": "Build Docker image", "completed": False},
]


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "backend"})


@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks)


@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    next_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": next_id,
        "title": title,
        "completed": False,
    }

    tasks.append(task)
    return jsonify(task), 201


@app.patch("/api/tasks/<int:task_id>")
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return jsonify({"message": "Task deleted"})

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
