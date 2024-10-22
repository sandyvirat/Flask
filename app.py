from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will render your HTML form

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

    return render_template('greet.html', 
                           greeting=greeting, 
                           age_message=age_message, 
                           hobby_message=hobby_message, 
                           color=color, 
                           mood_message=mood_message)

if __name__ == '__main__':
    app.run(debug=True)
