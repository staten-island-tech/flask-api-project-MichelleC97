from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data
movies = [
    {"id": 1, "title": "Avengers: Endgame", "price": 12},
    {"id": 2, "title": "Spider-Man: No Way Home", "price": 10},
    {"id": 3, "title": "Inception", "price": 8}
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', movies=movies)

app.run(debug=True)