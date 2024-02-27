from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class ToDoSimple(Resource):
    def get(self, todo_id):
        if todo_id not in todos:
            return {'error': 'Not Found'}, 404
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        if todo_id in todos:
            del todos[todo_id]
            return {'message': 'Deleted successfully'}
        return {'error': 'Not Found'}, 404


api.add_resource(ToDoSimple, "/<string:todo_id>")

if __name__ == '__main__':
    app.run(debug=True)
