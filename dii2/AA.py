import time                   ##擷取螢幕
from PIL import ImageGrab
print("RD")
time.sleep(2)
print("Go")
ImageGrab.grab().save(".\C\picccc.png")

