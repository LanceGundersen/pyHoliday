import CHIP_IO.GPIO as GPIO  # Import GPIO for controlling GPIO pins
# GPIO Setup

GPIO.setup("CSID0", GPIO.OUT)  # Set CSID0 as an output
GPIO.setup("CSID2", GPIO.IN)  # Set CSID2 as an input

# GPIO.output(light, GPIO.HIGH)
# playAudio('nuke-alarm.mp3')
# playAudio('nuke-alarm.mp3')
# GPIO.output(light, GPIO.LOW)
