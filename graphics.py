import tkinter
from PIL import ImageTk, Image


def loadImage(window, image):
    return ImageTk.PhotoImage(Image.open(image))