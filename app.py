from flask import Flask, request, jsonify
from chat import get_response


app = Flask(__name__)


@app.route('/predict', methods=["POST", "GET"])
def predict():
    text = request.get_json().get("message")
    print(text)
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
