
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
import re
import sys


class jobApply:

    #https://www.indeed.com/jobs?q=software+internshipo&l=Campbell%2C+CA'
    def __intit__(self, url):
        url = url
        job_id = []
        driver = webdriver.Chrome()
        blacklist_words = []
        whitelist_words = ["intern", "internship", "software"]  # List of required words in job title



    def get_html(self): #parse html from given url
        uCl = ur.urlopen(self.url)
        page_html = uCl.read()
        uCl.close()
        self.page = soup(page_html, "html.parser")
        self.job_id = []


    def getJobList(self):
        jobListings = self.page.find("td",{"id": "resultsCol"})
        jobs = jobListings.findAll("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})
        #print(len(jobs))
        for job in jobs:
            if job.find("div", {"class":"iaWrapper"}):
                self.job_id.append(job['id'])
        #print(job_id)








