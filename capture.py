import numpy as np
import pyautogui
import imutils
import cv2
import time
import os


def capture_ss(name):
    "Captures screenshot and writes to the given path"
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) #convert image to RGB format
    x=cv2.imwrite(name, image)
    

def take_screenshot(sleep_time=5,folder="screenshots",prefix="image"):
    "Takes screenshots periodically after the specified time and saves in the folder name given"
    print("Capturing screenshots now...")
    try:
        os.mkdir(folder)  #make the folder if it doesn't exist already
    except:
        pass
    base_path=os.getcwd()
    files=len(os.listdir(folder))  #num of files for naming the images
    full_path=base_path+"/"+folder+"/"+prefix+"_"   #concatenating the path together
    print(full_path)
    i=1
    while(True):
        capture_ss(full_path+str(files+i)+".png")
        time.sleep(sleep_time)
        

sleep_interval=2  #time for waiting before taking another screenshot in seconds
folder="screenshots"  #saving the screenshots in this folder
prefix="image"  #prefix to add before the images name, can be handy in identifying screenshots of different classes

take_screenshot(sleep_interval, folder, prefix)  #call the function to capture screenshots. Can specifiy sleep interval and folder name here