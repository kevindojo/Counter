from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "22"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else: session['count'] = session['count'] + 1
    return render_template('index.html')


app.run(debug=True)