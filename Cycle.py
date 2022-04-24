import time
import os

cwd = os.getcwd()

#- Configuration -

#Do not include "/" at end
path = "%s/Images" % cwd #Directory images are loaded from
inky_path = "/home/pi/Pimoroni/inky" #Directory of inky HAT repository

wait_time = 5 #Time delay in seconds
clear_inbetween = 1

#- Configuration -

images = list()

for x in os.listdir(path):
    if x.endswith(".png"):
        images.insert(1, x)

#If no images are found, do not start the program
if (len(images) < 1):
    print("No images found, cannot start.")
    quit()

print("%s Images detected in %s" % (len(images), str(path)))
print(str(images))

current_image = 0

#Wait for display to catch up
time.sleep(1)

print("\nStarting slideshow of %s images with %s second(s) delay" % (len(images), str(wait_time)))

#FUNCTIONS
def get_path():
    return "%s/%s" % (path, str(images[current_image]))

def inky_print(image_path):
    os.system("python3 %s/examples/7color/image.py %s" % (inky_path, image_path))
    time.sleep(0.1)
#FUNCTIONS

while True:
    try:
        
        #Print the current image
        print("\nPrinting image %s (%s)" % (images[current_image], get_path()))
        
        if (clear_inbetween == 1):
            inky_print("%s/white.png" % cwd)
        
        try:
            inky_print(get_path())
        except OSERROR as error :
            print("\n[Printing Failed]")
            print(error)
        
        #Get the next image
        current_image += 1
        
        if ((current_image) > (len(images) - 1)):
            print("\nNext image out of range; Reseting index")
            current_image = 0
        
        print("\nNext image will be %s (%s)" % (images[current_image], get_path()))
        print("Waiting %s seconds..." % str(wait_time))
        
        time.sleep(wait_time)
        
    except KeyboardInterrupt:
        print("")
        print("Keyboard Interrupt Detected")
        print("Exiting...")
        
        quit()