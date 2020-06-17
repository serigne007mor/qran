from ics import Calendar, Event
from flask import Flask, render_template, request
from flask.helpers import send_file, send_from_directory, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import os
import datetime
import utils
from werkzeug.utils import redirect
app = Flask(__name__)

def sendemail(receiver, calendar):
    COMMASPACE = ', '
    def main():
        sender = 'tourefamily161@gmail.com'
        gmail_password = 'Be@tslapsit090400'
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

result = open("templates/surahList.html", "w")
result.write("")
result = open("templates/prediction.html", "w")
result.write("")

@app.route("/")
def main():
    result = open("templates/surahList.html", "w")
    result.write("")
    result = open("templates/prediction.html", "w")
    result.write("")
    print("HEEERRRREEEE")
    return render_template("index.html")

@app.route("/", methods=["POST"])
def surah():
    result = open("templates/surahList.html", "w")
    result.write(utils.getHeader())
    beginDateForm = request.form['beginDate']
    endDateForm = request.form['endDate']
    precision = int(request.form['precision'])
    email = request.form['email']
    beginSurah = int(request.form['beginSurah'])
    endSurah = int(request.form['endSurah'])
    beginDateForm = beginDateForm.split("-")
    endDateForm = endDateForm.split("-")
    beginDate = datetime.date(int(beginDateForm[0]), int(beginDateForm[1]), int(beginDateForm[2]))
    endDate = datetime.date(int(endDateForm[0]), int(endDateForm[1]), int(endDateForm[2]))
    numberOfDays = utils.diff_dates(beginDate, endDate)
    returnValue = utils.getDaysPages(numberOfDays, beginSurah, endSurah, precision)
    dailyPageGoal = returnValue[0]
    surahFinishDay = returnValue[1]
    chaptersToLearn = returnValue[2]
    c = Calendar()
    result.write("<script type=\"text/javascript\">alert(\"Your calendar was sent to "+email+" \");</script>  ")
    result.write("<h2> You will have to learn "+str(dailyPageGoal)+" pages per day</h2>\n")
    for i in reversed(chaptersToLearn):
        finishDay =  beginDate+ datetime.timedelta(days=surahFinishDay[i.name])
        result.write("<p>"+i.name+ " Will be done on "+str(finishDay)+"</p>")
        e = Event()
        e.name = "Finish "  + i.name
        e.begin = str(finishDay)+" 00:00:00"
        c.events.add(e)
        c.events

    with open('calendar.ics', 'w') as f:
        f.write(str(c))
    ics = '/Users/serigne/Desktop/dev/project/python/qran/calendar.ics'
    sendemail(email, ics)
    os.remove(ics)
    # os.remove(txt)
    return redirect(url_for('surahList'))
    # return render_template("index.html")


@app.route("/surahList")
def surahListMain():
    # result.write("<script type=\"text/javascript\">alert(\"Your calendar was sent to your email\");</script>  ")
    return render_template("surahList.html")

@app.route("/surahList", methods=["POST"])
def surahList():
    return redirect(url_for('main'))
    # return render_template("surahLists.html")






@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/result")
def predictionResult():
    return render_template("when.html")

@app.route("/prediction", methods=["POST"])
def prediction2():
    currentSurah = request.form['currentSurah']
    numAyah = int(request.form['numAyah'])
    result = open("templates/when.html", "w")
    x = datetime.date.today
    result.write("<script type=\"text/javascript\">alert(\"Data received\");</script>  ")
    return redirect(url_for('p2'))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
