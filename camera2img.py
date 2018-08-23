import picamera
camera = picamera.PiCamera()
camera.resolution = (2592, 1944)
camera.capture('camera.jpg')

