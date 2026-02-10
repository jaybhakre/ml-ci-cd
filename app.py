from flask import Flask, render_template
import joblib
from sklearn.datasets import load_iris

app = Flask(__name__)

model = joblib.load("model.pkl")
X, y = load_iris(return_X_y=True)
accuracy = round(model.score(X, y), 3)

status = "pass" if accuracy >= 0.8 else "fail"

@app.route("/")
def home():
    return render_template(
        "index.html",
        accuracy=accuracy,
        status=status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006, debug=True)