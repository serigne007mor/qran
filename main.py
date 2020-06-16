from ics import Calendar, Event
from flask import Flask, render_template, request
from _datetime import date, timedelta
import utils
from flask.helpers import send_file, send_from_directory
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import os
app = Flask(__name__)

def sendemail(receiver, calendar):
    COMMASPACE = ', '
    def main():
        sender = 'mcrwv1990@gmail.com'
        gmail_password = 'Gelorsel1'
        recipients = [str(receiver)]

        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer['Subject'] = 'Your qran Calendar '
        outer['To'] = COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # List of attachments
        attachments = [str(calendar)]

        # Add the attachments to the message
        for file in attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        composed = outer.as_string()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            print("Unable to send the email. Error: ", sys.exc_info()[0])
            raise

    if __name__ == '__main__':
        main()



@app.route("/")
def main():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def Create():
    result = open("calendar.txt", "w")
    beginDateForm = request.form['beginDate']
    endDateForm = request.form['endDate']
    precision = request.form['precision']
    email = request.form['email']
    beginDateForm = beginDateForm.split("-")
    endDateForm = endDateForm.split("-")
    beginDate = date(int(beginDateForm[0]), int(beginDateForm[1]), int(beginDateForm[2]))
    endDate = date(int(endDateForm[0]), int(endDateForm[1]), int(endDateForm[2]))
    numberOfDays = utils.diff_dates(endDate, beginDate)
    returnValue = utils.getDaysPages(numberOfDays, 114, 1)
    dailyPageGoal = returnValue[0]
    surahFinishDay = returnValue[1]
    chaptersToLearn = returnValue[2]
    c = Calendar()
    for i in reversed(chaptersToLearn):
        finishDay =  beginDate+ timedelta(days=surahFinishDay[i.name])
        result.write(i.name+ " Will be done on "+str(finishDay)+"\n")
        e = Event()
        e.name = "Finish "  + i.name
        e.begin = str(finishDay)+" 00:00:00"
        c.events.add(e)
        c.events

    with open('calendar.ics', 'w') as f:
        f.write(str(c))
    ics = '/Users/serigne/Desktop/dev/project/python/qran/calendar.ics'
    # txt = '/Users/serigne/Desktop/dev/project/python/qran/calendar.txt'
    sendemail(email, ics)
    os.remove(ics)
    # os.remove(txt)
    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
