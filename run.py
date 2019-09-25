import os
from flask import Flask, url_for, redirect, render_template, request
from twitter_search import tsearch
from predict import classifier
from plot import plot_graph
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def index_post():
    if request.form['submit'] == 'Submit':
        try:
            query1 = request.form['Query1']
            query1 = str(query1)
            query2 = request.form['Query2']
            query2 = str(query2)
            # tsearch(query1, query2)
            p1, n1, p2, n2 = classifier()
            plot_graph(query1, query2, p1, n1, p2, n2)

            return render_template('home.html', q1=query1.upper(), q2=query2.upper(),
                                   p1=p1, n1=n1, p2=p2, n2=n2)
        except:
            return render_template('home.html', error="Sorry! No Tweets Found,Enter Again")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
