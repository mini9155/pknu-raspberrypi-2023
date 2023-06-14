import Adafruit_DHT as dht
import time

sensor = dht.DHT11
rcv_pin = 10

try:
    while True:
        humid, temp = dht.read_retry(sensor, rcv_pin)
        print(f'온도 : {temp}C / 습도 : {humid}%')
except Exception as ex:
    print(ex)
finally:
    print('프로그램 종료')