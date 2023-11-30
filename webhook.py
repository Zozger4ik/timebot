from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'




def get_result():
    # извлечение параметра
    req = request.get_json(force=True)
    print(req)
    current_time = get_time(45.1, 67.2)
    print(current_time)
def get_time(latitude, longitude):
    url = f'https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitude}'
    response = requests.get(url).json()
    time = response['time']
    date = response['date']
    return f'{time} {date}'




@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(get_result()))


app.run(host='0.0.0.0', port=81)
