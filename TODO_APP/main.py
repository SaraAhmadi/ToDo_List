from flask import request, jsonify
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from api import app, db
from api import models
from api.queries import resolve_todos, resolve_todo
from api.mutations import resolve_create_todo
from api.mutations import resolve_create_todo, resolve_delete_todo, resolve_update_due_date, \
    resolve_mark_done, resolve_mark_progress, resolve_filter_status, resolve_filter_date
from flask import Blueprint, redirect, url_for, request, flash
from flask_login import login_user
from api.models import User
from flask_login import LoginManager 

auth = Blueprint('auth', __name__)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

query = ObjectType("Query")

query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("deleteTodo", resolve_delete_todo)
mutation.set_field("updateDueDate", resolve_update_due_date)
mutation.set_field("markDone", resolve_mark_done)
mutation.set_field("markProgress", resolve_mark_progress)
mutation.set_field("filterStatus", resolve_filter_status)
mutation.set_field("filterDate", resolve_filter_date)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user: 
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) 

    login_user(user, remember=remember)
    return redirect(url_for('graphql_server')) 
