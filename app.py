from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Welcome! Try the <a href='/me'>/me</a> endpoint 🚀</h2>"

@app.route("/me")
def me():
    # Fetch a dynamic cat fact
    cat_fact_api = "https://catfact.ninja/fact"
    try:
        fact_response = requests.get(cat_fact_api, timeout=5)
        fact_data = fact_response.json()
        cat_fact = fact_data.get("fact", "Cats are mysterious creatures!")
    except Exception:
        cat_fact = "Cats are mysterious creatures!"

    # Build the JSON response
    response = {
        "status": "success",
        "user": {
            "name": "Emmanuel Lemuel",
            "email": "emmanuel@gmail.com",
            "stack": "backend"
        },
        "fact": cat_fact,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # Return as JSON with correct Content-Type
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
