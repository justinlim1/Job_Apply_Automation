
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
import re
import sys

url = 'https://www.indeed.com/jobs?q=Summer&l=Campbell%2C%20CA&start=10&advn=8857166483495170&vjk=a32a93717d9cf9f3' #url of the job search site
uCl = ur.urlopen(url)
page_html = uCl.read()
uCl.close()
page = soup(page_html, "html.parser") #parse html
job_id = []



jobListings = page.find("td",{"id": "resultsCol"})
jobs = jobListings.findAll('div', {"class": "jobsearch-SerpJobCard unifiedRow row result"})
for job in jobs:
    job_id.append(job['id'])
print(job_id)



#driver = webdriver.Chrome()


blacklist_words = []
whitelist_words = ["intern", "internship", "software"] #List of required words in job title


