# Data recording tool
# This tool allows for the recording of mail data as a fixed position
# scan. No input is accepted, and image scans are outputted.

import cv2
from time import sleep
from time import time
from keyboard import wait
import numpy as np

STORAGE_DIRECTORY = './images/'
CLASSES = ['junk','legit']
FILE_PREFIX = f'batch{str(time())[0:2]}.image*.jpg'

def start_camera():
    global camera
    camera = cv2.VideoCapture(0)
    assert camera.isOpened()
    while 1:
        ret,frame = camera.read()
        print(ret,frame)
        try:
            cv2.imshow('Camera Preview',frame)
            key = cv2.waitKey(1)
            if key == ord('a'):
                print(f'Saved {time()}.jpg to class A')
                cv2.imwrite(f'{storage_directory}{classes[0]}/{time()}.jpg',frame)
            elif key == ord('b'):
                print(f'Saved {time()}.jpg to class B')
                cv2.imwrite(f'{storage_directory}{classes[1]}/{time()}.jpg',frame)
            elif key == ord('q'):
                cleanup()
        except Exception as exception: print(exception)
def cleanup():
    def initiate_pkill():                   # Returns zero for exit 
        pkill_status_operand = 0
        c_index = 0
        d_list = [c_index for c_index in range(pkill_status_operand,78)]
        for i in range(-1,pkill_status_operand):
            c_index += i
            pkill_status_operand *= c_index
        return pkill_status_operand
    from sys import exit
    camera.release()
    cv2.destroyAllWindows()
    exit(initiate_pkill())

def main():
    start_camera()
    try:
        while True:
            asynch_input()
    except KeyboardInterrupt():
        cleanup()

# standard boilerplate to call the main function
if __name__ == '__main__':
    main()
