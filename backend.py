from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json  # Extract JSON data from frontend
    num1 = float(data.get("num1"))
    num2 = float(data.get("num2"))
    operation = data.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error (division by zero)"
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
