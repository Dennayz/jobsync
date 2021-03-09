from flask import Flask, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/parse/skills', methods=['POST'])
def parse_skills():
    req = request.get_json()
    user_input = req.get('data')

    url = "https://api.iki.ai/api/skills_extraction/"

    payload = {
        "text": user_input
    }

    headers = {
        'Content-Type': 'application/json'
    }

    r = requests.post(url=url, headers=headers, data=json.dumps(payload))

    # print(r.json())

    return r.json()


if __name__ == '__main__':
    app.run()