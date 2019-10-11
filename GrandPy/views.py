"""Views of the application GrandPy"""

from flask import Flask, render_template, jsonify, request

from .parseur import parse
from .wiki_info import get_wiki_extract, get_wiki_url
from .location import get_address, get_latitude, get_longitude

app = Flask(__name__)

@app.route('/')
def main():
    """Method which renders an html page"""
    return render_template("main.html")

@app.route('/process/', methods=['POST'])
def process():
    """Method which renders the data for the processing with ajax"""
    question = request.form['question']
    parsed_question = parse(question)
    wiki_extract = get_wiki_extract(parsed_question)
    wiki_url = get_wiki_url(parsed_question)
    address = get_address(parsed_question)
    lat = get_latitude(parsed_question)
    lng = get_longitude(parsed_question)
    return jsonify({'data': [question, address, wiki_extract, wiki_url, lat, lng, parsed_question]})

if __name__ == "__main__":
    app.run(debug=True)
