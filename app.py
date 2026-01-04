from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running 🚀"

@app.route("/about")
def about():
    return "This is my AI Automation backend"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}, welcome to AI world"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message","")
    return jsonify({" reply": f"you said:{ user_message}"})

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/status")
def status():
    return {"status": "ok"}

# ---------------------------------- below is same but with different concept ------------------------------------------------------
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status":"API is running🚀"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/uppercase", methods=["POST"])
def uppercase():
    text = request.json.get("text", "")
    return jsonify({"result": text.upper()})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Invalid input"}), 400 
    
    user_message = data["message"]
    # Here you can integrate with an AI model to generate a response
    reply = f"You said: {user_message}"

    return jsonify({"success": True,
                    "user_message": user_message,
                    "reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/status")
def status():
    return {"status": "ok"}


