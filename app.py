#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Albin TCHOPBA"
__copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
__credits__ = ["Albin TCHOPBA and contributors"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Albin TCHOPBA"
__email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
__status__ = "Production"

#------------------------------------------------------------------------------
# import flask lib
from flask import Flask, request, make_response
from flask import render_template

from treatment.data_treatment import extract_city_json, scraping_jobs

#------------------------------------------------------------------------------
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/extract_city', methods=['POST'])
def extract_city():
    city = request.form['search_city'].lower()
    resp = make_response(extract_city_json(city))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/scraping_job', methods=['POST'])
def scraping_job():
    q = request.form['q']
    city = request.form['city']
    contract = request.form['contract']
    resp = make_response(scraping_jobs(q, city, contract))
    resp.status_code = 200
    resp.headers["Access-Control-Allow-Origin"] = '*'
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)