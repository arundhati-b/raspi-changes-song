import RPi.GPIO as GPIO
import time
import pygame
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig1 = 21
echo1 = 20

trig2 = 17
echo2 = 27

playlist = ["blackpink-playing with fire.ogg","miso-take me.ogg","kim chungha-gotta go.ogg"]
maxi = 2
x = 0
# print ("Distance measurement in progress")

GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(echo2,GPIO.IN)

def songchangepos():
  pygame.mixer.init()
  global x
  if x > maxi:
    x = 0
  print(x,maxi)
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
  if x <= -1:
    x = maxi
  print(x,maxi)
  pygame.mixer.music.load(playlist[x])
  x-=1
  pygame.mixer.music.play()
  pygame.time.Clock().tick(1)

time1 = 0
time2 = 0
f = 0

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

  if (pulse_end - pulse_start)*17150 < 20:
    time1 = time.time()%10;
    dist1 = (pulse_end - pulse_start)*17150
#  print(dist1)

  GPIO.output(trig2,True)
  time.sleep(0.00001)
  GPIO.output(trig2,False)

  while GPIO.input(echo2) == 0:
    pass
  pulse_start = time.time()

  while GPIO.input(echo2) == 1:
    pass
  pulse_end = time.time()

  if (pulse_end - pulse_start)*17150 < 20:
    time2 = time.time()%10;
    dist2 = (pulse_end - pulse_start)*17150
#  print(dist2)
  timee = time1 - time2;
  timee *=20
  if timee < 40 and timee > 0 and time2 != 0:
    print(time1,time2)
    time1 = 0
    time2 = 0
    songchangeneg()
    time.sleep(0.005)

  elif timee > -40 and timee < 0 and time1!=0:
    print(time1,time2)
    time1 = 0
    time2 = 0
    songchangepos()
#    print("next playing")
    time.sleep(0.005)

GPIO.cleanup()


