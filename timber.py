import pyautogui
import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  

print("timber by os224 and klepek")

image_directory = os.path.join(os.path.expanduser("~"), "Images")
timbleft_path = os.path.join(image_directory, "timbleft.jpg")
timbright_path = os.path.join(image_directory, "timbright.jpg")





def timbright():
    try:
        return pyautogui.locateOnScreen(timbright_path, confidence=0.8, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False

def timbleft():
    try:
        return pyautogui.locateOnScreen(timbleft_path, confidence=0.85, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False





def main_loop():
    while True:
        if timbright():  
            print("Wykryto timbright =  a")
            pyautogui.rightClick()
            time.sleep(1)  
        if timbleft():  
            print("Wykryto timbleft = d")
            pyautogui.leftClick()
            time.sleep(1)  


if __name__ == "__main__":
    print("Startuję główną pętlę...")
    main_loop()