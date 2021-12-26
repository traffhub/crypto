import imapclient
import email
import re
# from tech_files.locators import VerificationMail
import base64
from bs4 import BeautifulSoup
import requests,traceback,time


class MailConfirm:
    def __init__(self,mail,password_secret):
        self.imap = 'imap.rambler.ru'
        self.criteria_FROM = 'noreply@discord.com'
        self.criteria_SUBJECT = 'Подтвердите свой e-mail в Discord'
        self.criteria_BODY = 'Спасибо за регистрацию'
        self.mail_criteria = [
            'FROM', self.criteria_FROM
        ]
        self.mail = mail
        self.password = password_secret

    def open_connection(self):
        # print('open_connection')
        try:
            # print('Login On mail Server...')
            self.server = imapclient.IMAPClient(self.imap) # i is easy to type
            self.server.login(self.mail, self.password)
        except(imapclient.exceptions.LoginError):
            print('Login Error. Change credentials!!!')
            raise AssertionError("Login Error. Dead Mail or Wrong Mail/Pass!!!...")
        # print('Successful Entrance...')
        # print('Looking For A Letter...')
        # try:

    def mail_should_be_in_inbox(self):
        try:
            self.server.select_folder('INBOX')
            inbox  = self.server.select_folder('INBOX')
            # print('%d messages in INBOX' % inbox[b'EXISTS'])
            self.mails = self.server.search(self.mail_criteria)
            # print(self.mails)
            # print(len(self.mails))
            assert len(self.mails)>0, '0 Mail Was Found. Resend the letter!!!'
        except AssertionError:
            print('0 Mail Was Found. Resend Letter')
            return False
        # print("%d messages from our best friend" % len(self.mails))
        return True

    def fetch_mail(self):
        for uid, message_data in self.server.fetch(self.mails, 'RFC822').items():
            self.email_message = email.message_from_bytes(message_data[b'RFC822'])
            # print(uid, self.email_message.get('From'), self.email_message.get('Subject'))

    def get_first_text_block(self):
        type = self.email_message.get_content_maintype()
        if type == 'multipart':
            for part in self.email_message.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload(decode=True)
        elif type == 'text':
            return self.email_message.get_payload()

    def get_mail_html(self):
        text = self.get_first_text_block()
        # base64_bytes = text.encode('ascii')
        # message_bytes = base64.b64decode(base64_bytes)
        message = text.decode('utf-8')
        # soup = BeautifulSoup(message, 'html.parser')
        # soup = soup.select('td')
        self.code = message.split(' ')[-1].replace('\r\n\r\n','')
        # print(self.code)
        return self.code

    def get_code(self):
        self.open_connection()
        if self.mail_should_be_in_inbox():
            self.fetch_mail()
            self.get_first_text_block()
            self.get_mail_html()
            print('Your Code is:   ', self.code)
            return self.code
        else:
            return None

    def check_connection(self):
        try:
            self.open_connection()
            return True
        except AssertionError:
            return False

# mail = MailConfirm('ksnraven@rambler.ru','x0fb8X70lhr')
# mail.get_code()