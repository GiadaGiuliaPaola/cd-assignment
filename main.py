from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "I did a thing!"

@app.route('/cow')
def cow():
  return "MooOOooO"

if __name__ == "__main__":
    app.run()