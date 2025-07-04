from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open("mandarin_verbs_flashcard_200_detailed.json", encoding="utf-8") as f:
    flashcards = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cards")
def cards():
    return jsonify(flashcards)

if __name__ == "__main__":
    app.run(debug=True)
