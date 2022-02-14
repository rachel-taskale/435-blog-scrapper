from scraper import read_html
from send_emails import create_email
from time import sleep
from threading import Thread


def func():
    emails = ['racheltaskale@gmail.com', 'patrickotoole49@gmail.com']
    blog_updates_log = read_html()
    counter = 0
    for i in blog_updates_log:
        print("counter: " + str(counter))
        print(i)
        counter += 1

    create_email(blog_updates_log, emails)


if __name__ == '__main__':

    Thread(target=func).start()
    while True:
        sleep(1800)
        Thread(target=func).start()