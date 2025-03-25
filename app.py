"""Simple Flask app for CI/CD demo."""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Hello, CI/CD!"