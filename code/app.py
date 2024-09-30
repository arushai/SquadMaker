from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app) 

@app.route('/')
def home():
    return 'Welcome to sample Webpage'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8986)
