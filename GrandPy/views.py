from flask import Flask, render_template, jsonify, request
import requests

from .parseur import Parseur
from .wiki_info import get_wiki_extract, get_wiki_url
from .location import Location 

app = Flask(__name__)

#app.config.from_object('config')

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/process/', methods=['POST'])
def process():
    question = request.form['question']
    data = Parseur()
    parsedlist = data.parser_list(question)
    parsed_str = data.parser_str(question)
    wiki_extract = get_wiki_extract(parsedlist)
    wiki_url = get_wiki_url(parsedlist)
    location = Location()
    address = location.get_address(parsedlist)
    lat = location.get_latitude(parsedlist)
    lng = location.get_longitude(parsedlist)
    return jsonify({'data': [question, address, wiki_extract, wiki_url, lat, lng, parsed_str]})

if __name__ == "__main__":
    app.run(debug=True)
