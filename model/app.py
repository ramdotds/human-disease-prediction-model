from flask import Flask,render_template,request
from input import input
from model import model


app = Flask(__name__,static_folder='static',template_folder='templates')


@app.route('/')
def index_():
    return render_template('index.html')


@app.route('/predict', methods=["GET","POST"])
def index():
    if request.method=='POST':
        lst = input()
        pred = model(lst)
        plate='result.html'
    else:
        plate='index.html'
    return render_template(plate,pred=pred)


if __name__=='__main__':
    app.run(debug=False)