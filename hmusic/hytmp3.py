import tkinter as tk
from tkinter import font
import yt_dlp
import math
import os 
from PIL import Image,ImageTk
import pyperclip

from pathlib import Path


"""

im=Image.open("data_hytmp3/copy.png")
im=im.resize((25,25))
im.save("data_hytmp3/copy.png")


im=Image.open("data_hytmp3/cancel.png")
im=im.resize((25,25))
im.save("data_hytmp3/cancel.png")
"""





directory_path = Path("downloads")

if directory_path.is_dir():
    pass
else:
    os.makedirs("downloads", exist_ok=True)





def download():
	global url
	global can,p,mess



	ydl_opts = {
	    'format': 'bestaudio/best',
	    'ffmpeg_location': r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
	    'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}


	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])

	can.delete(mess)

	mess=can.create_text(p[2]+15,p[1]+15,text="Done!",font=("FreeMono",13),fill="#ff0000",anchor="w")

url=""
def check_song():
	global ent
	global can,ent
	global d_st
	global url

	

	if url=="":

		can.itemconfig(song,text="Enter URL!")
		d_st=0
		draw_download("Can't Download")


	else:






		try:

			with yt_dlp.YoutubeDL() as ydl:
			    info = ydl.extract_info(url, download=False)
			    

			can.itemconfig(song,text=info['title'])
			d_st=1
			draw_download("Download")
		except:
			d_st=0

			can.itemconfig(song,text="Song not found!")
			draw_download("Can't Download")



ent_v=None
def check_ent():
	global ent_v
	global url

	url=ent.get()

	if ent_v!=url:

		check_song()
		ent_v=url




	root.after(1,check_ent)

p=[]
dwd=[0,0]

def draw_download(txt):
	
	global can,dwd
	global p
	global mess

	can.delete(mess)
	can.delete(dwd[0])
	can.delete(dwd[1])

	f=font.Font(family="FreeMono",size=13)

	l=f.measure(txt)


	p=[20,150,20+30+l,180]

	ar=[]

	cx,cy=p[0]+15,p[1]+15

	a_=180
	for a in range(180):

		x=int(round(15*math.sin(math.radians(a_))+cx,0))
		y=int(round(15*math.cos(math.radians(a_))+cy,0))

		ar.append(x)
		ar.append(y)
		a_+=1


	cx,cy=p[2]-15,p[1]+15

	a_=0
	for a in range(180):

		x=int(round(15*math.sin(math.radians(a_))+cx,0))
		y=int(round(15*math.cos(math.radians(a_))+cy,0))

		ar.append(x)
		ar.append(y)
		a_+=1

	dwd[0]=can.create_polygon(ar,fill="#ff0000",outline="#ff0000")
	dwd[1]=can.create_text(p[0]+15,p[1]+15,text=txt,font=("FreeMono",13),fill="#000000",anchor="w")

d_st=0
mess=0
def can_b1(e):

	global d_st,p
	global can,mess
	global ent

	can.delete(mess)



	if d_st==1:


		r=math.sqrt((e.x-p[0]+15)**2+(e.y-p[1]+15))

		if r<=15:
			download()
			return


		r=math.sqrt((e.x-p[2]-15)**2+(e.y-p[1]+15))

		if r<=15:
			download()
			return


		if p[0]+15<=e.x<=p[2]-15:
			if p[1]<=e.y<=p[3]:

				download()
				return


	if 492-12.5<=e.x<=492+12.5:
		if 58-12.5<=e.y<=58+12.5:

			ent.delete(0,tk.END)

			ent.insert(tk.END,pyperclip.paste())


			return

	if 492+35-12.5<=e.x<=492+35+12.5:
		if 58-12.5<=e.y<=58+12.5:

			ent.delete(0,tk.END)


			return



cancel,copy=0,0
def load_im():
	global cancel,copy

	cancel=ImageTk.PhotoImage(file="data_hytmp3/cancel.png")
	copy=ImageTk.PhotoImage(file="data_hytmp3/copy.png")


w,h=550,250
root=tk.Tk()
root.geometry(f"{w}x{h}+50+50")
root.title("hytmp3")
root.iconbitmap("data_hytmp3/icon.ico")


can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_b1)

ent=tk.Entry(bg="#ff0000",fg="#000000",font=("FreeMono",13),width=50,relief="flat",highlightthickness=0,border=0)

can.create_text(20,30,text="Youtube URL",fill="#ff0000",font=("FreeMono",13),anchor="w")

ent.place(in_=root,x=20,y=50)

ent.focus_set()

song=can.create_text(20,100,text="",font=("FreeMono",13),fill="#ffff00",anchor="w")

ar=[]

load_im()

can.create_image(492,58,image=copy,anchor="c")
can.create_image(492+35,58,image=cancel,anchor="c")



check_ent()
root.mainloop()