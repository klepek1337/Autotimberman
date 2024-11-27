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
timbright_path = os.path.join(image_directory, "timbright.png")
timbright2_path = os.path.join(image_directory, "timbright2.png")
timbleft2_path = os.path.join(image_directory, "timbleft2.png")





def timbright():
    try:
        return pyautogui.locateOnScreen(timbright_path, confidence=0.75, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False

def timbleft():
    try:
        return pyautogui.locateOnScreen(timbleft_path, confidence=0.75, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False
    
def timbright2():
    try:
        return pyautogui.locateOnScreen(timbright2_path, confidence=0.75, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False
    
def timbleft2():
    try:
        return pyautogui.locateOnScreen(timbleft2_path, confidence=0.75, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False







def main_loop():
    while True:
        if timbright():  
            print(" =  d")
            pyautogui.leftClick()
            time.sleep(0.3)  
        if timbleft():  
            print("a")
            pyautogui.rightClick()
            time.sleep(0.3)  
        if timbright2():
            print("b")
            pyautogui.leftClick()
            time.sleep(0.3) 
        if timbleft2():
            print("b")
            pyautogui.rightClick()
            time.sleep(0.3) 



if __name__ == "__main__":
    print("Startuję główną pętlę...")
    main_loop()
