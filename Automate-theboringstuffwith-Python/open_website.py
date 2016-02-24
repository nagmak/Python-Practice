# Open social network sites regularly used
# Use nohup python3 open_website.py & <- to run, after every reboot
# Allows program to run w/out Terminal open

import webbrowser
import schedule
import time
    
website = ['https://www.tumblr.com', 'https://www.reddit.com',
           'https://www.facebook.com', 'https://www.twitter.com']
def job():
    for site in website:
        webbrowser.open(site)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
