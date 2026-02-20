import tkinter as tk
from tkinter import font
import yt_dlp
import math
import os 
from PIL import Image,ImageTk
import pyperclip

from pathlib import Path
import threading

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
	global typ



	def progress_hook(d):
	    global can,mess,prog

	    if d['status'] == 'downloading':

	        total = d.get('total_bytes') or d.get('total_bytes_estimate')
	        downloaded = d.get('downloaded_bytes', 0)

	        if total:
	            percent = downloaded / total * 100
	        else:
	            percent = 0

	        speed = str(d.get('_speed_str', 'N/A'))
	        eta = str(d.get('_eta_str', 'N/A'))

	        #print(speed,eta)

	        #print(f"Progress: {percent:6.2f}% | Speed: {speed} | ETA: {eta}")

	        can.delete(prog[0])
	        can.delete(prog[1])


	        prog[0]=can.create_rectangle(0,int(can["height"])-30, int(can["width"]),int(can["height"]),fill="#500000",outline="#500000")
	        prog[1]=can.create_rectangle(0,int(can["height"])-30, int(can["width"])*percent/100,int(can["height"]),fill="#ff0000",outline="#ff0000")

	        can.delete(mess)
	        mess=can.create_text(int(can["width"])/2,int(can["height"])-15,text=f"{percent:6.2f}%",
	        	fill="#ffffff",font=("FreeMono",13),anchor="c")



	    elif d['status'] == 'finished':
	        can.delete(mess)
	        mess=can.create_text(int(can["width"])/2,int(can["height"])-15,text="Download Finished!",
	        	fill="#ffffff",font=("FreeMono",13),anchor="c")


	ydl_opts = {
	    'format': 'bestaudio/best',
	    'progress_hooks': [progress_hook],
	    'ffmpeg_location': r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
	    'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	    'quiet': True,
	    'no_warnings': True,
        'noprogress': True

	}


	ydl_opts_v = {
	    'format': 'best[ext=mp4]',
	    'progress_hooks': [progress_hook],
	    'ffmpeg_location': r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
	    'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),
	    'quiet': True,
	    'no_warnings': True,
        'noprogress': True	    

	}

	if typ=="mp3":

		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url])

	elif typ=="mp4":

		with yt_dlp.YoutubeDL(ydl_opts_v) as ydl:
		    ydl.download([url])


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
	global mess,prog



	url=ent.get()

	if ent_v!=url:

		check_song()
		ent_v=url

		can.delete(prog[0])
		can.delete(prog[1])
		can.delete(mess)



	root.after(1,check_ent)

p=[]
dwd=[0,0]

def draw_download(txt):
	
	global can,dwd
	global p

	can.delete(dwd[0])
	can.delete(dwd[1])

	f=font.Font(family="FreeMono",size=13)

	l=f.measure(txt)


	p=[20,150+25,20+30+l,180+25]

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
	global typ,typ_



	r=math.sqrt((e.x-71)**2+(e.y-140)**2)

	if r<=10:


		typ="mp3"

		can.delete(typ_)

		typ_=can.create_oval(71-7,140-7,71+7,140+7,fill="#ff0000",outline="#ff0000")


		return


	r=math.sqrt((e.x-152)**2+(e.y-140)**2)

	if r<=10:


		typ="mp4"

		can.delete(typ_)

		typ_=can.create_oval(152-7,140-7,152+7,140+7,fill="#ff0000",outline="#ff0000")


		return
		


	if d_st==1:


		r=math.sqrt((e.x-p[0]+15)**2+(e.y-p[1]+15))

		if r<=15:
			th=threading.Thread(target=download,daemon=True)
			th.start()
			return


		r=math.sqrt((e.x-p[2]-15)**2+(e.y-p[1]+15))

		if r<=15:
			th=threading.Thread(target=download,daemon=True)
			th.start()
			return


		if p[0]+15<=e.x<=p[2]-15:
			if p[1]<=e.y<=p[3]:

				th=threading.Thread(target=download,daemon=True)
				th.start()
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


w,h=550,270
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

f=font.Font(family="FreeMono",size=13)


typ="mp3"

can.create_text(20,140,text="mp3",font=("FreeMono",13),fill="#ff0000",anchor="w")

can.create_oval(20+f.measure("mp3")+10,140-10, 20+f.measure("mp3")+10+20,140+10,outline="#ff0000")


if typ=="mp3":

	typ_=can.create_oval(20+f.measure("mp3")+10+3,140-10+3, 20+f.measure("mp3")+10+20-3,140+10-3,outline="#ff0000",fill="#ff0000")

can.create_text(20+f.measure("mp3")+10+20+20,140,text="mp4",font=("FreeMono",13),fill="#ff0000",anchor="w")

can.create_oval(20+f.measure("mp3")+10+20+20+f.measure("mp4")+10,140-10, 20+f.measure("mp3")+10+20+20+f.measure("mp4")+10+20,140+10,outline="#ff0000")

if typ=="mp4":

	typ_=can.create_oval(20+f.measure("mp3")+10+20+20+f.measure("mp4")+10+3,140-10+3, 20+f.measure("mp3")+10+20+20+f.measure("mp4")+10+20-3,140+10-3,outline="#ff0000",fill="#ff0000")

prog=[0,0]


check_ent()
root.mainloop()