import RPi.GPIO as GPIO
import time
import Adafruit_DHT


class codSenRasp:
    def ultrasonico(self,tigger,echo):
        a=0
        GPIO.setmode(GPIO.BOARD)
        TRIG = int(tigger)
        ECHO = int(echo)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        # Esperar un corto tiempo para que se estabilice el sensor
        GPIO.output(TRIG, False)
        time.sleep(0.5)

        # Envío del pulso
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Lectura del pulso de retorno
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Cálculo de la distancia
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # Impresión del resultado
        #print("Distancia:", distance, "cm")


        # Liberar pines GPIO
        GPIO.cleanup()
        return distance


    def temperatura(self,pn):
        # Configuración del sensor
        sensor = Adafruit_DHT.DHT11
        pin = pn

        # Lectura de la temperatura
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Impresión del resultado
        if humidity is not None and temperature is not None:
            print('Temperatura={0:0.1f}°C'.format(temperature))
        else:
            print('No se pudo obtener la lectura del sensor.')



