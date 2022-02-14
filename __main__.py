from scraper import read_html
from send_emails import create_email
from time import sleep
from threading import Thread


def func():
    emails = ['racheltaskale@gmail.com']
    blog_updates_log = read_html()
    print("Checked_for_updates")
    create_email(blog_updates_log, emails)
    print("made it here")


if __name__ == '__main__':

    Thread(target=func).start()
    while True:
        sleep(1800)
        Thread(target=func).start()
