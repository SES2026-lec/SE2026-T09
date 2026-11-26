from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hi word! I'm using Flask. I`m happy. Hello. I love you. nice to me you. Help me."