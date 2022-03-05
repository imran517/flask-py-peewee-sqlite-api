
from api import api
from service import Service
from flask import jsonify
from flask import request


@api.route('/gettasks', methods=['GET'])
def get_tasks():
    svc = Service()
    return jsonify(svc.getTasks())

@api.route('/gettask/<id>', methods=['GET'])
def get_task(id):
    svc = Service()
    return jsonify(svc.getTask(id))

@api.route('/addtask', methods=['POST'])
def add_task():
    svc = Service()
    return jsonify(svc.addTask(request.get_json()))

@api.route('/updatetask', methods=['POST'])
def update_task():
    svc = Service()
    return jsonify(svc.updateTask(request.get_json()))

@api.route('/deletetask', methods=['POST'])
def delete_task():
    svc = Service()
    return jsonify(svc.deleteTask(request.get_json()))
