import json

from flask import Flask, request, make_response, jsonify

from forecast import Forecast, validate_params

app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook

    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'
    """
    KEY IN ACTIONS HERE

    if action == 'weather':
        res = weather(req)
    elif action == 'weather.activity':
        res = weather_activity(req)
    elif action == 'weather.condition':
        res = weather_condition(req)
    elif action == 'weather.outfit':
        res = weather_outfit(req)
    elif action == 'weather.temperature':
        res = weather_temperature(req)
    else:
        log.error('Unexpected action.')
    """
    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))
