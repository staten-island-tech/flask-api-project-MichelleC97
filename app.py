from flask import Flask, render_template, request, json
import os
app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    try:
        with open("spells.json") as f:
            spell_data = json.load(f)
            if query:
                spell_data = [s for s in spell_data if query in s["name"].lower()]
    except Exception as e:
        return f"Error reading JSON: {e}"
    return render_template("index.html", spells=spell_data, search_query=query)

@app.route("/spell/<id>")
def spell_detail(id):
    try:
        with open("spells.json") as f:
            spell_data = json.load(f)
        spell = next((s for s in spell_data if s["id"] == id), None)
        if not spell:
            return "Spell not found", 404
    except Exception as e:
        return f"Error reading spell: {e}"
    return render_template("spell.html", spell=spell)

if __name__ == "__main__":
    app.run(debug=True)