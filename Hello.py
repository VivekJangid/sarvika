from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

# dict1 = {"id": 1, "description": "Desc 1", "done": True}
# dict2 = {"id": 2, "description": "Desc 2", "done": False}
# dict3 = {"id": 3, "description": "Desc 3", "done": False}
# dict4 = {"id": 4, "description": "Desc 4", "done": True}
# dict5 = {"id": 5, "description": "Desc 5", "done": True}
# dict6 = {"id": 6, "description": "Desc 6", "done": False}
# dict7 = {"id": 7, "description": "Desc 7", "done": False}
# dict8 = {"id": 8, "description": "Desc 8", "done": True}
l1 = list()
for i in range(8):
    l1.append({"id": i, "description": f"Desc {i}", "done": i % 2 == 0})


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/gotologin')
def gotologin():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['pwd']
        if password == 'Hello':
            return redirect(url_for('todo'))
        else:
            return redirect(url_for('wrongpsw'))

    else:
        user = request.args.get('uname')
        password = request.args.get('pwd')
        if password == 'Hello':
            return redirect(url_for('todo'))
        else:
            return redirect(url_for('wrongpsw'))


@app.route('/wrongpsw')
def wrongpsw():
    return render_template('login.html')


@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/printdict', methods=['GET', 'POST'])
def printdict():
    choice = request.form['action']
    if choice == 'dict1':
        result = l1[0]
    if choice == 'dict2':
        result = l1[1]
    if choice == 'dict3':
        result = l1[2]
    if choice == 'dict4':
        result = l1[3]
    if choice == 'dict5':
        result = l1[4]
    if choice == 'dict6':
        result = l1[5]
    if choice == 'dict7':
        result = l1[6]
    if choice == 'dict8':
        result = l1[7]

    return render_template("finaloutput.html", result=result)


if __name__ == '__main__':
    app.run(port=5051, debug=True)
