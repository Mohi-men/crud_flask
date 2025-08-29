from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    completed=db.Column(db.Integer, default=0)
    date_created=db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f'Task {self.id}'


def add_task(content):
    new_task = Task(content=content)
    db.session.add(new_task)
    db.session.commit()

def get_tasks():
    return Task.query.order_by(Task.date_created).all()

def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()

def edit_task(task_id, new_content):
    task_to_update = Task.query.get_or_404(task_id)
    task_to_update.content = new_content
    db.session.commit() 

def get_task(task_id):
    return Task.query.get_or_404(task_id)