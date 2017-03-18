#!/usr/local/bin/python
# coding=utf-8
"""
 Simple example of a Python script used to query an API.

 @note:    This is a simple example without any error handling.
 @license: http://data.gc.ca/eng/open-government-licence-canada
"""
from flask import Flask, render_template, request
import json
import requests # Needed for API use

app = Flask(__name__)

# Must have html files under templates directory to work
@app.route('/results', methods=['GET'])
def results():
    url      = 'http://www.earthquakescanada.nrcan.gc.ca/api/earthquakes/'
    options  = { "Accept":"application/json", "Accept-Language":"en" }
    response = requests.get(url, headers=options)
    jdata    = response.json()
    #print jdata['metadata']['request']['name']['en']

    #for (key, value) in jdata['latest'].items():
    #        compiledresults =  key, "->", value  # works, except not iterating
    results = json.dumps(jdata['latest'], sort_keys = True)
    #return render_template('results.html', dataresults=jdata['latest'])
    #return render_template('results.html', dataresults=results)
    return render_template('results.html', dataresults=jdata['latest'])
#           print key, "->", value # Console Command
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
