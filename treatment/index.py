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

class scraping_index(object):
    
    def __init__(self, s_job, city, code_dpt, type_contract):
        self.s_job = s_job
        self.city = city
        self.code_dpt = code_dpt
        self.type_contract = type_contract
    
    def scrap_all_jobs(self):
        #
        import treatment.common as jc
        from treatment.scraping.jobs_apec import scraping_jobs_apec
        from treatment.scraping.jobs_indeed import scraping_jobs_indeed
        from treatment.scraping.jobs_monster import scraping_jobs_monster
        
        # array of jobs
        dict_jobs = []
        
        ## apec.fr
        sjapec = scraping_jobs_apec(self.s_job, self.type_contract)
        sjapec.set_code_dpt(self.code_dpt)
        dict_tmp = sjapec.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        
        ## indeed.fr
        sjindeed = scraping_jobs_indeed(self.s_job, self.type_contract)
        sjindeed.set_city(self.city)
        sjindeed.set_code_dpt(self.code_dpt)
        dict_tmp = sjindeed.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        
        ## monster.fr
        sjmonster = scraping_jobs_monster(self.s_job, self.type_contract)
        sjmonster.set_city(self.city)
        dict_tmp = sjmonster.scrap_job()
        if len(dict_tmp) > 0:
            dict_jobs += dict_tmp
        
        ### impression des jobs en json
        return jc.jprint(dict_jobs)