from flask import *
import requests

SERVER = Flask(__name__)


@SERVER.route("/")
def home():
    return render_template("index.html")

@SERVER.route("/search", methods=['GET', 'POST'])
def search():
    SEARCH = request.form.get("search")
    FIELD = request.form.get("field")

    URL = f"http://127.0.0.1:8000/?search={SEARCH}&field={FIELD}"
    RESPONSE = requests.get(URL)
    RESPONSE_JSON = RESPONSE.json()

    return render_template('info.html', json_information= RESPONSE_JSON)


if __name__ == '__main__':
    SERVER.run(debug= True)
