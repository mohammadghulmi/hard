import RPi.GPIO as GPIO
import sys
from gpiozero import LED
from time import sleep
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Hold a tag near the reader")

try:
    id, text = reader.read()
    print(id)
    print(text)
    if(id == "10"):
        led = LED(17)
        sleep(7)
        del led

finally:
    GPIO.cleanup()