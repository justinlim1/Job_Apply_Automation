
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import sys


class jobApply:

    #https://www.indeed.com/jobs?q=software+internshipo&l=Campbell%2C+CA
    def __init__(self, page_url):
        self.options = Options()
        self.options.add_argument("--headless")
        self.url = page_url
        self.job_id = []
        self.href_list = []
        self.driver = webdriver.Chrome(options=self.options)
        self.blacklist_words = []
        self.whitelist_words = ["intern", "internship", "software"]  # List of required words in job title
        self.get_html()

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
                for link in job.findAll("a", {"target":"_blank"}):
                    self.href_list.append(link['href'])
        print(self.href_list)



    def apply(self):
        self.getJobList()


url ="https://www.indeed.com/q-software-internshipo-l-Campbell,-CA-jobs.html?advn=7983672015724620&vjk=d86b7d62ea5e6c88"
bot = jobApply(url)
bot.apply()






