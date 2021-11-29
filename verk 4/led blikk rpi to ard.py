import serial
from gpiozero import LED
import time
from time import sleep

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):
    led = LED(pin)
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    

        

    
  
    return
while True:
        read_ser=ser.readline()
        msg = bytes.decode(read_ser)   # To convert byte strings to Unicode, líka hægt að nota bytes.decode(read_ser)
        print(msg) 
        if(msg.strip()=="Hello From Arduino!"):
            blink(17)