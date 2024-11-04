from flask import Flask, request, jsonify
from flask_httpauth import HTTPTokenAuth
import os

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Set environment variables
os.environ['RES'] = 'your_res_value'
os.environ['REQ'] = 'your_req_value'
os.environ['TOKEN'] = 'your_secret_token'

# Token verification function
@auth.verify_token
def verify_token(token):
    return token == os.getenv('TOKEN')

# GET endpoint with token authentication
@app.route('/get', methods=['GET'])
@auth.login_required
def get():
    res = os.getenv('RES')
    req = os.getenv('REQ')
    return jsonify({"res": res, "req": req})

# POST endpoint with token authentication
@app.route('/post', methods=['POST'])
@auth.login_required
def post():
    data = request.get_json()
    res = data.get('res')
    req = data.get('req')
    return jsonify({"res": res, "req": req})

if __name__ == '__main__':
    app.run(debug=True)

