import json

from flask import Flask, request, make_response, jsonify


app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    if action == 'error_code':
        res = find_error_code(req)

    else:
        log.error('Unexpected action.')

    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))


def find_error_code(req):
    code = req['queryResult']['parameters']['number']
    if code == '00000':
        return 'Payment Successful'
