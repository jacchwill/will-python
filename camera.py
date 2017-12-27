import picamera,time
camera = picamera.PiCamera()
camera.resolution = (1024, 768)

camera.start_preview()
time.sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
