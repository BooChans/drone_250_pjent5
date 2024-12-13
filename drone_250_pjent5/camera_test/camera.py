from picamera import PiCamera, Color
from time import sleep


camera = PiCamera()
camera.rotation = 180

times = True

def onePhoto():
    camera.start_preview()
    sleep(4)
    camera.capture('/home/srituhobby/Desktop/image.jpg')#change location
    camera.stop_preview()
    
def multiPhoto():
    camera.start_preview()
    for i in range(3):
        sleep(4)
        camera.capture('/home/srituhobby/Desktop/images%s.jpg'% i)#change location
    camera.stop_preview()

def video():
    camera.start_preview()
    camera.start_recording('/home/srituhobby/Desktop/video.h264')#change location
    sleep(6)
    camera.stop_recording()
    camera.stop_preview()
    
def modifyPhoto():
    camera.resolution = (800,800) #Max = 2592,1944 / Min = 64,64
    camera.framerate = 15
    camera.start_preview()
    camera.image_effect = 'oilpaint' #none,negative,solarize,sketch,denoise,emboss,oilpaint,hatch,gpen,pastel,watercolor ...
    camera.exposure_mode = 'snow' # off,auto,night, nightpreview, backlight, spotlight, sports, snow , beach , verylong ...
    camera.awb_mode = 'shade' # off, auto , sunlight , cloudy,shade,tungsten,fluorescent,incandescent,flash,horizon
    camera.brightness = 80 # 0 - 100
    camera.contrast = 50 # 0 - 100
    camera.annotate_background = Color('red')
    camera.annotate_foreground = Color('white')
    camera.annotate_text = "SriTu Hobby"
    camera.annotate_text_size = 50
    sleep(4)
    camera.capture('/home/srituhobby/Desktop/imagems.jpg')#change location
    camera.stop_preview()

    
    
while times:   
#    onePhoto()
#    multiPhoto()
#    video()
#    modifyPhoto()
    times = False