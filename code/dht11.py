#!/usr/bin/python
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

while 1:
        time.sleep(1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
                        print('Temp={0:0.1f}*C  Feuchtigkeit={1:0.1f}%'.format(temperature, humidity))
        else:
                        print('Fehler beim Einlesen der Daten. Starte einen weiteren Versuch!')
