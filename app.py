from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def get_store():
    return {"alive": True}