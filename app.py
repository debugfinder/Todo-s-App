from flask import Flask, render_template, request, jsonify, url_for, redirect, flash, session, Response
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.collection import Collection
import pkg_resources



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Set a secret key for session management

client = MongoClient('mongodb+srv://palp18989:6x5jvsOedmulCqqC@cluster0.ikn0c7m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
todos = db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    todo_count = sum(1 for _ in saved_todos)  # Count the number of todos by iterating over the cursor
    saved_todos.rewind()  # Rewind the cursor to its initial state for further use
    has_todos = todo_count > 0  # Check if there are any todo items
    return render_template('index.html', todos=saved_todos, has_todos=has_todos)


# Route handler for the /completed endpoint
@app.route('/completed')
def completed():
    
    # Retrieve completed todos from the database
    completed_todos = todos.find({'complete': True})
    return render_template('completed.html', completed_todos=completed_todos)

# Route handler for the /notcompleted endpoint
@app.route('/notcompleted')
def not_completed():
    
    # Retrieve not completed todos from the database
    not_completed_todos = todos.find({'complete': False})
    return render_template('notcompleted.html', not_completed_todos=not_completed_todos)

# Route handler for the /filter/todo endpoint
@app.route('/filter/todo', methods=['POST', 'GET'])
def filter_todo():
    
    if request.method == 'POST':
        # Retrieve filter options from form submission
        filter_date = request.form.get('filter-date')
        filter_status = request.form.get('filter-status')

        # Retrieve todos based on filter options
        query = {}
        if filter_date:
            query['created_at'] = {'$gte': datetime.strptime(filter_date, '%Y-%m-%d')}
        if filter_status == 'completed':
            query['complete'] = True
        elif filter_status == 'not_completed':
            query['complete'] = False
        elif filter_status == 'completed, not_completed':
            query['complete'] = True, False    


        filtered_todos = todos.find(query)
    else:
        # If no filter options are provided, display all todos
        filtered_todos = todos.find()

    return render_template('filter_todo.html', todos=filtered_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    
    new_todo = request.form.get('new-todo').strip()  # Remove leading/trailing whitespaces
    if new_todo:  # Check if new_todo is not empty
        current_time = datetime.now()
        todos.insert_one({'text': new_todo, 'complete': False, 'created_at': current_time})
    else:
        flash('Please enter a todo.')  # Import flash function from Flask
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    # Toggle the completion status
    new_status = not todo_item['complete']
    todos.update_one({'_id': ObjectId(oid)}, {'$set': {'complete': new_status}})
    return redirect(url_for('index'))

@app.route('/delete/<oid>')
def delete_todo(oid):
    
    todos.delete_one({'_id': ObjectId(oid)})
    return redirect(url_for('index'))



@app.route('/delete_completed')
def delete_completed():
    
    todos.delete_many({'complete' : True})
    return redirect(url_for('index'))


@app.route('/delete_all')
def delete_all():
    
    todos.delete_many({})
    return redirect(url_for('index'))

@app.route('/api/todos')
def get_todos():
    
    todo_list = list(todos.find({}, {'_id': 0}))  # Exclude _id field from the response
    return jsonify(todo_list)

@app.route('/documentation')
def documentation():
    
    return render_template('documentation.html')

@app.route('/appinfo')
def app_info():
     # Retrieve information about all installed packages
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return render_template('appinfo.html', installed_packages=installed_packages)


@app.route('/menu')
def menu():
    
    # All todo-s menu
    return render_template('menu.html')

@app.route('/developer')
def developer():
    
    # Developer profile area
    return render_template('developer.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/download-requirements')
def download_requirements():
    # Generate requirements.txt content
    requirements = "\n".join([f"{package}=={version}" for package, version in pkg_resources.working_set.by_key.items()])
    
    # Send the requirements as a file
    return Response(
        requirements,
        mimetype="text/plain",
        headers={"Content-disposition": "attachment; filename=requirements.txt"}
    )

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)