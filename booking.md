Absolutely! Let's add a **new page for booking tickets**, allowing users to select a movie and enter their details.

---

## 📌 1. Updating the Project Structure

We'll add a new template for the booking page and update our Flask routes.

```
flask_movie_app/
│── static/           # Contains CSS, images
│   ├── styles.css
│── templates/        # HTML templates
│   ├── index.html    # Home page (Movie List)
│   ├── book.html     # Booking Page
│── app.py            # Main Flask app
│── requirements.txt  # Dependencies
│── venv/             # Virtual environment
```

---

## 🏗️ 2. Updating `app.py` to Include Booking Page  

Modify your `app.py` to include a new route for booking:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data
movies = [
    {"id": 1, "title": "Avengers: Endgame", "price": 12},
    {"id": 2, "title": "Spider-Man: No Way Home", "price": 10},
    {"id": 3, "title": "Inception", "price": 8}
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST':
        name = request.form['name']
        seats = request.form['seats']
        return f"Booking confirmed for {name}, {seats} seat(s) for {movie['title']}!"

    return render_template('book.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
```
## **📌 Step 4.2: Understanding the Booking Function (`book(movie_id)`)**  

Now, let's **break down** the `book(movie_id)` function so you can understand **exactly what happens** when a user tries to book a ticket.  

---

## **🔹 What does `@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])` do?**  

This **special line** tells Flask that we are creating a **route** (a web page) that works like this:  
- The **`/book/<int:movie_id>`** part means that this route **expects a number** (like `1`, `2`, or `3` for different movies).  
- Example: If the user visits **`/book/1`**, Flask knows they want to book **movie #1**.  
- The **`methods=['GET', 'POST']`** part means that this page can:  
  - **Show the booking page** (`GET` request)  
  - **Handle form submissions** (`POST` request)  

---

## **🔹 Step-by-Step Breakdown of `book(movie_id)`**  

```python
@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book(movie_id):
```
This **defines the function** for our booking page. The `movie_id` comes from the URL (like `/book/1` for "Avengers: Endgame").  

---

### **📌 Step 1: Find the Movie Based on `movie_id`**  
```python
movie = next((m for m in movies if m["id"] == movie_id), None)
```
🔹 This **searches through our list of movies** to find the **one that matches the `movie_id`**.  

🔹 Here’s how it works:  
- `movies` is a **list of movie dictionaries**  
- The function **checks each movie** (`m`) in `movies`  
- If `m["id"] == movie_id`, we **select that movie**  
- If no movie is found, `movie` becomes `None`  

---

### **📌 Step 2: Handle the Case Where No Movie is Found**  
```python
if not movie:
    return "Movie not found", 404
```
🔹 If `movie` is `None`, it means the user tried to book a movie that **doesn't exist**.  

🔹 The function **returns an error message**:  
```
Movie not found
```
And the **404** tells the browser:  
🚫 "**This page does not exist!**"  

---

### **📌 Step 3: Check if the User Submitted the Form (`POST` Request)**  
```python
if request.method == 'POST':
```
🔹 This **checks if the user clicked "Submit" on the booking form**.  

🔹 When a form is submitted, Flask **receives the data** in a special way called a **POST request**.  

---

### **📌 Step 4: Get the User's Booking Information**  
```python
name = request.form['name']
seats = request.form['seats']
```
🔹 `request.form` is like **a box full of user input**.  

🔹 `request.form['name']` → Gets the **name** that the user typed.  
🔹 `request.form['seats']` → Gets the **number of seats** they want.  

---

### **📌 Step 5: Confirm the Booking**  
```python
return f"Booking confirmed for {name}, {seats} seat(s) for {movie['title']}!"
```
🔹 This **creates a message** confirming the booking.  

🔹 Example Output:  
```
Booking confirmed for Alice, 2 seat(s) for Avengers: Endgame!
```

---

### **📌 Step 6: If No Form is Submitted, Show the Booking Page (`GET` Request)**  
```python
return render_template('book.html', movie=movie)
```
🔹 If the user **just opened the booking page** and **hasn’t submitted a form yet**, we **show the page** where they can enter their details.  

🔹 `render_template('book.html', movie=movie)`  
  - Loads `book.html` (the booking page).  
  - **Passes the `movie` data** so the page knows which movie the user is booking.  

---

## **🚀 Final Summary**
Here’s what happens step by step:  

1️⃣ User visits **`/book/1`** (or any other movie ID).  
2️⃣ Flask **finds the correct movie** based on `movie_id`.  
3️⃣ If the movie **doesn’t exist**, it shows `"Movie not found"` (404 error).  
4️⃣ If the user **submits the form**, Flask **gets their name and seats**.  
5️⃣ Flask **confirms the booking** and displays a success message.  
6️⃣ If no form is submitted, Flask **shows the booking page**.  

---


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Ticket Booking</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>🎬 Movie Ticket Booking</h1>

    <div class="movies">
        {% for movie in movies %}
            <div class="movie">
                <h2>{{ movie.title }}</h2>
                <p>Price: ${{ movie.price }}</p>
                <a href="{{ url_for('book', movie_id=movie.id) }}"><button>Book Now</button></a>
            </div>
        {% endfor %}
    </div>

</body>
</html>
```

---

## 📝 4. Creating `book.html` (Booking Page)  

Create `templates/book.html` with a form for user details:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Tickets - {{ movie.title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>🎟️ Book Tickets for {{ movie.title }}</h1>
    
    <form method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="seats">Number of Seats:</label>
        <input type="number" id="seats" name="seats" min="1" required>

        <button type="submit">Confirm Booking</button>
    </form>

    <br>
    <a href="{{ url_for('home') }}">⬅️ Back to Movies</a>
</body>
</html>
```

---

## 🎨 5. Updating `static/styles.css` for Styling  

Modify `static/styles.css` to style the booking form:

```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

.movies {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.movie {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-top: 20px;
}

input, button {
    padding: 10px;
    width: 200px;
    font-size: 16px;
}

button {
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

---

## 🚀 6. Running the App  

Now run your Flask app:

```bash
python app.py
```

Go to **http://127.0.0.1:5000/** and try booking a ticket! 🎟️  

---

## ✅ 7. Summary  

✔ **Added a "Book Now" button** on the homepage.  
✔ **Created a new booking page (`book.html`)**.  
✔ **Used Flask forms to collect user data**.  
✔ **Styled the form with CSS**.