from flask import Flask, renderTemplate

app = Flask(__name__)

@app.route('/')

def home():
    return renderTemplate('home.html')

if __name__ == '__main__':
    app.run(debug=True)

