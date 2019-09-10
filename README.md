## Product Purpose + Goal

One of the problems I have during internship searching is the time consuming task of having to apply to every job individually.
Although many sites such as Linkedin provide features to expediate the process like "Easy Apply", I wanted to build a tool to apply 
to a list of jobs at a click of a button.
TLDR: a basic way to create leagues for you and your friends with a simple interface a la talk.gg.

While the initial iterations could be as simple as a basic CRUD application that keeps track of leagues, the later iterations could be much more complex, including interfaces with discord, auto inviting, sharing, and creating tournaments and scrambling based on teams. In the future, we could iterate to have specific league types ie in poker one way to keep track of who is a winner is to see who makes a lot of money. There are any number of iterations that this could go - a way for local leagues to manage their teams (local basketball leagues, baseball leagues, etc). Local high school teams could use this as a tool for creating leagues. It doesn't even have to calculate players in house - it should be extensible enough to record at whatever level, and allow for any number of personal customizations. At the base level however, it is a way to easily compete with friends and or create leagues of any sort - with an emphasis on local feel. I think that there's a desire to compete like the pros do, and for something like this to be widely adopted, it'd be important to capture that feeling somehow.

## Product Features

Basic Functionalities

- Basic CRUD capabilities - should be able to create a user account and save associated leagues - also should be able to create undefined amount of leagues
- Should be able to create as many leagues, with invite capabilities (whether it be through using an email link or just sending a generic link) and basic score keeping capabilities such as
    - W/L, GP, Point differentials, win percentage
- Look up leagues to join based on type, location, even id
- Need to have easy ways to record a game and save into a specific league etc. Initially should have the capability for one player to sign off on the result
    - option to have both players sign off on result - with some kind of consensus mechanism
- League management dashboard - as creator, should be easy to create leagues + tournaments
    - record games
    - kick people from league, invite people to league

Additional features to work on

- create tournaments from a set amount of users based on end of the season rankings
- individualized league types for different sports → how do we measure the separation of skill in poker, FIFA, league of legends, fortnite, even trading competitions
- integration with discordgg for easy accesses, easy keeping track of ranking

Tech stack: 

- Python, Selenium, BeautifulSoup, Tkinter

Design should be as simple as something like [talk.gg](http://talk.gg) → in the future could use a dashboard time schema to manage leagues
