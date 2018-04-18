from flask import Response, Flask, current_app as app
import os
app = Flask(__name__,static_url_path='/static')


@app.route("/")
def hello():
   return app.send_static_file('index.html')   

   
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/newPage")
def newPage():
   return "This is the new Page"

@app.route("/add/<a>/<b>")
def parameters(a,b):
   return str(int(a)+int(b))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
