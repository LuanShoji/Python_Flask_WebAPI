from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
   return "hello world!"

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
