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
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
