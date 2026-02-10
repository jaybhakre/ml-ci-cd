import joblib
from sklearn.datasets import load_iris

model = joblib.load("model.pkl")
X, y = load_iris(return_X_y=True)

accuracy = model.score(X, y)
print("Accuracy:", accuracy)

if accuracy < 0.8:
    raise Exception("Model accuracy too low")