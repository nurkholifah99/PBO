from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Datang di Fakultas Teknik! Namaku Nurkholifah dari Teknik Informatika'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("selamatdatang.mp3") 
playsound("selamatdatang.mp3", True)