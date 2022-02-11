
import os
from scraper import check_if_updated, read_html, email_formatter
from send_emails import create_email
# Main function
#Calls the check_if_updated function to see if 
def main():
    emails = ['racheltaskale@gmail.com']
    blog_updates_log = check_if_updated()
    create_email(blog_updates_log, emails )