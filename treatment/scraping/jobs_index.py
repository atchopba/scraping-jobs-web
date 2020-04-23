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


def scrap_jobs(s_job, city, num_dpt, type_contract):
    import treatment.scraping.jobs_common as jc
    import treatment.scraping.jobs_apec as japec
    import treatment.scraping.jobs_indeed as jindeed
    import treatment.scraping.jobs_monster as jmonster
    
    # array of jobs
    arr_jobs = []
    
    ## apec.fr
    arr_jobs = japec.scrap_job(arr_jobs, s_job, num_dpt, type_contract)
    
    ## indeed.fr
    arr_jobs = jindeed.scrap_job(arr_jobs, s_job, city, num_dpt, type_contract)
    
    ## monster.fr
    arr_jobs = jmonster.scrap_job(arr_jobs, s_job, city, type_contract)
    
    ### impression des jobs en json
    return jc.jprint(arr_jobs)