from flask import Flask
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok

app = Flask(__name__)
#run_with_ngrok(app)             # Start ngrok when app is run

@app.route('/')
def home():
    return 'Welcome to Box Cricket SquadMaker'

if __name__ == '__main__':
#    ngrok_tunnel = ngrok.connect(5000)
    app.run()
