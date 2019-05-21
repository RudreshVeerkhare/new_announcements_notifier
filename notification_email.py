import smtplib, ssl
import requests
import os
import datetime
from bs4 import BeautifulSoup as bs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(SUBJECT, BODY, TO, FROM):
    """ function to send email with html"""

    # Create message container here
    MESSAGE = MIMEMultipart("alternative")
    MESSAGE["subject"] = SUBJECT
    MESSAGE["to"] = TO
    MESSAGE["from"] = FROM

    # Record MIME type text/html
    HTML_BODY = MIMEText(BODY, "html")

    MESSAGE.attach(HTML_BODY)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(FROM, password)
        server.sendmail(FROM, [TO], MESSAGE.as_string())


def check_notification(notifications, email_content):
    # fetch top notification
    latest_notification = list(notifications[0].children)[1]
    content = None

    # checking for existince of file
    if not os.path.exists(".notifications"):
        with open("/home/rudresh/Desktop/Web_scrapping/.notifications", "w") as f:
            f.write(latest_notification.text)
        return

    with open("/home/rudresh/Desktop/Web_scrapping/.notifications", "r") as f:
        content = f.read()

    if content != latest_notification.text:
        for i in range(5):
            email_content += f"\n{str(list(notifications[i].children)[1])}"

        email_content += "\n<p style='font-size: larger;font-weight: 900;'>Will notify you when new notifications are available</p>"
        with open("/home/rudresh/Desktop/Web_scrapping/log.txt", "a+") as f:
            for i in receiver:
                try:
                    send_mail(latest_notification.text, email_content, i, sender)
                    f.write(f"{i} : Email Sent {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                except:
                    f.write(
                        f"{i} : Failed to send {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    )
        with open("/home/rudresh/Desktop/Web_scrapping/.notifications", "w") as f:
            f.write(latest_notification.text)


if __name__ == "__main__":
    port = 465
    sender = "chhayavirkhare@gmail.com"
    receiver = [
        "veerkharerudresh@gmail.com",
        "saitarun.yellamraju@gmail.com",
        "jitensidhpura2000@gmail.com",
    ]
    password = "9421741623"
    context = ssl.create_default_context()
    success = True
    now = datetime.datetime.now()
    try:
        r = requests.get("https://www.spit.ac.in/news-events")
        soup = bs(r.content, "html.parser")

        notifications = soup.find_all("div", class_="post-heading")

        email_content = "<style>font-family: monospace !important;</style><p style='font-size: larger;font-weight: 900;'>You have new announcements wating...</p><br>"

        check_notification(notifications, email_content)
    except:
        success = False

    with open("/home/rudresh/Desktop/Web_scrapping/log.txt", "a+") as f:
        f.write(
            f"Execution {'Success' if success else 'Failed'} {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

