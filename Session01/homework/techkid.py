import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/school')
def hello():
    return redirect("techkid.vn", code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)