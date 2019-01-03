from flask import Flask, request, jsonify
from requests import request as curl_request
from urllib.parse import quote_plus
from config import *

app = Flask(__name__)


def post_to_mattermost(text, channel=CHANNEL, username=USER_NAME, icon=USER_ICON):

    payload = """{}"channel": "{}", "text": "{}", "username": "{}", "icon_url":"{}"{}""".format("payload={", channel, text, username, quote_plus(icon), "}")

    # payload = "payload={"+payload+"}"
    print(payload)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    response = curl_request("POST", MM_URL+"hooks/"+HOOK_ID, data=payload, headers=headers)
    result = response.text
    print("---hook response---")
    print(result)
    return result


@app.route('/', methods=['GET'])
def hello_world():
    return "Welcome to W3IM"


@app.route('/hooks/<token>', methods=['POST', 'GET'])
def mattermost_jira(token):
    if token == HOOK_ID:
        try:
            data = request.json
        except Exception as ex:
            return str(ex)

        print(data)

        if data and data.get("project_name", None) and data.get("message", None):
            return post_to_mattermost(text=data['message'], username=data['project_name'])
        else:
            print("Project name and Message Missing!")
    else:
        print("Wrong hook.")

    return token


@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
    return "Thanks for using my app"


if __name__ == "__main__":
    app.run(debug=DEBUG)