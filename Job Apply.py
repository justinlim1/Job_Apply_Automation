
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import sys


MAX_JOBS = 100

class jobApply:

    #https://www.indeed.com/jobs?q=software+internshipo&l=Campbell%2C+CA
    def __init__(self, page_url):
        self.options = Options()
        #self.options.add_argument("--headless")
        self.url = page_url
        self.mainUrl = "http://indeed.com"
        self.job_id = [] #list of job ids
        self.job_urls = [] #list of job urls
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

        for job in jobs:
            if job.find("div", {"class":"iaWrapper"}):
                self.job_id.append(job['id']) #append job id
                for link in job.findAll("a", {"target":"_blank"}):
                    self.job_urls.append(self.mainUrl + link['href']) #append url of each job to list
        #print(self.job_urls)

    def jobPage(self):
        for url in self.job_urls:
            self.driver.get(url)
            time.sleep(5)

    def login(self,email,password):
        self.driver.get('https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=&from=gnav-util-homepage&_ga=2.210805846.21291967.1566709415-1824541224.1566527853')
        self.driver.find_element_by_name("__email").send_keys(email)
        time.sleep(1)
        self.driver.find_element_by_name("__password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='login-submit-button']").click()




    def apply(self):
        self.login("justinlim8@gmail.com", "gzzc2g93")
        #self.getJobList()
        #self.jobPage()


url ="https://www.indeed.com/q-software-internshipo-l-Campbell,-CA-jobs.html?advn=7983672015724620&vjk=d86b7d62ea5e6c88"
bot = jobApply(url)
bot.apply()






