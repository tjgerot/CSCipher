import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *
import tkMessageBox

# Setup application interface
app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

# Create the funtions to call from the GUI
def callback():
    string = labelText.get()
    tkMessageBox.showinfo("Caesar Cipher finished",caesar(string))

def beenClicked():
    cipherType = relStatus.get()
    print cipherType

# Make and put the buttons on a grid on the window
# Start with the textBox and Submit Button
labelText = StringVar(None)
textEntry = Entry(app, width=57, justify=CENTER, textvariable=labelText).grid(row=1, columnspan=4)
submitButton = Button(app, text="Start", width=10, command=callback).grid(row=1, column=4)
# Then put down the options for what cipher to use
relStatus = StringVar().set(None)
radiobutton = Radiobutton(app, text="Caesar", value="Caesar", variable=relStatus, command=beenClicked).grid(row=2, column=1)
radiobutton = Radiobutton(app, text="Vigenere", value="Vigenere", variable=relStatus, command=beenClicked).grid(row=2, column=2)
radiobutton = Radiobutton(app, text="Baconian", value="Baconian", variable=relStatus, command=beenClicked).grid(row=2, column=3)
radiobutton = Radiobutton(app, text="Morse", value="Morse", variable=relStatus, command=beenClicked).grid(row=2, column=4)
radiobutton = Radiobutton(app, text="Auto", value="Auto", variable=relStatus, command=beenClicked).grid(row=2, column=5)


# Start the application
app.mainloop()
