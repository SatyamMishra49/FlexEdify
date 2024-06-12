from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    c_answer = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
                             
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'Add Question':
            question = request.form['question']
            option1 = request.form['option1']
            option2 = request.form['option2']
            option3 = request.form['option3']
            option4 = request.form['option4']
            c_answer = request.form['c_answer']
            topic = request.form['topic']
            print(c_answer)
            new_task = Todo(
                question = question,
                c_answer = c_answer,
                option1 = option1,
                option2 = option2,
                option3 = option3,
                option4 = option4,
                topic = topic)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return "There was error adding"
        else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return redirect('/display/')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

@app.route('/display/', methods = ['POST', 'GET'])
def display():
    if request.method == 'POST':
        return redirect('/')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('display.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()

        # Retrieve all remaining tasks
        remaining_tasks = Todo.query.order_by(Todo.date_created).all()

        # Renumber the IDs sequentially starting from 1
        for index, task in enumerate(remaining_tasks, start=1):
            task.id = index
        
        # Commit the changes to the database
        db.session.commit()

        return redirect('/')
    except:
        return 'There was a problem deleting the task'


    

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.question = request.form['question']
        task.option1 = request.form['option1']
        task.option2 = request.form['option2']
        task.option3 = request.form['option3']
        task.option4 = request.form['option4']
        task.c_answer = request.form['c_answer']
        task.topic = request.form['topic']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Found some error in updating'
    else:
        return render_template('update.html', n = task)


if __name__ == '__main__':
    app.run(debug=True)