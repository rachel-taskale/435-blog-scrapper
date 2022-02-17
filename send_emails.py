import smtplib
from datetime import date, datetime
import markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from pytz import timezone


def format_email(body_text, url):
    final_body_text = ''
    i = 0
    final_body_text += markdown.markdown("##CMSC435 Blog Updates")
    final_body_text += markdown.markdown('***')
    for i in body_text[0]:
        date_txt = datetime.strptime(i[0:10], '%Y-%m-%d')
        date_string = date_txt.strftime("%m-%d-%Y")
        string_txt = i[11:len(i)]
        final_body_text += markdown.markdown('###' + date_string + '\n')
        final_body_text += markdown.markdown(string_txt + '\n')
        print(final_body_text)
        print(type(final_body_text))
        final_body_text += markdown.markdown('\n')
    final_body_text += markdown.markdown('***')
    final_body_text += markdown.markdown('**'+"Find the blog posts here: " + url + '**')

    return final_body_text


# Thank you, Patrick O'Toole :3
# Accepts file formatted in:
# Variable=value
# returns python dictionary
def load_creds(env_file):
    f = open(env_file)
    lines = f.readlines()
    env_vars = {}
    for line in lines:
        var = line.split("=")
        final = [elt.strip() for elt in var]
        env_vars[final[0]] = final[1]
    f.close()
    return env_vars


def create_email(body_text, emails):
    # open the env file and get credentials
    creds = load_creds(".env")
    # load values into variables
    gmail_user = creds["USERNAME"]
    gmail_password = creds["PASSWORD"]
    msg = EmailMessage()
    body = format_email(body_text, creds["URL"])

    multipart_msg = MIMEMultipart("alternative")
    est = timezone('EST')
    msg["SUBJECT"] = 'CMSC435 Update on ' + date.today().strftime("%m-%d-%Y") + " as of " + datetime.now(est).strftime("%I:%M:%S %p")
    msg["FROM"] = gmail_user
    msg["TO"] = emails
    html = markdown.markdown(body)
    main_txt = MIMEText(html, "html")
    multipart_msg.attach(main_txt)
    msg.set_content(main_txt)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        print("going to login now")
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong')
