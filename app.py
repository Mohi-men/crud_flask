from flask import Flask, render_template, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from model.Task import db, add_task, get_tasks, delete_task, edit_task, get_task

app = Flask(__name__)
Scss(app)

app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            add_task(task_content)
            redirect('/')
        except Exception as e:
            print(f'ERROR: {e}')
            return f'ERROR: {e}'
    
    tasks = get_tasks()
    
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id:int):
    try:
        delete_task(id)
        return redirect('/')
    except Exception as e:
        print(f'ERROR: {e}')
        return f'ERROR: {e}'
    
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id:int):
    if request.method == 'POST':
        new_content = request.form['content']
        try:
            edit_task(id, new_content)
            return redirect('/')
        except Exception as e:
            print(f'ERROR: {e}')
            return f'ERROR: {e}'
        
    
    task = get_task(id)
    return render_template('edit.html', task=task)