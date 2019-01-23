from flask import Flask, request
from requests import request as curl_request
from urllib.parse import quote, urlencode, quote_plus
from config import *

app = Flask(__name__)


def post_to_mattermost(text, channel=CHANNEL, username=USER_NAME, icon=USER_ICON):
    # text =quote_plus(text) # urlencode(text, quote_via=quote_plus)
    text = text.replace('"', '\\"').replace("'", "\\'")
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

        if data and data.get("project_name", None) and data.get("message", None):
            print(data['message'])
            sentry_url = "[Click Here For Details]("+data.get("url", "#")+")"

            return post_to_mattermost(text="`"+str(data['message']))+"`\n\n" +
                                           sentry_url.replace("/sentry/sentry/", "/sentry/", 1),
                                      username=data['project_name'].replace("-", " ").title())
        else:
            print("Project name and Message Missing!")
            print(data)
    else:
        print("Wrong hook.")

    return token


@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
    return "Thanks for using my app"


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
