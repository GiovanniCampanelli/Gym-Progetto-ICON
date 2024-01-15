import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image, ImageTk
import webbrowser
import os
from owlready2 import *
import requests
global pop
pop="1"
global nome
nome="1"
global owletto
owletto="0"
global giorno
giorno="1"
global legamenti
legamenti="1"
global preferenze
preferenze="1"
global difficolta
difficolta="1"
global pale
pale=0
global doman1
doman1=0
global doman2
doman2=0
global doman3
doman3=0
global doman4
doman4=0
global limiter
limiter=0
global limiter2
limiter2=0
global limiter3
limiter3=0
global limiter4
limiter4=0
global limiter5
limiter5=0
global limiter6
limiter6=0
global limiter7
limiter7=0
global limiter8
limiter8=0
global limiter9
limiter9=0
global limiter10
limiter10=0
global limiter11
limiter11=0
global limiter12
limiter12=0
global limiter13
limiter13=0
global limiter14
limiter14=0
global limiter15
limiter15=0
global limiter16
limiter16=0
global limiter17
limiter17=0
global limiter18
limiter18=0
global limiter19
limiter19=0
global limiter20
limiter20=0
global pettorali_easy
pettorali_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global dorsali_easy
dorsali_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global bicipiti_easy
bicipiti_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global tricipiti_easy
tricipiti_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global addominali_easy
addominali_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global lombari_easy
lombari_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global quadricipiti_easy
quadricipiti_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
global ischiocrurali_easy
ischiocrurali_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global glutei_easy
glutei_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global polpacci_easy
polpacci_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global pettorali_intermedio
pettorali_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global dorsali_intermedio
dorsali_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global bicipiti_intermedio
bicipiti_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global tricipiti_intermedio
tricipiti_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global addominali_intermedio
addominali_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global quadricipiti_intermedio
quadricipiti_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1",]
global glutei_intermedio
glutei_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global polpacci_intermedio
polpacci_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global addominali_avanzato
addominali_avanzato=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global quadricipiti_avanzato
quadricipiti_avanzato=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global spalle_easy
spalle_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global spalle_intermedio
spalle_intermedio=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global avambracci_easy
avambracci_easy=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global full
full=0
global full2
full2=0
global fullwork
fullwork=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]
global fullworkowl
fullworkowl=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1"]



global i
i=0
global j
j=0
global z
z=0

def reset_scrollbar():
    scrollbar.set(0.0, 0.0)

def on_configure(event):
    text_widget.yview_moveto(0.0)
def on_image_click(label):
    on_button_click2(label)

def on_image_click2(label):
    on_button_click3(label)

