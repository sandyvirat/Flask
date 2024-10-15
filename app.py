from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    age = request.form.get('age')
    hobby = request.form.get('hobby')
    color = request.form.get('color')
    mood = request.form.get('mood')

    greeting = f"Hi {name}, nice to meet you!"
    
    # Age-specific response
    if age.isdigit():
        age = int(age)
        if age < 18:
            age_message = "You're young and full of energy!"
        elif 18 <= age <= 30:
            age_message = "You're in the prime of your life!"
        elif 30 <= age <= 50:
            age_message = "Experienced and thriving!"
        else:
            age_message = "You're young at heart and wise!"
    else:
        age_message = "Age is just a number, right?"

    # Hobby-specific message
    if hobby:
        hobby_message = f"Enjoy your time {hobby}-ing!"
    else:
        hobby_message = ""

    # Mood-based message
    if mood == 'happy':
        mood_message = "Glad to hear you're in a good mood!"
    elif mood == 'sad':
        mood_message = "Sorry to hear you're feeling down. Cheer up!"
    elif mood == 'excited':
        mood_message = "Excitement is contagious!"
    else:
        mood_message = ""

    return render_template('greet.html', name=name, color=color, age_message=age_message, hobby_message=hobby_message, mood_message=mood_message)

if __name__ == "__main__":
    app.run(debug=True)
 
