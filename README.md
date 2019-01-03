# Mattermost JIRA Web Hook

### Prerequisites
 - Python (2/3)
 - Mattermost webhook. ([Go Here](https://docs.mattermost.com/developer/webhooks-incoming.html#) to create guide.)
 - Create a python file from `config.py.sample` as `config.py`
 - Change information based on yours on `config.py`
 - Configure Sentry Web hook (Configure the webhook in your Sentry) by following [http://yoursentryurl.com/settings/sentry/vrs-search-service/alerts/](#)
### How to test
- Run `pip install -r requirements.txt`
- Then on your project directory run `python app.py`

### Deployment
Follow [flask reference](http://flask.pocoo.org/docs/dev/tutorial/deploy/)

**N.B: For Sentry WebHook you need to set a valid host/endpoint**