def on_button_click3(label):
    current_state = label_states[label]
    global doman1
    global doman2
    global doman3
    global doman4
    #labell = tk.Label
    if current_state == "not_pressed":
        label_states[label] = "pressed"
        label.config(image=Immagine2)

        try:
           if (label!=label_avamclick1):
            label_avamclick1.config(image=Immagine)
            label_states[label_avamclick1] = "not_pressed"
           else:
               pop = "CURL HAMMER AI CAVI CON CORDA"
               popup = tk.Toplevel(app)
               popup.overrideredirect(True)
               imagee = pop + ".png"
               # image_path = imagee
               # webbrowser.open(image_path)
               project_folder = os.path.dirname(os.path.abspath(__file__))

               # Specifica il percorso della cartella delle immagini
               images_folder = os.path.join(project_folder, "FotoPalestra")

               # Specifica il nome dell'immagine
               # image_name = "your_image.jpg"

               # Crea il percorso completo dell'immagine
               image_path = os.path.join(images_folder, imagee)
               image = Image.open(image_path)
               resized_image = image.resize((400, 400))
               photo = ImageTk.PhotoImage(resized_image)
               labell = tk.Label(popup, image=photo)
               labell.resized_image = photo
               labell.pack()
           if (label!=label_avamclick2):
            label_avamclick2.config(image=Immagine)
            label_states[label_avamclick2] = "not_pressed"
           else:
               pop = "CURL INVERSO BILANCIERE IN PIEDI"
               popup = tk.Toplevel(app)
               popup.overrideredirect(True)
               imagee = pop + ".png"
               # image_path = imagee
               # webbrowser.open(image_path)
               project_folder = os.path.dirname(os.path.abspath(__file__))

               # Specifica il percorso della cartella delle immagini
               images_folder = os.path.join(project_folder, "FotoPalestra")

               # Specifica il nome dell'immagine
               # image_name = "your_image.jpg"

               # Crea il percorso completo dell'immagine
               image_path = os.path.join(images_folder, imagee)
               image = Image.open(image_path)
               resized_image = image.resize((400, 400))
               photo = ImageTk.PhotoImage(resized_image)
               labell = tk.Label(popup, image=photo)
               labell.resized_image = photo
               labell.pack()
        except:
            i=0
        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickfull2[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickfull2[i]):
                    label_clickfull2[i].config(image=Immagine)
                    label_states[label_clickfull2[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=fullworkowl[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click[i]):
                    label_click[i].config(image=Immagine)
                    label_states[label_click[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=pettorali_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click2[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click2[i]):
                    label_click2[i].config(image=Immagine)
                    label_states[label_click2[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=dorsali_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0


        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click3[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click3[i]):
                    label_click3[i].config(image=Immagine)
                    label_states[label_click3[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=spalle_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click4[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click4[i]):
                    label_click4[i].config(image=Immagine)
                    label_states[label_click4[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=bicipiti_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click5[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click5[i]):
                    label_click5[i].config(image=Immagine)
                    label_states[label_click5[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=tricipiti_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click6[i]):
                    label_click6[i].config(image=Immagine)
                    label_states[label_click6[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=addominali_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click7[i]):
                    label_click7[i].config(image=Immagine)
                    label_states[label_click7[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=quadricipiti_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click8[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click8[i]):
                    label_click8[i].config(image=Immagine)
                    label_states[label_click8[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=glutei_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click9[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click9[i]):
                    label_click9[i].config(image=Immagine)
                    label_states[label_click9[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=polpacci_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_click10[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_click10[i]):
                    label_click10[i].config(image=Immagine)
                    label_states[label_click10[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=avambracci_easy[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk[i]):
                    label_clickk[i].config(image=Immagine)
                    label_states[label_clickk[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=pettorali_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    # Specifica il percorso della cartella delle immagini
                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    # Specifica il nome dell'immagine
                    #image_name = "your_image.jpg"

                    # Crea il percorso completo dell'immagine
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk2[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk2[i]):
                    label_clickk2[i].config(image=Immagine)
                    label_states[label_clickk2[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=dorsali_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0


        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk3[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk3[i]):
                    label_clickk3[i].config(image=Immagine)
                    label_states[label_clickk3[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=spalle_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))
                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk4[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk4[i]):
                    label_clickk4[i].config(image=Immagine)
                    label_states[label_clickk4[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=bicipiti_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))
                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk5[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk5[i]):
                    label_clickk5[i].config(image=Immagine)
                    label_states[label_clickk5[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=tricipiti_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))


                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk6[i]):
                    label_clickk6[i].config(image=Immagine)
                    label_states[label_clickk6[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=addominali_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))


                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk7[i]):
                    label_clickk7[i].config(image=Immagine)
                    label_states[label_clickk7[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=quadricipiti_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))


                    images_folder = os.path.join(project_folder, "FotoPalestra")

                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickk8[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickk8[i]):
                    label_clickk8[i].config(image=Immagine)
                    label_states[label_clickk8[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=glutei_intermedio[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))


                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickkk6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickkk6[i]):
                    label_clickkk6[i].config(image=Immagine)
                    label_states[label_clickkk6[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=addominali_avanzato[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))

                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickkk7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickkk7[i]):
                    label_clickkk7[i].config(image=Immagine)
                    label_states[label_clickkk7[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=quadricipiti_avanzato[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))
                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_clickfull[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_clickfull[i]):
                    label_clickfull[i].config(image=Immagine)
                    label_states[label_clickfull[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    pop=fullwork[i]
                    popup = tk.Toplevel(app)
                    popup.overrideredirect(True)
                    imagee = pop + ".png"
                    #image_path = imagee
                    # webbrowser.open(image_path)
                    project_folder = os.path.dirname(os.path.abspath(__file__))
                    images_folder = os.path.join(project_folder, "FotoPalestra")
                    image_path = os.path.join(images_folder, imagee)
                    image = Image.open(image_path)
                    resized_image = image.resize((400, 400))
                    photo = ImageTk.PhotoImage(resized_image)
                    labell = tk.Label(popup, image=photo)
                    labell.resized_image = photo
                    labell.pack()
               i = i + 1
        except:
            i=0

    else:
        label_states[label] = "not_pressed"
        label.config(image=Immagine)
        #labell.pack_forget()

def open_website(event):
    # Apre un sito web nel browser predefinito
    webbrowser.open("https://www.evolutionfit.it")
def show_image(event):
    global pop
    global i
    u=0
    popup = tk.Toplevel(app)
    popup.overrideredirect(True)  # Rimuove la barra del titolo della finestra popup
    #popup.geometry('+{}+{}'.format(event.x_root, event.y_root))
    if (label_eserc[u].y>0 and event.y<3):
        pop=pettorali_easy[1]
    if (event.y>4 and event.y<7):
        pop=pettorali_easy[2]
    if (event.y>8 and event.y<10):
        pop=pettorali_easy[3]
    if (event.y>11 and event.y<12):
        pop=pettorali_easy[4]
    if (event.y>13 and event.y<15):
        pop=pettorali_easy[5]
    #while(u<limiter):

    stringa=pop
    path = ".png"
    stringas = stringa.lower()
    stringas = stringas.replace(" ", "-")
    imagee = "https://www.evolutionfit.it/wp-content/uploads/"
    #if (full==0):
        #while(u<limiter):
          #if (event==label_eserc[u]):
              #pop=pettorali_easy
          #u=u+1
    print(popup)

    imagee = pop + path
    image_path = imagee
    #webbrowser.open(image_path)
    print(event)
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    labell = tk.Label(popup, image=photo)
    labell.image = photo
    q = 0
    while (q < limiter):
        if (labell.bind("<Motion>", show_image) == label_eserc[q].bind("<Motion>", show_image)):
            pop = pettorali_easy[q]
        else:
            q = q + 1
    labell.pack()

def hide_image(event):
    global i
    i=i
    #event.widget.pack_forget()

def on_button_click():
    label.config(text="Ciao " + entry.get() + ", dammi alcune info su di te per poter creare il tuo programma per la palestra")
    label.configure(bg="lightblue")
    global pale
    pale=1

def on_button_click2(label):
    label.configure(bg="lightblue")
    current_state = label_states[label]
    global doman1
    global doman2
    global doman3
    global doman4
    global nome
    global giorno
    global preferenze
    global legamenti
    global difficolta
    nome = entry.get()

    if current_state == "not_pressed":
        label_states[label] = "pressed"
        label.config(image=Check)
        try:
         if (label!=label_status1):
            label_status1.config(image=Uncheck)
            label_states[label_status1] = "not_pressed"
         else:
             doman1=1
             giorno="Un Giorno"
         if (label != label_status2):
            label_status2.config(image=Uncheck)
            label_states[label_status2] = "not_pressed"
         else:
             doman1=2
             giorno = "Due Giorni"
         if (label != label_status3):
            label_status3.config(image=Uncheck)
            label_states[label_status3] = "not_pressed"
         else:
             doman1=3
             giorno = "Tre Giorni"
         if (label!=label_status4):
            label_status4.config(image=Uncheck)
            label_states[label_status4] = "not_pressed"
         else:
             doman1=4
             giorno = "Quattro Giorni"
         if (label!=label_status5):
            label_status5.config(image=Uncheck)
            label_states[label_status5] = "not_pressed"
         else:
             doman1=5
             giorno = "Cinque Giorni"
         if (label!=label_status6):
            label_status6.config(image=Uncheck)
            label_states[label_status6] = "not_pressed"
         else:
             doman1 = 6
             giorno = "Sei Giorni"
         if (label!=label_status7):
            label_status7.config(image=Uncheck)
            label_states[label_status7] = "not_pressed"
         else:
             doman1=7
             giorno = "Tutta la Settimana"
        except:
            pale=1
        try:
         if (label!=label_status8):
            label_status8.config(image=Uncheck)
            label_states[label_status8] = "not_pressed"
         else:
             doman2=1
             legamenti="Si"
         if (label!=label_status9):
            label_status9.config(image=Uncheck)
            label_states[label_status9] = "not_pressed"
         else:
             doman2=2
             legamenti = "No"
        except:
            pale=1
        try:
          if (label!=label_status10):
            label_status10.config(image=Uncheck)
            label_states[label_status10] = "not_pressed"
          else:
              doman3 = 1
              difficolta = "Facile"
          if (label!=label_status11):
            label_status11.config(image=Uncheck)
            label_states[label_status11] = "not_pressed"
          else:
              doman3 = 2
              difficolta = "Medio"
          if (label!=label_status12):
            label_status12.config(image=Uncheck)
            label_states[label_status12] = "not_pressed"
          else:
              doman3 = 3
              difficolta = "Difficile"
        except:
            pale=1
        try:
          if (label!=label_status13):
            label_status13.config(image=Uncheck)
            label_states[label_status13] = "not_pressed"
          else:
              doman4 = 1
              preferenze="Forza"
          if (label!=label_status14):
            label_status14.config(image=Uncheck)
            label_states[label_status14] = "not_pressed"
          else:
              doman4 = 2
              preferenze="Bodybuiling"
          if (label!=label_status15):
            label_status15.config(image=Uncheck)
            label_states[label_status15] = "not_pressed"
          else:
              doman4 = 3
              preferenze="Flessibilità"
          if (label!=label_status16):
            label_status16.config(image=Uncheck)
            label_states[label_status16] = "not_pressed"
          else:
              doman4 = 4
              preferenze="Potenza"
        except:
            pale=1
        try:
         if (label!=label_status17):
            label_status17.config(image=Uncheck)
            label_states[label_status17] = "not_pressed"
         else:
             doman5=1
         if (label!=label_status18):
            label_status18.config(image=Uncheck)
            label_states[label_status18] = "not_pressed"
         else:
             doman5=2
        except:
            pale=1
        try:
            i = 0
            #global i
            global limiter
            global full
            while (label_eserc[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               if (label != label_eserc[i]):
                    label_eserc[i].config(image=Uncheck)
                    label_states[label_eserc[i]] = "not_pressed"
                    #print(label_states)
               else:
                    #global fullwork
                    fullwork[full] = pettorali_easy[i]
               i = i + 1
            i=0
            #full = full + 1
        except:
            pale = 1
        try:
           i=0
           global limiter3
           #global full
           while(label_eserc2[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc2[i]):
               label_eserc2[i].config(image=Uncheck)
               label_states[label_eserc2[i]] = "not_pressed"
               #full=full-1
             else:
                 #global fullwork
                 fullwork[full]=dorsali_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter2
           #global full
           while(label_esercc[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc[i]):
               label_esercc[i].config(image=Uncheck)
               label_states[label_esercc[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=pettorali_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter4
           #global full
           while(label_esercc2[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc2[i]):
               label_esercc2[i].config(image=Uncheck)
               label_states[label_esercc2[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=dorsali_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter5
           #global full
           while(label_eserc3[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc3[i]):
               label_eserc3[i].config(image=Uncheck)
               label_states[label_eserc3[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=spalle_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_esercc3[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc3[i]):
               label_esercc3[i].config(image=Uncheck)
               label_states[label_esercc3[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=spalle_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1

        try:
           i=0
           global limiter5
           #global full
           while(label_eserc4[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc4[i]):
               label_eserc4[i].config(image=Uncheck)
               label_states[label_eserc4[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=bicipiti_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_esercc4[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc4[i]):
               label_esercc4[i].config(image=Uncheck)
               label_states[label_esercc4[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=bicipiti_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1

        try:
           i=0
           global limiter5
           #global full
           while(label_eserc5[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc5[i]):
               label_eserc5[i].config(image=Uncheck)
               label_states[label_eserc5[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=tricipiti_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_esercc5[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc5[i]):
               label_esercc5[i].config(image=Uncheck)
               label_states[label_esercc5[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=tricipiti_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1

        try:
           i=0
           global limiter5
           #global full
           while(label_eserc6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc6[i]):
               label_eserc6[i].config(image=Uncheck)
               label_states[label_eserc6[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=addominali_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_esercc6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc6[i]):
               label_esercc6[i].config(image=Uncheck)
               label_states[label_esercc6[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=addominali_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_eserccc6[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserccc6[i]):
               label_eserccc6[i].config(image=Uncheck)
               label_states[label_eserccc6[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=addominali_avanzato[i]
             i=i+1
           #full=full+1
        except:
            pale=1

        try:
           i=0
           global limiter5
           #global full
           while(label_eserc7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserc7[i]):
               label_eserc7[i].config(image=Uncheck)
               label_states[label_eserc7[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=quadricipiti_easy[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_esercc7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_esercc7[i]):
               label_esercc7[i].config(image=Uncheck)
               label_states[label_esercc7[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=quadricipiti_intermedio[i]
             i=i+1
           #full=full+1
        except:
            pale=1
        try:
           i=0
           global limiter6
           #global full
           while(label_eserccc7[i]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
             if (label != label_eserccc7[i]):
               label_eserccc7[i].config(image=Uncheck)
               label_states[label_eserccc7[i]] = "not_pressed"
             else:
                 #global fullwork
                 fullwork[full]=quadricipiti_avanzato[i]
             i=i+1
           #full=full+1
        except:
            pale=1

        try:
            i = 0
            global limiter5
            # global full
            while (label_eserc8[i] != tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
                if (label != label_eserc8[i]):
                    label_eserc8[i].config(image=Uncheck)
                    label_states[label_eserc8[i]] = "not_pressed"
                else:
                    # global fullwork
                    fullwork[full] = glutei_easy[i]
                i = i + 1
            #full = full + 1
        except:
            pale = 1
        try:
            i = 0
            global limiter6
            # global full
            while (label_esercc8[i] != tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
                if (label != label_esercc8[i]):
                    label_esercc8[i].config(image=Uncheck)
                    label_states[label_esercc8[i]] = "not_pressed"
                else:
                    # global fullwork
                    fullwork[full] = glutei_intermedio[i]
                i = i + 1
            #full = full + 1
        except:
            pale = 1


        try:
            i = 0
            global limiter5
            # global full
            while (label_eserc9[i] != tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
                if (label != label_eserc9[i]):
                    label_eserc9[i].config(image=Uncheck)
                    label_states[label_eserc9[i]] = "not_pressed"
                else:
                    # global fullwork
                    fullwork[full] = polpacci_easy[i]
                i = i + 1
            #full = full + 1
        except:
            pale = 1

        try:
            i = 0
            global limiter5
            # global full
            while (label_eserc10[i] != tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
                if (label != label_eserc10[i]):
                    label_eserc10[i].config(image=Uncheck)
                    label_states[label_eserc10[i]] = "not_pressed"
                else:
                    # global fullwork
                    fullwork[full] = avambracci_easy[i]
                i = i + 1
            #full = full + 1
        except:
            pale = 1

        try:
           if (label!=label_avambracci1):
            label_avambracci1.config(image=Uncheck)
            label_states[label_avambracci1] = "not_pressed"
           else:
              fullwork[full] = "CURL HAMMER AI CAVI CON CORDA"
           if (label!=label_avambracci2):
            label_avambracci2.config(image=Uncheck)
            label_states[label_avambracci2] = "not_pressed"
           else:
              fullwork[full] = "CURL INVERSO BILANCIERE IN PIEDI"


        except:
            pale = 1
        #full = full + 1
    else:
        label_states[label] = "not_pressed"
        label.config(image=Uncheck)
    try:
      if (label_states[label_status1] == "not_pressed" and label_states[label_status2] == "not_pressed" and label_states[label_status3] == "not_pressed" and label_states[label_status4] == "not_pressed" and label_states[label_status5] == "not_pressed" and label_states[label_status6] == "not_pressed" and label_states[label_status7] == "not_pressed" ):
          buttone.config(state=tk.DISABLED)
      else:
          buttone.config(state=tk.NORMAL)
    except:
        pale=1

    try:
      if (label_states[label_status8] == "not_pressed" and label_states[label_status9] == "not_pressed"):
          buttone2.config(state=tk.DISABLED)
      else:
          buttone2.config(state=tk.NORMAL)
    except:
        pale=1

    try:
      if (label_states[label_status10] == "not_pressed" and label_states[label_status11] == "not_pressed" and label_states[label_status12] == "not_pressed"):
          buttone3.config(state=tk.DISABLED)
      else:
          buttone3.config(state=tk.NORMAL)
    except:
        pale=1

    try:
        if (label_states[label_status13] == "not_pressed" and label_states[label_status14] == "not_pressed" and
                label_states[label_status15] == "not_pressed" and label_states[label_status16] == "not_pressed"):
            buttone4.config(state=tk.DISABLED)
        else:
            buttone4.config(state=tk.NORMAL)
    except:
        pale=1
    try:
     if (label_states[label_status18] == "not_pressed" and owletto==5):
        buttone4_5.pack()
        buttone4_5.config(state=tk.NORMAL)
        try:
            buttone4_55.pack_forget()
        except:
            pale = 2
            buttone4_5.pack_forget()
     if (label_states[label_status17] == "not_pressed" and owletto==5):
        try:
            buttone4_5.pack_forget()
        except:
            pale = 2
            buttone4_55.pack_forget()
        buttone4_55.pack()
        buttone4_55.config(state=tk.NORMAL)
     if (label_states[label_status17] == "not_pressed" and label_states[label_status18] == "not_pressed" and owletto==5):
        buttone4_5.config(state=tk.DISABLED)
        buttone4_55.config(state=tk.DISABLED)
    except:
        pale=1
    try:
        j=0
        #global limiter
        while(j<limiter and label_eserc[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and doman3==1):
           #label_states[label_eserc[j]].replace("!lable15"
                                                #"not_pressed","")
           if (label_states[label_eserc[j]]=="not_pressed" and doman3==1 and label_eserc[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone5.config(state=tk.DISABLED)
               j=j+1
           else:
               buttone5.config(state=tk.NORMAL)
               break

    except:
        pale=1
    try:
        j=0
        #global limiter
        while(j<limiter2 and label_esercc[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc[j]]=="not_pressed" and (doman3==3 or doman3==2) and label_esercc[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone5.config(state=tk.DISABLED)
               j=j+1
           else:
               buttone5.config(state=tk.NORMAL)
               break

    except:
        pale=1
    try:
        j=0
        #global limiter
        while(j<limiter3 and label_eserc2[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc2[j]]=="not_pressed" and doman3==1 and label_eserc2[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone6.config(state=tk.DISABLED)
               j=j+1
           else:


               buttone6.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        #global limiter4
        while(j<limiter4 and label_esercc2[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc2[j]]=="not_pressed" and (doman3==3 or doman3==2) and label_esercc2[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone6.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone6.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        #global limiter
        while(j<limiter5 and label_eserc3[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc3[j]]=="not_pressed" and doman3==1 and label_eserc3[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone7.config(state=tk.DISABLED)
               j=j+1
           else:


               buttone7.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        #global limiter4
        while(j<limiter6 and label_esercc3[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc3[j]]=="not_pressed" and (doman3==3 or doman3==2) and label_esercc3[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone7.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone7.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter7
        while(j<limiter7 and label_eserc4[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc4[j]]=="not_pressed" and doman3==1 and label_eserc4[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone8.config(state=tk.DISABLED)
               j=j+1
           else:


               buttone8.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter8
        while(j<limiter8 and label_esercc4[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc4[j]]=="not_pressed" and (doman3==3 or doman3==2) and label_esercc4[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone8.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone8.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter9
        while(j<limiter9 and label_eserc5[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc5[j]]=="not_pressed" and doman3==1 and label_eserc5[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone9.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone9.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter10
        while(j<limiter10 and label_esercc5[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc5[j]]=="not_pressed" and (doman3==3 or doman3==2) and label_esercc5[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone9.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone9.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter11
        while(j<limiter11 and label_eserc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc6[j]]=="not_pressed" and doman3==1 and label_eserc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone10.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone10.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter12
        while(j<limiter12 and label_esercc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==2)):
           if (label_states[label_esercc6[j]]=="not_pressed" and doman3==2 and label_esercc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone10.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone10.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter13
        while(j<limiter13 and label_eserccc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3)):
           if (label_states[label_eserccc6[j]]=="not_pressed" and doman3==3 and label_eserccc6[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone10.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone10.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter14
        while(j<limiter14 and label_eserc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc7[j]]=="not_pressed" and doman3==1 and label_eserc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone11.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone11.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter15
        while(j<limiter15 and label_esercc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==2)):
           if (label_states[label_esercc7[j]]=="not_pressed" and doman3==2 and label_esercc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone11.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone11.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter16
        while(j<limiter16 and label_eserccc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3)):
           if (label_states[label_eserccc7[j]]=="not_pressed" and doman3==3 and label_eserccc7[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone11.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone11.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
      if (label_states[label_avambracci1] == "not_pressed" and label_states[label_avambracci2] == "not_pressed"):
          buttone14.config(state=tk.DISABLED)
      else:
          buttone14.config(state=tk.NORMAL)
    except:
        pale=1

    try:
        j=0
        global limiter17
        while(j<limiter17 and label_eserc8[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc8[j]]=="not_pressed" and doman3==1 and label_eserc8[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone12.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone12.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter18
        while(j<limiter18 and label_esercc8[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?") and (doman3==3 or doman3==2)):
           if (label_states[label_esercc8[j]]=="not_pressed" and doman3==2 and label_esercc8[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone12.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone12.config(state=tk.NORMAL)
               break

    except:
        pale=1

    try:
        j=0
        global limiter19
        while(j<limiter19 and label_eserc9[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc9[j]]=="not_pressed" and doman3==1 and label_eserc9[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone13.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone13.config(state=tk.NORMAL)
               break
    except:
        pale=1

    try:
        j=0
        global limiter20
        while(j<limiter20 and label_eserc10[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")  and doman3==1):
           if (label_states[label_eserc10[j]]=="not_pressed" and doman3==1 and label_eserc10[j]!=tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")):
               buttone14.config(state=tk.DISABLED)
               j=j+1
           else:

               buttone14.config(state=tk.NORMAL)
               break
    except:
        pale=1

    global pop
    #try:
        #global pop
        #global i
        #j = 0
        #v = 0
        #ferri
        #while (v<limiter):
           #if (label.bind("<Enter>")==label_eserc[v]):
                #label_eserc[v].bind("<Enter>", show_image)
                #label_eserc[v].bind("<Leave>", hide_image)
                #pop = pettorali_easy[v]
                #j = 339
                #i = i + 1
           #else:
                #j = j + 1
           #v=v+1
            # j = j + 1
    #except:
        #j = j




domandestar=0
app = tk.Tk()
app.configure(bg="lightblue")
app.title("** MyGym **")

Check = tk.PhotoImage(file="Check.png")
Uncheck = tk.PhotoImage(file="Uncheck.png")
Immagine = tk.PhotoImage(file="Immagine.png")
Immagine2 = tk.PhotoImage(file="Immagine2.png")
Cornice = tk.PhotoImage(file="Cornice.png")
Manubri = tk.PhotoImage(file="Manubri.png")
Bilanciere = tk.PhotoImage(file="Bilanciere.png")
Kettlebell = tk.PhotoImage(file="Kettlebell.png")
RedManubri = tk.PhotoImage(file="RedManubri.png")
var = tk.StringVar()
var.set("not_pressed")








label = tk.Label(app, text="Inserisci il tuo username:")
label.pack()  # Pack posiziona il widget nella finestra
label.configure(bg="lightblue",font=("MingLiU", 13, "bold"))


entry = tk.Entry(app)
entry.pack(padx=650,pady=5)
def on_scroll(*args):
    canvas.yview(*args)



canvas = tk.Canvas(app, height=1000, width=1560, highlightbackground="lightblue",scrollregion=(0, 0, 5000, 5000,))
scrollbar = tk.Scrollbar(app, orient="vertical", command=on_scroll)
canvas.config(yscrollcommand=scrollbar.set)


app = tk.Frame(canvas)
canvas.create_window((0, 0), window=app, anchor="nw")


#for i in range(20):
    #tk.Button(frame, text=f"Label {i}").pack()


canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.configure(bg="lightblue")
app.option_add("*Label*background", "lightblue")
app.option_add("*Text Widgets*background", "lightblue")
scrollbar.configure(bg="lightblue")
app.option_add("*Label*font", ("MingLiU", 13, "bold"))
app.option_add("*Button*font", ("MingLiU", 13, "bold"))
app.configure(bg="lightblue")
canv = tk.Canvas(app, height=3000, width=300, highlightbackground="lightblue")
canv.pack(side="left")
canv.configure(bg="lightblue")
canv.create_rectangle(10, 10, 290, 190, outline="lightblue", width=2)
new_size = (360, 360)
new_size2 = (400, 400)
new_size3 = (700, 700)
new_size4 = (500, 375)
Manubri=Manubri.subsample(new_size[0] // 150, new_size[1] // 150)
Bilanciere = Bilanciere.subsample(new_size2[0] // 150, new_size2[1] // 150)
Kettlebell = Kettlebell.subsample(new_size3[0] // 150, new_size3[1] // 150)
RedManubri = RedManubri.subsample(new_size4[0] // 150, new_size4[1] // 150)
canv.create_image(0, 0, anchor=tk.NW, image=Manubri)
canv.create_image(0, 600, anchor=tk.NW, image=Bilanciere)
canv.create_image(0, 1200, anchor=tk.NW, image=Kettlebell)
canv.create_image(0, 1800, anchor=tk.NW, image=RedManubri)





label_states = {}
def on_button_clicks():
    label.config(text="Ciao " + entry.get() + ", dammi alcune info su di te per poter creare il tuo programma per la palestra")
    label.configure(bg="lightblue",font=("MingLiU", 13, "bold"))
    global pale
    pale=1
    domanda1()
def bottone():
    #buttone = tk.Button(app, text="Avanti", command=domanda2)
    buttone.pack(padx=200,pady=5)
    return buttone

def prova():
    if label_status1 == tk.Label(app, image=Check, text="Un giorno", compound="left"):
       label_status2.destroy()
       label_status2.pack()

def domanda1():
    nome = entry.get()
    label.configure(bg="lightblue")
    h=0
    i=0
    p=0
    start=0
    #if (pale == 1):
    button.destroy()
    cosetto=0
    for individuo in onto.individuals():
        for prop in individuo.get_properties():
            for value in prop[individuo]:
                #cosetto=0
                if (prop.python_name == "Nome" and value==nome):
                    cosetto = 1
                if (cosetto == 1):
                    fullworkowl[h] = value
                    if (fullworkowl[h].startswith("1)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("1)", "")
                    if (fullworkowl[h].startswith("2)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("2)", "")
                    if (fullworkowl[h].startswith("3)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("3)", "")
                    if (fullworkowl[h].startswith("4)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("4)", "")
                    if (fullworkowl[h].startswith("5)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("5)", "")
                    if (fullworkowl[h].startswith("6)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("6)", "")
                    if (fullworkowl[h].startswith("7)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("7)", "")
                    if (fullworkowl[h].startswith("8)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("8)", "")
                    if (fullworkowl[h].startswith("9)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("9)", "")
                    if (fullworkowl[h].startswith("0)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("0)", "")
                    fullworkowl[h] = fullworkowl[h].replace("10)", "")
                    fullworkowl[h] = fullworkowl[h].replace("11)", "")
                    fullworkowl[h] = fullworkowl[h].replace("12)", "")
                    fullworkowl[h] = fullworkowl[h].replace("13)", "")
                    fullworkowl[h] = fullworkowl[h].replace("14)", "")
                    fullworkowl[h] = fullworkowl[h].replace("15)", "")
                    fullworkowl[h] = fullworkowl[h].replace("16)", "")
                    fullworkowl[h] = fullworkowl[h].replace("17)", "")
                    fullworkowl[h] = fullworkowl[h].replace("18)", "")
                    fullworkowl[h] = fullworkowl[h].replace("19)", "")
                    h=h+1
                    p=p+1
                    if (p==25):
                        cosetto=0
                        start=3
    if start==3:
        if (fullworkowl[4] == "Un Giorno"):
            full2 = 15
            i=5
            labelTuttoilcorpo.pack(padx=150, pady=5)
            while (i <= full2 - 1):
                label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
                if (label_fullwork2[i] != tk.Label(app, text="1")):
                    label_fullwork2[i].pack(padx=150, pady=5)
                    label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                    label_states[label_clickfull2[i]] = "not_pressed"
                    label_clickfull2[i].bind("<Button-1>",
                                             lambda event, label=label_clickfull2[i]: on_image_click2(label))
                    label_clickfull2[i].pack()
                i = i + 1

        if (fullworkowl[4] == "Due Giorni"):
            full2 = 15
            i=5
            labelParteInferiore.pack(padx=150, pady=5)
            while (i <= full2 - 1):
                label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
                if (label_fullwork2[i] != tk.Label(app, text="1")):
                    label_fullwork2[i].pack(padx=150, pady=5)
                    label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                    label_states[label_clickfull2[i]] = "not_pressed"
                    label_clickfull2[i].bind("<Button-1>",
                                             lambda event, label=label_clickfull2[i]: on_image_click2(label))
                    label_clickfull2[i].pack()
                i = i + 1
                if (i == 5):
                    labelParteSuperiore.pack(padx=150, pady=5)
        # i = 0
        if (fullworkowl[4] == "Tre Giorni" or fullworkowl[4] == "Quattro Giorni" or fullworkowl[4] == "Cinque Giorni" or fullworkowl[4] == "Sei Giorni" or fullworkowl[4] == "Tutta la Settimana"):
            full2 = 25
            i = 5
            if (fullworkowl[4] == "Tre Giorni" or fullworkowl[4] == "Cinque Giorni" or fullworkowl[4] == "Tutta la Settimana"):
                labelTuttoilcorpo.pack(padx=150, pady=5)
            if (fullworkowl[4] == "Quattro Giorni" or fullworkowl[4] == "Sei Giorni"):
                labelTuttoilcorpo2.pack(padx=150, pady=5)
            while (i <= 14):
                label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
                if (label_fullwork2[i] != tk.Label(app, text="1")):
                    label_fullwork2[i].pack(padx=150, pady=5)
                    label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                    label_states[label_clickfull2[i]] = "not_pressed"
                    label_clickfull2[i].bind("<Button-1>",
                                             lambda event, label=label_clickfull2[i]: on_image_click2(label))
                    label_clickfull2[i].pack()
                i = i + 1
            if (fullworkowl[4] == "Tre Giorni" or fullworkowl[4] == "Quattro Giorni"):
                labelParteInferiore.pack(padx=150, pady=5)
            if (fullworkowl[4] == "Cinque Giorni" or fullworkowl[4] == "Sei Giorni"):
                labelParteInferiore2.pack(padx=150, pady=5)
            if (fullworkowl[4] == "Tutta la Settimana"):
                labelParteInferiore3.pack(padx=150, pady=5)
            # i=9
            while (i <= full2 - 1):
                label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
                if (label_fullwork2[i] != tk.Label(app, text="1")):
                    label_fullwork2[i].pack(padx=150, pady=5)
                    label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                    label_states[label_clickfull2[i]] = "not_pressed"
                    label_clickfull2[i].bind("<Button-1>",
                                             lambda event, label=label_clickfull2[i]: on_image_click2(label))
                    label_clickfull2[i].pack()
                i = i + 1
                if (i == 15):
                    if (fullworkowl[4] == "Tre Giorni" or fullworkowl[4] == "Quattro Giorni"):
                        labelParteSuperiore.pack(padx=150, pady=5)
                    if (fullworkowl[4] == "Cinque Giorni" or fullworkowl[4] == "Sei Giorni"):
                        labelParteSuperiore2.pack(padx=150, pady=5)
                    if (fullworkowl[4] == "Tutta la Settimana"):
                        labelParteSuperiore3.pack(padx=150, pady=5)
        i = 0

    if(cosetto==0 and start==0):

      #labelGiorni = tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")
      labelGiorni.pack(padx=250,pady=5)
      labelGiorni.configure(bg="lightblue")
      #label_status1 = tk.Label(app, image=Uncheck, text="Un giorno", compound="left")
      label_status1.pack(padx=250,pady=5)
      label_status1.bind("<Button-1>", lambda event, label=label_status1: on_image_click(label))
      label_states[label_status1] = "not_pressed"

      #label_status2 = tk.Label(app, image=Uncheck, text="Due giorni", compound="left")
      label_status2.pack()
      label_status2.bind("<Button-1>", lambda event, label=label_status2: on_image_click(label))
      label_states[label_status2] = "not_pressed"

      #label_status3 = tk.Label(app, image=Uncheck, text="Tre giorni", compound="left")
      label_status3.pack()
      label_status3.bind("<Button-1>", lambda event, label=label_status3: on_image_click(label))
      label_states[label_status3] = "not_pressed"

    #label_status4 = tk.Label(app, image=Uncheck, text="Quattro giorni", compound="left")
      label_status4.pack()
      label_status4.bind("<Button-1>", lambda event, label=label_status4: on_image_click(label))
      label_states[label_status4] = "not_pressed"

    #label_status5 = tk.Label(app, image=Uncheck, text="Cinque giorni", compound="left")
      label_status5.pack()
      label_status5.bind("<Button-1>", lambda event, label=label_status5: on_image_click(label))
      label_states[label_status5] = "not_pressed"

    #label_status6 = tk.Label(app, image=Uncheck, text="Sei giorni", compound="left")
      label_status6.pack()
      label_status6.bind("<Button-1>", lambda event, label=label_status6: on_image_click(label))
      label_states[label_status6] = "not_pressed"

    #label_status7 = tk.Label(app, image=Uncheck, text="Tutta la settimana", compound="left")
      label_status7.pack()
      label_status7.bind("<Button-1>", lambda event, label=label_status7: on_image_click(label))
      global pale
      label_states[label_status7] = "not_pressed"
      if (label_states[label_status1] == "not_pressed" and label_states[label_status2] == "not_pressed"):
        buttone.config(state=tk.DISABLED)
      else:
        buttone.config(state=tk.NORMAL)

        #label_status2.pack()
      bottone()

def domanda2():
    global pale
    buttone.destroy()
    label_status1.destroy()
    label_status2.destroy()
    label_status3.destroy()
    label_status4.destroy()
    label_status5.destroy()
    label_status6.destroy()
    label_status7.destroy()
    labelGiorni.destroy()
    pale=2
    #labelDieta = tk.Label(app, text="Fai una dieta?")
    labelDieta.pack(padx=250,pady=5)
    #label_status8 = tk.Label(app, image=Uncheck, text="Sì", compound="left")
    label_status8.pack()
    label_status8.bind("<Button-1>", lambda event, label=label_status8: on_image_click(label))
    label_states[label_status8] = "not_pressed"

    #label_status9 = tk.Label(app, image=Uncheck, text="No", compound="left")
    label_status9.pack()
    label_status9.bind("<Button-1>", lambda event, label=label_status9: on_image_click(label))
    label_states[label_status9] = "not_pressed"
    buttone2.pack()
    #bottone().pack(side=tk.BOTTOM)

def domanda3():
    global pale
    buttone2.destroy()
    label_status8.destroy()
    label_status9.destroy()
    labelDieta.destroy()
    pale=2
    #labelDieta = tk.Label(app, text="Fai una dieta?")
    labelEsperienza.pack(padx=300,pady=5)
    #label_status8 = tk.Label(app, image=Uncheck, text="Sì", compound="left")
    label_status10.pack()
    label_status10.bind("<Button-1>", lambda event, label=label_status10: on_image_click(label))
    label_states[label_status10] = "not_pressed"

    #label_status9 = tk.Label(app, image=Uncheck, text="No", compound="left")
    label_status11.pack()
    label_status11.bind("<Button-1>", lambda event, label=label_status11: on_image_click(label))
    label_states[label_status11] = "not_pressed"

    label_status12.pack()
    label_status12.bind("<Button-1>", lambda event, label=label_status12: on_image_click(label))
    label_states[label_status12] = "not_pressed"
    buttone3.pack()
    #bottone().pack(side=tk.BOTTOM)

def domanda4():
    global pale
    buttone3.destroy()
    label_status10.destroy()
    label_status11.destroy()
    label_status12.destroy()
    labelEsperienza.destroy()
    pale=2
    #labelDieta = tk.Label(app, text="Fai una dieta?")
    labelObbiettivo.pack(padx=350,pady=5)
    #label_status8 = tk.Label(app, image=Uncheck, text="Sì", compound="left")
    label_status13.pack()
    label_status13.bind("<Button-1>", lambda event, label=label_status13: on_image_click(label))
    label_states[label_status13] = "not_pressed"

    #label_status9 = tk.Label(app, image=Uncheck, text="No", compound="left")
    label_status14.pack()
    label_status14.bind("<Button-1>", lambda event, label=label_status14: on_image_click(label))
    label_states[label_status14] = "not_pressed"

    label_status15.pack()
    label_status15.bind("<Button-1>", lambda event, label=label_status15: on_image_click(label))
    label_states[label_status15] = "not_pressed"

    label_status16.pack()
    label_status16.bind("<Button-1>", lambda event, label=label_status16: on_image_click(label))
    label_states[label_status16] = "not_pressed"
    buttone4.pack()

def domanda5():
    global pale
    global owletto
    buttone4.destroy()
    label_status13.destroy()
    label_status14.destroy()
    label_status15.destroy()
    label_status16.destroy()
    labelObbiettivo.destroy()
    pale=2
    #labelDieta = tk.Label(app, text="Fai una dieta?")
    labelOwl.pack(padx=400,pady=5)
    #label_status8 = tk.Label(app, image=Uncheck, text="Sì", compound="left")
    label_status17.pack()
    label_status17.bind("<Button-1>", lambda event, label=label_status17: on_image_click(label))
    label_states[label_status17] = "not_pressed"

    #label_status9 = tk.Label(app, image=Uncheck, text="No", compound="left")
    label_status18.pack()
    label_status18.bind("<Button-1>", lambda event, label=label_status18: on_image_click(label))
    label_states[label_status18] = "not_pressed"
    buttone4_5.pack()
    #buttone4_55.pack()
    buttone4_5.config(state=tk.DISABLED)
    buttone4_55.config(state=tk.DISABLED)
    owletto=5



def Owl():
    global pale
    global cosetto
    global full2
    global doman1
    global difficolta
    h=0
    cosetto=0
    buttone4_55.destroy()
    label_status18.destroy()
    label_status17.destroy()
    labelOwl.destroy()
    pale=2
    i=0
    j=0
    p=0
    cont="345"
    for individuo in onto.individuals():
        for prop in individuo.get_properties():
            for value in prop[individuo]:
                cosetto=0
                if (prop.python_name == "Nome" and i==0 and value==difficolta):
                    if(value==difficolta):
                        cosetto = 1
                        i = i + 1
                        print("fer")
                    else:
                     cosetto = 0
                     cont="34"
                     i = 0
                else:
                    Fals=1


                if (prop.python_name == "Nome" and i==1 and value ==preferenze):
                    if (value ==preferenze):
                        cosetto = 1
                        i = i + 1
                    else:
                     cosetto = 0
                     cont = "35"
                     i = 0
                else:
                    Fals=1

                if (prop.python_name == "Nome" and i==2 and value ==legamenti):
                    if (value ==legamenti):
                        cosetto = 1
                        i = i + 1
                    else:
                     cosetto = 0
                     cont = "36"
                     i = 0
                else:
                    Fals=1

                if (prop.python_name == "Nome" and i==3 and value == giorno):
                    if (value == giorno):
                        cosetto = 1
                        i = i + 1
                    else:
                     cosetto = 0
                     cont = "37"
                     i = 0
                else:
                    Fals=1
                j = j + 1
                cont="38"
                if (cosetto==0 and i!=4):
                    i=0
                print(i)
                print(prop.python_name)
                print(value)

                if (prop.python_name == "Nome" and i==4 and value != giorno and p<=21):
                    fullworkowl[h] = value
                    p=p+1
                    if (fullworkowl[h].startswith("1)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("1)", "")
                    if (fullworkowl[h].startswith("2)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("2)", "")
                    if (fullworkowl[h].startswith("3)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("3)", "")
                    if (fullworkowl[h].startswith("4)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("4)", "")
                    if (fullworkowl[h].startswith("5)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("5)", "")
                    if (fullworkowl[h].startswith("6)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("6)", "")
                    if (fullworkowl[h].startswith("7)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("7)", "")
                    if (fullworkowl[h].startswith("8)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("8)", "")
                    if (fullworkowl[h].startswith("9)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("9)", "")
                    if (fullworkowl[h].startswith("0)")==True):
                        fullworkowl[h] = fullworkowl[h].replace("0)", "")
                    fullworkowl[h] = fullworkowl[h].replace("10)", "")
                    fullworkowl[h] = fullworkowl[h].replace("11)", "")
                    fullworkowl[h] = fullworkowl[h].replace("12)", "")
                    fullworkowl[h] = fullworkowl[h].replace("13)", "")
                    fullworkowl[h] = fullworkowl[h].replace("14)", "")
                    fullworkowl[h] = fullworkowl[h].replace("15)", "")
                    fullworkowl[h] = fullworkowl[h].replace("16)", "")
                    fullworkowl[h] = fullworkowl[h].replace("17)", "")
                    fullworkowl[h] = fullworkowl[h].replace("18)", "")
                    fullworkowl[h] = fullworkowl[h].replace("19)", "")
                    print(value)
                    print(prop.python_name)
                    print("prova")
                    h=h+1
                    if (p==21):
                       i=0
    print(fullworkowl)
    i=0
    if (doman1 == 1):
        full2 = 10
        labelTuttoilcorpo.pack(padx=100, pady=5)
        while (i <= full2 - 1):
            label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
            if (label_fullwork2[i] != tk.Label(app, text="1")):
                label_fullwork2[i].pack(padx=100, pady=5)
                label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull2[i]] = "not_pressed"
                label_clickfull2[i].bind("<Button-1>", lambda event, label=label_clickfull2[i]: on_image_click2(label))
                label_clickfull2[i].pack()
            i = i + 1

    if (doman1 == 2):
        full2=10
        labelParteInferiore.pack(padx=100, pady=5)
        while (i <= full2 - 1):
            label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
            if (label_fullwork2[i] != tk.Label(app, text="1")):
                label_fullwork2[i].pack(padx=100, pady=5)
                label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull2[i]] = "not_pressed"
                label_clickfull2[i].bind("<Button-1>", lambda event, label=label_clickfull2[i]: on_image_click2(label))
                label_clickfull2[i].pack()
            i = i + 1
            if (i == 5):
                labelParteSuperiore.pack(padx=200, pady=5)
    #i = 0
    if (doman1 > 2):
        full2=20

        if (doman1 == 3 or doman1 == 5 or doman1 == 7):
            labelTuttoilcorpo.pack(padx=100, pady=5)
        if (doman1 == 4 or doman1 == 6):
            labelTuttoilcorpo2.pack(padx=100, pady=5)
        while (i <= 9):
            label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
            if (label_fullwork2[i] != tk.Label(app, text="1")):
                label_fullwork2[i].pack(padx=100, pady=5)
                label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull2[i]] = "not_pressed"
                label_clickfull2[i].bind("<Button-1>", lambda event, label=label_clickfull2[i]: on_image_click2(label))
                label_clickfull2[i].pack()
                # with onto:
                # corsa = Utente()
                # corsa.Utente.append(nome)
                # corsa.Nome.append(fullwork[i])
                # corsa.Difficolta.append(difficolta)
                # corsa.Utente = [nome]
                # corsa.Nome+=[fullwork[i]]
                # corsa.Difficolta = [difficolta]
                # onto.save()
            i = i + 1
        if (doman1 == 3 or doman1 == 4):
            labelParteInferiore.pack(padx=100, pady=5)
        if (doman1 == 5 or doman1 == 6):
            labelParteInferiore2.pack(padx=100, pady=5)
        if (doman1 == 7):
            labelParteInferiore3.pack(padx=100, pady=5)
        # i=9
        while (i <= full2 - 1):
            label_fullwork2[i] = tk.Label(app, text=fullworkowl[i])
            if (label_fullwork2[i] != tk.Label(app, text="1")):
                label_fullwork2[i].pack(padx=100, pady=5)
                label_clickfull2[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull2[i]] = "not_pressed"
                label_clickfull2[i].bind("<Button-1>", lambda event, label=label_clickfull2[i]: on_image_click2(label))
                label_clickfull2[i].pack()
                # with onto:
                # corsa = Utente()
                # corsa.Utente.append(nome)
                # corsa.Nome.append(fullwork[i])
                # corsa.Difficolta.append(difficolta)
                # corsa.Utente = [nome]
                # corsa.Nome+=[fullwork[i]]
                # corsa.Difficolta = [difficolta]
                # onto.save()
            i = i + 1
            if (i == 15):
                if (doman1 == 3 or doman1 == 4):
                    labelParteSuperiore.pack(padx=100, pady=5)
                if (doman1 == 5 or doman1 == 6):
                    labelParteSuperiore2.pack(padx=100, pady=5)
                if (doman1 == 7):
                    labelParteSuperiore3.pack(padx=100, pady=5)
    i = 0




def scelta():
   global i
   global pop
   global full
   #if (full>6):
       #full=full+1
   i = 0
   try:
       buttone4_5.destroy()
       label_status18.destroy()
       label_status17.destroy()
       labelOwl.destroy()
   except:
    i=0
   labelPettorali.pack(padx=100, pady=5)
   if (doman1!=0):
       if (doman3==1):
           while(pettorali_easy[i]!="1"):
              bellim=label_eserc[i]
              label_eserc[i] = tk.Label(app, image=Uncheck, text=pettorali_easy[i], compound="left")
              label_click[i] = tk.Label(app, image=Immagine,compound="right")
              label_eserc[i].bind("<Button-1>", lambda event, label=label_eserc[i]: on_image_click(label))
              label_states[label_eserc[i]] = "not_pressed"
              label_states[label_click[i]] = "not_pressed"
              label_eserc[i].pack()
              label_click[i].bind("<Button-1>", lambda event, label=label_click[i]: on_image_click2(label))
              label_click[i].pack()
              #pop = pettorali_easy[i]
              i=i+1
       if (doman3==2 or doman3==3):
           while(i<limiter2):
              bellim=label_esercc[i]
              label_esercc[i] = tk.Label(app, image=Uncheck, text=pettorali_intermedio[i], compound="left")
              label_esercc[i].bind("<Button-1>", lambda event, label=label_esercc[i]: on_image_click(label))
              label_states[label_esercc[i]] = "not_pressed"
              label_esercc[i].pack()
              label_clickk[i] = tk.Label(app, image=Immagine, compound="right")
              label_states[label_clickk[i]] = "not_pressed"
              label_clickk[i].bind("<Button-1>", lambda event, label=label_clickk[i]: on_image_click2(label))
              label_clickk[i].pack()
              i=i+1
   buttone5.pack(padx=100,pady=5)



def scelta2():
       canvas.yview_moveto(0.0)
       global full
       full = full + 1
       global i
       i = 0
       labelPettorali.pack_forget()
       buttone5.pack_forget()
       if (doman3 == 1):
          while(i<limiter):
            label_eserc[i].destroy()
            label_click[i].destroy()
            i=i+1
       if (doman3 == 2 or doman3==3):
          while(i<limiter2):
            label_esercc[i].destroy()
            label_clickk[i].destroy()
            i=i+1
       i=0
       labelDorsali.pack(padx=100, pady=5)
       if (doman1 != 0):
           if (doman3 == 1):
               while (pettorali_easy[i] != "1"):
                   #bellim = label_eserc[i]
                   label_eserc2[i] = tk.Label(app, image=Uncheck, text=dorsali_easy[i], compound="left")
                   label_eserc2[i].bind("<Button-1>", lambda event, label=label_eserc2[i]: on_image_click(label))
                   label_states[label_eserc2[i]] = "not_pressed"
                   label_eserc2[i].pack()
                   label_click2[i] = tk.Label(app, image=Immagine, compound="right")
                   label_states[label_click2[i]] = "not_pressed"
                   label_click2[i].bind("<Button-1>", lambda event, label=label_click2[i]: on_image_click2(label))
                   label_click2[i].pack()
                   i = i + 1
               buttone6.pack(padx=100,pady=5)
           if (doman3 == 2):
               while (i<limiter4):
                   #bellim = label_eserc[i]
                   label_esercc2[i] = tk.Label(app, image=Uncheck, text=dorsali_intermedio[i], compound="left")
                   label_esercc2[i].bind("<Button-1>", lambda event, label=label_esercc2[i]: on_image_click(label))
                   label_states[label_esercc2[i]] = "not_pressed"
                   label_esercc2[i].pack()
                   label_clickk2[i] = tk.Label(app, image=Immagine, compound="right")
                   label_states[label_clickk2[i]] = "not_pressed"
                   label_clickk2[i].bind("<Button-1>", lambda event, label=label_clickk2[i]: on_image_click2(label))
                   label_clickk2[i].pack()
                   i = i + 1
               buttone6.pack(padx=100,pady=5)
           if (doman3 == 3):
               global fullwork
               #global full
               fullwork[full]="STACCHI UNA GAMBA 2 KETTLEBELL"
               scelta3()





def scelta3():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    global limiter3
    global limiter4

    i = 0
    buttone6.pack_forget()
    labelDorsali.pack_forget()
    if (doman3 == 1):
        while (i < limiter3):
            label_eserc2[i].destroy()
            label_click2[i].destroy()
            i = i + 1
    if (doman3 == 2 or doman3 == 3):
        while (i < limiter4):
            label_esercc2[i].destroy()
            label_clickk2[i].destroy()
            i = i + 1
    i = 0

    labelSpalle.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter5):
                # bellim = label_eserc[i]
                label_eserc3[i] = tk.Label(app, image=Uncheck, text=spalle_easy[i], compound="left")
                label_eserc3[i].bind("<Button-1>", lambda event, label=label_eserc3[i]: on_image_click(label))
                label_states[label_eserc3[i]] = "not_pressed"
                label_eserc3[i].pack()
                label_click3[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click3[i]] = "not_pressed"
                label_click3[i].bind("<Button-1>", lambda event, label=label_click3[i]: on_image_click2(label))
                label_click3[i].pack()
                i = i + 1
            buttone7.pack(padx=100,pady=5)
        if (doman3 == 2):
            while (i < limiter6):
                # bellim = label_eserc[i]
                label_esercc3[i] = tk.Label(app, image=Uncheck, text=spalle_intermedio[i], compound="left")
                label_esercc3[i].bind("<Button-1>", lambda event, label=label_esercc3[i]: on_image_click(label))
                label_states[label_esercc3[i]] = "not_pressed"
                label_esercc3[i].pack()
                label_clickk3[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk3[i]] = "not_pressed"
                label_clickk3[i].bind("<Button-1>", lambda event, label=label_clickk3[i]: on_image_click2(label))
                label_clickk3[i].pack()
                i = i + 1
            buttone7.pack(padx=100,pady=5)
        if (doman3 == 3):
            global fullwork
            #global full
            fullwork[full] = "ALZATE LATERALI BUSTO 90° 2 MANUBRI"
            scelta4()



def scelta4():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    i = 0
    try:
       buttone7.pack_forget()
       labelSpalle.pack_forget()
       if (doman3 == 1):
           while (i < limiter5):
               label_eserc3[i].destroy()
               label_click3[i].destroy()
               i = i + 1
       if (doman3 == 2 or doman3 == 3):
           while (i < limiter6):
               label_esercc3[i].destroy()
               label_clickk3[i].destroy()
               i = i + 1

    except:
        i=0

    labelBicipiti.pack(padx=100, pady=5)
    i = 0
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter7):
                # bellim = label_eserc[i]
                label_eserc4[i] = tk.Label(app, image=Uncheck, text=bicipiti_easy[i], compound="left")
                label_eserc4[i].bind("<Button-1>", lambda event, label=label_eserc4[i]: on_image_click(label))
                label_states[label_eserc4[i]] = "not_pressed"
                label_eserc4[i].pack()
                label_click4[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click4[i]] = "not_pressed"
                label_click4[i].bind("<Button-1>", lambda event, label=label_click4[i]: on_image_click2(label))
                label_click4[i].pack()
                i = i + 1
            buttone8.pack(padx=100,pady=5)
        if (doman3 == 2 or doman3==3):
            while (i < limiter8):
                # bellim = label_eserc[i]
                label_esercc4[i] = tk.Label(app, image=Uncheck, text=bicipiti_intermedio[i], compound="left")
                label_esercc4[i].bind("<Button-1>", lambda event, label=label_esercc4[i]: on_image_click(label))
                label_states[label_esercc4[i]] = "not_pressed"
                label_esercc4[i].pack()
                label_clickk4[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk4[i]] = "not_pressed"
                label_clickk4[i].bind("<Button-1>", lambda event, label=label_clickk4[i]: on_image_click2(label))
                label_clickk4[i].pack()
                i = i + 1
            buttone8.pack(padx=100,pady=5)



def scelta5():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    i = 0
    buttone8.pack_forget()
    labelBicipiti.pack_forget()
    if (doman3 == 1):
        while (i < limiter7):
            label_eserc4[i].destroy()
            label_click4[i].destroy()
            i = i + 1
    if (doman3 == 2 or doman3 == 3):
        while (i < limiter8):
            label_esercc4[i].destroy()
            label_clickk4[i].destroy()
            i = i + 1
    i = 0
    labelTricipiti.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter9):
                # bellim = label_eserc[i]
                label_eserc5[i] = tk.Label(app, image=Uncheck, text=tricipiti_easy[i], compound="left")
                label_eserc5[i].bind("<Button-1>", lambda event, label=label_eserc5[i]: on_image_click(label))
                label_states[label_eserc5[i]] = "not_pressed"
                label_eserc5[i].pack()
                label_click5[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click5[i]] = "not_pressed"
                label_click5[i].bind("<Button-1>", lambda event, label=label_click5[i]: on_image_click2(label))
                label_click5[i].pack()
                i = i + 1
            buttone9.pack(padx=100,pady=5)
        if (doman3 == 2 or doman3==3):
            while (i < limiter10):
                # bellim = label_eserc[i]
                label_esercc5[i] = tk.Label(app, image=Uncheck, text=tricipiti_intermedio[i], compound="left")
                label_esercc5[i].bind("<Button-1>", lambda event, label=label_esercc5[i]: on_image_click(label))
                label_states[label_esercc5[i]] = "not_pressed"
                label_esercc5[i].pack()
                label_clickk5[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk5[i]] = "not_pressed"
                label_clickk5[i].bind("<Button-1>", lambda event, label=label_clickk5[i]: on_image_click2(label))
                label_clickk5[i].pack()
                i = i + 1
            buttone9.pack(padx=100,pady=5)


def scelta6():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    i = 0
    labelTricipiti.pack_forget()
    buttone9.pack_forget()
    if (doman3 == 1):
        while (i < limiter9):
            label_eserc5[i].destroy()
            label_click5[i].destroy()
            i = i + 1
    if (doman3 == 2 or doman3 == 3):
        while (i < limiter10):
            label_esercc5[i].destroy()
            label_clickk5[i].destroy()
            i = i + 1
    i = 0
    labelAddominali.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter11):
                # bellim = label_eserc[i]
                label_eserc6[i] = tk.Label(app, image=Uncheck, text=addominali_easy[i], compound="left")
                label_eserc6[i].bind("<Button-1>", lambda event, label=label_eserc6[i]: on_image_click(label))
                label_states[label_eserc6[i]] = "not_pressed"
                label_eserc6[i].pack()
                label_click6[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click6[i]] = "not_pressed"
                label_click6[i].bind("<Button-1>", lambda event, label=label_click6[i]: on_image_click2(label))
                label_click6[i].pack()
                i = i + 1
            buttone10.pack(padx=100,pady=5)
        if (doman3 == 2):
            while (i < limiter12):
                # bellim = label_eserc[i]
                label_esercc6[i] = tk.Label(app, image=Uncheck, text=addominali_intermedio[i], compound="left")
                label_esercc6[i].bind("<Button-1>", lambda event, label=label_esercc6[i]: on_image_click(label))
                label_states[label_esercc6[i]] = "not_pressed"
                label_esercc6[i].pack()
                label_clickk6[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk6[i]] = "not_pressed"
                label_clickk6[i].bind("<Button-1>", lambda event, label=label_clickk6[i]: on_image_click2(label))
                label_clickk6[i].pack()
                i = i + 1
            buttone10.pack(padx=100,pady=5)
        if (doman3==3):
            while (i < limiter13):
                # bellim = label_eserc[i]
                label_eserccc6[i] = tk.Label(app, image=Uncheck, text=addominali_avanzato[i], compound="left")
                label_eserccc6[i].bind("<Button-1>", lambda event, label=label_eserccc6[i]: on_image_click(label))
                label_states[label_eserccc6[i]] = "not_pressed"
                label_eserccc6[i].pack()
                label_clickkk6[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickkk6[i]] = "not_pressed"
                label_clickkk6[i].bind("<Button-1>", lambda event, label=label_clickkk6[i]: on_image_click2(label))
                label_clickkk6[i].pack()
                i = i + 1
            buttone10.pack(padx=100,pady=5)


def scelta7():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    i = 0
    buttone10.pack_forget()
    labelAddominali.pack_forget()
    if (doman3 == 1):
        while (i < limiter11):
            label_eserc6[i].destroy()
            label_click6[i].destroy()
            i = i + 1
    if (doman3 == 2):
        while (i < limiter12):
            label_esercc6[i].destroy()
            label_clickk6[i].destroy()
            i = i + 1
    if (doman3 == 3):
        while (i < limiter13):
            label_eserccc6[i].destroy()
            label_clickkk6[i].destroy()
            i = i + 1
    i = 0
    labelQuadricipiti.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter14):
                # bellim = label_eserc[i]
                label_eserc7[i] = tk.Label(app, image=Uncheck, text=quadricipiti_easy[i], compound="left")
                label_eserc7[i].bind("<Button-1>", lambda event, label=label_eserc7[i]: on_image_click(label))
                label_states[label_eserc7[i]] = "not_pressed"
                label_eserc7[i].pack()
                label_click7[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click7[i]] = "not_pressed"
                label_click7[i].bind("<Button-1>", lambda event, label=label_click7[i]: on_image_click2(label))
                label_click7[i].pack()
                i = i + 1
            buttone11.pack(padx=100,pady=5)
        if (doman3 == 2):
            while (i < limiter15):
                # bellim = label_eserc[i]
                label_esercc7[i] = tk.Label(app, image=Uncheck, text=quadricipiti_intermedio[i], compound="left")
                label_esercc7[i].bind("<Button-1>", lambda event, label=label_esercc7[i]: on_image_click(label))
                label_states[label_esercc7[i]] = "not_pressed"
                label_esercc7[i].pack()
                label_clickk7[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk7[i]] = "not_pressed"
                label_clickk7[i].bind("<Button-1>", lambda event, label=label_clickk7[i]: on_image_click2(label))
                label_clickk7[i].pack()
                i = i + 1
            buttone11.pack(padx=100,pady=5)
        if (doman3==3):
            while (i < limiter16):
                # bellim = label_eserc[i]
                label_eserccc7[i] = tk.Label(app, image=Uncheck, text=quadricipiti_avanzato[i], compound="left")
                label_eserccc7[i].bind("<Button-1>", lambda event, label=label_eserccc7[i]: on_image_click(label))
                label_states[label_eserccc7[i]] = "not_pressed"
                label_eserccc7[i].pack()
                label_clickkk7[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickkk7[i]] = "not_pressed"
                label_clickkk7[i].bind("<Button-1>", lambda event, label=label_clickkk7[i]: on_image_click2(label))
                label_clickkk7[i].pack()
                i = i + 1
            buttone11.pack(padx=100,pady=5)


def scelta8():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    global limiter3
    global limiter4
    i = 0
    buttone11.pack_forget()
    labelQuadricipiti.pack_forget()
    if (doman3 == 1):
        while (i < limiter14):
            label_eserc7[i].destroy()
            label_click7[i].destroy()
            i = i + 1
    if (doman3 == 2):
        while (i < limiter15):
            label_esercc7[i].destroy()
            label_clickk7[i].destroy()
            i = i + 1
    if (doman3 == 3):
        while (i < limiter16):
            label_eserccc7[i].destroy()
            label_clickkk7[i].destroy()
            i = i + 1
    i = 0
    labelGlutei.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter17):
                # bellim = label_eserc[i]
                label_eserc8[i] = tk.Label(app, image=Uncheck, text=glutei_easy[i], compound="left")
                label_eserc8[i].bind("<Button-1>", lambda event, label=label_eserc8[i]: on_image_click(label))
                label_states[label_eserc8[i]] = "not_pressed"
                label_eserc8[i].pack()
                label_click8[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click8[i]] = "not_pressed"
                label_click8[i].bind("<Button-1>", lambda event, label=label_click8[i]: on_image_click2(label))
                label_click8[i].pack()
                i = i + 1
            buttone12.pack(padx=100,pady=5)
        if (doman3 == 2):
            while (i < limiter18):
                # bellim = label_eserc[i]
                label_esercc8[i] = tk.Label(app, image=Uncheck, text=glutei_intermedio[i], compound="left")
                label_esercc8[i].bind("<Button-1>", lambda event, label=label_esercc8[i]: on_image_click(label))
                label_states[label_esercc8[i]] = "not_pressed"
                label_esercc8[i].pack()
                label_clickk8[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickk8[i]] = "not_pressed"
                label_clickk8[i].bind("<Button-1>", lambda event, label=label_clickk8[i]: on_image_click2(label))
                label_clickk8[i].pack()
                i = i + 1
            buttone12.pack(padx=100,pady=5)
        if (doman3 == 3):
            global fullwork
            #global full
            fullwork[full] = "ALZATE GAMBE STABILITY BALL"
            scelta9()


def scelta9():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    global limiter3
    global limiter4
    i = 0
    buttone12.pack_forget()
    labelGlutei.pack_forget()
    if (doman3 == 1):
        while (i < limiter17):
            label_eserc8[i].destroy()
            label_click8[i].destroy()
            i = i + 1
    if (doman3 == 2 or doman3 == 3):
        while (i < limiter18):
            label_esercc8[i].destroy()
            label_clickk8[i].destroy()
            i = i + 1
    i = 0
    labelPolpacci.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter19):
                # bellim = label_eserc[i]
                label_eserc9[i] = tk.Label(app, image=Uncheck, text=polpacci_easy[i], compound="left")
                label_eserc9[i].bind("<Button-1>", lambda event, label=label_eserc9[i]: on_image_click(label))
                label_states[label_eserc9[i]] = "not_pressed"
                label_eserc9[i].pack()
                label_click9[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click9[i]] = "not_pressed"
                label_click9[i].bind("<Button-1>", lambda event, label=label_click9[i]: on_image_click2(label))
                label_click9[i].pack()
                i = i + 1
            buttone13.pack(padx=100,pady=5)
        if (doman3 == 3 or doman3 == 2):
            global fullwork
            #global full
            fullwork[full] = "CALF BILANCIERE CON RIALZO IN PIEDI"
            scelta10()

def scelta10():
    canvas.yview_moveto(0.0)
    global full
    full = full + 1
    global i
    global limiter3
    global limiter4
    i = 0
    try:
      labelPolpacci.pack_forget()
      buttone13.pack_forget()
      if (doman3 == 1):
          while (i < limiter19):
              label_eserc9[i].destroy()
              label_click9[i].destroy()
              i = i + 1
    except:
      i=0
    i = 0
    labelAvambracci.pack(padx=100, pady=5)
    if (doman1 != 0):
        if (doman3 == 1):
            while (i < limiter20):
                # bellim = label_eserc[i]
                label_eserc10[i] = tk.Label(app, image=Uncheck, text=avambracci_easy[i], compound="left")
                label_eserc10[i].bind("<Button-1>", lambda event, label=label_eserc10[i]: on_image_click(label))
                label_states[label_eserc10[i]] = "not_pressed"
                label_eserc10[i].pack()
                label_click10[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_click10[i]] = "not_pressed"
                label_click10[i].bind("<Button-1>", lambda event, label=label_click10[i]: on_image_click2(label))
                label_click10[i].pack()
                i = i + 1
            buttone14.pack(padx=100,pady=5)
        if (doman3 == 3 or doman3 == 2):
            global fullwork
            #global full
            label_avambracci1.bind("<Button-1>", lambda event, label=label_avambracci1: on_image_click(label))
            label_states[label_avambracci1] = "not_pressed"
            label_avambracci1.pack()
            label_states[label_avamclick1] = "not_pressed"
            label_avamclick1.bind("<Button-1>", lambda event, label=label_avamclick1: on_image_click2(label))
            label_avamclick1.pack()
            label_avambracci2.bind("<Button-1>", lambda event, label=label_avambracci2: on_image_click(label))
            label_states[label_avambracci2] = "not_pressed"
            label_avambracci2.pack()
            label_states[label_avamclick2] = "not_pressed"
            label_avamclick2.bind("<Button-1>", lambda event, label=label_avamclick2: on_image_click2(label))
            label_avamclick2.pack()
            buttone14.pack(padx=100, pady=5)
            #fullwork[full] = "CALF BILANCIERE CON RIALZO IN PIEDI"
            #full = full + 1

def final_results():
    canvas.yview_moveto(0.0)
    i=0
    global full
    global nome
    global difficolta
    full=full+1
    difficolta="1"
    buttone14.pack_forget()
    labelAvambracci.pack_forget()
    if (doman3 == 1):
        while (i < limiter20):
            label_eserc10[i].destroy()
            label_click10[i].destroy()
            difficolta="Facile"
            i = i + 1
    if (doman3 == 2 or doman3 == 3):
        label_avambracci1.pack_forget()
        label_avambracci2.pack_forget()
        label_avamclick1.pack_forget()
        label_avamclick2.pack_forget()
        if (doman3 == 2):
            difficolta = "Medio"
        if (doman3 == 3):
            difficolta = "Difficile"

    i=0
    if (full==10 and doman1<=2):
       with onto:
        corsa = Utente()
        corsa.Utente.append(nome)
        #corsa.Difficolta.append(difficolta)
        corsa.Utente = [nome]
        #corsa.Preferenze.append(preferenze)
        corsa.Legamenti = [legamenti]
        corsa.Difficolta = [difficolta]
        corsa.Preferenze = [preferenze]
        corsa.Legamenti = [legamenti]
        corsa.Giorni = [giorno]
        corsa.Nome.append(nome)
        corsa.Nome.append(difficolta)
        corsa.Nome.append(preferenze)
        corsa.Nome.append(legamenti)
        corsa.Nome.append(giorno)

       onto.save()
    if(doman1==1):
        labelTuttoilcorpo.pack(padx=100, pady=5)
        while(i<=full-1):
           label_fullwork[i] = tk.Label(app, text=fullwork[i])
           if(label_fullwork[i] != tk.Label(app, text="1")):
               label_fullwork[i].pack(padx=100, pady=5)
               label_clickfull[i] = tk.Label(app, image=Immagine, compound="right")
               label_states[label_clickfull[i]] = "not_pressed"
               label_clickfull[i].bind("<Button-1>", lambda event, label=label_clickfull[i]: on_image_click2(label))
               label_clickfull[i].pack()
               with onto:
                 #corsa = Utente()
                 #corsa.Utente.append(nome)
                 corsa.Nome.append(str(i) + ")" + fullwork[i])
                 #corsa.Difficolta.append(difficolta)
                 #corsa.Utente = [nome]
                 #corsa.Nome+=[fullwork[i]]
                 #corsa.Difficolta = [difficolta]
               onto.save()
           i=i+1

    if (doman1 == 2):
        labelParteInferiore.pack(padx=100, pady=5)
        while (i <= full-1):
            label_fullwork[i] = tk.Label(app, text=fullwork[i])
            if (label_fullwork[i] != tk.Label(app, text="1")):
                label_fullwork[i].pack(padx=100, pady=5)
                label_clickfull[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull[i]] = "not_pressed"
                label_clickfull[i].bind("<Button-1>", lambda event, label=label_clickfull[i]: on_image_click2(label))
                label_clickfull[i].pack()
                with onto:
                    #corsa = Utente()
                    #corsa.Utente.append(nome)
                    corsa.Nome.append(str(i) + ")" + fullwork[i])
                    #corsa.Difficolta.append(difficolta)
                    #corsa.Utente = [nome]
                    #corsa.Nome+=[fullwork[i]]
                    #corsa.Difficolta = [difficolta]
                onto.save()
            i = i + 1
            if (i==5):
                labelParteSuperiore.pack(padx=100, pady=5)
    if(doman1>2 and full==10):
        labelAvviso.pack(padx=0, pady=5)
        scelta()
    i=0
    if (doman1>2 and full > 11):
        labelAvviso.destroy()

        with onto:
            corsa = Utente()
            corsa.Utente.append(nome)
            # corsa.Difficolta.append(difficolta)
            corsa.Utente = [nome]
            # corsa.Preferenze.append(preferenze)
            corsa.Legamenti = [legamenti]
            corsa.Difficolta = [difficolta]
            corsa.Preferenze = [preferenze]
            corsa.Legamenti = [legamenti]
            corsa.Giorni = [giorno]
            corsa.Nome.append(nome)
            corsa.Nome.append(difficolta)
            corsa.Nome.append(preferenze)
            corsa.Nome.append(legamenti)
            corsa.Nome.append(giorno)
        onto.save()
        b=0
        print(fullwork)
        while(fullwork[b]!="1"):
            corsa.Nome.append(str(b) + ")" + fullwork[b])
            b=b+1
            onto.save()

        if (doman1 == 3 or doman1 == 5 or doman1 == 7):
            labelTuttoilcorpo.pack(padx=100, pady=5)
        if (doman1 == 4 or doman1 == 6):
            labelTuttoilcorpo2.pack(padx=100, pady=5)
        while (i <= 9):
            label_fullwork[i] = tk.Label(app, text=fullwork[i])
            if (label_fullwork[i] != tk.Label(app, text="1")):
                label_fullwork[i].pack(padx=100, pady=5)
                label_clickfull[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull[i]] = "not_pressed"
                label_clickfull[i].bind("<Button-1>", lambda event, label=label_clickfull[i]: on_image_click2(label))
                label_clickfull[i].pack()
                #with onto:
                    #corsa = Utente()
                    #corsa.Utente.append(nome)
                    #corsa.Nome.append(fullwork[i])
                    #corsa.Difficolta.append(difficolta)
                    #corsa.Utente = [nome]
                    #corsa.Nome+=[fullwork[i]]
                    #corsa.Difficolta = [difficolta]
                #onto.save()
            i = i + 1
        if(doman1==3 or doman1==4):
           labelParteInferiore.pack(padx=100, pady=5)
        if (doman1 == 5 or doman1 == 6):
            labelParteInferiore2.pack(padx=100, pady=5)
        if (doman1 == 7):
            labelParteInferiore3.pack(padx=100, pady=5)
        #i=9
        while (i <= full-1):
            label_fullwork[i] = tk.Label(app, text=fullwork[i])
            if (label_fullwork[i] != tk.Label(app, text="1")):
                label_fullwork[i].pack(padx=100, pady=5)
                label_clickfull[i] = tk.Label(app, image=Immagine, compound="right")
                label_states[label_clickfull[i]] = "not_pressed"
                label_clickfull[i].bind("<Button-1>", lambda event, label=label_clickfull[i]: on_image_click2(label))
                label_clickfull[i].pack()
                #with onto:
                    #corsa = Utente()
                    #corsa.Utente.append(nome)
                    #corsa.Nome.append(fullwork[i])
                    #corsa.Difficolta.append(difficolta)
                    #corsa.Utente = [nome]
                    #corsa.Nome+=[fullwork[i]]
                    #corsa.Difficolta = [difficolta]
                #onto.save()
            i = i + 1
            if (i == 15):
                if (doman1 == 3 or doman1 == 4):
                    labelParteSuperiore.pack(padx=100, pady=5)
                if (doman1 == 5 or doman1 == 6):
                    labelParteSuperiore2.pack(padx=100, pady=5)
                if (doman1 == 7):
                    labelParteSuperiore3.pack(padx=100, pady=5)
    i=0




button = tk.Button(app, text="Inserisci", command=on_button_clicks)
button.pack(padx=435,pady=5)


buttone = tk.Button(app,text="Avanti", command=domanda2)
buttone2 = tk.Button(app,text="Avanti", command=domanda3)
buttone3 = tk.Button(app, text="Avanti", command=domanda4)
buttone4 = tk.Button(app, text="Avanti", command=domanda5)
buttone4_5 = tk.Button(app, text="Avanti", command=scelta)
buttone4_55 = tk.Button(app, text="Avanti", command=Owl)
buttone5 = tk.Button(app, text="Avanti", command=scelta2)
buttone6 = tk.Button(app, text="Avanti", command=scelta3)
buttone7 = tk.Button(app, text="Avanti", command=scelta4)
buttone8 = tk.Button(app, text="Avanti", command=scelta5)
buttone9 = tk.Button(app, text="Avanti", command=scelta6)
buttone10 = tk.Button(app, text="Avanti", command=scelta7)
buttone11 = tk.Button(app, text="Avanti", command=scelta8)
buttone12 = tk.Button(app, text="Avanti", command=scelta9)
buttone13 = tk.Button(app, text="Avanti", command=scelta10)
buttone14 = tk.Button(app, text="Avanti", command=final_results)
labelGiorni = tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")
label_status1 = tk.Label(app, image=Uncheck, text="Un giorno", compound="left")
label_eserc = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc3 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc3 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc4 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc4 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc5 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc5 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserccc6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserccc7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc8 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_esercc8 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc9 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_eserc10 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_fullwork = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_fullwork2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click3 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click4 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click5= [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click8 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click9 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_click10 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk3 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk4 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk5 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickk8 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickkk6 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickkk7 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickfull = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_clickfull2 = [tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?"),tk.Label(app, text="Quanti giorni alla settimana vorresti fare workout?")]
label_status2 = tk.Label(app, image=Uncheck, text="Due giorni", compound="left")
label_status3 = tk.Label(app, image=Uncheck, text="Tre giorni", compound="left")
label_status4 = tk.Label(app, image=Uncheck, text="Quattro giorni", compound="left")
label_status5 = tk.Label(app, image=Uncheck, text="Cinque giorni", compound="left")
label_status6 = tk.Label(app, image=Uncheck, text="Sei giorni", compound="left")
label_status7 = tk.Label(app, image=Uncheck, text="Una settimana", compound="left")
labelDieta = tk.Label(app, text="Hai problemi alle articolazione o ai legamenti?")
label_status8 = tk.Label(app, image=Uncheck, text="Si", compound="left")
label_status9 = tk.Label(app, image=Uncheck, text="No", compound="left")
labelEsperienza = tk.Label(app, text="E la tua esperienza con la palestra?")
label_status10 = tk.Label(app, image=Uncheck, text="Sono alle prime armi", compound="left")
label_status11 = tk.Label(app, image=Uncheck, text="Ho già un pò di esperienza", compound="left")
label_status12 = tk.Label(app, image=Uncheck, text="Ho molta esperienza", compound="left")
labelObbiettivo = tk.Label(app, text="Qual'è il tuo obbiettivo?")
label_status13 = tk.Label(app, image=Uncheck, text="Forza", compound="left")
label_status14 = tk.Label(app, image=Uncheck, text="Bodybuilding", compound="left")
label_status15 = tk.Label(app, image=Uncheck, text="Flessibilità", compound="left")
label_status16 = tk.Label(app, image=Uncheck, text="Potenza", compound="left")
labelOwl = tk.Label(app, text="Come vuoi procedere?")
label_status17 = tk.Label(app, image=Uncheck, text="Vuoi Eseguire il questionario?", compound="left")
label_status18 = tk.Label(app, image=Uncheck, text="O vuoi un consiglio in base alle tue preferenze?", compound="left")
label_avambracci1 = tk.Label(app, image=Uncheck, text="CURL HAMMER AI CAVI CON CORDA", compound="left")
label_avambracci2 = tk.Label(app, image=Uncheck, text="CURL INVERSO BILANCIERE IN PIEDI", compound="left")
label_avamclick1 = tk.Label(app, image=Immagine, compound="right")
label_avamclick2 = tk.Label(app, image=Immagine, compound="right")
labelParteSuperiore = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte superiore del corpo")
labelParteInferiore = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte inferiore del corpo")
labelTuttoilcorpo = tk.Label(app, text="Ecco il workout per il giorno dedicato a tutto il corpo")
labelTuttoilcorpo2 = tk.Label(app, text="Ecco il workout per il giorno dedicato a tutto il corpo (per due giorni)")
labelParteSuperiore2 = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte superiore del corpo (per due giorni)")
labelParteInferiore2 = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte inferiore del corpo (per due giorni)")
labelParteSuperiore3 = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte superiore del corpo (per tre giorni)")
labelParteInferiore3 = tk.Label(app, text="Ecco il workout per il giorno dedicato alla parte inferiore del corpo (per tre giorni)")
labelAvviso = tk.Label(app, text="Passiamo alla parte del questionario relativa ai giorni dedicati alla parte superiore e inferiore del corpo")
labelPettorali = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei pettorali")
labelDorsali = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dorsale")
labelSpalle = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento delle spalle")
labelBicipiti = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei bicipiti")
labelTricipiti = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei tricipiti")
labelAddominali = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento degli addominali")
labelQuadricipiti = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei quadricipiti")
labelGlutei = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei glutei")
labelPolpacci = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento dei polpacci")
labelAvambracci = tk.Label(app, text="Seleziona l'esercizio che preferisci relativo all'allenamento degli avambracci")





#buttone.pack()
if (pale==1):
    domandestar=1
if (domandestar==1):
    label = tk.Label(app, text="Rispondi a questa domanda")
    label.pack()
    label_status = tk.Label(app, image=Uncheck,text="Testo se si",compound="left")
    label_status.pack()
    label_status.bind("<Button-1>", lambda event, label=label_status: on_image_click(label))
    label_states[label_status] = "not_pressed"


    label_status2 = tk.Label(app, image=Uncheck,text="Testo se si",compound="left")
    label_status2.pack()
    label_status2.bind("<Button-1>", lambda event, label=label_status2: on_image_click(label))
    label_states[label_status2] = "not_pressed"


with urlopen("https://www.evolutionfit.it/esercizi/pettorali/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


with urlopen("https://www.evolutionfit.it/esercizi/pettorali/page/2/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/pettorali/page/3/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/pettorali/page/4/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           pettorali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            pettorali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
while(pettorali_intermedio[i]!="1"):
    print(pettorali_intermedio[i])
    i=i+1
    if (pettorali_intermedio[i] == "1"):
        # global limiter
        limiter2 = i
print(" ")
while(pettorali_easy[j]!="1"):
    print(pettorali_easy[j])
    j=j+1
    if(pettorali_easy[j]=="1"):
       #global limiter
       limiter = j
i=0
j=0


with urlopen("https://www.evolutionfit.it/esercizi/dorsali/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/dorsali/page/2/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


with urlopen("https://www.evolutionfit.it/esercizi/dorsali/page/3/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


with urlopen("https://www.evolutionfit.it/esercizi/dorsali/page/4/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           dorsali_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            dorsali_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
print(" ")
while(dorsali_intermedio[i]!="1"):
    print(dorsali_intermedio[i])
    i=i+1
    if (dorsali_intermedio[i] == "1" or dorsali_intermedio[i] == "11"):
        # global limiter
         limiter4 = i


print(" ")
while(dorsali_easy[j]!="1"):
    print(dorsali_easy[j])
    j=j+1
    if (dorsali_easy[j] == "1"):
        # global limiter
        limiter3 = j

i=0
j=0

print("spalle")

with urlopen("https://www.evolutionfit.it/esercizi/spalle/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/2/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/3/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/4/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/5/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/6/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/spalle/page/7/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           spalle_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            spalle_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

i=0
j=0
print(" ")
while(spalle_intermedio[i]!="1"):
    print(spalle_intermedio[i])
    i=i+1
    if (spalle_intermedio[i]=="1"):
        limiter6=i
print(" ")
while(spalle_easy[j]!="1"):
    print(spalle_easy[j])
    j=j+1
    if (spalle_easy[j]=="1"):
        limiter5=j

i=0
j=0


with urlopen("https://www.evolutionfit.it/esercizi/bicipiti") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/bicipiti/page/2/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/bicipiti/page/3/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           bicipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            bicipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
print(" ")
while(bicipiti_intermedio[i]!="1"):
    print(bicipiti_intermedio[i])
    i=i+1
    if (bicipiti_intermedio[i]=="1"):
        limiter8=i
print(" ")
while(bicipiti_easy[j]!="1"):
    print(bicipiti_easy[j])
    j=j+1
    if (bicipiti_easy[j]=="1"):
        limiter7=j

i=0
j=0


with urlopen("https://www.evolutionfit.it/esercizi/tricipiti") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/tricipiti/page/2/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break

with urlopen("https://www.evolutionfit.it/esercizi/tricipiti/page/3/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           tricipiti_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            tricipiti_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
print("trici")
while(tricipiti_intermedio[i]!="1"):
    print(tricipiti_intermedio[i])
    i=i+1
    if(tricipiti_intermedio[i]=="1"):
        limiter10=i
print(" ")
while(tricipiti_easy[j]!="1"):
    print(tricipiti_easy[j])
    j=j+1
    if (tricipiti_easy[j] == "1"):
        limiter9 = j

i=0
j=0
urlprova="https://www.evolutionfit.it/esercizi/addominali/page/1/"
gg=0
while(urlprova!="https://www.evolutionfit.it/esercizi/addominali/page/11/"):

    with urlopen(urlprova) as response:

      soup = BeautifulSoup(response, 'html.parser')
      for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
          # print(i)
          bellino=0
          belluno=0
          bellano=0
          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              bellino=1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              bellino=2

          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              belluno = 1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              belluno = 2
          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Avanzato" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              bellano = 1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              bellano = 2
          if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
             addominali_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
          if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
             addominali_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
          if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
              addominali_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
          if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
              addominali_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
          if (bellano==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Avanzato"):
              addominali_avanzato[z] = anchor.next_element.text
              z = z + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
          if (bellano==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Avanzato"):
              addominali_avanzato[z] = anchor.next_element.text
              z = z + 1
            # print(anchor.next_element.text)


          if (i == 200):
              break
    gg=gg+1
    g=str(gg)
    urlprova="https://www.evolutionfit.it/esercizi/addominali/page/"+ g + "/"


i=0
j=0
z=0
print("medio")
while(addominali_intermedio[i]!="1"):
    print(addominali_intermedio[i])
    i=i+1
    if (addominali_intermedio[i] == "1"):
        limiter12=i
print("facile")
while(addominali_easy[j]!="1"):
    print(addominali_easy[j])
    j=j+1
    if (addominali_easy[j] == "1"):
        limiter11=j
print("avanz")
while(addominali_avanzato[z]!="1"):
    print(addominali_avanzato[z])
    z=z+1
    if (addominali_avanzato[z] == "1"):
        limiter13=z

i=0
j=0
z=0
urlprova2="https://www.evolutionfit.it/esercizi/quadricipiti/page/1/"
gg=0


while(urlprova2!="https://www.evolutionfit.it/esercizi/quadricipiti/page/8/"):

    with urlopen(urlprova2) as response:

      soup = BeautifulSoup(response, 'html.parser')
      for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
          # print(i)
          bellino=0
          belluno=0
          bellano=0
          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              bellino=1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              bellino=2

          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              belluno = 1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              belluno = 2
          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Avanzato" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              bellano = 1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              bellano = 2
          if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
             quadricipiti_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
          if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
             quadricipiti_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
          if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
              quadricipiti_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
          if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
              quadricipiti_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
          if (bellano==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Avanzato"):
              quadricipiti_avanzato[z] = anchor.next_element.text
              z = z + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
          if (bellano==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Avanzato"):
              quadricipiti_avanzato[z] = anchor.next_element.text
              z = z + 1
            # print(anchor.next_element.text)


          if (i == 200):
              break
    gg=gg+1
    g=str(gg)
    urlprova2="https://www.evolutionfit.it/esercizi/quadricipiti/page/"+ g + "/"


i=0
j=0
z=0
print("medio")
while(quadricipiti_intermedio[i]!="1"):
    print(quadricipiti_intermedio[i])
    i=i+1
    if (quadricipiti_intermedio[i] == "1"):
        limiter15=i
print("facile")
while(quadricipiti_easy[j]!="1"):
    print(quadricipiti_easy[j])
    j=j+1
    if (quadricipiti_easy[j] == "1"):
        limiter14=j
print("avanz")
while(quadricipiti_avanzato[z]!="1"):
    print(quadricipiti_avanzato[z])
    z=z+1
    if (quadricipiti_avanzato[z] == "1"):
        limiter16=z

i=0
j=0
z=0


urlprova3="https://www.evolutionfit.it/esercizi/glutei/page/1/"
gg=0


while(urlprova3!="https://www.evolutionfit.it/esercizi/glutei/page/4/"):

    with urlopen(urlprova3) as response:

      soup = BeautifulSoup(response, 'html.parser')
      for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
          # print(i)
          bellino=0
          belluno=0
          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              bellino=1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              bellino=2

          if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
              belluno = 1
          else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
              belluno = 2
          if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
             glutei_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
          if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
             glutei_intermedio[i] = anchor.next_element.text
             i = i + 1
           #print(anchor.next_element.text)
          if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
              glutei_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
          if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
              glutei_easy[j] = anchor.next_element.text
              j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.next_element.text)


          if (i == 200):
              break
    gg=gg+1
    g=str(gg)
    urlprova3="https://www.evolutionfit.it/esercizi/glutei/page/"+ g + "/"


i=0
j=0
z=0
print("glumedio")
while(glutei_intermedio[i]!="1"):
    print(glutei_intermedio[i])
    i=i+1
    if (glutei_intermedio[i] == "1"):
        limiter18=i
print("glufacile")
while(glutei_easy[j]!="1"):
    print(glutei_easy[j])
    j=j+1
    if (glutei_easy[j] == "1"):
        limiter17 = j

i=0
j=0
z=0


with urlopen("https://www.evolutionfit.it/esercizi/polpacci/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            bellino=1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            bellino=2

        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
        if(bellino==1 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Intermedio"):
           polpacci_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
           #print(anchor.find_next("a").text)
        if(bellino==2 and anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text=="Intermedio"):
           polpacci_intermedio[i] = anchor.next_element.text
           i = i + 1
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            polpacci_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            polpacci_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
print("polp")
while(polpacci_easy[j]!="1"):
    print(polpacci_easy[j])
    j=j+1
    if (polpacci_easy[j] == "1"):
        limiter19=j


i=0
j=0

with urlopen("https://www.evolutionfit.it/esercizi/avambracci/") as response:

    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all("h2",class_="entry-title fusion-post-title"):
        # print(i)
        bellino=0
        belluno=0
        if (anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile" or anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text=="Facile"):
            #print(anchor.find_next("span",class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text)
            belluno = 1
        else:
            #print(anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text)
            belluno = 2
           #print(anchor.next_element.text)
        if (belluno==1 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").text == "Facile"):
            avambracci_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)
            # print(anchor.find_next("a").text)
        if (belluno==2 and anchor.find_next("span", class_="fusion-inline-sep").next_element.find_next("a").find_next("a").find_next("a").text == "Facile"):
            avambracci_easy[j] = anchor.next_element.text
            j = j + 1
            # print(anchor.next_element.text)


        if (i == 200):
            break


i=0
j=0
print("avambra")
while(avambracci_easy[j]!="1"):
    print(avambracci_easy[j])
    j=j+1
    if (avambracci_easy[j] == "1"):
        limiter20=j

i=0
j=0

onto_path.append("C:/Users/Vanni/PycharmProjects/pythonProject")
onto = get_ontology("http://www.w3.org/2002/07/owl#Thing").load()
onto.save(file="owl#Thing.owl", format="rdfxml")

file_path = "C:/Users/Vanni/PycharmProjects/pythonProject/owl#Thing.owl"
into = get_ontology(file_path).load()


with onto:
    class Esercizi(Thing):
        pass

    class Utente(Property):
        domain = [Esercizi]
        range = [str]

    class Nome(Property):
        domain = [Esercizi]
        range = [str]
        multiple = True

    class Tipologia(Property):
        domain = [Esercizi]
        range = [str]

    class Difficolta(Property):
        domain = [Esercizi]
        range = [str]

    class Preferenze(Property):
        domain = [Esercizi]
        range = [str]

    class Legamenti(Property):
        domain = [Esercizi]
        range = [str]

    class Giorni(Property):
        domain = [Esercizi]
        range = [str]


onto.save()
human_results = onto.search(label ="Nome" , _case_sensitive = False)
global cosetto
cosetto=0
for individuo in onto.individuals():
    for prop in individuo.get_properties():
        for value in prop[individuo]:
            if(prop.python_name=="Difficolta" and value=="Facile"):
                cosetto=1
            if (prop.python_name == "Difficolta" and value == "Medio"):
                cosetto = 2
            if (prop.python_name == "Difficolta" and value == "Difficile"):
                cosetto = 3
            if(cosetto==1):
               print(".%s == %s" % (prop.python_name, value))
    #print(individuo.get_properties().python_name)
    #if 'Medio' in individuo.annotations:
        #etichetta = individuo.annotations['Medio'][0]
        #print(f"Individuo: {individuo}, Etichetta: {etichetta}")






app.mainloop()