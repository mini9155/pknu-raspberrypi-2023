# MQTT 패키지 설치 - paho-mqtt
# sudo pip install paho-mqtt
## 동시에 publish(데이터를 전송[출판]) / subscribe(데이터 수신[구독]) 처리

from threading import Thread, Timer
import time
import json
import datetime as dt
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import Adafruit_DHT as dht

# GPIO, DHT 설정
sensor = dht.DHT11
rcv_pin = 10
green = 22
servo_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3)

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
    def __init__(self):
        Thread.__init__(self)
        self.host = '210.119.12.67'
        self.port = 1883
        self.clientId = 'IOT67_SUB'
        self.topic = 'pknu/monitor/control'
        print('subscrib 스레드 시작')
        self.client = mqtt.Client(client_id=self.clientId)

    def run(self):
        self.client.on_connect = self.onConnect # 접속 성공 시그널 처리
        self.client.on_message = self.onMessage # 접속 후 메세지 수신되면 처리
        self.client.connect(self.host, self.port)
        self.client.subscribe(topic=self.topic)
        self.client.loop_forever()

    def onConnect(self, mqttc, obj, flags, rc):
        print(f'subscriber 연결됨 rc > {rc}')

    def onMessage(self, mqttc, obj, msg):
        rcv_msg = str(msg.payload.decode('utf-8'))
        print(f'{msg.topic} / {rcv_msg}')
        data = json.loads(rcv_msg)
        stat = data['STAT']
        print(f'현재 STAT : {stat}')
        time.sleep(1.0)
        if(stat == )
 
if __name__ == '__main__':
    thPub = publisher()
    thSub = subscriber()
    thPub.start() # run()이 자동으로 실행
    thSub.start()