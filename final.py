import RPi.GPIO as GPIO
import time
import pygame
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig1 = 23
echo1 = 24

trig2 = 17
echo2 = 27

playlist = ["blackpink-playing with fire.ogg","miso-take me.ogg","kim chungha-gotta go.ogg"]
max = 2
x = 0
# print ("Distance measurement in progress")

GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(echo2,GPIO.IN)

def songchangepos():
  pygame.mixer.init()
  global x
  if x == max:
    x = 0
  pygame.mixer.music.load(playlist[x])
  x+=1
  pygame.mixer.music.play()
  # while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(1)
  # y = input()
  # if y == 'n':
  #   pygame.mixer.music.stop()

def songchangeneg():
  pygame.mixer.init()
  global x
  if x == -1:
    x = max-1
  pygame.mixer.music.load(playlist[x])
  x-=1
  pygame.mixer.music.play()
  pygame.time.Clock().tick(1)

time1 = 0
time2 = 0

songchangepos();

while True:
  GPIO.output(trig1,True)
  time.sleep(0.00001)
  GPIO.output(trig1,False)

  while GPIO.input(echo1) == 0:
    pass
  pulse_start = time.time()

  while GPIO.input(echo1) == 1:
    pass
  pulse_end = time.time()

  dur = pulse_end - pulse_start

  dist = 17150*dur

  if dist < 10:
    time1 = time.time()

  GPIO.output(trig2,True)
  time.sleep(0.00001)
  GPIO.output(trig2,False)

  while GPIO.input(echo2) == 0:
    pass
  pulse_start = time.time()

  while GPIO.input(echo2) == 1:
    pass
  pulse_end = time.time()

  dur = pulse_end - pulse_start

  dist = 17150*dur

  if dist < 10:
    time2 = time.time();

  if time1 - time2 < 2 and time1 - time2 > 0:
    songchangeneg()

  elif time2 - time1 < 2 and time2 - time1 > 0:
    songchangepos()

GPIO.cleanup()

