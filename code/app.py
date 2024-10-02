from flask import Flask
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok

app = Flask(__name__)
run_with_ngrok(app) 

@app.route('/')
def home():
    return 'Welcome to sample Webpage'

if __name__ == '__main__':
    ngrok_tunnel = ngrok.connect(5000)
    app.run()
