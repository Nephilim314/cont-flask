#!/usr/bin/env python3

from flask import *
from flask import render_template
from sentiment_analysis_string import senti_analysis

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/background_process')
def background_process():
    try:
        story = request.args.get('story')
        if story:
            result = senti_analysis(story)
            print(result)
            return jsonify(result=result[0])#+' '+'Scores: '+result[1]+' '+result[2]+' '+result[3])
        else:
            return jsonify(result='Input needed')
    except Exception as e:
        return (str(e))

if __name__ == "__main__":
    app.debug=True
    app.run()