from flask import Flask, request, jsonify
from llm.model.response_generator import generate_sql_response

app = Flask(__name__)


@app.route('/get-sql', methods=['POST'])
def get_sql_response():
    req = request.get_json()
    resp = generate_sql_response(req['message'])

    return generate_sql_response(resp)


if __name__ == '__main__':
    app.run(debug=True)
