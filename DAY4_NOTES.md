
Day 4 Notes — REST APIs & JSON with Flask
🎯 Objective

Learn and implement REST APIs using Flask, handle JSON requests/responses, validate input, return proper HTTP status codes, and test APIs like a backend developer.

1️⃣ What is an API?
An API (Application Programming Interface) allows two software systems to communicate.

Example flow:

Client → API Request → Flask Server → Response (JSON)


APIs are used in:
AI Chatbots
Mobile Apps
Web Apps
Automation tools
SaaS products

2️⃣ REST API Basics
REST stands for Representational State Transfer.

Key principles:
Each endpoint does one job
APIs are stateless
Communication happens via HTTP
Data is exchanged using JSON

Example endpoints:

POST /chat
GET  /health
POST /uppercase

3️⃣ HTTP Methods
Method	Purpose
GET	Fetch data
POST	Send data
PUT	Update data
DELETE	Delete data

In this project:

GET → system status
POST → send JSON data securely

4️⃣ HTTP Status Codes
Code	Meaning
200	Success
201	Created
400	Bad Request
404	Not Found
500	Server Error

Status codes help clients understand what happened.

5️⃣ JSON Fundamentals

JSON = JavaScript Object Notation
Used for sending structured data.

Example:

{
  "message": "Hello",
  "user": "gaurav"
}


Rules:

Data is key-value based

Keys are strings

Values can be string, number, boolean, object, array

6️⃣ Flask Request Handling

To read JSON sent by the client:

data = request.get_json()


Why get_json()?

Safer than request.json

Avoids crashes on invalid input

Access values:

message = data["message"]

7️⃣ Input Validation

Always validate user input.

Example:

if not data or "message" not in data:
    return jsonify({"error": "Message is required"}), 400


Validation prevents:

App crashes

Bad data

Security issues

8️⃣ Flask Response Handling

Always return JSON for APIs.

Correct way:

return jsonify({"success": True}), 200


Avoid returning raw strings in APIs.

9️⃣ Sample API Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message required"}), 400

    user_message = data["message"]
    reply = f"Echo: {user_message}"

    return jsonify({
        "success": True,
        "user_message": user_message,
        "reply": reply
    }), 200

🔟 API Testing

Use tools like:
Postman
VS Code REST Client

Test cases:
Valid JSON
Missing fields
Empty input
Observe status codes
Testing is part of backend development.

1️⃣1️⃣ API Documentation (README)
Good APIs are documented.

Example:

POST /chat
Body:
{
  "message": "Hello"
}


Documentation increases project professionalism.

1️⃣2️⃣ What I Learned on Day 4
How REST APIs work
Difference between GET and POST
Handling JSON safely
Input validation
Returning proper HTTP responses
Testing APIs like a professional
