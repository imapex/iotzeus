from zeus import client
import random
import datetime
import os
import time

class ZeusAlert():
    """
    Sends alerts to a Cisco Zeus
    """

    def __init__(self):
        self.api = client.ZeusClient(os.environ("ZEUS_TOKEN"),
                                     os.environ("ZEUS_API_HOST"))
        self.log = os.getenv("ZEUS_KEY")
        self.key = os.getenv("ZEUS_KEY")

    def _send_to_zeus(self, msg):
        logs = [{self.key: msg
                 }]
        self.api.sendLog(self.log, logs)

    def trigger(self, alertdata):
        self._send_to_zeus(alertdata)



def main():

    zeus = ZeusAlert()
    while True:
        amstart = datetime.time(6)
        amend = datetime.time(9)
        lunchstart = datetime.time(11)
        lunchend = datetime.time(13)
        rushstart = datetime.time(17)
        rushend = datetime.time(18)
        timestamp = datetime.datetime.now().time()
        msg = "Car Passed".format(random.randint(1,4))
        if amstart <= timestamp <= amend:
            if random.randint(0,100) < 50:
                zeus.trigger(msg)
        elif lunchstart <= timestamp <= lunchend:
            if random.randint(0,100) < 70:
                zeus.trigger(msg)
        elif rushstart <= timestamp <= rushend:
            if random.randint(0,100) < 70:
                zeus.trigger(msg)
        else:
            if random.randint(0,100) < 20:
                zeus.trigger(msg)
        time.sleep(30)
