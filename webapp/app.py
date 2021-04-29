from flask import Flask, abort, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Lavanya is a good girl"

@app.route("/kids")
def kids():
    return jsonify("sahasra", "naithik")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


