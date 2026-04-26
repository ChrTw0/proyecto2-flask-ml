import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    _model = pickle.load(f)


def predict_fahrenheit(celsius: float) -> float:
    value = np.array([[celsius]])
    return float(_model.predict(value)[0][0])


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data or "celsius" not in data:
        return jsonify({"error": "Se requiere el campo 'celsius'"}), 400

    try:
        celsius = float(data["celsius"])
    except (ValueError, TypeError):
        return jsonify({"error": "'celsius' debe ser un numero"}), 400

    fahrenheit = predict_fahrenheit(celsius)
    return jsonify({"celsius": celsius, "fahrenheit": round(fahrenheit, 2)})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=False)
