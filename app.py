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

# ----------------------------------

