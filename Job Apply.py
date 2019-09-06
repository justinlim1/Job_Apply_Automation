
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import sys


MAX_JOBS = 100

class jobApply:


    def __init__(self, page_url):
        self.options = Options()
        #self.options.add_argument("--headless")
        self.url = page_url
        self.mainUrl = "http://linkedin.com"
        self.job_id = [] #list of job ids
        self.job_urls = [] #list of job urls
        self.driver = webdriver.Chrome(options=self.options)
        self.blacklist_words = []
        self.whitelist_words = ["intern", "internship", "software"]  # List of required words in job title
        self.resumePath = ""
        self.phoneNumber = "4086655117"

    def find_page(self, url):
        self.driver.get(url)
        self.driver.find_element_by_xpath("//button[@aria-controls='linkedin-features-facet-values']").click()
        self.driver.find_element_by_xpath("//label[@for='f_LF-f_AL']").click()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.RETURN)
        sleep(1)
        self.jobResults = self.driver.find_element_by_xpath("//div[@class='t-12 t-black--light t-normal']").text





    def getJobList(self):

        self.find_page("https://www.linkedin.com/jobs/search/?keywords=software%20internship")
        #self.driver.set_window_position(0, 0)
        #self.driver.maximize_window()
        page = self.load_page()

        #while len(self.job_urls) < MAX_JOBS:

        jobListings = page.find("ul", {"class": "jobs-search-results__list artdeco-list"})

        jobs = jobListings.findAll("div", {"data-control-name": "A_jobssearch_job_result_click"})

        for job in jobs:

            self.job_id.append(job['data-job-id'].split(":")[3])  # append job id
            self.job_urls.append("https://www.linkedin.com" + job.find("a", {"data-control-name":"A_jobssearch_job_result_click"})['href'])

        print(self.job_urls)





    def jobPage(self, url):

        self.driver.set_window_position(0, 0)
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@data-control-name='jobdetails_topcard_inapply']").click()
        sleep(1)
        uploadFile = self.driver.find_element_by_id("file-browse-input")
        sleep(1)
        uploadFile.send_keys(self.resumePath)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@id='apply-form-phone-input']").send_keys(self.phoneNumber)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@class='jobs-apply-form__submit-button artdeco-button artdeco-button--3 ']").click()

    def load_page(self):
        scroll_page = 0
        while scroll_page < 50:
            self.driver.find_element_by_xpath("//div[@class='jobs-search-results jobs-search-results--is-two-pane']").send_keys(Keys.PAGE_DOWN)
            scroll_page += 1



        page = soup(self.driver.page_source, "html.parser")
        return page

    def chooseResume(self):
        Tk().withdraw()
        self.resumePath = askopenfilename()
        print(self.resumePath)

    def login(self,email,password):
        self.driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
        self.driver.find_element_by_id("username").send_keys(email)
        sleep(1)
        self.driver.find_element_by_id("password").send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)



    def apply(self):
        self.login("justinlim8@gmail.com", "201404")
        self.getJobList()
        self.chooseResume()
        self.jobPage("https://www.linkedin.com/jobs/view/1481475066/?eBP=JOB_SEARCH_ORGANIC&refId=5af40094-07c1-4bcc-9fa2-5878723a1904&trk=d_flagship3_search_srp_jobs")

    # def uploadResume(self):
    #     bool_upload_resume = input("Would you like to upload a new resume?")
    #     if bool_upload_resume == True:



url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=software%20internship&location=San%20Jose%2C%20California%2C%20United%20States"
bot = jobApply(url)
bot.apply()






