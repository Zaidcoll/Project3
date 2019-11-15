from flask import Flask, render_template,redirect,request,url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

@app.route('/test')
def test():
    return render_template('test.html',test=mongo.db.tasks.find())
    
@app.route('/')
def recipes():
    return render_template('home.html', tasks = mongo.db.tasks.find())
    
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe_db = mongo.db.tasks.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe_db)

@app.route('/edit/<recipe_id>')
def edit(recipe_id):
    recipe_db = mongo.db.tasks.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit.html', recipe=recipe_db,categories=all_categories)


@app.route('/recipes')
def home():
    return render_template('recipes.html',recipe = mongo.db.tasks.find())

@app.route('/add')
def add():
    return render_template('add.html',categories = mongo.db.categories.find())
    
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))
    
@app.route('/update_task/<recipe_id>', methods=["POST"])
def update_task(recipe_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'description': request.form.get('description'),
        'ingredients': request.form.get('ingredients'),
        'steps':request.form.get('steps'),
        'url':request.form.get('url')
    })
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
