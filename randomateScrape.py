from flask import Flask, render_template, url_for, request
app = Flask(__name__)

import json
from search import processSearch
from top import read

@app.route("/")
@app.route("/homepage", methods=['GET', 'POST'])
def homepage():

    with open("countriesSpotify.json", 'r') as l:
            countries = json.loads(l.read())


    return render_template("homepage.html", countries=countries)

# link to just receive the info for playlists
@app.route("/info/playlist/<word>/<size>", methods=["GET", "POST"])
def info(word, size):
    processSearch(word, size)
    with open("dataSearch.json", 'r') as j:
            infos = json.loads(j.read())
    return render_template("info.html", infos=json.dumps(infos, indent=4))
    # return json.dumps(infos, indent=4)

# link to just receive the info for x country top tracks
@app.route("/info/top/<country>/<num>", methods=["GET", "POST"])
def infoCountry(country, num):
    num = int(num)
    infos = read(country, num)
    # with open("dataTop.json", 'r') as j:
    #         infos = json.loads(j.read())
    return render_template("info.html", infos=json.dumps(infos, indent=4))
    # return json.dumps(infos, indent=4)



# FOR ERRORS
@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == '__main__':
    app.run(debug=True)