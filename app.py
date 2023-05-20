import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def root():
    return jsonify({
        "message": "OK"
    })


@app.route('/api/upload-json', methods=['POST'])
def upload_file():
    # Assuming the JSON file is sent as a 'file' field in the request
    file = request.files['file']
    raw_data = file.read().decode('utf-8')  # Read the file contents as a string

    data = json.loads(raw_data)
    data['status'] = 'processed'

    return jsonify({
        'message': 'File uploaded successfully',
        "data": data
    })

@app.route('/api/env-variable')
def get_env_variable():
    return jsonify({
        'user': os.environ.get('user'),
        'number': os.environ.get('number'),
    })


if __name__ == '__main__':
    app.run()

