from flask import Flask, render_template,redirect,request,url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')
@app.route('/tasks')
def hello():
    return render_template('get_tasks.html', tasks = mongo.db.tasks.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)