import smtplib
from datetime import date



def create_email(body_text, emails):
    gmail_user = 'cmsc435digest@gmail.com'
    gmail_password = '57a72P98YJF3vxR'

    sent_from = gmail_user
    to = emails
    subject = 'CMSC435 Update' + date.today().strftime("%m-%d-%Y")
    body = body_text

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong')