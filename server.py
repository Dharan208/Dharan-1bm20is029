from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello,My Name is Dharan Pramod 1BM20IS029"

if _name_ == "_main_":
    app.run(host='0.0.0.0')
