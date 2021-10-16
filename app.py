from flask import Flask, render_template, request
import pathlib
from dotenv import load_dotenv
from textblob import TextBlob

from summerize import get_summary

load_dotenv('.flaskenv')

BASE_DIR = pathlib.Path().parent

STATIC_DIR = BASE_DIR / 'static'

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/static/')


@app.route('/', methods=['GET', 'POST'])
def index():
    content = new_value = None
    is_danger_alert = is_success_alert = False
    if request.method == 'POST':
        content = request.form.get('content')
        words = len(content.split())
        if content != '' and words >= 100:
            value = get_summary(content=content)
            new_value = TextBlob(value).correct()
            is_danger_alert = False
            is_success_alert = True

        else:
            is_danger_alert = True
            is_success_alert = False
    return render_template(
        'index.html', 
        data=new_value,
        content=content,
        is_danger_alert=is_danger_alert,
        is_success_alert=is_success_alert,
    )


if __name__ == '__main__':
    app.run(load_dotenv=True)
