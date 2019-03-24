from PIL import Image
from google.cloud import storage
from google.cloud import vision
from gtts import gTTS
import os
import pygame
from visionHandler import VisionHandler
import time


#global variables
textList = []
i= 0

storage_client = storage.Client.from_service_account_json('Linguo-495a24a54222.json')


#textDraw font specification
fnt = ImageFont.truetype(font="Montserrat-Medium.otf", size=50)

# Make an authenticated API request
bucketslist = list(storage_client.list_buckets())
bucket = storage_client.get_bucket("storage_photos")
blobs = bucket.list_blobs()



#initiate visionHandler
vh = VisionHandler("Linguo-495a24a54222.json")



for blob in blobs:
    print(blob.name)
    filename = "blob" + str(x) + ".jpeg"
    blob.download_to_filename(filename)
    labelDict = vh.process_image(filename)
    for i in range(0,3):
         textList.append(labelDict[i].description)
        
    print(textList)
    base = Image.open(filename).convert('RGBA')
    break

    
    
# make a blank image for the text, initialized to transparent text color
txt = Image.new(base.mode, base.size, (255,255,255,0))

# get a drawing context
d = ImageDraw.Draw(txt)
width, height = base.size
shadowcolor = (255,255,255,300)
positionList = [(width/2, height/2), (width/2, (height/2) + 100), (width/2, (height/2) + 200)]

#d.ellipse((1, 1, 180, 180), fill = 'blue', outline ='blue')
for i in range(0, len(textList)):
    d.text(positionList[i], '{}'.format(textList[i]), font=fnt, fill=shadowcolor)
    
    
    
out = Image.alpha_composite(base, txt)
out.show()

    
# Language in which you want to convert 
language = 'pt-BR'
text = "meu nome é neel"
language = "en"


for i in range(0, len(textList)):
    myobj = gTTS(text=textList[i], lang=language, slow=False) 
    audioFile = "{}.mp3".format(textList[i])
    print(audioFile)
    
    #saving audiofile
    myobj.save(audioFile)
    
    #playing audiofile
    pygame.mixer.init()
    pygame.mixer.music.load(audioFile)
    pygame.mixer.music.play()
    time.sleep(.8)
    

