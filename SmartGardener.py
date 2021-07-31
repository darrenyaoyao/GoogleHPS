from flask import Flask

app = Flask("Smart Gardener")

@app.route("/")
def home():
    return "Hello World"
