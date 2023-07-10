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
    node_name = os.getenv('NODE_NAME') or get_node_name()

    return jsonify({
        'user': os.environ.get('user'),
        'number': os.environ.get('number'),
        'NODE_NAME': node_name,
    })

def get_node_name():
    import subprocess
    result = subprocess.run(['kubectl', 'get', 'pod', '-o', 'jsonpath={.spec.nodeName}', os.getenv('HOSTNAME')], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return 'Unknown node'

if __name__ == '__main__':
    app.run()

