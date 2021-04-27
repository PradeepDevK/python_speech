from gtts import gTTS
import playsound
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def textToSpeech():
    text = entry.get()
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output1.mp3')

    # wait for the sound to finish playing?
    blocking = True

    playsound.playsound("output1.mp3", block=blocking)

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 230, window=button)



root.mainloop()