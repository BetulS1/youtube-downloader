from tkinter import *  
import tkinter as tk 
from pytube import YouTube 

#** Gerekli kütüphaneler :  pip install tk ve pip install pytube *#

def download_function():
    video = YouTube(str(link.get())) #link 
    video = video.streams.filter(file_extension = 'mp4').get_by_itag(var.get()) #video kalitesi 720p ve mp4 format
    video.download(output_path = str(file_url.get())) #indirme yapılacak dosya url
    Label(window, text="*Video İndirildi*", font="arial 14", fg="#FF0000").place(x=280, y=210) 


#tkinter uı penceresi 
window=tk.Tk(className='Youtube Downloader') ##pencere başlığı
window.geometry("700x350") ##boyutu
window.configure(bg='#66CDAA')##pencere rengi
window.resizable(width=FALSE, height=FALSE) ##pecrenin boyutu kullanıcı tarafından değiştirilemez
#başlık 
Label(window, text="Youtube Video Downloader", font='san-serif 14 bold', bg= "#66CDAA", fg="#191970").place(x=220, y=25)
link = StringVar() 
Label(window, text=" Youtube Link", font='san-serif 10 bold').place(x=10, y=85)
#link giriş alanı input box
link_enter = Entry(window, width=70,  font='san-serif 11 ', textvariable=link).place(x=109, y=85)
Label(window, text="Video Kalitesi", font='san-serif 10 bold').place(x=10, y=122)
var = IntVar()
#video kalitesi radiobutton
R1 = Radiobutton(window, text="720p", variable=var,font='san-serif 10 ', value=22).place(x=110, y=120)
R2 = Radiobutton(window, text="480p", variable=var,font='san-serif 10 ', value=397).place(x=180, y=120)
R3 = Radiobutton(window, text="360p", variable=var,font='san-serif 10 ',value=18).place(x=250, y=120)
Label(window, text="İndirme Konumu", font='san-serif 10 bold').place(x=10, y=162)
file_url = StringVar() 
#dosya yolu giriş alanı input box
url_enter = Entry(window, width=67,  font='san-serif 11 ', textvariable=file_url).place(x=129, y=163)
#indirme butonu
Button(window, text='Download', font='san-serif 12 ', bg='#00CED1' ,padx=2, activebackground = 'blue', activeforeground = 'white', command=lambda: download_function()).place(x=300, y=250)
Label(window, text="İndirme İşlemi İçin Lütfen Bekleyin!", bg='#66CDAA', font="arial 12", fg="#006400").place(x=220, y=300)
window.mainloop()
