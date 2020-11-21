from gpiozero import Button
from signal import pause

from picamera import PiCamera


def capture():
  print('Capturing picture...')
  camera = PiCamera()
  camera.resolution = (1024, 768)
  camera.capture('capture.jpg')
  print('Picture saved')




button = Button(2)

button.when_pressed = capture

pause()
