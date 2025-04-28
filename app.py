from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data
about_me = [
    {"Name": "Mich", "Age": "14", "Fav Color": "Pink and Teal"},
    {"Sibling": "Viv", "Fav Color": "Red"},
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', about_me=about_me)

app.run(debug=True)