import os
from flask import Flask, render_template, url_for, request, redirect
from jeugdfonds.controllers.Router import Router

app = Flask(__name__,root_path=os.path.join(os.getcwd(), 'jeugdfonds'))


@app.route('/',methods=['POST','GET'])
def index():
    c = Router.GetController("map")
    return render_template('index.html', controller = c)

@app.route('/form',methods=['POST','GET'])
def form():
    c = Router.GetController("form")
    return render_template('form.html',controller=c)

@app.route('/chart',methods=['POST','GET'])
def chart():
    c = Router.GetController("chart")
    return render_template('chart.html', controller=c)

@app.route('/form_success',methods=['GET'])
def form_success():
    return render_template('form_success.html')

if __name__ == "__main__":
    app.run(debug=True)
