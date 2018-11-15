import datetime
import os
from picamera import PiCamera 
from gpiozero import MotionSensor, LED, Button
from signal import pause

def video_on(time):
    infredLEDs.on()
    now = datetime.datetime.now()
    if camera.recording == False:
        print("video on")
        camera.start_recording(os.path.expanduser('~/video/') + now.strftime('%Y-%m-%dT%H:%M:%S') + '.h264')
    else: 
        print("Still motion")
    camera.wait_recording(time)
    

def video_off():
    if camera.recording == True:
        print("video off")
        camera.stop_recording()
        infredLEDs.off()

def motion_not_detected_handler():
    video_off()

def motion_detection_handler():
    print("motion detected")
    video_on(120)

def switch_hold_handler():
    print("switch off, exiting")
    onLED.off()
    exit()


if __name__== "__main__":
    print("starting")
    infredLEDs = LED(5)
    onLED = LED(24)
    onLED.on()
    switch = Button(10)
    switch.when_held = switch_hold_handler
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    pir = MotionSensor(25)
    pir.when_motion = motion_detection_handler
    pir.when_no_motion = motion_not_detected_handler
    pause()
