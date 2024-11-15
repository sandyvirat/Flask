from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

print("connecting to mongdo")
client = MongoClient("mongodb://localhost:27017/myDatabase?retryWrites=true&w=majority")
db = client['myDatabase']  # Replace with your database name
collection = db['sandy']  # Replace with your collection name
print("Mongo db connected sucessfully")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will render your HTML form

@app.route('/add', methods=['POST'])
def add_document():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"Inserted ID": str(result.inserted_id)})

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    age = request.form['age']
    hobby = request.form['hobby']
    color = request.form['color']
    mood = request.form['mood']

    greeting = f"Hello, {name}!"
    age_message = f"You are {age} years old."
    hobby_message = f"Your favorite hobby is {hobby}."
    mood_message = f"You're feeling {mood} today!"
    try:
        data = {name:name, age:age, hobby:hobby}
        result = collection.insert_one(data)
    except KeyError:
        return {name:"vamsi"}
    except ConnectionRefusedError:
        print("Conection refused")
    # return jsonify({"Inserted ID": str(result.inserted_id)})
    return render_template('greet.html', 
                           greeting=greeting, 
                           age_message=age_message, 
                           hobby_message=hobby_message, 
                           color=color, 
                           mood_message=mood_message)

if __name__ == '__main__':
    app.run(debug=True)
