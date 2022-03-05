# flask-py-sqlite-api

A simple api using flask (python) peewee (ORM) and sqlite

## Requirements

* flask ([https://github.com/pallets/flask](https://))
* peewee ([https://github.com/coleifer/peewee](https://))  
* sqlite ([https://sqlite.org/index.html](https://))
* sqlite3 ([https://docs.python.org/3/library/sqlite3.html](https://))
* Postman (optional for testing api)
* SQLiteStudio (optional for managing database) ([https://sqlite.org/index.html](https://))

## Diagram

![Alt text](./diagram.svg)

## Components

* **config (config.json, config.py)**

  - configuration file
* **server (api.py)**

  - creates server and listens on a port 3000
* **controller (controller.py)**

  - defines routing and request handlers
* **service (service.py)**

  - handles business logic
* **model (model.py)**

  - data model using pewee ORM
* **dbContext (dbContext.py)**

  - handles db connection
* **database (sqlite)**

  - sqlite database

## Run

Run the following command from the root directory:

```
python api.py
```

## Tests

Try the following urls in Postman.

* GetTasks (GET)

  * http://127.0.0.1:3000/gettasks
* GetTask (GET)

  * http://127.0.0.1:3000/gettask/1
* AddTask (POST)

  * http://127.0.0.1:3000/addtask
  * body -> raw, json
  * { "id" : "1", "name": "task1", "description": "task1", "priority": "low", "status": "none" }
* UpdateTask (POST)

  * http://127.0.0.1:3000/updatetask
  * body -> raw, json
  * { "id" : "1", "name": "task11", "description": "task11", "priority": "medium", "status": "started" }
* DeleteTask (POST)

  * http://127.0.0.1:3000/deletetask
  * body -> raw, json
  * { "id" : "1" }
