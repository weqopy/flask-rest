from flask import Flask, url_for, jsonify, abort
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'root':
        return '1230'
    return None


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

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class TaskListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            type=str,
            required=True,
            help='No task title provided',
            location='json')
        self.reqparse.add_argument(
            'description', type=str, default="", location='json')
        super(TaskListAPI, self).__init__()

    def make_public_task(self, task):
        new_task = {}
        for field in task:
            if field == 'id':
                new_task['uri'] = url_for(
                    'tasks', id=task['id'], _external=True)
            else:
                new_task[field] = task[field]
        return new_task

    def get(self):
        # return jsonify({'tasks': list(map(self.make_public_task, tasks))})
        return {'tasks': list(map(self.make_public_task, tasks))}
        # TODO
        # return {'tasks': list(map(marshal, tasks, task_fields))}

    def post(self):
        if not request.json or 'title' not in request.json:
            abort(400)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201


class TaskAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        return jsonify({'tasks': task[0]})

    def put(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v
        # return jsonify({'task': make_public_task(task)})
        # return {'task': make_public_task(task)}, 201
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return jsonify({'result': True})


api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(TaskListAPI, '/todo/api/v2.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v2.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)
