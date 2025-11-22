from flask import Flask, request
import webbrowser

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return (
        "Flask To-Do List App!<br><br>"
        "Use these endpoints:<br>"
        "/add?task=YourTaskName — to add a task<br>"
        "/list — to view all tasks<br>"
        "/delete?task=YourTaskName — to delete a task"
    )

@app.route('/add')
def add_task():
    task = request.args.get('task')
    if not task:
        return "Please add a task using /add?task=TaskName"
    tasks.append(task)
    return f"Task added: {task}"

@app.route('/list')
def list_tasks():
    if not tasks:
        return "No tasks added yet!"
    output = "<br>".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
    return f"Your Tasks:<br>{output}"

@app.route('/delete')
def delete_task():
    task = request.args.get('task')
    if not task:
        return "Please specify a task using /delete?task=TaskName"
    if task in tasks:
        tasks.remove(task)
        return f"Task deleted: {task}"
    else:
        return "Task not found!"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5002/")
    
if __name__ == '__main__':
    app.run(debug=True, port=5002)