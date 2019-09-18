from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from time import sleep
import Bot_GUI
from selenium.webdriver.common.keys import Keys
import csv

MAX_JOBS = 500


class jobApply():

    def __init__(self, email, password, resumePath, keywords, location):
        self.options = Options()
        # self.options.add_argument("--headless")
        self.email = email
        self.password = password
        self.mainUrl = "http://linkedin.com"
        self.job_id = []  # list of job ids
        self.job_urls = []  # list of job urls
        self.driver = webdriver.Chrome(options=self.options)
        self.blacklist_words = []
        self.whitelist_words = ["intern", "internship", "software"]  # List of required words in job title
        self.resumePath = resumePath
        self.phoneNumber = "4086655117"
        self.keywords = keywords  # job title/keywords user is searching for
        self.location = location  # location of jobs user is searching for
        self.pageNum = 0
        self.csvfile = open('jobs.csv', 'w')
        self.filewriter = csv.writer(self.csvfile, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self.filewriter.writerow(['Job Title', 'Company', 'location', 'Seniority Level', 'Employment Type', 'Job URL'])

    def __del__(self):
        self.csvfile.close()

    def getJobList(self):

        # self.driver.set_window_position(0, 0)
        # self.driver.maximize_window()
        self.getNextPage()
        page = self.load_page()  # load html of all jobs on page by scrolling down
        self.jobResults = int(
            self.driver.find_element_by_xpath("//div[@class='t-12 t-black--light t-normal']").text.split()[
                0])  # get number of jobs

        while len(self.job_urls) < MAX_JOBS and len(self.job_urls) != self.jobResults:

            jobListings = page.find("ul", {"class": "jobs-search-results__list artdeco-list"})

            jobs = jobListings.findAll("div", {"data-control-name": "A_jobssearch_job_result_click"})

            for job in jobs:
                self.job_id.append(job['data-job-id'].split(":")[3])  # append job id
                self.job_urls.append(
                    "https://www.linkedin.com" + job.find("a", {"data-control-name": "A_jobssearch_job_result_click"})[
                        'href'])  # append url of main job page on Linkedin

            self.pageNum += 25
            self.getNextPage()
            page = self.load_page()

        # remove duplicates
        self.job_urls = list(dict.fromkeys(self.job_urls))
        self.job_id = list(dict.fromkeys(self.job_id))

    def jobPage(self, url):

        self.driver.set_window_position(0, 0)
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@data-control-name='jobdetails_topcard_inapply']").click()
        sleep(1)
        uploadFile = self.driver.find_element_by_id("file-browse-input")
        sleep(1)
        uploadFile.send_keys(self.resumePath)  # upload resume
        sleep(1)
        self.driver.find_element_by_xpath("//input[@id='apply-form-phone-input']").send_keys(self.phoneNumber)
        sleep(1)
        self.driver.find_element_by_xpath(
            "//button[@class='jobs-apply-form__submit-button artdeco-button artdeco-button--3 ']").click()

    def load_page(self):
        scroll_page = 0
        while scroll_page < 50:
            self.driver.find_element_by_xpath(
                "//div[@class='jobs-search-results jobs-search-results--is-two-pane']").send_keys(Keys.PAGE_DOWN)
            scroll_page += 1

        page = soup(self.driver.page_source, "html.parser")
        return page

    def login(self):
        self.driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
        self.driver.find_element_by_id("username").send_keys(self.email)
        sleep(1)
        self.driver.find_element_by_id("password").send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)

    def apply(self):
        self.login()
        self.getJobList()
        for i in self.job_urls:
            self.jobPage(i)
            self.getJobInfo(i)

    def getNextPage(self):
        url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=" + self.keywords + "&location=" + self.location + "&start=" + str(
            self.pageNum)
        self.driver.get(url)
        return url

    def getJobInfo(self, url):
        title = self.driver.find_element_by_xpath("//h1[@class='jobs-top-card__job-title t-24']").text
        company = self.driver.find_element_by_xpath("//a[@data-control-name='company_link']").text
        location = self.driver.find_element_by_xpath("//span[@class='jobs-top-card__bullet']").text
        level = self.driver.find_element_by_xpath("//p[@class='jobs-box__body js-formatted-exp-body']").text
        type = self.driver.find_element_by_xpath(
            "//p[@class='jobs-box__body js-formatted-employment-status-body']").text
        print(title, company, location, level, type)

        self.filewriter.writerow([title, company, location, level, type, url])



if __name__ == "__main__":
    main_gui = Bot_GUI.GUI()
    main_gui.wm_geometry("300x130")
    main_gui.mainloop()
    user_email = main_gui.frames["LoginFrame"].email
    user_password = main_gui.frames["LoginFrame"].password
    resume_path = main_gui.frames["ResumeFrame"].resumePath
    keywords = main_gui.frames["SearchFrame"].keywords
    location = main_gui.frames["SearchFrame"].location

    applyBot = jobApply(user_email, user_password, resume_path, keywords, location)
    applyBot.apply()
