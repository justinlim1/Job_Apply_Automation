
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
import re
import sys

url = 'https://www.indeed.com/jobs?q=software+internshipo&l=Campbell%2C+CA' #url of the job search site
uCl = ur.urlopen(url)
page_html = uCl.read()
uCl.close()
page = soup(page_html, "html.parser") #parse html
job_id = []



jobListings = page.find("td",{"id": "resultsCol"})
jobs = jobListings.findAll("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})
print(len(jobs))
for job in jobs:
    if job.find("div", {"class":"iaWrapper"}):
        job_id.append(job['id'])
print(job_id)



#driver = webdriver.Chrome()


blacklist_words = []
whitelist_words = ["intern", "internship", "software"] #List of required words in job title


