from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Google Academy!</h1><img src='https://storage.googleapis.com/la-gcp-labs-resources/essentials/Logo-Pinehead-NVY.png' width='40%' alt='Pinehead @ Google Academy'></div>"
    return html

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=8080, debug=True)
