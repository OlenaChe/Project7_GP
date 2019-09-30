from flask import Flask, render_template, jsonify, request
import requests

from parseur import parser_list, parser_str
from wiki_info import get_data
from location import get_latitude, get_longitude, get_address
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/process/', methods=['POST'])
def process():
    question = request.form['question']
    parsedlist = parser_list(question)
    parsed_str = parser_str(question)
    wiki_response = get_data(parsedlist)
    address = get_address(parsedlist)
    lat = get_latitude(parsedlist)
    lng = get_longitude(parsedlist)
    return jsonify({'data': [question, address, wiki_response, lat, lng, parsed_str]})

if __name__ == "__main__":
    app.run(debug=True)
