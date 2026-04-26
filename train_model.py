import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# C = (F - 32) * 5/9  =>  F = C * 9/5 + 32
celsius = np.array(range(-50, 151)).reshape(-1, 1)
fahrenheit = celsius * 9 / 5 + 32

model = LinearRegression()
model.fit(celsius, fahrenheit)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado en model.pkl")
print(f"  coef={model.coef_[0][0]:.4f}  intercept={model.intercept_[0]:.4f}")
