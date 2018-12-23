import os
import smtplib


def readFile(fpath: str):
    with open(fpath, 'r') as f:
        content = f.readlines()
    return content


class Monitor():
    def __init__(self, config_path = os.path.expanduser('~/.monitorPower/config.yaml')):
        # Read config file
        config_content = readFile(config_path)

        # Put config content into dictionary
        config = dict()
        for line in config_content:
            key, info = line.split(':')
            config[key.strip()] = info.strip()

        # Sender Gmail
        self.senderGmail = config['user-email']

        # Sender Gmail Password
        self.senderPassword = config['user-password']

    def sendGmail(self, text: str, subject: str):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.senderGmail, self.senderPassword)

        body = """
        To: {}
        From: {}
        Subject: {}
        {}
        """.format(self.senderGmail, self.senderEmail, subject, text)

        server.sendmail(self.senderGmail, [self.senderEmail], body)
        print ('email sent')

if __name__ == '__main__':
    m = Monitor()
    m.sendGmail("Hi there. This is a test!", "Test Message")
