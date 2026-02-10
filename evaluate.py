import joblib
from sklearn.datasets import load_iris

model = joblib.load("model.pkl")     # Load the trained model from the file
X, y = load_iris(return_X_y=True)

accuracy = model.score(X, y)
print("MODEL_ACCURACY =", accuracy)

if accuracy < 0.99:
    raise Exception("Model accuracy too low")



