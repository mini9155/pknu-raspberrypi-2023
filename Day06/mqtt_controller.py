# MQTT 패키지 설치 - paho-mqtt
# sudo pip install paho-mqtt
## 동시에 publish(데이터를 전송[출판]) / subscribe(데이터 수신[구독]) 처리

from threading import Thread, Timer
import time
import json
import datetime as dt

import paho.mqtt.client as mqtt
import Adafruit_DHT as dht

sensor = dht.DHT11
rcv_pin = 10

class publisher(Thread):
    def __init__(self):
        Thread.__init__(self) # 스레드 초기화
        self.host = '210.119.12.67' # 본인 pc ip
        self.port = 1883
        self.clientId = 'IOT67'
        print('publisher 스레드 시작')
        self.client = mqtt.Client(client_id= self.clientId)

    def run(self):
        self.client.connect(self.host, self.port)
        self.publish_data_auto()

    def publish_data_auto(self):
        humid, temp = dht.read_retry(sensor, rcv_pin)
        curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        orign_data = { 'DEV_ID' : self.clientId, 'CURR_DT' : curr, 'Type' : 'TEMPHUMID', 'STAT' : f'{temp}|{humid}' }
        pub_data = json.dumps(orign_data)
        self.client.publish(topic='pknu/rpi/control/', payload=pub_data)
        print('Data published')
        Timer(2.0, self.publish_data_auto).start() # 2초마다 출판

class subscriber(Thread):
    pass

if __name__ == '__main__':
    thPub = publisher()
    thSub = subscriber()
    thPub.start() # run()이 자동으로 실행