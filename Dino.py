import pyautogui
from PIL import Image,  ImageGrab
import time

def takeScreenshot():

    return image
def hit(key):
    pyautogui.keyDown(key)
    return 

def iscollide(data):

    for i in range(690, 784):
            for j in range(335,360):
                if data[i, j] < 50:
                    hit('down')
                    return
    for i in range(680, 838):
            for j in range(380,410):
                if data[i, j] < 100:
                    hit('up')
                    return
    return False


if __name__ == "__main__":

    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
        

        
        # # for cactus
        # for i in range(685, 833):
        #     for j in range(370,410):
        #         data[i, j] = 0
        
        # # for bird
        # for i in range(690, 785):
        #     for j in range(325,360):
        #         data[i, j] = 71
        # image.show()

        # break
    
        
