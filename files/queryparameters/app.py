from flask import Flask
# from uuid import UUID
app = Flask(__name__)

@app.route("/")
def home():
    return "hello guyz what's up"


if __name__ == "__main__":
    app.run(debug=True)
