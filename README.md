## Product Purpose + Goal

One of the problems I have during internship searching is the time consuming task of having to apply to every job individually.
Although many sites such as Linkedin provide features to expediate the process like "Easy Apply", I wanted to build a tool to automate this task.

While the initial iterations could be a simple bot to web scrape a list of jobs based on user provided key words and apply to those jobs via "Easy Apply". the later iterations could be much more complex, including UI, generation of CSV file containing information of every job the bot has applied to, switching between different sites. In the future, we could iterate to have customized CVs based on the job info. 

## Product Features

Basic Functionalities


- Grab a list of jobs and their job IDs without duplicates
- Ask the user for preference of key words, blacklisted words, location, salary, job level etc...
- Upload resume and cover letter to Linkedin
- Display the info of every job the tool has applied to
- UI

Additional features to work on

- Error checking and exceptions
- Custom cover letters/emails
- Allow user to choose which jobs to apply for

Tech stack: 

- Python, Selenium, BeautifulSoup, Tkinter

