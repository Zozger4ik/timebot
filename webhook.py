from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'



def get_time(latitude, longitude):
    url = f'https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitude}'
    response = requests.get(url).json()
    time = response['time']
    date = response['date']
    return f'{time} {date}'
def get_result():
    req = request.get_json(force=True)
    print(req)
    parameters = req['queryResult']['parameters']
    latitude = parameters['latitude']
    longitude = parameters['longitude']
    current_time = get_time(latitude, longitude)
    print(current_time)
    return {
        'fulfillmentText': current_time
    }




@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(get_result()))


app.run(host='0.0.0.0', port=81)
