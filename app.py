
from flask import Flask, jsonify
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

@app.route('/')
def authenticate():
    full_name = os.getenv('FULL_NAME', 'Default Name')
    return f"Welcome {full_name}! You are authenticated to use the API."

@app.route('/store-data')
def store_data():
    username = os.getenv('USERNAME', 'mongodb_test_user')
    password = os.getenv('PASSWORD', 'mongodb_test_password')
    cluster_url = os.getenv('CLUSTER_URL', '127.0.0.1:27017')
    data = {
        "age": 18,
        "height": 183,
        "Weight": 83
    }
    response = {
        "CLUSTER_URL": f"mongodb://{username}:{password}@{cluster_url}",
        "DATA": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)