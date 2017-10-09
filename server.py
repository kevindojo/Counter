from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "22"       # secret key needs to be put up here

@app.route('/')
def index():
    if 'count' not in session:           # create if and else statement in increment counter
        session['count'] = 0
    else: session['count'] = session['count'] + 1
    return render_template('index.html')


app.run(debug=True)