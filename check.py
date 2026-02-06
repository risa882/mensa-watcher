import requests
import smtplib
from email.mime.text import MIMEText

URL = "https://mensa.jp/exam/"

def check_mensa():
    html = requests.get(URL, timeout=10).text
    return 'exam/index/notice' in html

def send_mail():
    msg = MIMEText("Mensa試験が募集開始しました！\n\nhttps://mensa.jp/exam/")
    msg["Subject"] = "【通知】Mensa試験が募集開始"
    msg["From"] = "YOUR_GMAIL_ADDRESS"
    msg["To"] = "YOUR_GMAIL_ADDRESS"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("YOUR_GMAIL_ADDRESS", "YOUR_APP_PASSWORD")
        smtp.send_message(msg)

if __name__ == "__main__":
    if check_mensa():
        send_mail()
