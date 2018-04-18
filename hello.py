from flask import Response, Flask, current_app as app
import os
import requests
import random
import string
app = Flask(__name__,static_url_path='/static')

'''
@app.route("/")
def hello():
   return app.send_static_file('index.html')   
'''
   
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
'''
@app.route("/newPage")
def newPage():
   return "This is the new Page"

@app.route("/add/<a>/<b>")
def parameters(a,b):
   return str(int(a)+int(b))
'''


def email_alert(first, second, key):
    report = {}
    report["value1"] = first
    report["value2"] = second
    #report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/bitcoin/with/key/iYiYhj3KyPFEwyVRuJzEb", data=report)    

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@app.route("/device1")
def device1():
   user_emailID = os.environ.get('device1')
   secret_code = random_generator()
   IFTTT_KEY = os.environ.get('IFTTT_KEY')
   email_alert(user_emailID, secret_code, IFTTT_KEY)
   #return app.send_static_file('index.html')

@app.route("/device2")
def device2():
   user_emailID = os.environ.get('device2')
   secret_code = random_generator()
   IFTTT_KEY = os.environ.get('IFTTT_KEY')
   email_alert(user_emailID, secret_code, IFTTT_KEY)
   #return app.send_static_file('index.html')   



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
