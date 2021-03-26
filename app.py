from flask import Flask, render_template, request, send_file, url_for

from utils import get_last_frame


app = Flask(__name__)
app.secret_key = 'alex'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', url='')

@app.route('/result', methods=['GET'])
def result():
    return send_file('result.png')

@app.route('/get_frame', methods=['GET'])
def get_frame():
    url = request.args.get('url', type=str)
    if url:
        filename = get_last_frame(url)
        return render_template('index.html', url='https://gif-frame-extraction.herokuapp.com/'+filename)
        # return send_file(filename)
    return render_template('index.html', url='What rubbish did you use as a url parameter?')


if __name__ == '__main__':
    app.run(port=5000, debug=True)