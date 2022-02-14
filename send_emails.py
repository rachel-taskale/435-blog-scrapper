import smtplib
from datetime import date


def format_email(body_text):
    final_body_text = ''
    i = 0
    for i in body_text[0]:
        date_txt = i[1:10]
        string_txt = i[11:len(i)]
        final_body_text += date_txt + '\n'
        final_body_text += string_txt + '\n'
        final_body_text += '\n'
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

    sent_from = gmail_user
    to = emails
    subject = 'CMSC435 Update on ' + date.today().strftime("%m-%d-%Y")
    body = format_email(body_text)
    print(body)

    email_text = """
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    # Send email to email list
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        print("going to login now")
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong')
