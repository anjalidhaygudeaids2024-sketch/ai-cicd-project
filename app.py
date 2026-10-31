
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return jsonify({
        "message": "AI Model API is running successfully!"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]

    prediction = model.predict([features])

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
