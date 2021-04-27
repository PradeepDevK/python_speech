from gtts import gTTS
# import os
import playsound

text = "LOL this is real funny"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')

# os.system("afplay output.mp3")
# wait for the sound to finish playing?
blocking = True

playsound.playsound("output.mp3", block=blocking)