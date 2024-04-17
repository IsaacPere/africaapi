from flask import Flask 
from flask import request 

sms_server = Flask(__name__)

@sms_server.route("/")
def hello_sms():
    return "<p>Hello World!</p"

@sms_server.route("/callback", methods=['POST'])
def callback():
    print(request.method)
    print(request.form)
    reponse(request.form["from"], "Yes I gotten your text")
    return "Sucess", 201

api_key = "fb59ef19aa9dc260caa2f9cacbbfb0c4df8d338d3b867e0ec370c09421f1c283"

def reponse():
    requests.method(
        "https://api.sandbox.africastalking.com/version1/messaging",
        data= {
            "username" : "sandbox",
            "to" : clients_number,
            "message" : message,
            "from" : "99580"
        },
        headers =  {
            "apikey" : api_key,
            "Accept" : "application/json",
            "Content-Type" : "application/x-www-form-urlencoded"
        }
    )
