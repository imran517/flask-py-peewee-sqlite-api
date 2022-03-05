from dbContext import db
from helpers import *
from model import *
from peewee import *
from playhouse.shortcuts import model_to_dict

import logging
logger = logging.getLogger(__name__)

class Service :
    def __init__(self):
        self.service = "Service"

    def getTasks(self) :            
        try:             
            result = []
            for task in Task.select().dicts():
                result.append(task)

            serviceResult = { "status":"success", "message": "Tasks retrieved.","service": self.service, "method": "getTasks", "data": result }
            return serviceResult    
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "getTasks", "data": []}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult 

    def getTask(self, id) :
        try:
            task = Task.select().where(Task.id == 8).get()
            serviceResult = { "status":"success", "message": "Task retrieved.","service": self.service, "method": "getTask", "data": model_to_dict(task) }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "getTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def addTask(self, task):
        try:
            model = Task()
            model.name = task['name']
            model.description = task['description']
            model.priority= task['priority']
            model.status=task['status']
            model.save();

            serviceResult = { "status":"success", "message": "Task added.","service": self.service, "method": "addTask", "data": {} }            
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "addTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def updateTask(self, task):
        try:
            model = Task()
            model.id = task['id']
            model.name = task['name']
            model.description = task['description']
            model.priority= task['priority']
            model.status=task['status']
            model.save();

            serviceResult = { "status":"success", "message": "Task updated.","service": self.service, "method": "updateTask", "data": {} }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "updateTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def deleteTask(self, task):
        try:
            model = Task()
            model.id = task['id']
            model.delete_instance()

            serviceResult = { "status":"success", "message": "Task deleted.","service": self.service, "method": "deleteTask", "data": {} }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "deleteTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult
