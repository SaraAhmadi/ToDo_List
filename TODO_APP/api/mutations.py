from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Todo, User

@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, title, description, author, due_date):
    try:
        author = User.query.filter_by(username=author).first()
        due_date = datetime.strptime(due_date, '%d-%m-%Y').date()
        todo = Todo(
            title=title, description=description, author=author, due_date=due_date
        )
        db.session.add(todo)
        db.session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
    try:
        todo = Todo.query.get(todo_id)
        if todo:
            todo.due_date = datetime.strptime(new_date, '%d-%m-%Y').date()
        db.session.add(todo)
        db.session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": ["Incorrect date format provided. Date should be in "
                       "the format dd-mm-yyyy"]
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
    try:
        todo = Todo.query.get(todo_id)
        todo.status = "Done"
        db.session.add(todo)
        db.session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors":  [f"Todo matching id {todo_id} was not found"]
        }

    return payload

@convert_kwargs_to_snake_case
def resolve_mark_progress(obj, info, todo_id):
    try:
        todo = Todo.query.get(todo_id)
        todo.status = "in Progress"
        db.session.add(todo)
        db.session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors":  [f"Todo matching id {todo_id} was not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_filter_status(obj, info, todo_status):

    try:
        todo = Todo.query.filter_by(status=todo_status).first()
        
        print(todo)
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching query {todo_status} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_filter_date(obj, info, todo_due_date):

    try:
        duedate = datetime.strptime(todo_due_date, '%d-%m-%Y').date()
        todo = Todo.query.filter_by(due_date=duedate).first()
     
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching query {duedate} not found"]
        }

    return payload