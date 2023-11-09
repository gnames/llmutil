from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return "<html><body>Hello</body></html>"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')