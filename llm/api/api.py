import json
import os
import sys

from flask import Flask, request, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from llm.model.response_generator import generate_sql_response

app = Flask(__name__)


@app.route('/get-sql', methods=['POST'])
def get_sql_response():
    req = request.get_json()
    resp = generate_sql_response(req['message'])

    lines = resp.strip().split('\n')[1:-1]
    resp = '\n'.join(lines)

    return json.loads(resp)


if __name__ == '__main__':
    app.run(debug=True)
