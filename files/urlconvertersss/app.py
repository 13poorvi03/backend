from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "hello guyz what's up"

@app.route("/numbs/<int:id>")     #this is an integer url converter
def numbs(id):
    return f"USER ID: {id}"        


@app.route("/price/<float:amount>")    #this is a float url converter
def price(amount):
    return f"Price: {amount}" 

@app.route("/user/<string:name>")    #this is a string url converter
def user(name):                       #in this u can get numbers float too
    return f"USER NAME: {name}" 


@app.route("/files/<path:file_path>")     #this is a path converter
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")     #this is a path converter
def student(user_id):
    return str(user_id)


if __name__ == "__main__":
    app.run(debug=True)
