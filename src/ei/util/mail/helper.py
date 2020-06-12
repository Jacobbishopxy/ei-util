"""
@author Jacob Xie
@time 12/10/2019
"""

import os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from typing import List


class EmailHelper(object):
    def __init__(self,
                 smtp_host: str,
                 smtp_port: int):
        self.host = smtp_host
        self.port = smtp_port
        self.sender = None
        self.sender_psw = None
        self.recipients = None

        self._smtp = smtplib.SMTP()
        self._num_image = 0
        self._num_attachment = 0
        self._title = None
        self._msg_content = []
        self._msg = None
        self._msg_cst = False

    def set_sender(self, user: str, password: str):
        self.sender = user
        self.sender_psw = password

    def set_recipients(self, recipients: List[str]):
        self.recipients = ','.join(recipients)

    def set_mail_title(self, title: str):
        self._title = title

    def _connect(self):
        self._smtp.connect(self.host, self.port)
        self._smtp.login(self.sender, self.sender_psw)
        self._msg.attach(MIMEText('</br>'.join(self._msg_content), 'html'))

    def _disconnect(self):
        self._smtp.quit()
        self._num_image = 0
        self._num_attachment = 0
        self._title = None
        self._msg = None
        self._msg_cst = False

    def _msg_constructor(self):
        self._msg = MIMEMultipart('related')
        self._msg['Subject'] = self._title
        self._msg['From'] = self.sender
        self._msg['To'] = self.recipients

    def send_mail(self):
        check_list = [self.sender, self.sender_psw, self.recipients, self._title]
        if any([i is None for i in check_list]):
            raise Exception('please check sender and recipients are set!')
        self._connect()
        self._smtp.sendmail(self.sender, self.recipients, self._msg.as_string())
        self._disconnect()

    def attach_text(self, txt: str):
        if not self._msg_cst:
            self._msg_cst = True
            self._msg_constructor()
        self._msg_content.append(f'<div>{txt}</div>')

    def attach_image(self, path: str):
        if not self._msg_cst:
            self._msg_cst = True
            self._msg_constructor()
        self._num_image += 1
        img_num = self._num_image
        self._msg_content.append(f'<img src="cid:image{img_num}">')
        with open(path, 'rb') as fp:
            img = MIMEImage(fp.read())
        img.add_header('Content-ID', f'<image{img_num}>')
        self._msg.attach(img)

    def attach_attachment(self, path: str, filename=None):
        if not self._msg_cst:
            self._msg_cst = True
            self._msg_constructor()
        self._num_attachment += 1
        with open(path, 'rb') as fp:
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(fp.read())
        encoders.encode_base64(att)
        fn = os.path.basename(path) if filename is None else filename
        att.add_header('Content-Disposition', 'attachment', filename=fn)
        self._msg.attach(att)


if __name__ == '__main__':
    _host, _port = 'c1.icoremail.net', 25
    _user, _psw = 'qi@jaspercapital.com', 'blLTmuD2BUhUTo5u'
    _recipients = [
        "jacob.xie@jasperam.com",
    ]

    helper = EmailHelper(_host, _port)
    helper.set_sender(_user, _psw)
    helper.set_recipients(_recipients)
    helper.set_mail_title('测试')

    helper.attach_text('测试1')
    helper.attach_image('./tmp/tst.png')
    helper.attach_text('测试2')
    helper.attach_text('测试3')
    helper.attach_attachment('./tmp/tst.png')

    helper.send_mail()
