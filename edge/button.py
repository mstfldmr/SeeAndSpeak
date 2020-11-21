from gpiozero import Button
from signal import pause

from picamera import PiCamera
from datetime import datetime



camera = PiCamera()
camera.resolution = (1024, 768)



def capture():
  print('Capturing picture...')
  now = datetime.now()
  timestamp = now.strftime('%Y%m%d%H%M%S')
  camera.capture(timestamp + '.jpg')
  print('Picture saved: ' + timestamp)




button = Button(2)

button.when_pressed = capture

pause()
