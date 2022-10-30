from flask import Flask

app = Flask(__name__)

@app.route("/user")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug = True, port = 8080)