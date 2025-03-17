from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    flask_input = ""
    if request.method == 'POST':
        flask_input = request.form.get('user_input')
        return redirect(url_for('result', user_input=flask_input))
    return render_template('index.html')

@app.route('/result')
def result():
    user_input = request.args.get('user_input', '')
    return f"Received Input: {user_input}"  # input --> var:user_input

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)