# Capture_Screenshots
Captures screenshots repeatedly after taking some parameters like:

- Time to skip between two consecutive screenhots
- Name of folder where to save the images
- Prefix to add before each screenshot name. Can be handy in identifying screenshots later.


## Execution Process
- Clone or download the repository and install python3
- Install the libraries for python3 like:
```
pip install numpy pyautogui opencv-python imutils
```
- Execute "python3 capture.py"


## Usage
Just change the parameters according to your need and call the function. Sample coe is shown below:

```
sleep_interval=2  #time for waiting before taking another screenshot in seconds
folder="screenshots"  #saving the screenshots in this folder
prefix="image"  #prefix to add before the images name, can be handy in identifying screenshots of different classes

take_screenshot(sleep_interval, folder, prefix)  #call the function to capture screenshots. Can specifiy sleep interval and folder name here
```
Sample screenshots saved are present [here](https://github.com/AsimMessi/Capture_Screenshots/tree/master/screenshots)

## License
It is a free public tool for anyone to use :-)
