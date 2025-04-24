# 🎬 **Flask Movie Ticket Booking Website – A Beginner’s Guide**  

Welcome, future web developers! 🌟 Today, we’ll build a **simple movie ticket booking website** using **Flask**. This guide is perfect for high school freshmen with basic Python knowledge.  

By the end of this tutorial, you'll:  
✅ Set up **Flask** and a **virtual environment**  
✅ Understand **Flask routing** (how URLs work in Flask)  
✅ Use **Flask templates** for dynamic web pages  
✅ Style your website with **CSS**  

Let’s get started! 🚀  

---

## 📌 **1. What is Flask?**  
Flask is a **Python web framework** that helps us create websites quickly and easily. Think of Flask as a **toolbox** that gives us everything we need to build web apps.  

### **Why Use Flask?**  
🔹 **Lightweight** – Doesn’t include unnecessary features  
🔹 **Flexible** – You can add only what you need  
🔹 **Uses Python** – No need to learn another language  

---

## 🛠️ **Setting Up Flask**  

### **Step 1: Set Up a Virtual Environment**  
A **virtual environment** keeps your project dependencies organized.  

1️⃣ **Create Git Ignore**:
Create a file called .gitignore  
```bash
venv
.venv
```

2️⃣ **Create a virtual environment**:  
```bash
python -m venv venv
```

3️⃣ **Activate the virtual environment**:  
- **Windows**:  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` in your terminal, meaning the environment is active.  

---

### **Step 3: Install Flask**  
Inside the virtual environment, install Flask:  

```bash
pip install flask
```

Then, create a `requirements.txt` file to track dependencies:  

```bash
pip freeze > requirements.txt
```

Now, Flask is installed! 🎉  

---
## **📌 Step 3: Understanding Routes (How Pages Talk to Each Other)**  

When you visit a website, you type something like:  
```
www.example.com/home
```
That `/home` part is the **route**. Flask lets us create routes, so when someone visits a page, it knows what to show them.  

---

### **Step 3.1: Writing Our First Flask App (`app.py`)**  

Inside your project folder, create a new file called **`app.py`** and add this code:  

```python
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
```

Add this at bottom of app.py
```Python

app.run(debug=True)

```

#### **🔹 What’s Happening Here?**
1️⃣ **We import Flask** – This lets us use Flask’s features.  
2️⃣ **We create a list of movies** – Each movie has a title and price.  
3️⃣ **We create a route for the homepage (`/`)** – When someone visits our website, Flask will show them the `index.html` page.  

## 🎨 **4. Understanding Flask Templates (HTML + Python Together!)**  

A **template** is an HTML file that can include Python code using **Jinja2**, Flask’s templating engine.  

### **Why Use Templates?**  
✅ Avoids writing the same code multiple times  
✅ Lets us **insert dynamic content** (like movie names and prices)  
✅ Keeps Python and HTML **separate** for clean code  

---

### **Step 5: Creating `index.html` (Home Page)**  
Inside a `templates/` folder, create `index.html`:  

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
                <a href=""><button>Book Now</button></a>
            </div>
        {% endfor %}
    </div>

</body>
</html>
```

### **Understanding Jinja2 Syntax**  
- `{% for movie in movies %}` → Loops through each movie  
- `{{ movie.title }}` → Displays the movie’s title dynamically  
- `url_for('book', movie_id=movie.id)` → Creates the correct URL for each movie  

---
---

## 🎨 **5. Styling with CSS (Making It Look Nice!)**  
Inside a `static/` folder, create `styles.css`:  

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

button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

---

## 🚀 **6. Running the Flask App**  
Run the Flask app:  
```bash
python app.py
```

Visit: **http://127.0.0.1:5000/** 🎉  

---

## ✅ **Summary**  
✔ **Routing** → Connects URLs to Python functions  
✔ **Templates** → Mixes Python & HTML for dynamic pages  
✔ **CSS** → Styles the website  