# ToDo List
Usage
------------------------

1. Creating a virtual env
```python
python3 -m virtualenv .venv
 ```
 and activate it by:
 ```python
 source .venv/bin/activate # for windows `.venv/Scripts/activate.ps1`
 ```
2- Installing Requirements

```python
 pip install flask ariadne flask-sqlalchemy flask-login
 ```
3- Setting up environment variables
-  in ubutu:
  ```python
  export FLASK_APP=main.py
 ```
-  in windows:

 ```python
  $env:FLASK_APP = "main.py"
  set FLASK_APP=main.py
 ```
4-Runninig the app
 ```python
  flask run
 ```
# App demonstaration
Navigate to / endpoint to login
 ```python
username: admin
password: adminadmin
 ```
-Example commands

- Retrieve all todos
 ```python
    todos {
    success
    errors
    todos {
     title
      description
      author
      status
      dueDate
      id
    }
  }
}
  ```
- Retrieve todo with id 1
 ```python
query fetchTodo {
  todo(todoId: "1") {
    success
    errors
    todo { id author status title description dueDate }
  }
}
  ```
- Create new todo
 ```python
 mutation newTodo {
  createTodo(author:"admin",  title:"new title", description:"meeting at 2", dueDate:"24-10-2021") {
    success
    errors
    todo {
      id
      author
      title
      status
      dueDate
      description
    }
  }
}
  ```
- Delete todo with id 1
 ```python
 mutation {
  deleteTodo(todoId: "1") {
    success
    errors
  }
}
  ```
- Update todo dueDate
 ```python
 mutation updateDueDate {
  updateDueDate(todoId: "1", newDate: "20-11-2021") {
    success
    errors
  }
}

  ```
- Change the status of an item as in-progress
 ```python
 mutation markProgress {
  markProgress(todoId: "1") {
    success
    errors
    todo { id status title description dueDate }
  }
}
  ```
 - Change the status of an item as done
  ```python
 mutation markDone {
  markDone(todoId: "2") {
    success
    errors
    todo { id status title description dueDate }
  }
}
  ```
 - Query todo based on status
  ```python
 mutation filterStatus {
  filterStatus(todoStatus: "in Progress") {
    success
    errors
    todo { id author status title description dueDate }
  }
}
  ```
- Query todo based on due date
```python
 mutation filterDate {
  filterDate(todoDueDate: "25-11-2021") {
    success
    errors
    todo { id author status title description  }
  }
}
  ```
