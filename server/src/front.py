from visionHandler import VisionHandler
from audioHandler import AudioHandler
from storageHandler import StorageHandler
from translationHandler import TranslationHandler
import tkinter as tk


r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 