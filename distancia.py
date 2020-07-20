import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ECHO = 29
TRIG = 31

def setup_sensor():
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG,GPIO.OUT)

def roda_medicao():
    global distancia_cm
    distancia_cm = 0
    while True:
        time.sleep(2)
        GPIO.output(TRIG,GPIO.HIGH)
        time.sleep (0.000010)
        GPIO.output(TRIG,GPIO.LOW)
        while GPIO.input(ECHO)== 0:
            pulso_inicial = time.time()
        while GPIO.input(ECHO)== 1:
            pulso_final = time.time()
        trigger = pulso_final - pulso_inicial
        distancia_cm = trigger * 17150
        distancia_cm = round(distancia_cm,0)
#        print (distancia_cm, 'cm   ',end="\r")

def get_distancia():
    return distancia_cm

#setup_sensor()
#roda_medicao()
