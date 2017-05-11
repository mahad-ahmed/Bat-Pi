import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)
 
# GPIO_TRIGGER = 18
# GPIO_ECHO = 24
 
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 6666))
        
while True:
    try:
        GPIO.output(18, True)
        time.sleep(0.00001)
        GPIO.output(18, False)

        StartTime = time.time()
        StopTime = time.time()
     
        while GPIO.input(24) == 0:
            StartTime = time.time()
     
        while GPIO.input(24) == 1:
            StopTime = time.time()
     
        TimeElapsed = StopTime - StartTime
        # distance = (TimeElapsed * 34300) / 2
        distance = (TimeElapsed * 34029) / 2
        # print("Distance: "+str(distance))
        n = sock.send(str(distance))
    
    except:
        print "Bye"
        GPIO.cleanup()
        sock.close()
        break
