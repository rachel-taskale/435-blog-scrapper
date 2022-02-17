from scraper import read_html
from send_emails import create_email
from time import sleep
from threading import Thread
import csv



def func():
    emails = []
    with open('435_emails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            emails.append(', '.join(row))

    blog_updates_log = read_html()
    if len(blog_updates_log[0]) > 0:
        create_email(blog_updates_log, emails)
    else:
        print("blah")

if __name__ == '__main__':
    Thread(target=func).start()
    while True:
        sleep(1800)
        Thread(target=func).start()