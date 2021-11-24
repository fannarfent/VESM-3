import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import PWMLED

reader = SimpleMFRC522()
led = PWMLED(17)
led1 = PWMLED(19)
try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        led.value = 1
        led1.value = 0
        print("Written")
finally:
        GPIO.cleanup()
        led.value = 0
        led1.value = 1