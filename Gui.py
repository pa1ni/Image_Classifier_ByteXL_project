from tkinter import *
from PIL import ImageTk, Image  
from tkinter import filedialog
from imageai.Classification import ImageClassification 
#import image_classifier as imc
root=Tk()
root.title('𝕴𝖒𝖆𝖌𝖊 𝖈𝖑𝖆𝖘𝖘𝖎𝖋𝖎𝖊𝖗')
root.geometry("720x720+10+20")
lbl=Label(root, text="𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝕴𝖒𝖆𝖌𝖊 𝖈𝖑𝖆𝖘𝖘𝖎𝖋𝖎𝖊𝖗", fg='red',font=32)
lbl.place(x=300, y=20)
lb2=Label(root, text="𝖈𝖍𝖔𝖔𝖘𝖊 𝖙𝖍𝖊 𝖎𝖒𝖆𝖌𝖊 𝕿𝖔 𝖕𝖗𝖔𝖈𝖊𝖊𝖉", fg='blue',font=20)
lb2.place(x=75, y=100)
root.resizable(width = True, height = True)


def open_img():
    x = openfilename()
    open_img.z = x
    img = Image.open(x)  
    img = img.resize((480, 360), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img) 
    panel = Label(root, image = img) 
    panel.image = img
    panel.place(x=0,y=200)

