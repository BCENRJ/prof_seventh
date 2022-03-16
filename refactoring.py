import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login, password, gmail_smtp='smtp.gmail.com', gmail_imap='imap.gmail.com'):
        self.login = login
        self.password = password
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap

    def send_msg(self, recipients: list, subject: str, message_text: str):
        msg = MIMEMultipart()
        msg['From'], msg['To'] = self.login, ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text))
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, msg['To'], msg.as_string())
        ms.quit()

    def receive_msg(self, header):
        mail = imaplib.IMAP4_SSL(self.gmail_imap, 993)
        mail.login(self.login, self.password)
        mail.list()
        mail.select('inbox')
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.search(None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        print(email_message)
        mail.close()
        mail.logout()


if __name__ == '__main__':
    obj = Email('login@gmail.com', 'qwerty')
    obj.send_msg(recipients=['vasya@email.com', 'petya@email.com'], subject='Subject', message_text='Message')
    obj.receive_msg(header=None)
