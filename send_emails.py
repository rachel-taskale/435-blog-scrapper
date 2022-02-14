import smtplib
from datetime import date


def format_email(body_text):
    final_body_text = ''
    i = 0
    for i in body_text:
        print(i)
        print("hi" + str(i) + "\n")
        # string_txt = i[1:len(i)]
        # final_body_text += string_txt + "\n"
        # print(i)
    return final_body_text


def create_email(body_text, emails):

    gmail_user = 'cmsc435digest@gmail.com'
    gmail_password = '5QGmC9KnMkKumMb'

    sent_from = gmail_user
    to = emails
    subject = 'CMSC435 Update' + date.today().strftime("%m-%d-%Y")
    body = format_email(body_text)
    print(body_text)
    print(body)

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)
    #
    # try:
    #
    #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     print("1 line")
    #     server.ehlo()
    #     print(gmail_user)
    #     print(gmail_password)
    #     server.login(gmail_user, gmail_password)
    #     print("3 line")
    #     server.sendmail(sent_from, to, email_text)
    #     print("4 line")
    #     server.close()
    #     print('Email sent!')
    # except:
    #     print('Something went wrong')
# import smtplib


# def create_email(body_text, emails):
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login("cmsc435digest@gmail.com", "57a72P98YJF3vxR")
#     server.sendmail("cmsc435digest@gmail.com", "racheltaskale@gmail.com", "hi, from python")
#     server.quit()
