from flask import Flask, jsonify
import random
import json
import os

app = Flask(__name__)

FILE_PATH = "words.json"

# Initialize words if file doesn't exist
if not os.path.exists(FILE_PATH):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]  # Replace with 100 words
    with open(FILE_PATH, "w") as file:
        json.dump(words, file)
else:
    with open(FILE_PATH, "r") as file:
        words = json.load(file)

@app.route("/get-word", methods=["GET"])
def get_word():
    global words
    if not words:
        return jsonify({"word": "All words have been shown!"})
    
    selected_word = random.choice(words)
    words.remove(selected_word)

    with open(FILE_PATH, "w") as file:
        json.dump(words, file)

    return jsonify({"word": selected_word})

@app.route("/reset", methods=["POST"])
def reset_words():
    global words
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]  # Replace with 100 words
    
    with open(FILE_PATH, "w") as file:
        json.dump(words, file)

    return jsonify({"message": "Word list reset successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
