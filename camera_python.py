import sys
from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
timestamp = str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")
filename = '/home/pi/touch-screen-pi-sonos-app-experimental/images/'+timestamp+"_"+sys.argv[1]+'_image.jpg'

print(filename)
camera.capture(filename)