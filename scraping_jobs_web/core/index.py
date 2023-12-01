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
# -*- coding: utf-8 -*-

from collections import namedtuple

Params = namedtuple("Params", "s_job city code_dpt type_contract")

class scraping_index(object):
    
    def __init__(self, params):
        self.s_job = params.s_job
        self.city = params.city
        self.code_dpt = params.code_dpt
        self.type_contract = params.type_contract
    
    def scrap_all_jobs(self):
        #
        import scraping_jobs_web.core.common as jc
        from scraping_jobs_web.core.scraping.jobs_apec import scraping_jobs_apec
        from scraping_jobs_web.core.scraping.jobs_indeed import scraping_jobs_indeed
        from scraping_jobs_web.core.scraping.jobs_monster import scraping_jobs_monster
        
        # array of jobs
        dict_jobs = []
        
        ## apec.fr
        sjapec = scraping_jobs_apec(self.s_job, self.type_contract)
        sjapec.set_code_dpt(self.code_dpt)
        dict_tmp = sjapec.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        
        ## indeed.fr
        '''
        sjindeed = scraping_jobs_indeed(self.s_job, self.type_contract)
        sjindeed.set_city(self.city)
        sjindeed.set_code_dpt(self.code_dpt)
        dict_tmp = sjindeed.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        '''
        ## monster.fr
        sjmonster = scraping_jobs_monster(self.s_job, self.type_contract)
        sjmonster.set_city(self.city)
        dict_tmp = sjmonster.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        
        ### impression des jobs en json
        return jc.jprint(dict_jobs)
