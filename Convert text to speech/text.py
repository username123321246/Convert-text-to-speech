

from tkinter import *
from gtts import gTTS

import os

root = Tk()

root.geometry("600x500")
root.title("Text to Speech Convertor")


def convert():

    language = "en"
    qwerty = gTTS(asdfg.get(), lang = language, slow = False)
    qwerty.save("Save.wav")
    os.system("Save.wav")



asd = Frame(root, bg = "Lightblue", height = 200)
asd.pack(fill = X)


asdf = Frame(root, bg = "Lightgrey", height = 300)
asdf.pack(fill = X)

frame1 = Label(root, text = "Text to Speech Convertor", font = "bold, 25", bg = "Lightblue")
frame1.place(x =120, y = 50)

asdfg = Entry(root, width = 40)
asdfg.place(x = 170, y = 250)

asdfgh = Button(root, text = "Convert", width = 20, font = "bold, 10", command = convert)
asdfgh.place(x = 210, y = 300)





root.mainloop()



