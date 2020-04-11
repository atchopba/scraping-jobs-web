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

import json
import re

#from treatment.scraping.jobs_index import scrap_jobs
from treatment.scraping.jobs_index import scrap_jobs

CITIES_JSON_FILE = "./static/data/json/cities.json"
SCRAPING_PY_FILE = "./treatment/scraping/job_index.py"


def extract_city_json(city_name):
    """
    extract city on json file
    """
    city_name_search = city_name
    city_name_search_regex = re.compile(r'(.*)'+ city_name_search + '(.*)')
    # chargement du fichier
    with open(CITIES_JSON_FILE, "r") as file:
        cities_dict = json.load(file)
     
    city_found_dict_tmp = []
    city_found_dict = []
    for city in cities_dict:
        city_name = city["name"].lower()
        if city_name not in city_found_dict_tmp:
            city_found_dict_tmp.append(city_name)
            #
            if city_name_search_regex.search(city_name):
                city_found_dict.append(city)
    
    return json.dumps(city_found_dict)


def scraping_jobs(query, city, contract):
    """
    extract jobs with python scrpit
    """
    numdpt_regex = re.compile(r'\([0+9]{2}\)')
    numdpt_regex_search = numdpt_regex.search(city)
    numdpt = "44"
    if numdpt_regex_search:
        numdpt = numdpt_regex_search[0]
    #
    tmp_city = city.split(" ")
    if len(tmp_city) > 0:
        city = tmp_city[0]
    #
    jobs_dict = []
    # scrap job    
    jobs_dict = json.loads(scrap_jobs(query, city, numdpt, contract))
    #print(jobs_dict[0])
    ### print(jobs_dict[0]["salary"])
    return_html = ""
    # check if jobs found
    if len(jobs_dict) > 0:
        return_html += "<br/>"
        return_html += (""
            "<table border='1'>"
			"<thead>"
			"	<td></td>"
			"	<td>Libelle</td>"
			"	<td>Localisation</td>"
			"	<td>salaire</td>"
			"	<td>Date de pub / Depuis</td>"
			"	<td></td>"
			"</thead>"
			"<tbody>")
        # 
        i = 1
        for job in jobs_dict:
            return_html += (""
                "<tr>"
                "    <td>"+ str(i) +"</td>"
                "    <td>"+ job["title"] +"</td>"
                "    <td>"+ job["location"] +"</td>"
                "    <td>"+ job["salary"] + "</td>"
                "    <td>"+ job["publication_date"] + "</td>"
                "    <td><a href='"+ job["link"] +"' target='_blank' title='"+ job["description"].replace("=>", "") +"'>En savoir plus</a>"
                "</tr>")
            i += 1
        return_html += (""
            "</tbody"
            "</table>")
    return return_html 

### scraping_job("developpement", "Nantes (44)", "free")