import os
import datetime
import time
import psutil
import smtplib


def readFile(fpath: str):
    with open(fpath, 'r') as f:
        content = f.readlines()
    return content


def get_current_weekday():
    return datetime.datetime.now().weekday()


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
        """.format(self.senderGmail, self.senderGmail, subject, text)

        server.sendmail(self.senderGmail, self.senderGmail, body)
        server.quit()


if __name__ == '__main__':
    FREQUENCY = 1

    m = Monitor()
    m.sendGmail(text="A monitor is setup to monitor your power supply. An email will be sent to this address when the power supply cuts off.", subject="Test Message")

    current_weekday = get_current_weekday()

    while True:
        power = psutil.sensors_battery()

        if not power.power_plugged:
            m.sendGmail(text=str(power), subject="Power Supply Lost")
            break
        
        if current_weekday is not get_current_weekday():
            current_weekday = get_current_weekday()
            m.sendGmail(text=str(power), subject="Daily Power Supply Update")

        print(str(power))
        time.sleep(FREQUENCY)

