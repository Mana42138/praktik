from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    with open('backups/output-1.json') as f:
        data = json.load(f)
    return render_template('index.html', d=data)

if __name__ == '__main__':
    app.run(debug=True)