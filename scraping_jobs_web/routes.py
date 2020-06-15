#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

from flask import Blueprint, request, make_response
from flask import render_template

from .core.data_treatment import extract_city_json, get_jobs

# Blueprint Configuration
main_bp = Blueprint('main_bp', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route("/")
def hello():
    return render_template('index.html')


@main_bp.route('/extract_city', methods=['POST'])
def extract_city():
    city = request.form['search_city'].lower()
    resp = make_response(extract_city_json(city))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@main_bp.route('/scraping_job', methods=['POST'])
def scraping_job():
    q = request.form['q']
    city = request.form['city']
    contract = request.form['contract']
    resp = make_response(get_jobs(q, city, contract))
    resp.status_code = 200
    resp.headers["Access-Control-Allow-Origin"] = '*'
    return resp