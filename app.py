from flask import Flask, render_template
app.secret_key = 'supersecretmre'

@app.route('/')
def index():
    return render_template('index.html')
