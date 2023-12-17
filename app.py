from flask import Flask, render_template
from datetime import datetime, date
import os

app = Flask(__name__)

@app.route('/')
def countdown():
    today = date.today()
    christmas = date(today.year, 12, 25)
    if today > christmas:
        christmas = date(today.year + 1, 12, 25)  # Next year's Christmas
    delta = christmas - today
    custom_name = os.environ.get('CUSTOM_NAME', 'Merry Christmas')
    return render_template('countdown.html', days_until_christmas=delta.days, custom_name=custom_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
