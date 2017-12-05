import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from modules import maildata
import xlrd
import json

def getemail(file):
    mail = list()
    for i in file:
        id = i.split('.')
        id = id[0]
        with open('./speakers.json') as data_file:
            data = json.load(data_file)

        for i in id:
            mail.append(data["speakers"][int(i)-1]["mail"])
    return mail

def sende(file):
    print(file)
    mail = getemail(file)
    for i in range(len(mail)):
        email = mail[i]
        filename = file[i]
        toaddr = email

        msg = MIMEMultipart()
        msg['From'] = maildata.fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Invitación Meetup TechWo"

        body = """\
        <html>
          <head></head>
          <body>"""

        with open('./modules/message', 'r') as mymessage:
            body += mymessage.read().replace('\n', '')

        body += """</body>
        </html>
        """

        msg.attach(MIMEText(body, 'html'))

        attachment = open("./static/invitations/" + filename, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)
        print(toaddr, filename)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(maildata.fromaddr, maildata.password)
        text = msg.as_string()
        server.sendmail(maildata.fromaddr, toaddr, text)
        server.quit()
