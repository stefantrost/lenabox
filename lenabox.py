import RPi.GPIO as GPIO
import time, sys, subprocess

GPIO.setmode(GPIO.BCM)
btn_to_led = dict([(14, 11), (15, 9), (23, 10), (24, 22), (25, 27)])

def led_toggle(pin):
    all_led_off()
    LED = btn_to_led[pin] 
    GPIO.output(LED, not GPIO.input(LED))

def all_led_off():
    for l in [11, 9, 10, 22, 27]:
        GPIO.output(l, False)    

def init_device():
    init_button_gpio()
    subprocess.call(["spotify_player", "-d"])
    subprocess.call(["spotify_player", "connect", "-n", "LenaBox"])
    subprocess.call(["spotify_player", "playback", "volume", "55"])
    all_led_off()

def init_button_gpio():
# playlist buttons
    for k, v in btn_to_led.items():
        GPIO.setup(k, GPIO.IN)
        GPIO.setup(v, GPIO.OUT)
        GPIO.add_event_detect(k, GPIO.FALLING, bouncetime=500)
        GPIO.add_event_callback(k, led_toggle)

# prev button
# play pause button
# next button
# vol down button
# vol up button

try:
    print("starting up")
    init_device() 
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    print("cleaning up and exiting")
    GPIO.cleanup()
    sys.exit()

# subprocess.call(["spotify_player", "playback", "volume", "55"])
