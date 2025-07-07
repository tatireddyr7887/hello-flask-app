from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World from AWS!"

if __name__ == "__main__":
    print("Flask app is starting on port 5000...")
    app.run(host='127.0.0.1', port=8080)