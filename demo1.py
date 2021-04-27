from gtts import gTTS
import playsound

text = open('demo.txt', 'r').read()

language='en'
output = gTTS(text=text, lang=language, slow=False)
output.save('fileoutput.mp3')

# wait for the sound to finish playing?
blocking = True

playsound.playsound("fileoutput.mp3", block=blocking)