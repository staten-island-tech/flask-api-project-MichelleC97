from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data
about_me = [
    {"Title": "Myself", "Description": "I am a freshmen in Highschool. My favorite color is pink and teal. I LOVE the subject math. Summer is my favorite season because my brithday is during that time!"}, 
    {"Title": "Sibling", "Description": "I have a sister name Viv, she is 2 years older than me. I like to annoy her (A LOT) during my free time. She goes to Susan E. Wagner High School."}, 
    {"Title": "Hobby", "Description": "I like to play with my family and friends. My favorite sport is Badminton. I don't hate dancing but it's not my favorite as well. I also want to have a dog so badly!!"},
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', about_me=about_me)

app.run(debug=True)