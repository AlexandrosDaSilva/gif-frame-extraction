from flask import Flask, render_template, request, send_file

from utils import get_last_frame


app = Flask(__name__)
app.secret_key = 'alex'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_frame', methods=['GET', 'POST'])
def get_frame():
    url = request.args.get('url', type=str)
    filename = get_last_frame(url)
    return send_file(filename)


if __name__ == '__main__':
    app.run(port=5000, debug=True)