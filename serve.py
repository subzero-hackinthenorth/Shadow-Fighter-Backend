from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods = ["GET"])
def index():
  print(request.args)
  return "YES"
app.run("127.0.0.1",5000, debug = False)
