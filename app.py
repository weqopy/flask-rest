from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [{
    'id': 1,
    'title': 'Buy groceries',
    'description': 'Milk, Cheese, Pizza',
    'done': False
}, {
    'id': 2,
    'title': 'Learn Python',
    'description': 'Need to find a good Python tutorial on the web',
    'done': False
}]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})


if __name__ == '__main__':
    app.run(debug=True)
