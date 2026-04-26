import numpy as np
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify

app = Flask(__name__)

# Entrena el modelo en memoria al arrancar (F = C * 9/5 + 32)
_celsius = np.array(range(-50, 151)).reshape(-1, 1)
_fahrenheit = _celsius * 9 / 5 + 32
_model = LinearRegression()
_model.fit(_celsius, _fahrenheit)


def predict_fahrenheit(celsius: float) -> float:
    return float(_model.predict([[celsius]])[0][0])


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
