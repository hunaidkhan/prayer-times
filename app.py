from flask import Flask
import json
import datetime

app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])

    
def welcome():
    current_date = datetime.datetime.now()
    current_month = current_date.strftime("%B")
    current_day = current_date.day

    with open("data.json", 'r') as file:
        all_prayer_times = json.load(file)
    current_prayer_times = all_prayer_times.get(current_month, {}).get(str(current_day), {})

    return current_prayer_times


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)