import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__,root_path=os.path.join(os.getcwd(), 'jeugdfonds'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
