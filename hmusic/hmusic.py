
#pyinstaller --noconfirm --onefile --windowed --icon C:\Users\admin\Desktop\my projects\hmusic\data\icon.ico C:\Users\admin\Desktop\my projects\hmusic\hmusic.py --distpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh\application --workpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh\build --specpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh


import sys
import psutil
from PIL import Image,ImageTk,ImageGrab,ImageDraw
import os

def get_running_programs():
    programs = []
    for proc in psutil.process_iter(['name']):
        try:
            programs.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return programs

# Get the list of running programs
running_programs = get_running_programs()


v=running_programs.count("hmusic.exe")

if v>2:
    os._exit(0)



import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
import pygame
import subprocess
from mutagen.mp3 import MP3

import math
import time
import json
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import shutil
import random
from tkinter import font
import wave
import numpy as np
from pathlib import Path
import pyperclip
#import cv2

import ctypes
from ctypes import wintypes

import threading
import time
from datetime import datetime
import pyautogui

import cv2

cap=None 


def get_frame_at(video_path, seconds, output_path="data/frame.jpg"):
    global cap
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        pass
        #raise IOError("Error: Cannot open video file.")

    # Get frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate frame number from seconds
    frame_number = int(fps * seconds)
    
    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    # Read the frame
    ret, frame = cap.read()
    
    if not ret:
        pass
        #raise ValueError("Error: Could not read frame at {} seconds.".format(seconds))
    
    # Save the frame if output path is provided
    cv2.imwrite(output_path, frame)
    
    cap.release()

# Example usage
"""
# Example usage
video_path = "path/to/your/video.mp4"
target_time_ms = 5000  # 5 seconds
get_frame_at_time(video_path, target_time_ms, )



self.canvas.itemconfig(self.canvas_image, image=self.images[self.current_image_index])
"""


vframe=[0,0,0]
def play_vid():

    global tm,play_st
    global vid_st
    global current_playing
    global vframe

    global sort_st,can_sort

    global w,h


    if play_st==1 and vid_st==1:

        #get_frame_at_time("videos/"+current_playing.replace(".mp3",".mp4"), 3)

        try:

            get_frame_at("videos/"+current_playing.replace(".mp3",".mp4"), tm)



            im=Image.open("data/frame.jpg")
            x,y=im.size

            x_,y_=w,h




            if x/y>x_/y_:


                xx=x_

                yy=int(xx*y/x)

                im=im.resize((xx,yy))

            elif x/y<x_/y_:


                yy=y_

                xx=int(yy*x/y)

                im=im.resize((xx,yy))
            else:

                im=im.resize((x_,y_))

            im.save("data/frame.jpg")


            vframe[0]=ImageTk.PhotoImage(file="data/frame.jpg")


            im=Image.open("data/frame.jpg")
            x,y=im.size

            


            


            if vframe[-1]==0:
                draw_can()
            else:
                can.itemconfig(vframe[1],image=vframe[0])
                can.coords(vframe[1],(w-x)/2,(h-y)/2)
        except:
            pass


    root.after(10,play_vid)

def configure_theme(pcol):
    global _theme

    col1=hex_to_rgb(pcol)

    mxc=max(col1)

    col2=(int(col1[0]*119/mxc),int(col1[1]*119/mxc),int(col1[2]*119/mxc))
    col3=(int(col1[0]*32/mxc),int(col1[1]*32/mxc),int(col1[2]*32/mxc))

    ar=["#%02x%02x%02x" % col2,"#%02x%02x%02x" % col3]


    _theme[1]=ar


    ar=[pcol]



    for c in _theme[4]:

        if c!=pcol:
            ar.append(c)


    if len(ar)>7:

        _theme[4]=ar[:7]

    else:
        _theme[4]=ar

    print(_theme[4])




def hex_to_rgb(hex_color: str) -> tuple:
    # Remove the '#' if it exists
    hex_color = hex_color.lstrip('#')
    # Convert to RGB
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def change_theme(pcol):

    col1=hex_to_rgb(pcol)

    mxc=max(col1)

    col2=(int(col1[0]*119/mxc),int(col1[1]*119/mxc),int(col1[2]*119/mxc))
    col3=(int(col1[0]*32/mxc),int(col1[1]*32/mxc),int(col1[2]*32/mxc))




    images_=[]


    for i in os.listdir("data/im_ref/"):

        if i.split(".")[-1]=="png":

            images_.append(i)



    for i in images_:

        im=Image.open("data/im_ref/"+i)


        x,y=im.size

        #print(x,y)


        image_ = Image.new('RGBA', (x, y), (0, 0, 0, 0))
        pixels = image_.load()


        for x_ in range(x):
            for y_ in range(y):


                col=im.getpixel((x_, y_))

                mxc=max(col[:3])

                if 240<=mxc<=255:

                    pixels[x_,y_]=(*col1, 255)

                elif 119-10<=mxc<=119+10:
                    pixels[x_,y_]=(*col2, 255)


                elif 32-10<=mxc<=32+10:
                    pixels[x_,y_]=(*col3, 255)

                else:

                    if col[-1]!=0:
                        pixels[x_,y_]=(0,0,0, 255)



                #print(col,pixels[x_,y_])

            root.after(2,update)


        




        if i=="icon.png":
            image_.save("data/"+i.split(".png")[0]+".ico")
        else:
            image_.save("data/"+i, "PNG", quality=10000)



        #print("ok")



#change_theme(_theme[0])


def darken_image(image_path, output_path,col, alpha):
    """
    Darkens an image by overlaying a semi-transparent black layer.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the darkened image.
        opacity (float): Opacity of the dark layer (0.0 to 1.0).
    """
    # Open the original image
    img = Image.open(image_path).convert("RGBA")
    
    # Create a black overlay with the same size as the image
    black_overlay = Image.new("RGBA", img.size, (*col, int(255 * alpha)))
    
    # Composite the black overlay onto the image
    darkened_img = Image.alpha_composite(img, black_overlay)
    
    # Save the result
    darkened_img.save(output_path)


# Example usage

#darken_image("data/bg_ref.png", "data/bg.png", opacity=0.45)


#import pyautogui


def capture_canvas():

    global can
    # Ensure Tkinter updates before capturing
    root.update_idletasks()

    # Get the absolute coordinates of the canvas
    x = root.winfo_rootx() + can.winfo_x()
    y = root.winfo_rooty() + can.winfo_y()
    x1 = x + can.winfo_width()
    y1 = y + can.winfo_height()

    # Capture the specified screen region
    image = ImageGrab.grab(bbox=(x, y, x1, y1))

    # Convert and save as high-quality image
    image = image.convert("RGB")  
    image.save("capture.png", quality=100)


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG)
    ]

def get_taskbar_height():
    # Get the screen dimensions
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    
    # Get the work area (excluding taskbar)
    rect = RECT()
    ctypes.windll.user32.SystemParametersInfoW(0x0030, 0, ctypes.byref(rect), 0)
    
    work_area_height = rect.bottom - rect.top
    taskbar_height = screen_height - work_area_height
    
    return max(0, taskbar_height)  # Ensure no negative values







def resize_im():

    im=Image.open("data/no-music.png")
    im=im.resize((300,300))
    im.save("data/no-music.png")



    im=Image.open("data/filter.png")
    im=im.resize((25,25))
    im.save("data/filter.png")



    im=Image.open("data/vid1.png")
    im=im.resize((25,25))
    im.save("data/vid1.png")


    im=Image.open("data/vid2.png")
    im=im.resize((25,25))
    im.save("data/vid2.png")


    im=Image.open("data/vid3.png")
    im=im.resize((25,25))
    im.save("data/vid3.png")




    im=Image.open("data/delete.png")
    im=im.resize((25,25))
    im.save("data/delete.png")


    im=Image.open("data/delete2_.png")
    im=im.resize((25,25))
    im.save("data/delete2_.png")

    im=Image.open("data/crop.png")
    im=im.resize((25,25))
    im.save("data/crop.png")

    im=Image.open("data/crop2.png")
    im=im.resize((25,25))
    im.save("data/crop2.png")


    im=Image.open("data/settings.png")
    im=im.resize((25,25))
    im.save("data/settings.png")

    im=Image.open("data/cursor.png")
    im=im.resize((30,30))
    im.save("data/cursor.png")

    im=Image.open("data/circlex.png")
    im=im.resize((50,50))
    im.save("data/circlex.png")

    im=Image.open("data/musical_note1.png")
    im=im.resize((30,30))
    im.save("data/musical_note1.png")



    im=Image.open("data/musical_note2.png")
    im=im.resize((30,30))
    im.save("data/musical_note2.png")


    im=Image.open("data/search.png")
    im=im.resize((25,25))
    im.save("data/search.png")


    im=Image.open("data/circle8.png")
    im=im.resize((6,6))
    im.save("data/circle8.png")


    im=Image.open("data/circle.png")
    im=im.resize((60,60))
    im2=im.resize((50,50))
    im3=im.resize((30,30))
    im4=im.resize((20,20))
    im5=im.resize((8,8))
    im6=im.resize((7,7))
    im7=im.resize((3,3))
    im8=im.resize((4,4))    
    im.save("data/circle.png")
    im2.save("data/circle2.png")
    im3.save("data/circle3.png")
    im4.save("data/circle4.png")
    im8.save("data/circle6.png")
    im5.save("data/circle7.png")
    im6.save("data/circle5.png")
    im6.save("data/circle10.png")
    im7.save("data/circle9.png")


    im=Image.open("data/quit.png")
    im=im.resize((25,25))
    im2=im.resize((20,20))
    im.save("data/quit.png")
    im.save("data/bin.png")
    im2.save("data/cancel.png")



    im=Image.open("data/minimize.png")
    im=im.resize((25,25))
    im.save("data/minimize.png")



    im=Image.open("data/favourite2.png")
    im=im.resize((25,25))
    im.save("data/favourite2.png")


    im=Image.open("data/favourite2_.png")
    im=im.resize((25,25))
    im.save("data/favourite2_.png")


    im=Image.open("data/favourite1.png")
    im=im.resize((25,25))
    im.save("data/favourite1.png")


    im=Image.open("data/favourite1_.png")
    im=im.resize((25,25))
    im.save("data/favourite1_.png")


    im=Image.open("data/playlist2.png")
    im=im.resize((25,25))
    im.save("data/playlist2.png")

    im=Image.open("data/playlist3.png")
    im=im.resize((25,25))
    im2=im.resize((20,20))
    im.save("data/playlist3.png")
    im2.save("data/playlist4.png")


    im=Image.open("data/list2.png")
    im=im.resize((25,25))
    im.save("data/list2.png")


    im=Image.open("data/list1.png")
    im=im.resize((25,25))
    im.save("data/list1.png")



    im=Image.open("data/sort.png")
    im=im.resize((25,25))
    im.save("data/sort.png")


    im=Image.open("data/sort2.png")
    im=im.resize((25,25))
    im.save("data/sort2.png")

    im=Image.open("data/shuffle2.png")
    im=im.resize((25,25))
    im.save("data/shuffle2.png")


    im=Image.open("data/shuffle1.png")
    im=im.resize((25,25))
    im.save("data/shuffle1.png")


    im=Image.open("data/loop2.png")
    im=im.resize((25,25))
    im.save("data/loop2.png")


    im=Image.open("data/loop1.png")
    im=im.resize((25,25))
    im.save("data/loop1.png")



    im=Image.open("data/forward.png")
    im=im.resize((25,25))
    im.save("data/forward.png")

    im=im.rotate(180)
    im.save("data/backward.png")



    im=Image.open("data/previous.png")
    im=im.resize((25,25))
    im.save("data/previous.png")

    im=im.rotate(-180)
    im.save("data/next.png")


    im=Image.open("data/play.png")
    im=im.resize((30,30))
    im.save("data/play.png")


    im=Image.open("data/pause.png")
    im=im.resize((30,30))
    im.save("data/pause.png")


    im=Image.open("data/speaker.png")
    im=im.resize((30,30))
    im.save("data/speaker.png")



    im=Image.open("data/add.png")
    im=im.resize((25,25))
    im.save("data/add.png")


    im=Image.open("data/add2.png")
    im=im.resize((25,25))
    im.save("data/add2.png")


    im=Image.open("data/checked.png")
    im=im.resize((20,20))
    im.save("data/checked.png")



    im=Image.open("data/bin2.png")
    im=im.resize((25,25))
    im2=im.resize((20,20))
    im.save("data/bin2.png")
    im2.save("data/bin3.png")





directory_path = Path("music")

if directory_path.is_dir():
    pass

 
else:
    os.makedirs("music", exist_ok=True)



directory_path = Path("waves")

if directory_path.is_dir():
    pass
else:
    os.makedirs("waves", exist_ok=True)


directory_path = Path("videos")

if directory_path.is_dir():
    pass
else:
    os.makedirs("videos", exist_ok=True)



def minimize_window():
    root.iconify()

def close_window():
    root.destroy()




def get_playback_time():
    return pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds


sig=[]
sig_=0
sig2=[]
tts=0

def draw_wave():

    global lst,can,st,sig,sig_,sig2,tm,tts,play_st,current_playing,w,h



    global lyric_st

    global play_video_st

    global root_st

    global tot_tm_

    global current_volume

    global vid_st



    col1=_theme[0]
    col2=_theme[1][0]







    xv=5
    amp=(((h-121-30)-50)-40)/2

    if play_st==1:



        can.delete(sig_)

        if play_video_st==0:

            try:






                amplitude = get_amplitude_at_time("waves/"+current_playing[:-3]+"wav", get_playback_time()+tts)





                sig.append(-amplitude*amp*current_volume)


                xn=int((w-20)/xv)


                if len(sig)>=xn:
                    sig.pop(0)




                sig2=[]
                x=10
                for a in sig:

                    sig2.append(x)
                    sig2.append(a+50+((h-121-30)-50)/2)

                    x+=xv




                try:

                    if lst==0 and st!=4 and lyric_st==0 and root_st==0 and vid_st==0:



                        if not tts>tot_tm_:
                            sig_=can.create_line(sig2,fill=col1)
                except:
                    pass












            except:
                pass

    root.after(2,draw_wave)



def get_amplitude_at_time(file_path, time_sec):
    """
    Get the amplitude of a WAV audio file at a specific time, scaled to the range [-1, 1].

    :param file_path: Path to the WAV audio file.
    :param time_sec: Time in seconds to check the amplitude.
    :return: Scaled amplitude at the given time in the range [-1, 1].
    """
    # Open the WAV file
    with wave.open(file_path, 'rb') as wav_file:
        # Extract parameters
        num_channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()
        sample_width = wav_file.getsampwidth()  # Bytes per sample
        num_frames = wav_file.getnframes()
        
        # Calculate the total duration
        duration = num_frames / sample_rate
        if time_sec > duration:
            raise ValueError("Specified time exceeds the duration of the audio file.")
        
        # Calculate the frame index for the given time
        frame_index = int(time_sec * sample_rate)
        
        # Set the read position to the desi#38fca5 frame
        wav_file.setpos(frame_index)
        
        # Read the frame data
        frame_data = wav_file.readframes(1)
        
        # Determine the correct data type for the sample width
        dtype_map = {1: np.uint8, 2: np.int16, 4: np.int32}
        if sample_width not in dtype_map:
            raise ValueError(f"Unsupported sample width: {sample_width} bytes.")
        dtype = dtype_map[sample_width]
        
        # Convert frame data to amplitude
        amplitude = np.frombuffer(frame_data, dtype=dtype)[0]
        
        # Normalize the amplitude to the range [-1, 1]
        max_amplitude_map = {1: 255, 2: 32767, 4: 2147483647}  # Max values for 8-bit, 16-bit, and 32-bit
        max_amplitude = max_amplitude_map[sample_width]
        
        # If the audio is signed, use the max absolute value for negative numbers as well
        if np.issubdtype(dtype, np.signedinteger):
            scaled_amplitude = amplitude / max_amplitude
        else:
            # For unsigned, normalize by dividing by the max amplitude
            scaled_amplitude = (amplitude - max_amplitude / 2) / (max_amplitude / 2)
        
        # Handle stereo audio (average or choose one channel)
        if num_channels > 1:
            scaled_amplitude = scaled_amplitude.mean()  # Average channels
        
        return scaled_amplitude


def convert_mp3_to_wav(mp3_file):

    all_songs = os.listdir("waves")


    wav_file="waves/"+mp3_file.split("/")[-1][:-3]+"wav"


    try:

        v=all_songs.index(mp3_file.split("/")[-1][:-3]+"wav")
    except:


        ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

        try:
            # Ensure the ffmpeg executable exists
            if not os.path.isfile(ffmpeg_path):
                raise FileNotFoundError(f"ffmpeg not found at: {ffmpeg_path}")
            
            # Execute the ffmpeg command
            subprocess.run(
                [ffmpeg_path, "-i", mp3_file, wav_file],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except:
            pass



def del_wave():
    all_music=os.listdir("music")
    all_waves=os.listdir("waves")

    for w in all_waves:

        try:
            v=all_music.index(w[:-3]+"mp3")
        except:
            os.remove("waves/"+w)


def update_waves():
    all_songs = os.listdir("music")


    for s in all_songs:


        convert_mp3_to_wav("music/"+s)





update_waves()





images = []  # to hold the newly created image

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
    global images
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        can.create_image(x1, y1, image=images[-1], anchor='nw')



def hex_to_rgba(hex_color, alpha):
    """Convert hex color like '#38fca5' to RGBA tuple."""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b, int(alpha * 255))


def create_polygon(*args, **kwargs):
    global can





    if "alpha" in kwargs:         
        if "fill" in kwargs:
            # Get and process the input data
            c=kwargs.pop("can")
            outline = kwargs.pop("outline") if "outline" in kwargs else None

            # We need to find a rectangle the polygon is inscribed in
            # (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
            # and they also are the width and height of it respectively (the image will be inserted into
            # (0, 0) coords for simplicity)
            image = Image.new("RGBA", (max(args[::2])+1, max(args[1::2])+1))

            fill=hex_to_rgba(kwargs.pop("fill"), kwargs.pop("alpha"))

            ImageDraw.Draw(image).polygon(args, fill=fill, outline=outline)



            images.append(ImageTk.PhotoImage(image))  # prevent the Image from being garbage-collected


            return c.create_image(0, 0, image=images[-1], anchor="nw")  # insert the Image to the 0, 0 coords





def convert_folder_to_audio():

    global can,load,load2,load3,load4,w,h
    global input_folder,convert,st




    col1=_theme[0]
    col2=_theme[1][0]



    if convert==1:




        ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
        sample_rate=44100
        channels=2
        bitrate="190k"



        def sort_data_added(directory: str, descending: bool = True):


            from pathlib import Path
            # Get the list of all files and directories
            items = [Path(directory) / item for item in os.listdir(directory)]

            # Filter only valid paths (ignores broken symbolic links)
            items = [item for item in items if item.exists()]

            # Sort by modification time (or creation time, platform-dependent)
            sorted_items = sorted(items, key=lambda x: x.stat().st_mtime, reverse=descending)

            return sorted_items

            




        try:
        



            all_items = []



            for i in sort_data_added(input_folder, False):

                all_items.append(str(i).split("\\")[-1])


            saved=os.listdir("music")





            for i in all_items:



                con=0

                for i_ in saved:

                    if i[:-3]==i_[:-3]:
                        con=1

                if con==1:
                    continue

                if i[-3:]=="mp3":

                    destination_file = os.path.join("music", os.path.basename(input_folder+"\\"+i))
                    shutil.copy(input_folder+"\\"+i, "music")

                    continue


                name=i[:-3]


                command = [
                    ffmpeg_path,
                    "-i", input_folder+"\\"+i,       # Input file
                    "-vn",                  # Disable video
                    "-ar", str(sample_rate), # Set audio sample rate
                    "-ac", str(channels),   # Set number of audio channels
                    "-b:a", bitrate,        # Set audio bitrate


                    "music\\"+name+"mp3"             # Output file (MP3 format)


                    ]

                try:
                    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                    root.after(2,update)


                except:
                    root.after(2,update)
                    






        except:
            pass


        can.create_text(w/2,499,text="Done!",fill=_theme[0],font=("FreeMono",17))

        convert=0
        update_waves()






def convert_file_to_audio():

    global can,load,load2,load3,load4,w,h
    global convert,input_file,st



    col1=_theme[0]
    col2=_theme[1][0]



    if convert==2:





        ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
        sample_rate=44100
        channels=2
        bitrate="190k"

        try:

        


            saved=os.listdir("music")






            i=input_file.split("/")[-1]

            con=0

            for i_ in saved:

                if i[:-3]==i_[:-3]:
                    con=1



            if i[-3:]=="mp3":

                destination_file = os.path.join("music", os.path.basename(input_file))
                shutil.copy(input_file, "music")


                con=1


            if not con==1:





                name=i[:-3]



                command = [
                    ffmpeg_path,
                    "-i", input_file,       # Input file
                    "-vn",                  # Disable video
                    "-ar", str(sample_rate), # Set audio sample rate
                    "-ac", str(channels),   # Set number of audio channels
                    "-b:a", bitrate,        # Set audio bitrate


                    "music\\"+name+"mp3"             # Output file (MP3 format)


                    ]

                try:
                    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

                    root.after(2,update)
                    

                except:
                    root.after(2,update)
                    


        except:
            pass


        can.create_text(w/2,499,text="Done!",fill=_theme[0],font=("FreeMono",17))

        convert=0
        update_waves()
        



def start_conversion():

    global convert


    if convert==1:

        threading.Thread(target=convert_folder_to_audio, daemon=True).start()

    elif convert==2:

        threading.Thread(target=convert_file_to_audio, daemon=True).start()







# Get system audio devices
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Get current volume level
current_volume = volume.GetMasterVolumeLevelScalar()  # Returns volume as a float (0.0 to 1.0)


# Set volume to 50%
#volume.SetMasterVolumeLevelScalar(0.5, None)

def check_sound_device():
    global devices,volume

    if AudioUtilities.GetSpeakers()!=devices:


        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = interface.QueryInterface(IAudioEndpointVolume)

    root.after(2,check_sound_device)


music_details={}



def update_details(s="",con=-1,_lyric_=""):
    global music_details


    try:



        try:

            with open("data/music_details.json", "r") as file:
                data = json.load(file)


        except:
            data={}






        all_songs = os.listdir("music")


        ar=[]

        for i in data:


            try:
                v=all_songs.index(i)

            except:


                ar.append(i)



        for v in ar:
            data.pop(v)

            ar=os.listdir("videos")

            try:
                v_=ar.index(v.replace(".mp3",".mp4"))
                os.remove("videos/"+v.replace(".mp3",".mp4"))
            except:
                pass

        for song in all_songs:
            
            try:
                v=data[song]
            except:

                #favourite,no of plays
                data[song]=[0,0,""]



        if con==0:
            f=data[s][0]

            if f==0:
                f=1
            elif f==1:
                f=0

            data[s][0]=f

        elif con==1:

            n=data[s][1]

            n+=1



            data[s][1]=n

        elif con==2:

            data[s][2]=_lyric_










        music_details=data







        with open("data/music_details.json", "w") as file:
            json.dump(data, file, indent=4) 
    except:
        pass


update_details()



playlist={}


def create_playlist(pl="",con="",song=""):
    global playlist



    try:


        try:

            with open("data/playlist.json", "r") as file:
                data = json.load(file)


        except:
            data={}


        all_songs = os.listdir("music")

        for i in data:

            ar=data[i]
            ar2=[]

            for v in range(len(ar)):

                try:
                    all_songs.index(ar[v])

                except:
                    ar2.append(v)


            try:


                for v in ar2:
                    ar.pop(v)
            except:
                pass

            data[i]=ar




        if con==0:

            try:
                data[pl]
            except:
                data[pl]=[]

        elif con==1:
            ar=data[pl]

            try:
                v=ar.index(song)

                ar.pop(v)

            except:
                ar.append(song)
            data[pl]=ar
        elif con==2:
            ar=data[pl]
            p=ar.index(song)

            ar.pop(p)
            data[pl]=ar

        elif con==3:
            data.pop(pl)


        playlist=data








        with open("data/playlist.json", "w") as file:
            json.dump(data, file, indent=4) 
    except:
        pass
create_playlist()




def save():

    global st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,save_,shuffle_ar,shuffle_st,songs_status
    global _theme
    global filter_val,filter_pl
    global f1_,f2_




    data={"save":[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status,_theme,f1_,f2_]}





    with open("data/save.json", "w") as file:
        json.dump(data, file, indent=4) 





"""import librosa

def get_amplitude_at_time(file_path, target_time):
    # Load the audio file
    audio_data, sample_rate = librosa.load(file_path, sr=None)  # Preserve original sample rate
    
    # Convert the target time to the corresponding sample index
    sample_index = int(target_time * sample_rate)
    
    # Ensure the sample index is within bounds
    if sample_index >= len(audio_data):
        raise ValueError("Target time exceeds the audio duration.")
    
    # Get the amplitude at the target time
    amplitude = audio_data[sample_index]
    return amplitude

# Usage
file_path = "music/24.mp3"  # Replace with the path to your MP3 file
target_time = 10.5  # Time in seconds (e.g., 10.5 seconds)
amplitude = get_amplitude_at_time(file_path, target_time)

print(f"Amplitude at {target_time} seconds: {amplitude}")
"""




prog3=0
def prog():

    global play_st,tm,start_time,can
    global ctime,tot_tm_
    global prog1,prog2,prog3
    global tvar
    global w,h
    global wd,ht



    global select_st
    global current_playing
    global circle9,circle5,circle7,circle8,circle11
    global cur_can,can

    global cursor
    global vid_st2
    global root_st



    if not select_st==1:


        if not tot_tm_==0:

            if not current_playing=="":


                col1=_theme[0]
                col2=_theme[1][0]




                seconds=tm

                seconds = seconds % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60

                if int(hour)>0:


                    if int(minutes)<10:
                        mm="0"+str(int(minutes))
                    else:
                        mm=str(int(minutes))

                    if int(seconds)<10:
                        ss="0"+str(int(seconds))
                    else:
                        ss=str(int(seconds))

                    tt=str(int(hour))+":"+mm+":"+ss
                else:


                    if int(minutes)<10:
                        mm="0"+str(int(minutes))
                    else:
                        mm=str(int(minutes))

                    if int(seconds)<10:
                        ss="0"+str(int(seconds))
                    else:
                        ss=str(int(seconds))


                    tt=mm+":"+ss




                can.delete(ctime)
                can.delete(prog1)
                can.delete(prog2)
                can.delete(prog3)

                if vid_st2==0 and vid_st==1:
                    return






                ctime=can.create_text(10,h-20-60-20+20+10+5-3+5-2+2,text=tt,font=("FreeMono",11),fill=col1,anchor="w")


                x_=tm*(w-20)/tot_tm_

                prog1=can.create_line(10,h-20-60-20+10+2+5-3+10, x_+10,h-20-60-20+10+2+5-3+10,fill=col1,width=2)

                prog2=can.create_image(x_+10-4,h-20-60-20+10+2+5-3-4+10,image=circle7,anchor="nw")
                prog3=can.create_image(x_+10-3,h-20-60-20+10+2+5-3-3+10,image=circle8,anchor="nw")

                if not root_st==1:

                    x,y=pyautogui.position()


                    xx,yy=x-(wd-w)/2,y-(ht-h)/2

                    if 10<=xx<=w-10:
                        if h-20-60-20+10+2+5-3+10-30<=yy<=h-20-60-20+10+2+5-3+10+1:


                            can.delete(cur_can)

                            

                            cur_can=can.create_image(xx-4,yy-4,image=cursor,anchor="nw")






def timer():
    global play_st,tm,start_time,can
    global ctime,tot_tm_
    global prog1,prog2
    global tvar
    global mvar
    global current_playing,songs
    global w,h,add_st,frame2,can2
    global loop,lvar,play_video_st
    global play_video_st
    global vid_canvas
    global lyric_st
    global cap
    global _songs_,songs_status
    global tts
    global playlist_st,st,current_playlist

    if play_st==1:


        try:




            prog()

            tm=get_playback_time()+tts

            if tm+0.5>=tot_tm_:


                st_=st
                cp=current_playlist
                p=playlist_st


                st=songs_status[0]
                current_playlist=songs_status[1]
                playlist_st=1

                main()

                st=st_
                current_playlist=cp
                playlist_st=p




                play_video_st=0
                

                if loop==0:
                    mvar+=1
                add_st=0
                frame2.place_forget()
                can2.focus_set()


                if mvar+1>len(_songs_):
                    mvar=0

                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))


                tm=0
                tts=0
                
                current_playing=_songs_[mvar][0]


                play_st=1

                play_music("music/"+current_playing,tm)

                pp=1

                get_audio_duration("music/"+current_playing)

                #update_details(current_playing,1)

                lvar=0

                play_video_st=0
                lyric_st=0

                cap=None

                main()

                move_to_playing()
        except:
            pass

    root.after(1,timer)


def can3_b1(e):
    global sel_playlist,can3,frame2,add_st,current_playing,current_playlist,playlist,songs,mvar,tm
    global st,songs_status,_songs_
    global playlist_st



    global sb2_sz,sb2_col,sb2_h,sb2_st

    if int(can3["width"])-sb2_sz-4<=e.x<=int(can3["width"]):

        sb2_st=1

        #can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

        h_=int(can3["height"])/int(can3["scrollregion"].split(" ")[-1])*int(can3["height"])

        if not e.y+h_>int(can3["height"]):
            sb2_move(e.y,e.y*int(can3["scrollregion"].split(" ")[-1])/int(can3["height"]))
        else:
            sb2_move(int(can3["height"])-h_,(int(can3["height"])-h_)*int(can3["scrollregion"].split(" ")[-1])/int(can3["height"]))


        return




    #add_st=0
    #frame2.place_forget()

    for p in sel_playlist:

        if p[2]<=can3.canvasy(e.y)<=p[2]+50:

            create_playlist(p[0],1,p[1])
            main()


            if current_playing==p[1]:

                if songs_status[1]==p[0]:

                    try:
                        v=playlist[songs_status[1]].index(current_playing)
                    except:




                        cp=p[1]


                        





                        ar=[]
                        for s in range(len(_songs_)):

                            if cp==_songs_[s][0]:

                                ar.append(s)

                        for p in ar:
                            _songs_.pop(p)

                        if len(_songs_)==1:
                            mvar=0
                        elif len(_songs_)==0:

                            current_playing=""
                            pygame.mixer.quit()
                        elif mvar==len(_songs_):
                            mvar=0

                        if not current_playing=="":


                            current_playing=_songs_[mvar][0]

                            tm=0

                            

                            if play_st==0:
                                play_music("music/"+current_playing,tm,1)
                                pygame.mixer.quit()
                            else:
                                play_music("music/"+current_playing,tm)

                            move_to_playing()






                            
                        songs_status[-1]=current_playing



            add_playlist()
            can2.focus_set()

            main()
            return


song_add_pl=0
bgp=0
cp2_im=0
def add_playlist():
    global can4,can3,can5,can6
    global sel_playlist,playlist,playlist2,checked
    global songs
    global song_add_pl
    global bgp
    global cp2_im
    global sb2_sz
    global cur_can3,cur_can4,cur_can6
    global bg2_
    global bg



    col1=_theme[0]
    col2=_theme[1][0]



    can4.delete("all")
    can3.delete("all")
    can6.delete("all")
    #40,250-40,350+100

    #x=(w-550)/2,y=(h-(40+250-40+10))/2


    can4.create_image(-((w-550)/2),-((h-(40+250-40+50+40))/2),image=bg2_,anchor="nw")
    can6.create_image(-((w-550)/2),-((h-(40+250-40+50+40))/2+40+250+10),image=bg2_,anchor="nw")

    can4.create_text(550/2,20,text="Playlists",font=("FreeMono",13),fill=col1)
    can4.create_line(2,38,550-2,38,fill=col1)


    draw_round_rec(can4,1,2 ,550-2,80,15,col1,"",1)

    draw_round_rec(can6,1,-15 ,550-2,38,15,col1,"",1)






    can3.delete("all")

    bgp=can3.create_image(-((w-550)/2),-((h-(40+250-40+50+40))/2+40)+can3.canvasy(0),image=bg2_,anchor="nw")

    ar=[]

    cx,cy=3+10,10

    a_=180

    for a in range(90):

        x=10*math.sin(math.radians(a_))+cx
        y=10*math.cos(math.radians(a_))+cy

        x=int(round(x,0))
        y=int(round(y,0))

        ar.append(x)
        ar.append(y)

        a_+=1


    cx,cy=3+10,40

    a_=270

    for a in range(90):

        x=10*math.sin(math.radians(a_))+cx
        y=10*math.cos(math.radians(a_))+cy

        x=int(round(x,0))
        y=int(round(y,0))

        ar.append(x)
        ar.append(y)

        a_+=1


    cx,cy=int(can3["width"])-sb2_sz-6-10,40

    a_=0

    for a in range(90):

        x=10*math.sin(math.radians(a_))+cx
        y=10*math.cos(math.radians(a_))+cy

        x=int(round(x,0))
        y=int(round(y,0))

        ar.append(x)
        ar.append(y)

        a_+=1

    cx,cy=int(can3["width"])-sb2_sz-6-10,10

    a_=90

    for a in range(90):

        x=10*math.sin(math.radians(a_))+cx
        y=10*math.cos(math.radians(a_))+cy

        x=int(round(x,0))
        y=int(round(y,0))

        ar.append(x)
        ar.append(y)

        a_+=1



    cp2_im=create_polygon(*ar, fill=_theme[0], alpha=_theme[3],can=can3)


    y=0
    
    sel_playlist=[]

    for p in playlist:

        ar=playlist[p]

        can3.create_image(10,y+10+4,image=playlist2,anchor="nw")

        if get_text_length(can3, p, "FreeMono", 13)>int(can3["width"])-(10+30+10)-(sb2_sz+2+10+20)-10:
            l=get_text_length(can3, "...", "FreeMono", 13)
            can3.create_text(10+30+10,y+25,text=_text_(can2,p,"FreeMono",13,int(can3["width"])-(10+30+10)-(sb2_sz+2+10+20)-10-l)+"...",font=("FreeMono",13),anchor="w",fill=col1)
        else:
            can3.create_text(10+30+10,y+25,text=p,font=("FreeMono",13),anchor="w",fill=col1)


        #can3.create_line(0,y+50,550-7,y+50,fill="#000000")

        try:
            v=ar.index(song_add_pl)



            can3.create_image(int(can3["width"])-1-sb2_sz-1-10-20,y+15, image=checked,anchor="nw")
            
        except:
            pass




        sel_playlist.append([p,song_add_pl,y])
        pl_var=[p,song_add_pl,y]



        y+=50



    if y<250-40+50:


        can3.create_line(1,0, 1,250-40+50,fill=col1)
        can3.create_line(550-2,0, 550-2,250-40+50,fill=col1)
    else:

        can3.create_line(1,0, 1,y,fill=col1)
        can3.create_line(550-2,0, 550-2,y,fill=col1)


    if len(playlist)==0:
        can3.create_text(10+30+10,(250-40)/2,text="No record",font=("FreeMono",13),anchor="w")



    if y<=int(can3["height"]):

        can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))
    else:
        can3["scrollregion"]=(0,0,int(can3["width"]),y)


    def label_sel_song(song):


        n=len(song)

        sz=int(can6["width"])-20


        if get_text_length(can6, song, "FreeMono", 12)<=sz:


            return song

        else:


            p=-1



            for s_ in range(len(song)):

                if get_text_length(can6, song[:p]+"...", "FreeMono", 12)<=sz:

                    return song[:p]+"..."


                p-=1



    can6.create_text(int(can6["width"])/2,20,text=label_sel_song(song_add_pl),font=("FreeMono",12),fill=_theme[0])







    draw_sb2()



def can2_b1(e):
    global current_playing,songs,play_st
    global pp
    global start_time
    global tot_tm
    global tm
    global mvar
    global can2
    global st,npl,playlist_st,_playlist,current_playlist,playlist
    global search,_search,search_var,frame
    global add_st,frame2,can3,can4,can5,can6
    global sel_playlist
    global _npl,npl
    global can_sort
    global shuffle_st,shuff,sort_val,sort_ar,sort_st

    global playlist_select,select_st
    global songs2

    global songs_status
    global loop
    global lyric_st
    global song_add_pl
    global _songs_
    global sb_sz


    global sb_sz,sb_col,sb_h,sb_st

    global can4,can3,can6
    global npl_var,can_npl
    global f1_,f2_
    global filter_val,filter_pl,filter_st

    if (int(can2["width"])-sb_sz-1)<=e.x<=(int(can2["width"])):

        sb_st=1


        h_=int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])*int(can2["height"])

        if not e.y+h_>int(can2["height"]):
            sb_move(e.y,e.y*int(can2["scrollregion"].split(" ")[-1])/int(can2["height"]))
        else:
            sb_move(int(can2["height"])-h_,(int(can2["height"])-h_)*int(can2["scrollregion"].split(" ")[-1])/int(can2["height"]))

        return


    if select_st==1:


        for a in range(len(songs2)):


            if songs2[a][-1]<=can2.canvasy(e.y)<=songs2[a][-1]+50:

                create_playlist(playlist_select,1,songs2[a][0])


                main()



                if current_playing==songs2[a][0]:

                    if songs_status[1]==playlist_select:

                        try:
                            v=playlist[songs_status[1]].index(current_playing)
                        except:




                            cp=songs2[a][0]


                            





                            ar=[]
                            for s in range(len(_songs_)):

                                if cp==_songs_[s][0]:

                                    ar.append(s)

                            for p in ar:
                                _songs_.pop(p)

                            if len(_songs_)==1:
                                mvar=0
                            elif len(_songs_)==0:

                                current_playing=""
                                pygame.mixer.quit()

                            elif mvar==len(_songs_):
                                mvar=0

                            if not current_playing=="":


                                current_playing=_songs_[mvar][0]

                                tm=0

                                

                                if play_st==0:
                                    play_music("music/"+current_playing,tm,1)
                                    pygame.mixer.quit()
                                else:
                                    play_music("music/"+current_playing,tm)






                                
                            songs_status[-1]=current_playing




                main()

                return




    
    _npl=0



    can_npl.place_forget()

    main()   



    can_sort.place_forget()
    sort_st=0
    
    frame2.place_forget()
    can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))





    if st==2 and playlist_st==0:


        cx,cy=(int(can2["width"])-sb_sz-1)-10-5-20+10,5+10

        if cx-10<=e.x<=cx+10:
            if cy-10<=e.y<=cy+10:

            
                _npl=0
                
                can_npl.place_forget()

                main()
                return



        if 10<=e.x<=(int(can2["width"])-sb_sz-1)-10:
            if 5<=e.y<=35:

                can2["scrollregion"]=(0,0,(int(can2["width"])-sb_sz-1),int(can2["height"]))
                
                _npl=1
                npl_var=""


                can_npl["width"]=((int(can2["width"])-sb_sz-1)-10-5-20-5-10-10-5)
                can_npl["height"]=28

                can_npl.delete("all")

                can_npl.create_image(-(10+15+10),-(5+1+88),image=bg,anchor="nw")
                    

                can_npl.place(in_=root,x=10+15+10,y=5+1+88)


                can_npl.focus_set()
                main()

                return

        # create new playlist


        cx,cy=(int(can2["width"])-sb_sz-1)/2-100,45+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            if not npl_var=="":
                create_playlist(npl_var,0)
                
                can_npl.place_forget()
                _npl=0

                main()
            return


        cx,cy=(int(can2["width"])-sb_sz-1)/2+100,45+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            if not npl_var=="":
                create_playlist(npl_var,0)
                
                _npl=0
                can_npl.place_forget()
                main()

            return


        if (int(can2["width"])-sb_sz-1)/2-100<=e.x<=(int(can2["width"])-sb_sz-1)/2+100:
            if 45<=e.y<=45+30:

                if not npl_var=="":
                    create_playlist(npl_var,0)
                    _npl=0
                    
                    can_npl.place_forget()
                    main()
                return


        for _pl in _playlist:

            
            cx,cy=(int(can2["width"])-sb_sz-1)-10-25-15-25+12.5,_pl[1]+12.5+12.5
            r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
            if r<=12.5:

                playlist_select=_pl[0]
                select_st=1

                can2["scrollregion"]=(0,0,(int(can2["width"])-sb_sz-1),int(can2["height"]))


                _search=0
                search_var=""

                

                can_search.place_forget()

                main()

                return






            cx,cy=(int(can2["width"])-sb_sz-1)-10-25+12.5,_pl[1]+12.5+12.5
            if cx-12.5<=e.x<=cx+12.5:
                if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:


                    conf_del_(_pl[0],"playlist")


                    return



            if e.x<=(int(can2["width"])-sb_sz-1)-10-25-15-25-10:


                if _pl[1]<=can2.canvasy(e.y)<=_pl[1]+50:




                    filter_val,filter_pl="None",None

                    can2["scrollregion"]=(0,0,(int(can2["width"])-sb_sz-1),int(can2["height"]))

                    
                    current_playlist=_pl[0]
                    playlist_st=1

                    shuffle_st=0
                    sort_val=sort_ar[0][0]








                    main()
                    return



        main()


        return




    #favourite

    for s in songs:


        y=s[-1]

        cx,cy=(int(can2["width"])-sb_sz-1)-10-25-15-25-15-25-15-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                update_details(s[0],0)
                main()

                con_=0
                


                if songs_status[0]==1:
                    if current_playing==s[0]:


                        if len(_songs_)==1:
                            mvar=0
                        elif mvar==len(_songs_)-1:
                            mvar=0
                        else:
                            mvar=mvar+1


                        current_playing=_songs_[mvar][0]

                        tm=0

                        if play_st==0:

                            play_music("music/"+current_playing,tm,1)
                            pygame.mixer.quit()
                        else:
                            play_music("music/"+current_playing,tm)





                        if len(_songs_)==1:
                            current_playing=""
                        
                        songs_status[-1]=current_playing

                        con_=1
                main()


                st_=st
                cp=current_playlist
                p=playlist_st


                st=songs_status[0]
                current_playlist=songs_status[1]
                playlist_st=1

                main()

                st=st_
                current_playlist=cp
                playlist_st=p


                main()

                if songs_status[0]==1:
                    if con_==1:

                        move_to_playing()


                if st==songs_status[0]:

                    if st==2:

                        if current_playlist==songs_status[1]:

                            update_song_status()

                    else:
                        update_song_status()

                return

    #playlist

    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=(int(can2["width"])-sb_sz-1)-10-25-15-25-15-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                if add_st==0:
                    add_st=1
                elif add_st==1:
                    add_st=0


                if add_st==1:



                    song_add_pl=s[0]


                    add_playlist()

                    frame2.place(in_=root,x=(w-550)/2,y=(h-(int(can4["height"])+int(can3["height"])+int(can6["height"])))/2)

                    #can3.focus_set()

                    main()

                return

    """
    #add video


    for s in songs:
        y=s[1]
    
        cx,cy=(int(can2["width"])-sb_sz-1)-10-25-15-25+12.5,y+12.5+12.5
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            if music_details[s[0]][3]==False:

                file=filedialog.askopenfilename()


                if file!="":

                    if file.split("/")[-1].split(".")[-1]=="mp4":



                        shutil.copy(file,"videos")

                        file_=file.split("/")[-1]

                        os.rename("videos/"+file_,"videos/"+s[0][:-3]+"mp4")



                        main()

            elif music_details[s[0]][3]==True:

                cap=None


                os.remove("videos/"+s[0][:-3]+"mp4")

                main()
            return

    """
    #add/remove video


    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=(int(can2["width"])-sb_sz-1)-10-25-15-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                

                ar=os.listdir("videos")

                try:

                    v=ar.index(s[0].replace(".mp3",".mp4"))


                    conf_del_("videos/"+s[0].replace(".mp3",".mp4"),"video")


                except:


                    file=filedialog.askopenfilename()

                    try:

                        if file[-3:]=="mp4":

                            destination_file = os.path.join("videos", os.path.basename(file))
                            shutil.copy(file, "videos")

                            os.rename("videos/"+file.split("/")[-1],"videos/"+s[0].replace(".mp3",".mp4"))

                    except:
                        pass


                    main()
                return

    #delete file


    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=(int(can2["width"])-sb_sz-1)-10-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:


                try:

                    conf_del_("music/"+s[0],"music")



                

                except:
                    pass

                main()
                return




    #play song

    if e.x<=(int(can2["width"])-sb_sz-1)-1:
        for a in range(len(songs)):


            if songs[a][-1]<=can2.canvasy(e.y)<=songs[a][-1]+50:

                if st==2 and playlist_st==0:
                    return




                add_st=0
                frame2.place_forget()

                tm=0
                
                current_playing=songs[a][0]
                mvar=a
                play_st=1

                play_music("music/"+current_playing,tm)

                pp=1

                get_audio_duration("music/"+current_playing)



                con=0
                if st==songs_status[0]:

                    if st==2:
                        if current_playlist==songs_status[1]:
                            con=1
                    else:
                        con=1


                    




                if con==0:

                    shuffle_st=0
                    sort_val=sort_ar[0][0]
                    f1_,f2_="None",None

                loop=0

                songs_status[-2]=0

                lyric_st=0





                if not st==2:
                    current_playlist=""

                
                filter_st=0
                filter_can1.place_forget()
                filter_can2.place_forget()

                

                update_song_status()

                main()


                move_to_playing()

                return
    add_st=0




def move_to_playing(con_=0):
    global current_playing,can2
    global songs,_songs_
    global select_st
    global playlist_st,can2

    global st,current_playlist,songs_status
    global sb_h


    try:

        if select_st==1:
            return
        if st==2:
            if playlist_st==0:
                return


        if not current_playing=="":

            con=0


            for s in songs:

                if s[0]==current_playing:

                    con=1



            if con==1:

                main()


                for s in songs:

                    if s[0]==current_playing:


                        t=len(songs)*50


                        v=s[1]

                        if con_==0:

                            if can2.canvasy(0)<=v<=can2.canvasy(0)+int(can2["height"])-50:
                                #main()
                                return

                        if s[1]+int(can2["height"])/2-25<t:
                            v=s[1]-(int(can2["height"])/2-25)



                        pixel_value = v
                        fraction = pixel_value / int(can2["scrollregion"].split(" ")[-1])
                        can2.yview_moveto(fraction)
                        move_bg()
                        sb_h=can2.canvasy(0)*int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])
                        draw_sb()
    except:
        pass






def can_b3(e):

    """

    global can
    # Get the canvas position on the screen
    x = can.winfo_rootx() + e.x
    y = can.winfo_rooty() + e.y

    # Capture the screen area around the canvas
    image = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    color = image.getpixel((0, 0))


    print(f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')



    """



    def get_pixel_color(pixel_x, pixel_y):
        # Get the canvas coordinates relative to the screen
        x = root.winfo_rootx() + can.winfo_x()
        y = root.winfo_rooty() + can.winfo_y()
        width = can.winfo_width()
        height = can.winfo_height()

        # Capture the canvas area
        image = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        
        # Get the color of a specific pixel (e.g., center of the canvas)
        
        color = image.getpixel((pixel_x, pixel_y))

        # Display the color
        print("#%02x%02x%02x" % color)

    #get_pixel_color(e.x,e.y)


    #capture_canvas()
    move_to_playing()


convert=0
input_file=""
input_folder=""

v_st=0
play_st2=0
csv_im=0

im_bg=0

bg_so=0

def can_b1(e):
    global st,w,h,tm,current_playing
    global pp,play_st
    global prog1,prog2
    global ctime
    global mvar,songs
    global search,search_var
    global lst
    global current_volume,vol1,vol2
    global playlist_st,current_playlist
    global frame2,can3,add_st,sel_playlist,playlist2,npl,playlist
    global checked
    global load_st,load_ang
    global pl_st
    global load,load2,load3,load4
    global sort_st,sort_val,sort_ar,can_sort,_sort,checked
    global shuffle_st,shuff
    global loop
    global _search
    global _npl
    global input_folder,input_file,convert
    global sig,tts

    global expand_st

    global sa

    global lyric_st,_lyric
    global can_lyrics,lvar

    global play_video_st
    global music_details
    global vid_canvas
    global paused
    global cap
    global root_st
    global select_st
    global play_st

    global _songs_
    global songs_status

    global forward,backward,tot_tm_
    global can2
    global bg
    global can3
    global bg__
    global v_st,play_st2
    global csv_im
    global cur_can_sort
    global can_settings,theme_ent
    global im_bg
    global circle3
    global sel_op_ent
    global bg2_
    global quit
    global _theme
    global vid_st,vid_st2
    global vframe,vid_tm
    global settings_st2

    global filter_can1,filter_can2
    global favourite2,playlist2,vid1
    global filter_st,filter_val,filter_pl

    global bg_so
    global conf_del
    global can_search



    col1=_theme[0]
    col2=_theme[1][0]




    wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()
    if root_st==1:



        root_st=0




        root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))

        main()

        move_to_playing()

        return



    if select_st==1:

        

        cx,cy=w-10-25+12.5,(h-121+75)+((h-1)-(h-121+75)-25)/2+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:
                select_st=0

                _search=0
                _npl=0

                search_var=""

                
                can_search.place_forget()

                
                can_npl.place_forget()


                main()
                return



    if 10<=e.x<=10+25:
        if 12.5<=e.y<=12.5+25:


            settings_st2=1
            can_settings["width"]=int(can_settings["height"])*1.5

            _search=0
            search_var=""
            can_search.place_forget()

            draw_settings()





    _npl=0

    can_npl.place_forget()

    main()   













    main()




    add_st=0
    frame2.place_forget()
    can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))



    xv=w/6




    if xv-60<=e.x<=xv+60:
        if 50/2-15<=e.y<=50/2+15:



            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass                
            


            st=0


            conf_del.place_forget()

            filter_st=0
            filter_val="None"
            filter_pl=None
            filter_can1.place_forget()
            filter_can2.place_forget()


            vid_st=0
            vid_st2=0


            lyric_st=0

            select_st=0

            play_video_st=0
            

            lst=1
            _search=0
            _npl=0

            search_var=""

            
            can_search.place_forget()
            sort_st=0
            can_sort.place_forget()
            sort_st=0

            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))
            
            lst=1
            current_playlist=""

            add_st=0
            frame2.place_forget()

            can2.focus_set()
                        
            _npl=0
            can_npl.place_forget()



            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            main()


            
            return


    if xv*2-60<=e.x<=xv*2+60:
        if 50/2-15<=e.y<=50/2+15:


            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass   


            st=1

            conf_del.place_forget()

            filter_st=0
            filter_val="None"
            filter_pl=None
            filter_can1.place_forget()
            filter_can2.place_forget()

            vid_st=0
            vid_st2=0
            lyric_st=0

            select_st=0




            play_video_st=0
            

            lst=1

            _search=0
            search_var=""
            _npl=0

            
            can_search.place_forget()
            sort_st=0
            can_sort.place_forget()
            sort_st=0


            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]


            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))

            
            lst=1
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            
            
            _npl=0
            can_npl.place_forget()
            



            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            main()




            return

    if xv*3-60<=e.x<=xv*3+60:
        if 50/2-15<=e.y<=50/2+15:

            if st==2:
                pl_st=1

            else:
                pl_st=0


            if st==4:

                try:

                    current_playing=songs_status[-1]
                    
                    get_audio_duration("music/"+current_playing)
                except:
                    pass   
                

            st=2


            search_var=""
            conf_del.place_forget()

            filter_st=0
            filter_val="None"
            filter_pl=None
            filter_can1.place_forget()
            filter_can2.place_forget()

            vid_st=0
            vid_st2=0
            lyric_st=0

            select_st=0


            play_video_st=0
            

            lst=1

            _search=0
            _npl=0

            
            can_search.place_forget()
            sort_st=0
            can_sort.place_forget()
            sort_st=0





            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))

            
            playlist_st=0
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            
            
            _npl=0
            can_npl.place_forget()


            current_playlist=songs_status[1]

            






            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            main()

            return


    if xv*4-60<=e.x<=xv*4+60:
        if 50/2-15<=e.y<=50/2+15:


            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass   

            st=3

            search_var=""
            conf_del.place_forget()


            filter_st=0
            filter_val="None"
            filter_pl=None
            filter_can1.place_forget()
            filter_can2.place_forget()

            vid_st=0
            vid_st2=0
            lyric_st=0

            select_st=0



            play_video_st=0
            


            lst=1

            _search=0
            _npl=0

            
            can_search.place_forget()
            sort_st=0
            can_sort.place_forget()
            sort_st=0

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]




            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))

            
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            
            
            _npl=0
            can_npl.place_forget()


            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            main()




            return


    if xv*5-60<=e.x<=xv*5+60:
        if 50/2-15<=e.y<=50/2+15:

            

            search_var=""

            conf_del.place_forget()


            filter_st=0
            filter_val="None"
            filter_pl=None

            filter_can1.place_forget()
            filter_can2.place_forget()

            vid_st=0
            vid_st2=0
            lyric_st=0




            st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing=songs_status

            if st==2:
                if current_playlist!="":
                    playlist_st=1




            select_st=0



            play_video_st=0
            


            lst=1
            _search=0
            _npl=0

            
            can_search.place_forget()
            can_sort.place_forget()
            sort_st=0



            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))


            can2.focus_set()
            add_st=0
            frame2.place_forget()
            
            
            _npl=0
            can_npl.place_forget()



            st=4

            main()





            return



    if h-20-60-20+10+2+5-10-3+10+5<=e.y<=h-20-60-20+10+2+5+10-3+10-5:



        if e.x<10:
            tm=0
            lvar=0
        elif e.x>w-10:
            tm=tot_tm_

        elif 10<=e.x<=w-10:

            x=e.x-10

            tm=x*tot_tm_/(w-20)

            play_st2=1



        if play_st==1:

            tts=tm
            sig=[]

            if tm>0:
                play_music("music/"+current_playing,tm,1)

            else:
                play_music("music/"+current_playing,tm)


            if play_video_st==1:
                cap.release()
                play_vid(tm)

            

        prog()
        main()

        return


    con=0

    if select_st==1:

        con=1



    if con==0:


        #play/pause


        cx,cy=w/2,h-20-30-30+5+10+30-3

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=30:

            if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
                pass
            else:

                if not current_playing=="":

                    if pp==0:
                        pp=1
                        play_st=1

                        paused=False

                        tts=tm

                        if tm>0:
                            play_music("music/"+current_playing,tm,1)

                        else:
                            play_music("music/"+current_playing,tm)


                        if play_video_st==1:
                            play_vid(tm)
                        main()
                    elif pp==1:

                        paused=True
                        pp=0
                        play_st=0

                        pygame.mixer.quit()

                        main()



                        prog()

            return

        #previous

        cx,cy=w/2-30-30-25+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:



                if st==2 and playlist_st==0 and pl_st==0:
                    return


                if current_playing=="":
                    return



                st_=st
                cp=current_playlist
                p=playlist_st


                st=songs_status[0]
                current_playlist=songs_status[1]
                playlist_st=1

                main()

                st=st_
                current_playlist=cp
                playlist_st=p


                if loop==0:

                    mvar-=1

                if mvar<0:
                    mvar=len(_songs_)-1


                tm=0

                
                current_playing=_songs_[mvar][0]
                play_st=1

                play_music("music/"+current_playing,tm)

                pp=1

                get_audio_duration("music/"+current_playing)


                play_video_st=0

                



                lvar=0
                lyric_st=0

                cap=None

                main()

                move_to_playing()
                return

        #next


        cx,cy=w/2+30+30+12.5,h-20-30-15+5+10-3+2.5+12.5


        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:



                if st==2 and playlist_st==0 and pl_st==0:
                    return


                if current_playing=="":
                    return


                st_=st
                cp=current_playlist
                p=playlist_st


                st=songs_status[0]
                current_playlist=songs_status[1]
                playlist_st=1

                main()

                st=st_
                current_playlist=cp
                playlist_st=p


                if loop==0:

                    if mvar+1==len(_songs_):
                        mvar=0
                    else:
                        mvar+=1


                tm=0
                
                current_playing=_songs_[mvar][0]
                play_st=1

                play_music("music/"+current_playing,tm)

                pp=1

                get_audio_duration("music/"+current_playing)

                lvar=0
                play_video_st=0
                lyric_st=0

                cap=None


                

                main()

                move_to_playing()
                return

        #backward
        cx,cy=w/2-30-30-25-15-25-10+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:



                if play_st==1:
                    if not tm-5<0:
                
                        tm-=5
                        tts=tm
                        sig=[]

                        play_music("music/"+current_playing,tm)


        #forward
        cx,cy=w/2+30+30+25+15+10+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                if play_st==1:
                    if not tm+5>tot_tm_:

                        tm+=5
                        tts=tm
                        sig=[]

                        play_music("music/"+current_playing,tm)


        #list

        cx,cy=10+12.5,h-20-30-15+5+12.5+10-3+2.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:




                if lst==0:
                    lyric_st=0
                    lst=1

                    vid_st=0
                    vid_st2=0


                    can_lyrics.place_forget()

                    

                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

                elif lst==1:

                    if st==2 and playlist_st==0:
                        pass
                    else:
                        lst=0
                        _search=0
                        _npl=0
                        search_var=""

                        
                        can_search.place_forget()
                        frame.place_forget()

                        conf_del.place_forget()

                        filter_st=0
                        filter_can1.place_forget()
                        filter_can2.place_forget()

                main()

                if st==songs_status[0]:

                    if st==2:
                        if current_playlist==songs_status[1]:
                            move_to_playing()

                    else:
                        move_to_playing()




        #volume
        if w-10-120-10<=e.x<=w-10+10:
            if h-20-30+5-10+10-3<=e.y<=h-20-30+5+10+10-3:

                if e.x<w-10-120:
                    current_volume=0
                    volume.SetMasterVolumeLevelScalar(current_volume, None)
                elif e.x>w-10:
                    current_volume=1
                    volume.SetMasterVolumeLevelScalar(current_volume, None)
                elif w-10-120<=e.x<=w-10:

                    x=e.x-(w-10-120)

                    r=120

                    current_volume=x/r





                    volume.SetMasterVolumeLevelScalar(current_volume, None)

                    v_st=1



                main()


        #sort

        cx,cy=10+25+15+12.5,h-20-30-15+5+12.5+10-3+2.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                if songs_status[0]==3 or st==3:
                    return


                if sort_st==0:
                    sort_st=1
                elif sort_st==1:
                    sort_st=0






                if sort_st==1:

                    if sort_val=="":
                        sort_val=sort_ar[0][0]



                    col1=_theme[0]
                    col2=_theme[1][0]






                    can_sort.delete("all")

                    bg_so=can_sort.create_image(-(10+25+15+25),-(h-20-30-15+5+10+2.5-160),image=bg2_,anchor="nw")




                    ar=[]

                    cx,cy=3+10,10

                    a_=180

                    for a in range(90):

                        x=10*math.sin(math.radians(a_))+cx
                        y=10*math.cos(math.radians(a_))+cy

                        x=int(round(x,0))
                        y=int(round(y,0))

                        ar.append(x)
                        ar.append(y)

                        a_+=1


                    cx,cy=3+10,20

                    a_=270

                    for a in range(90):

                        x=10*math.sin(math.radians(a_))+cx
                        y=10*math.cos(math.radians(a_))+cy

                        x=int(round(x,0))
                        y=int(round(y,0))

                        ar.append(x)
                        ar.append(y)

                        a_+=1


                    cx,cy=int(can_sort["width"])-5-10,20

                    a_=0

                    for a in range(90):

                        x=10*math.sin(math.radians(a_))+cx
                        y=10*math.cos(math.radians(a_))+cy

                        x=int(round(x,0))
                        y=int(round(y,0))

                        ar.append(x)
                        ar.append(y)

                        a_+=1

                    cx,cy=int(can_sort["width"])-5-10,10

                    a_=90

                    for a in range(90):

                        x=10*math.sin(math.radians(a_))+cx
                        y=10*math.cos(math.radians(a_))+cy

                        x=int(round(x,0))
                        y=int(round(y,0))

                        ar.append(x)
                        ar.append(y)

                        a_+=1



                    csv_im=create_polygon(*ar, fill=_theme[0], alpha=_theme[3],can=can_sort)





                    draw_round_rec(can_sort,0,0, 250-2,160-1,15,col1,col1,1)

                    can_sort.create_text(125,15,text="Sort",font=("FreeMono",13),fill=col1)


                    can_sort.create_line(3,30, 250-2,30,fill=col1 )
                    y=30
                    for _ in sa:

                        can_sort.create_text(10,y+15,text=_,font=("FreeMono",13),fill=col1,anchor="w")

                        #can_sort.create_line(0,y+30,250,y+30,fill="#000000")

                        sort_ar.append([_,y])

                        y+=30



                    for s in sort_ar:

                        if s[0]==sort_val:

                            _sort=can_sort.create_image(250-5-20,s[1]+5,image=checked,anchor="nw")


                    can_sort.place(in_=root,x=10+25+15+25,y=h-20-30-15+5+10+2.5-160)

                    shuff=0
                    shuffle_st=0









                    main()


                    if st==songs_status[0]:

                        if st==2:

                            if current_playlist==songs_status[1]:

                                update_song_status()
                                move_to_playing(0)

                        else:
                            update_song_status()

                            move_to_playing(0)



                else:
                    can_sort.place_forget()
                    sort_st=0

                return



        #shuffle




        cx,cy=10+25+15+25+15+12.5,h-20-30-15+5+12.5+10-3+2.5


        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                if songs_status[0]==3:
                    return

                if st==songs_status[0]:

                    if st==2:
                        if current_playlist==songs_status[1]:

                            con=1
                    else:
                        con=1

                if con==1:

                    loop=0

                    if shuffle_st==0:
                        can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
                        mvar=0
                        shuffle_st=1
                        shuff=1

                        sort_val=""
                        sort_st=0

                        main()

                        if st==songs_status[0]:

                            if st==2:

                                if current_playlist==songs_status[1]:

                                    update_song_status()
                                    move_to_playing(1)

                            else:
                                update_song_status()
                                move_to_playing(1)

                            main()


                    elif shuffle_st==1:
                        can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
                        shuffle_st=0
                        shuff=0

                        sort_val=sort_ar[0][0]
                        main()

                        if st==songs_status[0]:

                            if st==2:

                                if current_playlist==songs_status[1]:

                                    update_song_status()
                                    move_to_playing(1)

                            else:
                                update_song_status()
                                move_to_playing(1)
                        main()

                    elif shuffle_st==2:
                        can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
                        shuffle_st=0
                        shuff=0
                        sort_val=sort_ar[0][0]            
                        main()
                    
                        if st==songs_status[0]:

                            if st==2:

                                if current_playlist==songs_status[1]:

                                    update_song_status()
                                    move_to_playing(1)

                            else:
                                update_song_status()
                                move_to_playing(1)

                        main()



        #loop

        cx,cy=10+25+15+25+15+25+15+12.5,h-20-30-15+5+12.5+10-3+2.5



        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:



                if loop==0:
                    if current_playing!="":
                        loop=1
                elif loop==1:
                    loop=0

                main()


                if st==songs_status[0]:

                    if st==2:

                        if current_playlist==songs_status[1]:

                            update_song_status()

                    else:
                        update_song_status()


        #play_vid


        if 10+25+15+25+15+25+15+25+15<=e.x<=10+25+15+25+15+25+15+25+15+25:
            if h-20-30-15+5+10-3+2.5<=e.y<=h-20-30-15+5+10-3+2.5+25:

                ar=os.listdir("videos")

                try:




                    v=ar.index(current_playing.replace(".mp3",".mp4"))
                    
                    if vid_st==0:
                        ar=os.listdir("data")
                        try:
                            v=ar.index("frame.jpg")
                            os.remove("data/frame.jpg")

                        except:
                            pass

                        vid_st=1
                    elif vid_st==1:
                        vid_st=0
                        vid_st2=0

                    if vid_st==1:

                        

                        vid_tm=time.time()
                        lst=0
                        _search=0
                        _npl=0

                        lyric_st=0

                        search_var=""

                        
                        can_search.place_forget()
                        frame.place_forget()

                        can_lyrics.place_forget()

                        filter_st=0
                        filter_can1.place_forget()
                        filter_can2.place_forget()

                        conf_del.place_forget()


                        vframe=[0,0,0]



                    
                except:
                    vid_st=0
                    vid_st2=0
                main()

        #lyrics


        if not st==4:

            if not vid_st==1:

                x=w/2
                y=h-121-30



                cx,cy=x-40+15,y+15
                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
                if r<=15:

                    if lyric_st==0:
                        lyric_st=1
                    elif lyric_st==1:
                        lyric_st=0
                        can_lyrics.place_forget()

                    lvar=0

                    main()
                    prog()
                    return





                cx,cy=x+40-30+15,y+15
                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
                if r<=15:

                    if lyric_st==0:
                        lyric_st=1
                    elif lyric_st==1:
                        lyric_st=0
                        can_lyrics.place_forget()

                    lvar=0

                    main()
                    prog()
                    return


                if x-40+15<=e.x<=x+40-15:
                    if y<=e.y<=y+30:


                        if lyric_st==0:
                            lyric_st=1
                        elif lyric_st==1:
                            lyric_st=0
                            can_lyrics.place_forget()

                        lvar=0

                        main()
                        prog()
                        return


                if lyric_st==1:



                    cx,cy=x+40+10+12.5,y+2.5+12.5

                    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)


                    if r<=12.5:

                        clipboard()


                        if not current_playing=="":
                            update_details(current_playing,2,_lyric)

                            lvar=0

                            main()
                            prog()




                        return


                    if music_details[current_playing][2]!="":

                        cx,cy=x+40+10+25+10+12.5,y+2.5+12.5

                        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)


                        if cx-12.5<=e.x<=cx+12.5:
                            if cy-12.5<=e.y<=cy+12.5:

                                conf_del_(current_playing,"lyrics")




                                return



        """
        #play_video

        cx,cy=10+75+45+12.5,h-20-30-15+5+10+12.5-3+2.5
        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=12.5:

            if play_video_st==0:

                if music_details[current_playing][-1]==True:
                    play_video_st=1

                    lst=0
                    main()
                    frame.place_forget()
                    can_search.place_forget()
                    can_npl.place_forget()
                    play_vid(tm)


            elif play_video_st==1:
                cap=None
                play_video_st=0
                
                main()

        """





        


    #search

    cx,cy=w-10-5-20+10-10-25,40+5+30-10-5-5+10

    if cx-10<=e.x<=cx+10:
        if cy-10<=e.y<=cy+10:



            
            can_search.place_forget()
            can.focus_set()
            _search=0

            search_var=""

            main()

            move_to_playing()


            return

    if 10<=e.x<=w-10-5-30:
        if 40+30-10-5<=e.y<=40+30+30-10-5:

            _search=1

            vid_st=0
            vid_st2=0

            #search.place(in_=root,x=10+15,y=45+30-10-5-5)
            #search.focus_set()

            can_search["width"]=w-10-10-25-10-15-10-20
            can_search["height"]=28


            search_var=""

            can_search.delete("all")

            can_search.create_image(-(10+15),-(50+1),image=bg,anchor="nw")



            can_search.place(in_=root,x=10+15,y=50+1)
            can_search.focus_set()

            main()



            return






    #add songs

    if st==4:

        yv=50+(((h-121)-50)-90)/2



        #can.create_rectangle(w/2-150,yv, w/2+150,yv+30, fill=col1)


        cx,cy=w/2-80,yv+15

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:


            if convert==0:

                input_folder=filedialog.askdirectory(title="Select a Folder")

                if not input_folder=="":
                    convert=1
                    start_conversion()



            return


        cx,cy=w/2+80,yv+15

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:


            if convert==0:
                input_folder=filedialog.askdirectory(title="Select a Folder")

                if not input_folder=="":
                    convert=1
                    start_conversion()

            return


        if w/2-80<=e.x<=w/2+80:
            if yv<=e.y<=yv+30:


                if convert==0:
                    input_folder=filedialog.askdirectory(title="Select a Folder")

                    if not input_folder=="":
                        convert=1
                        start_conversion()


                return


















        cx,cy=w/2-80,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:


            if convert==0:
                input_file=filedialog.askopenfilename()

                if not input_file=="":
                    convert=2
                    start_conversion()



            return



        cx,cy=w/2+80,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:

            if convert==0:

                input_file=filedialog.askopenfilename()
                if not input_file=="":
                    convert=2
                    start_conversion()


            return



        if w/2-80<=e.x<=w/2+80:
            if yv+60<=e.y<=yv+30+60:


                if convert==0:
                    input_file=filedialog.askopenfilename()

                    if not input_file=="":
                        convert=2
                        start_conversion()


                return






    #minimize

    cx,cy=w-10-25-10-25+12.5,(50-25)/2+12.5

    if cx-12.5<=e.x<=cx+12.5:
        if cy-12.5<=e.y<=cy+12.5:
            root_st=1

            main()

            return


    #quit

    cx,cy=w-10-25+12.5,(50-25)/2+12.5

    if cx-12.5<=e.x<=cx+12.5:
        if cy-12.5<=e.y<=cy+12.5:


            root.destroy()

            return

        



    """
    #fullscreen

    cx,cy=w-10-20+10,10+10

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)
    if r<=10:
        if expand_st==0:
            expand_st=1

            root.wm_attributes("-fullscreen",1)
            main()
        elif expand_st==1:        
            expand_st=0

            if len(sig)==673:
                sig=sig[(673-465):]



            root.wm_attributes("-fullscreen",0)
            root.geometry("950x680+208+0")
            main()
    """


    #return to status


                

                



    if 10<=e.x<=w-10:
        if h-20-60-20-27-15+3+10+3+2+2-3+1+10<=e.y<=h-20-60-20-27-15+3+10+3+2+2-3+30-1+1+10:

            try:
                con=0
                if st==songs_status[0]:
                    if st==2:
                        if current_playlist==songs_status[1]:
                            con=1
                    else:
                        con=1





                st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing=songs_status

                if st==2:
                    if current_playlist!="":
                        playlist_st=1


                
                if con==0 or lst==0 or st!=songs_status[0]:
                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))





                lst=1
                lyric_st=0

                filter_st=0
                filter_can1.place_forget()
                filter_can2.place_forget()

                vid_st=0
                vid_st2=0

                

                main()

                move_to_playing(1)


                return


            except:
                pass


    if w-10-25<=e.x<=w-10:
        if 40+30-10-5-5+2.5<=e.y<=40+30-10-5-5+2.5+25:

            if lst==1:

                if filter_st==0:

                    filter_st=1



                    filter_can2["scrollregion"]=(0,0,int(filter_can2["width"]),int(filter_can2["height"]))

                    if filter_val=="Playlists" and filter_pl==None:
                        filter_val="None"


                    draw_can()

                elif filter_st==1:
                    filter_st=0

                    filter_can1.place_forget()
                    filter_can2.place_forget()

                    draw_can()


        
filter_val="None"

vol1,vol2,vol3,vol4=0,0,0,0
def check_volume():
    global current_volume
    global can,vol1,vol2,vol3,vol4

    global circle7,circle8
    global volume




    col1=_theme[0]
    col2=_theme[1][0]


    if volume.GetMasterVolumeLevelScalar()!=current_volume:

        current_volume=volume.GetMasterVolumeLevelScalar()

        can.delete(vol1)
        can.delete(vol2)
        can.delete(vol3)
        can.delete(vol4)        


        r=(w-10)-(w-10-120)

        vol1=can.create_line(w-10-120,h-20-30+5+10-3 ,w-10-120+current_volume*r,h-20-30+5+10-3,fill=col1,width=2)

        vol2=can.create_text(w-10,h-20-30+5+10-3+12,text=str(int(current_volume*100))+"%",fill=col1,font=("FreeMono",11),anchor="e")

        vol3=can.create_image(w-10-120+current_volume*r-4,h-20-30+5+10-3-4,image=circle7,anchor="nw")
        vol4=can.create_image(w-10-120+current_volume*r-3,h-20-30+5+10-3-3,image=circle8,anchor="nw")
  

    root.after(500,check_volume)






def play_music(file,time,con=0):
    global current_playing
    global sig,tts
    global play_st

    global vid_st,vid_st2


    if play_st==1:

        if time==0:

            vid_st=0
            vid_st2=0

            sig=[]
            tts=0



        # Initialize Pygame Mixer
        pygame.mixer.init()


        # Load the audio file
        pygame.mixer.music.load(file)  # Replace with your audio file path

        if con==0:

            update_details(current_playing,1)

        # Start playing the audio from a specific position (in seconds)
        start_time = time  # Replace with the desi#38fca5 starting time in seconds
        pygame.mixer.music.play(start=round(start_time))  # Use round for an integer value

        pygame.mixer.music.set_volume(1.0)

        songs_status[-1]=current_playing








def get_audio_duration(file_path):
    global tot_tm,tot_tm_
    """
    Get the duration of an audio file in seconds using Mutagen.

    Parameters:
    file_path (str): Path to the audio file.

    Returns:
    float: Duration of the audio file in seconds.
    """
    try:
        audio = MP3(file_path)
        seconds = audio.info.length  # Duration in seconds

        tot_tm_=seconds


        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        if int(hour)>0:


            if int(minutes)<10:
                mm="0"+str(int(minutes))
            else:
                mm=str(int(minutes))

            if int(seconds)<10:
                ss="0"+str(int(seconds))
            else:
                ss=str(int(seconds))

            tt=str(int(hour))+":"+mm+":"+ss
        else:


            if int(minutes)<10:
                mm="0"+str(int(minutes))
            else:
                mm=str(int(minutes))

            if int(seconds)<10:
                ss="0"+str(int(seconds))
            else:
                ss=str(int(seconds))


            tot_tm=mm+":"+ss

    except:
        pass

# Example usage
#file_path = "music/24.mp3"  # Replace with your file path
#duration = get_audio_duration(file_path)
#print(f"Duration: {duration} seconds")


expand_st=0

songs2=[]
playlist_select=""

_bg2_=None


def _text_(c,text,font,size,l):



    while 1:


        if get_text_length(c, text,font,size)<=l:

            
            return text

        else:
            text=text[:-1]


def draw_active(c,x,y,x2,sz,col):

    #draw_round_rec(can2,x,y, int(can2["width"])-1,y+50,10,col1,col1,1)
    #draw_round_rec(can2,x+2,y+2, int(can2["width"])-1-2,y+50-2,10,col1,col1,1)
    #return
    



    c.create_image(x,y,image=circle4,anchor="nw")
    c.create_image(x2,y,image=circle4,anchor="ne")
    c.create_image(x2,y+sz,image=circle4,anchor="se")
    c.create_image(x,y+sz,image=circle4,anchor="sw")

    c.create_polygon(x+10,y, x2-10-1,y, x2-1,y+10, x2-1,y+sz-10-1,
    x2-10-1,y+sz-1, x+10,y+sz-1, x,y+sz-10-1, x,y+10, fill=col,outline=col )



_bg4_=0

bg2=0
cp_im=0

cp_im2=0
cp_im3=0
def main():

    global can,st,w,h,wd,ht
    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global pp,fv,lst
    global frame,can2
    global current_playing
    global yyy

    global songs
    global search,search_var,_search
    global cancel,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,sort,delete,favourite1_,favourite2_,delete2,playlist3
    global music_details
    global vol1,vol2,current_volume
    global playlist,playlist_st
    global can2,sb
    global current_playlist
    global _playlist
    global ctime,prog1,prog2
    global pl_st
    global shuff,shuffle_st,shuffle_ar

    global _pl_,_fv_,_del_
    global sort_val,sort2
    global tm,mvar
    global loop,loop1,loop2
    global wallpaper,wallpaper2
    global _search,_npl
    global circle2,circle3,circle4,circle4

    global expand,expand2,expand_st

    global playlist4

    global style,style2

    global red,mint,cyan
    global paste
    global lyric_st
    global video1,video2,video3
    global play_video_st
    global can_lyrics
    global quit,minimize
    global root_st

    global vid_canvas,play_video_st
    global circlex

    global select_st

    global checked,add,add2
    global songs2,playlist_select
    global nomusic
    global _songs_,songs_status
    global _bg2_

    global transparent_im,transparent_im2
    global note
    global note2,_bg4_
    global can2_cur,cur
    global bg2,bg
    global sb_sz
    global images
    global cp_im,cp_im2,cp_im3

    global cur_can,circle7,circle11

    global cursor
    global settings
    global _theme
    global filter_val,filter_pl
    global no_music
    global can_npl,npl_var
    global settings_st2
    global f1_,f2_



    wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()
    can["bg"]="#333333"

    if root_st==1:

        root.geometry(str(50)+"x"+str(50)+"+"+str(wd-3-50)+"+"+str(ht-51-50))

        can.delete("all")

        can.create_image(0,0, image=circlex, anchor="nw")

        can.create_image(10,10, image=musical_note2, anchor="nw")

        frame.place_forget()
        search_var=""
        _search=0
        can_search.place_forget()
        
        play_video_st=0


    else:





        if add_st==0 and sort_st==0:

            images=[]




        col1=_theme[0]



        

        can2["bg"]="#000000"






        update_details()
        create_playlist()




        if shuff==1 or shuff==2:
            sort_val=""








        frame["width"]=w-12
        frame["height"]=((h-121)-80-10)

        can2["width"]=w-12
        can2["height"]=((h-121)-80-10)


        can["width"]=w
        can["height"]=h







        






        def sort_data_added(descending: bool = True):


            ar=[]

            for s in music_details:
                ar.append(s)


            if descending==True:

                ar2=[]

                p=-1

                for s in range(len(ar)):

                    ar2.append(ar[p])
                    p-=1

                return ar2

            return ar





        def sort_title(directory: str, descending: bool = False):
            # Get the list of all items in the directory
            items = os.listdir(directory)

            # Sort the items alphabetically (case-insensitive)x
            sorted_items = sorted(items, key=str.lower, reverse=descending)

            return sorted_items     


        can2.delete("all")


        bg2=can2.create_image(-10,-(90-2)+int(can2.canvasy(0)),image=bg,anchor="nw")



        ar=[]

        r=10
        y_=0

        a_=180


        cx,cy=r,y_+r

        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy



            ar.append(int(round(x,0)))
            ar.append(int(round(y,0)))

            a_+=1

        a_=270

        cx,cy=r,y_+50-r

        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy



            ar.append(int(round(x,0)))
            ar.append(int(round(y,0)))

            a_+=1
        

        a_=0

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,y_+50-r

        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy



            ar.append(int(round(x,0)))
            ar.append(int(round(y,0)))

            a_+=1

     
        a_=90

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,y_+r

        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy



            ar.append(int(round(x,0)))
            ar.append(int(round(y,0)))

            a_+=1


        #can2.create_polygon(ar,fill="red")

        cp_im=create_polygon(*ar, fill=_theme[0], alpha=_theme[3],can=can2)


        r=10

        ar=[]

        a_=270

        cx,cy=((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50+r*2,r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1


        r=10
        a_=180

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1


        r=10
        a_=90

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,50-r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1



        r=10
        a_=0

        cx,cy=((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50,50-r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_+=1




        cp_im2=create_polygon(*ar, fill="#000000", alpha=0.7,can=can2)





        r=10

        ar=[]

        a_=270

        cx,cy=((int(can2["width"])-sb_sz-1)-25*2-15*2-10)-10+r*2,r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1


        r=10
        a_=180

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1


        r=10
        a_=90

        cx,cy=(int(can2["width"])-sb_sz-1)-2-r,50-r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_-=1



        r=10
        a_=0

        cx,cy=((int(can2["width"])-sb_sz-1)-25*2-15*2-10)-10,50-r
        for a in range(90):

            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy

            x=int(round(x,0))
            y=int(round(y,0))

            ar.append(x)
            ar.append(y)

            a_+=1




        cp_im3=create_polygon(*ar, fill="#000000", alpha=0.7,can=can2)

        can2.coords(cp_im,0,-100)
        can2.coords(cp_im2,0,-100)
        can2.coords(cp_im3,0,-100)        












        if select_st==1:


            y=1

            


            all_songs = sort_data_added(descending=True)



            ar=[]
            for i in all_songs:
                try:
                
                        ar.append(str(i).split("\\")[1])
                except:
                    ar.append(i)
                    pass




            all_songs=ar

            frame["height"]=int(frame["height"])+75
            can2["height"]=int(can2["height"])+75





            songs2=[]
            

            for song in all_songs:

                scon=0


                sval=search_var.lower()

                if sval.find(" ")!=-1:

                    ss=[]

                    s_ar=sval.split(" ")

                    for sv in s_ar:

                        if song.lower().find(sv)!=-1:
                            ss.append(1)
                        else:
                            ss.append(0)

                    scon=1

                    for ss_ in ss:

                        if ss_==0:
                            scon=0
                            break

                else:
                    if song.lower().find(sval)!=-1:
                        scon=1


                if scon==1:

                    if filter_val=="None":
                        pass

                    elif filter_val=="Favourites":


                        if music_details[song][0]==0:
                            scon=0

                    elif filter_val=="With Video":

                        ar=os.listdir("videos")


                        try:

                            v_=ar.index(song.replace(".mp3",".mp4"))
                        except:
                            scon=0
                    elif filter_val=="Playlists":

                        if not filter_pl==None:

                            


                            try:

                                ar=playlist[filter_pl]


                                p=ar.index(song)
                            except:
                                scon=0











                if scon==1:

                    can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                    col=col1



                    if get_text_length(can2, song[:-4], "FreeMono", 13)>(int(can2["width"])-20-20-20)-50:

                        l=get_text_length(can2, "...", "FreeMono", 13)
                        txt=_text_(can2,song[:-4],"FreeMono",13,(int(can2["width"])-20-20-20)-50-l)+"..."

                    else:
                        txt=song[:-4]


                    can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                    
                    try:

                        v=playlist[playlist_select].index(song)



                        can2.create_image(int(can2["width"])-20-20,y+15,image=checked,anchor="nw")

                    except:
                        pass








                    #can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col3)

                    ar=[song,y]

                    songs2.append(ar)

                    y+=50

            if len(songs2)==0:

                can2.create_image((w-7)/2-150,((h-121)-80-10)/2-150,image=no_music,anchor="nw")



            if y+1<=int(can2["height"]):

                can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            else:
                can2["scrollregion"]=(0,0,int(can2["width"]),y+1)





        else:




            if st==songs_status[0]:

                if st==2:

                    if current_playlist==songs_status[1]:

                        filter_val=f1_
                        filter_pl=f2_


                       


                else:

                    filter_val=f1_
                    filter_pl=f2_



            y=0

            if shuffle_st==1 or shuffle_st==2:
                shuff=1
            else:
                shuff=0

                if sort_val=="":
                    sort_val=sort_ar[0][0]



            


            all_songs = os.listdir("music")

            if shuffle_st==0:

                if sort_val=="Date Added (Descending)":
                    all_songs = sort_data_added(descending=True)

                elif sort_val=="Date Added (Ascending)":
                    all_songs = sort_data_added(descending=False)

                elif sort_val=="Title (Descending)":
                    all_songs= sort_title("music", descending=True)

                elif sort_val=="Title (Ascending)":
                    all_songs= sort_title("music", descending=False)





            elif shuffle_st==1:


                if current_playing!="":
                    shuffle_ar=[current_playing]

                    ar=all_songs

                    v=ar.index(current_playing)

                    ar.pop(v)

                    random.shuffle(ar)

                    for s in ar:
                        shuffle_ar.append(s)


                else:

                    shuffle_ar=all_songs
                    random.shuffle(shuffle_ar)

                    all_songs=shuffle_ar


                all_songs=shuffle_ar


                """
                try:
                    current_playing=all_songs[0]
                    tm=0
                    mvar=0
                    play_music("music/"+current_playing,tm,1)
                    get_audio_duration("music/"+current_playing)

                    if play_st==0:
                        pygame.mixer.quit()
                    main()
                    prog()
                except:
                    pass
                """
                shuffle_st=2


            elif shuffle_st==2:
                all_songs=shuffle_ar













            #hex(can,-30,-30,w+60,h+60,30,"#390200","#000000")

            """
            if expand_st==0:
                can.create_image(w-10-20,10,image=expand,anchor="nw")
            elif expand_st==1:
                can.create_image(w-10-20,10,image=expand2,anchor="nw")"""







            #can2.create_image(-10,can2.canvasy(-(80-30+40))-h,image=wallpaper,anchor="nw")
            #can2.create_image(-10,can2.canvasy(-(80-30+40)),image=wallpaper,anchor="nw",tags="fixed_image")
            #can2.create_image(-10,can2.canvasy(-(80-30+40))+h,image=wallpaper,anchor="nw")
            #create_rectangle(can2,0, int(can2.canvasy(0))-h, int(can2["width"]), int(can2.canvasy(int(can2["height"])))+h, fill='#000000', alpha=.65)















            if lst==1 and st!=4:

                
                pass
                #can.create_line(10,80-30+40+5+int(can2["height"]),w-10,80-30+40+5+int(can2["height"]),fill=col2)

            


            if st==0:
                y=1

                songs=[]
                

                for song in all_songs:


                    scon=0


                    sval=search_var.lower()

                    if sval.find(" ")!=-1:

                        ss=[]

                        s_ar=sval.split(" ")

                        for sv in s_ar:

                            if song.lower().find(sv)!=-1:
                                ss.append(1)
                            else:
                                ss.append(0)

                        scon=1

                        for ss_ in ss:

                            if ss_==0:
                                scon=0
                                break
                    else:
                        if song.lower().find(sval)!=-1:
                            scon=1



                    ["None","Favourites","Playlists","With Video"]


                    if scon==1:

                        if filter_val=="None":
                            pass

                        elif filter_val=="Favourites":


                            if music_details[song][0]==0:
                                scon=0

                        elif filter_val=="With Video":

                            ar=os.listdir("videos")


                            try:

                                v_=ar.index(song.replace(".mp3",".mp4"))
                            except:
                                scon=0
                        elif filter_val=="Playlists":

                            if not filter_pl==None:

                                


                                try:

                                    ar=playlist[filter_pl]


                                    p=ar.index(song)
                                except:
                                    scon=0







                    if scon==1:



                        if song==current_playing:



                            #can2.create_rectangle(2,y, (int(can2["width"])-sb_sz-1),y+50-1,fill=col1,outline=col1)

                            #draw_round_rec(can2,2,y, (int(can2["width"])-sb_sz-1),y+50,10,col1,col1,0)

                            #draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)
                            draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)

                            can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                            col="#000000"



                        else:



                            can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                            col=_theme[0]


                        if get_text_length(can2, song[:-4], "FreeMono", 13)>((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50:

                            l=get_text_length(can2, "...", "FreeMono", 13)
                            txt=_text_(can2,song[:-4],"FreeMono",13,((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50-l)+"..."

                        else:
                            txt=song[:-4]


                        can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                        



                        """

                        if music_details[song][3]==True:

                            if song==current_playing:
                                can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=video3,anchor="nw")
                            else:

                               can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=video2,anchor="nw")
                        elif music_details[song][3]==False:

                            can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=video1,anchor="nw")

                        """







                        #if not song==current_playing:

                        #    can2.create_line(0,y+50,(int(can2["width"])-sb_sz-1),y+50,fill=col3)

                        ar=[song,y]

                        songs.append(ar)

                        y+=50

                if len(songs)==0:
                    


                    can2.create_image((int(can2["width"])-sb_sz-1)/2-150,int(can2["height"])/2-150,image=no_music,anchor="nw")
                    




            elif st==1:
                y=1
                songs=[]


                for song in all_songs:


                    scon=0


                    sval=search_var.lower()

                    if sval.find(" ")!=-1:
                        ss=[]

                        s_ar=sval.split(" ")

                        for sv in s_ar:

                            if song.lower().find(sv)!=-1:
                                ss.append(1)
                            else:
                                ss.append(0)

                        scon=1

                        for ss_ in ss:

                            if ss_==0:
                                scon=0
                                break
                    else:
                        if song.lower().find(sval)!=-1:
                            scon=1

                    if scon==1:

                        if filter_val=="None":
                            pass

                        elif filter_val=="Favourites":


                            if music_details[song][0]==0:
                                scon=0

                        elif filter_val=="With Video":

                            ar=os.listdir("videos")


                            try:

                                v_=ar.index(song.replace(".mp3",".mp4"))
                            except:
                                scon=0
                        elif filter_val=="Playlists":

                            if not filter_pl==None:

                                


                                try:

                                    ar=playlist[filter_pl]


                                    p=ar.index(song)
                                except:
                                    scon=0




                    if scon==1:

                        if music_details[song][0]==1:

                            if song==current_playing:

                                #can2.create_rectangle(2,y, (int(can2["width"])-sb_sz-1),y+50-1,fill=col1,outline=col1)
                                #draw_round_rec(can2,2,y, (int(can2["width"])-sb_sz-1),y+50,10,col1,col1,0)

                                draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)
                                col="#000000"

                                can2.create_image(0,y+10,image=musical_note1,anchor="nw")

                            else:
                                col=col1
                                can2.create_image(0,y+10,image=musical_note2,anchor="nw")



                            if get_text_length(can2, song[:-4], "FreeMono", 13)>((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50:

                                l=get_text_length(can2, "...", "FreeMono", 13)
                                txt=_text_(can2,song[:-4],"FreeMono",13,((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50-l)+"..."

                            else:
                                txt=song[:-4]


                            can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                            


     
                            #if not song==current_playing:

                            #    can2.create_line(0,y+50,(int(can2["width"])-sb_sz-1),y+50,fill=col3)





                            ar=[song,y]

                            songs.append(ar)

                            y+=50



                if len(songs)==0:


                    can2.create_image((int(can2["width"])-sb_sz-1)/2-150,int(can2["height"])/2-150,image=no_music,anchor="nw")
                    




            elif st==2:




                if playlist_st==0:
                    y=0
                    y=5



                    ar=[]

                    a_=180
                    for a in range(180):
                        x=15*math.sin(math.radians(a_))+10+15
                        y_=15*math.cos(math.radians(a_))+y+15

                        ar.append(int(round(x,0)))
                        ar.append(int(round(y_,0)))

                        a_+=1


                    a_=0
                    for a in range(180):
                        x=15*math.sin(math.radians(a_))+(int(can2["width"])-sb_sz-1)-10-15
                        y_=15*math.cos(math.radians(a_))+y+15



                        ar.append(int(round(x,0)))
                        ar.append(int(round(y_,0)))

                        
                        a_+=1


                    

                    if _npl==1:
                        pass

                    else:

                        create_polygon(*ar, fill=_theme[0], alpha=0.35,can=can2)



                    draw_round_rec(can2,10,y,(int(can2["width"])-sb_sz-1)-10,y+30,15,col1,"",1)



                    can2.create_text(30,y+15,text="New Playlist",font=("FreeMono",13),fill=_theme[0],anchor="w")

                    can2.create_image((int(can2["width"])-sb_sz-1)-10-5-20,y+5,image=cancel,anchor="nw")


                    y+=40






                    #can2.create_rectangle((int(can2["width"])-sb_sz-1)/2-100,y, (int(can2["width"])-sb_sz-1)/2+100,y+30, outline=col1)

                    can2.create_image((int(can2["width"])-sb_sz-1)/2-100-15,y,image=circle3,anchor="nw")
                    can2.create_image((int(can2["width"])-sb_sz-1)/2+100-15,y,image=circle3,anchor="nw")

                    can2.create_rectangle((int(can2["width"])-sb_sz-1)/2-100,y, (int(can2["width"])-sb_sz-1)/2+100,y+30-1,fill=col1,outline=col1)


                    can2.create_text((int(can2["width"])-sb_sz-1)/2,y+15,text="Create New Playlist",font=("FreeMono",13),fill="#000000")

                    y+=30+20


                    _playlist=[]

                    conx=0


                    for pl in playlist:



                        scon=0


                        sval=search_var.lower()

                        if sval.find(" ")!=-1:

                            ss=[]

                            s_ar=sval.split(" ")

                            for sv in s_ar:

                                if pl.lower().find(sv)!=-1:
                                    ss.append(1)
                                else:
                                    ss.append(0)

                            scon=1

                            for ss_ in ss:

                                if ss_==0:
                                    scon=0
                                    break
                        else:
                            if pl.lower().find(sval)!=-1:
                                scon=1


                        if scon==1:
                            
                            if conx==0:

                                #can2.create_line(2,y, (int(can2["width"])-sb_sz-1)-3,y,fill=col3)


                                conx=1




                            if current_playlist==pl:

                                #can2.create_rectangle(2,y, (int(can2["width"])-sb_sz-1),y+50-1,fill=col1,outline=col1)
                                #draw_round_rec(can2,2,y, (int(can2["width"])-sb_sz-1),y+50,10,col1,col1,0)

                                draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)

                                col="#000000"
                                _pl_=playlist3
                                

                            else:

                                col=col1

                                _pl_=playlist2
                                



                            can2.create_image(5,y+25-12.5,image=_pl_,anchor="nw")



                            if get_text_length(can2, pl, "FreeMono", 13)>((int(can2["width"])-sb_sz-1)-25*2-15*2-10)-50:

                                l=get_text_length(can2, "...", "FreeMono", 13)
                                txt=_text_(can2,pl,"FreeMono",13,((int(can2["width"])-sb_sz-1)-25*2-15*2-10)-50-l)+"..."

                            else:
                                txt=pl


                            can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                            





                            #if current_playlist!=pl:
                            #    can2.create_line(0,y+50, (int(can2["width"])-sb_sz-1),y+50,fill=col3)

                            _playlist.append([pl,y])



                            y+=50

                    if len(_playlist)==0:

                        
                        can2.create_image((int(can2["width"])-sb_sz-1)/2-150,int(can2["height"])/2-150,image=no_music,anchor="nw")
                    
                        




                elif playlist_st==1:

                    y=1

                    songs=[]


                    ar=playlist[current_playlist]




                    for song in all_songs:



                        scon=0


                        sval=search_var.lower()

                        if sval.find(" ")!=-1:

                            ss=[]

                            s_ar=sval.split(" ")

                            for sv in s_ar:

                                if song.lower().find(sv)!=-1:
                                    ss.append(1)
                                else:
                                    ss.append(0)

                            scon=1

                            for ss_ in ss:

                                if ss_==0:
                                    scon=0
                                    break
                        else:
                            if song.lower().find(sval)!=-1:
                                scon=1


                        if scon==1:

                            if filter_val=="None":
                                pass

                            elif filter_val=="Favourites":


                                if music_details[song][0]==0:
                                    scon=0

                            elif filter_val=="With Video":

                                ar_=os.listdir("videos")


                                try:

                                    v_=ar_.index(song.replace(".mp3",".mp4"))
                                except:
                                    scon=0
                            elif filter_val=="Playlists":

                                if not filter_pl==None:

                                    


                                    try:

                                        ar_=playlist[filter_pl]


                                        p=ar_.index(song)
                                    except:
                                        scon=0



                        if scon==1:

                            try:
                                v=ar.index(song)

                            
                                if song==current_playing:

                                    #can2.create_rectangle(2,y, (int(can2["width"])-sb_sz-1),y+50-1,fill=col1,outline=col1)
                                    #draw_round_rec(can2,2,y, (int(can2["width"])-sb_sz-1),y+50,10,col1,col1,0)

                                    draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)


                                    can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                                    col="#000000"

                                else:



                                    can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                                    col=col1




                                if get_text_length(can2, song[:-4], "FreeMono", 13)>((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50:

                                    l=get_text_length(can2, "...", "FreeMono", 13)
                                    txt=_text_(can2,song[:-4],"FreeMono",13,((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50-l)+"..."

                                else:
                                    txt=song[:-4]


                                can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                                




                                songs.append([song,y])

                                y+=50
                            except:
                                pass
                    if len(songs)==0:


                        can2.create_image((int(can2["width"])-sb_sz-1)/2-150,int(can2["height"])/2-150,image=no_music,anchor="nw")
                    



            elif st==3:
                y=1
                songs=[]

                ar_=[]
                for song in all_songs:

                    scon=0


                    sval=search_var.lower()

                    if sval.find(" ")!=-1:

                        ss=[]

                        s_ar=sval.split(" ")

                        for sv in s_ar:

                            if song.lower().find(sv)!=-1:
                                ss.append(1)
                            else:
                                ss.append(0)

                        scon=1

                        for ss_ in ss:

                            if ss_==0:
                                scon=0
                                break
                    else:
                        if song.lower().find(sval)!=-1:
                            scon=1

                    if scon==1:

                        if filter_val=="None":
                            pass

                        elif filter_val=="Favourites":


                            if music_details[song][0]==0:
                                scon=0

                        elif filter_val=="With Video":

                            ar=os.listdir("videos")


                            try:

                                v_=ar.index(song.replace(".mp3",".mp4"))
                            except:
                                scon=0
                        elif filter_val=="Playlists":

                            if not filter_pl==None:

                                


                                try:

                                    ar=playlist[filter_pl]


                                    p=ar.index(song)
                                except:
                                    scon=0


                    if scon==1:
                        ar_.append([song,music_details[song][1]])

                #print(len(ar_))


                ar_=sorted(ar_, key=lambda row: row[1], reverse=True)



                for song in ar_:



                    if song[0]==current_playing:

                        #can2.create_rectangle(2,y, (int(can2["width"])-sb_sz-1),y+50-1,fill=col1,outline=col1)

                        #draw_round_rec(can2,2,y, (int(can2["width"])-sb_sz-1),y+50,10,col1,col1,0)

                        draw_active(can2,0,y,(int(can2["width"])-sb_sz-1)-1,51,col1)

                        col="#000000"

                        can2.create_image(0,y+10,image=musical_note1,anchor="nw")

                    else:


                        can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                        col=col1



                    if get_text_length(can2, song[0][:-4], "FreeMono", 13)>((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50:

                        l=get_text_length(can2, "...", "FreeMono", 13)
                        txt=_text_(can2,song[0][:-4],"FreeMono",13,((int(can2["width"])-sb_sz-1)-25*3-15*3-10)-50-l)+"..."

                    else:
                        txt=song[0][:-4]


                    can2.create_text(50,y+25,text=txt,font=("FreeMono",13),fill=col,anchor="w")
                    










                    ar=[song[0],y]

                    songs.append(ar)

                    y+=50

                if len(songs)==0:





                    can2.create_image((int(can2["width"])-sb_sz-1)/2-150,int(can2["height"])/2-150,image=no_music,anchor="nw")
                    
            """
            if y<=((h-121)-80-10):
                hex(can2,-30,-30,w+60,int(can2["height"])+60,30,"#390200","#000000")


            else:

                hex(can2,-30,-30,w+60,y+60,30,"#390200","#000000")

            """


            if lst==0:

                if not playlist_st==0:

                    _search=0
                    _npl=0

                    search_var=""

                    
                    can_search.place_forget()



                    _npl=0
                    can_npl.place_forget()

            
            if lyric_st==0:
                can_lyrics.place_forget()

            if _search==0 and _npl==0 and settings_st2==0:
                can.focus_set()



            if y+1<=int(can2["height"]):

                can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            else:
                can2["scrollregion"]=(0,0,int(can2["width"]),y+1)


        if st==songs_status[0]:

            if st==2:

                if current_playlist==songs_status[1]:

                    if _search==0:


                        _songs_=songs

                   


            else:

                if _search==0:
                    _songs_=songs


        draw_can()



    x,y=pyautogui.position()

    xx,yy=x-(wd-w)/2,y-(ht-h)/2


    can.delete(cur_can)

    cur_can=can.create_image(xx,yy,image=cursor,anchor="nw")

    can_label(xx,yy)

def get_text_length(canvas, text, font_name, font_size):
    # Create a tkinter font object with the given font name and size
    text_font = font.Font(family=font_name, size=font_size)

    # Measure the width of the text in pixels
    text_width = text_font.measure(text)
    return text_width  



images_ = []  # to hold the newly created image

def create_rectangle_(can,x1, y1, x2, y2, **kwargs):
    global images_
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images_.append(ImageTk.PhotoImage(image))
        can.create_image(x1, y1, image=images_[-1], anchor='nw')
_bg_=None

vid_tm=0
def vid_timer():
    global vid_tm,vid_st2,vid_st2_
    global vid_st
    global can,cur_can
    global sort_st,settings_st2
    global play_st


    if settings_st2==1 or sort_st==1 or play_st==0:
        vid_tm=time.time()

    if vid_st==1:

        if time.time()<vid_tm+5:
            vid_st2=1
        else:
            vid_st2=0
            can.delete(cur_can)
            

    else:
        vid_st2=0
        vid_st2_=0






    if vid_st2!=vid_st2_:
        draw_can()
        vid_st2_=vid_st2





    root.after(2,vid_timer)


vid_st=0
vid_st2=0
vid_st2_=0

filter_st=0
filter_pl=None

bg_f2=0


def draw_can(con=0):

    global can,st,w,h
    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global pp,fv,lst
    global frame,can2
    global current_playing
    global yyy

    global songs
    global search,search_var
    global cancel,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,sort,delete,favourite1_,favourite2_,delete2,playlist3
    global music_details
    global vol1,vol2,vol3,vol4,current_volume
    global playlist,playlist_st
    global can2,sb
    global current_playlist
    global _playlist
    global ctime,prog1,prog2,prog3
    global pl_st
    global shuff,shuffle_st,shuffle_ar

    global _pl_,_fv_,_del_
    global sort_val,sort2
    global tm,mvar
    global loop,loop1,loop2
    global wallpaper,wallpaper2
    global _search,_npl,npl
    global circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle5

    global expand,expand2,expand_st

    global playlist4

    global style,style2

    global lyric_st

    global play_video_st


    global select_st
    global songs_status
    global quit,minimize
    global forward,backward
    global _bg_

    global transparent_im,transparent_im2,transparent_im3

    global note
    global circle6
    global bg,bg2_
    global favourite2
    global can_cur,cur
    global delete
    global volume
    global copy
    global settings
    global _theme
    global delete_
    global vid1,vid2
    global vid_st
    global vframe,vid_st
    global vid_st2
    global root_st


    global filter_st,filter_val,filter_
    global filter_can1,filter_can2
    global filter_pl
    global f2
    global bg_f2
    global f1_,f2_



    if root_st==1:

        can["bg"]="#333333"

        root.geometry(str(50)+"x"+str(50)+"+"+str(wd-3-50)+"+"+str(ht-51-50))

        can.delete("all")

        can.create_image(0,0, image=circlex, anchor="nw")

        can.create_image(10,10, image=musical_note2, anchor="nw")

        frame.place_forget()

        search_var=""
        _search=0
        can_search.place_forget()

        return



    can.delete("all")

    vframe=[0,0,0]







    if shuff==1 or shuff==2:
        sort_val=""



    col1=_theme[0]
    col2=_theme[1][0]




    can["bg"]="#000000"

    can.create_image(0,0,image=bg,anchor="nw")




    if vid_st==1:

        can.create_rectangle(0,0,w,h,fill="#000000",outline="#000000")









        if vframe[-1]==0:

            try:

                im=Image.open("data/frame.jpg")
                x,y=im.size

                x_,y_=(w-x)/2,(h-y)/2

                if vframe[0]==0:
                    vframe[0]=ImageTk.PhotoImage(file="data/frame.jpg")

                vframe[1]=can.create_image(x_,y_,image=vframe[0],anchor="nw")

                vframe[-1]=1

            except:
                pass

    if vid_st2==1:

        ar=[]

        r=20

        cx,cy=r,50+r
        a_=270
        for a in range(90):
            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy
            
            x=int(round(x,0))
            y=int(round(y,0))
            
            ar.append(x)
            ar.append(y)
            a_-=1



        cx,cy=w-r,50+r
        a_=180
        for a in range(90):
            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy
            
            x=int(round(x,0))
            y=int(round(y,0))
            
            ar.append(x)
            ar.append(y)
            a_-=1



        ar.append(w)
        ar.append(0)

        ar.append(0)
        ar.append(0)


        create_polygon(*ar, fill="#000000", alpha=0.7,can=can)



        ar=[]



        cx,cy=r,90+int(can2["height"])-r
        a_=270
        for a in range(90):
            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy
            
            x=int(round(x,0))
            y=int(round(y,0))
            
            ar.append(x)
            ar.append(y)
            a_+=1



        cx,cy=w-r,90+int(can2["height"])-r
        a_=0
        for a in range(90):
            x=r*math.sin(math.radians(a_))+cx
            y=r*math.cos(math.radians(a_))+cy
            
            x=int(round(x,0))
            y=int(round(y,0))
            
            ar.append(x)
            ar.append(y)
            a_+=1

        ar.append(w)
        ar.append(h)

        ar.append(0)
        ar.append(h)

        


        create_polygon(*ar, fill="#000000", alpha=0.7,can=can)


    def draw_round_rec2(c,x,y,x2,y2,r,col):


        ar=[]

        a_=270

        cx,cy=x+r,y+r
        for a in range(90):

            x_=r*math.sin(math.radians(a_))+cx
            y_=r*math.cos(math.radians(a_))+cy

            ar.append(x_)
            ar.append(y_)

            a_-=1

        ar.append(x)
        ar.append(y)


        c.create_polygon(ar,fill=col,outline=col)



        ar=[]

        a_=180

        cx,cy=x2-r,y+r
        for a in range(90):

            x_=r*math.sin(math.radians(a_))+cx
            y_=r*math.cos(math.radians(a_))+cy

            ar.append(x_)
            ar.append(y_)

            a_-=1
        ar.append(x2)
        ar.append(y)

        c.create_polygon(ar,fill=col,outline=col)




        ar=[]

        a_=90

        cx,cy=x2-r,y2-r
        for a in range(90):

            x_=r*math.sin(math.radians(a_))+cx
            y_=r*math.cos(math.radians(a_))+cy

            ar.append(x_)
            ar.append(y_)

            a_-=1
        ar.append(x2)
        ar.append(y2)

        c.create_polygon(ar,fill=col,outline=col)


        ar=[]

        a_=0

        cx,cy=x+r,y2-r
        for a in range(90):

            x_=r*math.sin(math.radians(a_))+cx
            y_=r*math.cos(math.radians(a_))+cy

            ar.append(x_)
            ar.append(y_)

            a_-=1
        ar.append(x)
        ar.append(y2)

        c.create_polygon(ar,fill=col,outline=col)


    draw_round_rec2(can,0,0,w-1,h-1,25,"#000000")



    search["bg"]=_theme[1][1]
    search["fg"]=col1
    search["insertbackground"]=col1

    npl["bg"]=_theme[1][1]
    npl["fg"]=col1
    npl["insertbackground"]=col1
 





    #lyrics

    if lst==0:

        if not st==4:

            x=w/2
            y=h-121-30


            if not vid_st==1:

                if not current_playing=="":



                    if lyric_st==0:
                        can.create_image(x-40,y,image=circle3,anchor="nw")
                        can.create_image(x+40-30,y,image=circle3,anchor="nw")


                        can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col1,outline=col1)

                        """

                        can.create_image(x-40+1,y+1,image=circle6,anchor="nw")
                        can.create_image(x+40-30+1,y+1,image=circle6,anchor="nw")


                        can.create_rectangle(x-40+15+1,y+1, x+40-15+1,y+30-1-1, fill="#010b0e",outline="#010b0e")
                        """


                        can.create_text(x,y+15,text="Lyrics",font=("FreeMono",13),fill="#000000")


                        try:


                            if not music_details[current_playing][2]=="":


                                can.create_image(x+40+5,y+15-4, image=circle7,anchor="nw")
                        except:
                            pass

                    elif lyric_st==1:


                        can.create_image(x-40,y,image=circle3,anchor="nw")
                        can.create_image(x+40-30,y,image=circle3,anchor="nw")


                        can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col1,outline=col1)

                        can.create_text(x,y+15,text="Lyrics",font=("FreeMono",13),fill="#000000")


                        can.create_image(x+40+10,y+2.5,image=add,anchor="nw")

                        if music_details[current_playing][2]!="":
                            can.create_image(x+40+10+25+10,y+2.5,image=delete_,anchor="nw")








    if lst==1:


        if st==4:
            pass

        else:

            ar=[]

            a_=180
            for a in range(180):
                x=15*math.sin(math.radians(a_))+10+15
                y=15*math.cos(math.radians(a_))+40+30-10-5-5+15

                ar.append(int(round(x,0)))
                ar.append(int(round(y,0)))

                a_+=1


            a_=0
            for a in range(180):
                x=15*math.sin(math.radians(a_))+w-10-15-25-10
                y=15*math.cos(math.radians(a_))+40+30-10-5-5+15

                ar.append(int(round(x,0)))
                ar.append(int(round(y,0)))
                
                a_+=1





            can.create_text(10+15+20+10,40+15+30-10-5-5,text="Search",font=("FreeMono",13),fill=_theme[0],anchor="w")



            can.create_image(10+15,45+30-10-5-5-2.5,image=search_im,anchor="nw")
            
            if _search==1:

                pass
            else:

                create_polygon(*ar, fill=_theme[0], alpha=0.35,can=can)
            

            draw_round_rec(can,10,40+30-10-5-5,w-10-25-10,40+30-10-5-5+30,15,col1,"",1)

            can.create_image(w-10-5-20-25-10,40+5+30-10-5-5,image=cancel,anchor="nw")




            if playlist_st==0 and st==2:

                ar=[]

                a_=270

                cx,cy=10+15,80-10-30+40+30-10+15

                for a in range(90):

                    x=15*math.sin(math.radians(a_))+cx
                    y=15*math.cos(math.radians(a_))+cy

                    ar.append(x)
                    ar.append(y)

                    a_-=1



                a_=180

                cx,cy=w-10-15,80-10-30+40+30-10+15

                for a in range(90):

                    x=15*math.sin(math.radians(a_))+cx
                    y=15*math.cos(math.radians(a_))+cy

                    ar.append(x)
                    ar.append(y)

                    a_-=1



            can.create_image(w-10-25,40+30-10-5-5+2.5,image=filter_,anchor="nw")                

            can.create_line(10,90-5,w-10,90-5,fill=col1,width=1)

            can.create_line(10,90+int(can2["height"]),w-10,90+int(can2["height"]),fill=col1,width=1)

            frame.place(in_=root,x=10,y=90-1-1)


    

    if lyric_st==1:
        show_lyrics()















    if vid_st2==0 and vid_st==1:



        


            
        draw_round_rec(can,0,0,w-1,h-1,25,_theme[0],"",1)





        save()

        draw_sb()

        move_bg()

        return



    xv=w/6
    x=xv


    label=["All Songs","Favourites","Playlist","Most Played","Add Song"]

    for l in range(len(label)):

        col=col1

        if l==st:
            col="#000000"




            can.create_image(x-60,50/2-15,image=circle3,anchor="nw")
            can.create_image(x+60-30,50/2-15,image=circle3,anchor="nw")


            can.create_rectangle(x-60+15,50/2-15, x+60-15,50/2+15-1, fill=col1,outline=col1)










        can.create_text(x,50/2,text=label[l],fill=col,font=("FreeMono",13),anchor="c")



        x+=xv







    if select_st==1:

        pass


    else:

        if playlist_st==0 and st==2 and pl_st==0 and current_playing=="":

            pass

        else:


            try:


                if songs_status[1]!="":

                        current_playlist_=songs_status[1]

                        
                        length_in_pixels = get_text_length(can, current_playlist_, "FreeMono", 12) 

                        can.create_image(10,h-20-60-20-27-15+3+10+3+2+2-3+1+10,image=circle3,anchor="nw")
                        can.create_image(10+15+length_in_pixels+30-15,h-20-60-20-27-15+3+10+3+2+2-3+1+10,image=circle3,anchor="nw")

                        can.create_rectangle(10+15,h-20-60-20-27-15+3+10+3+2+2-3+1+10, 10+15+length_in_pixels+30,h-20-60-20-27-15+3+10+3+2+2-3+30-1+1+10,
                            fill=col1,outline=col1)


                        can.create_image(10+15,h-20-60-20-27-15+3+10+5+3+2+2-3+2+10, image=playlist4,anchor="nw")

                        can.create_text(10+15+30,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=current_playlist_,font=("FreeMono",13,),anchor="w",fill="#000000")
                              
                        can.create_text(10+15+length_in_pixels+15+10+30,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"FreeMono",13,(w-10)-(10+15+length_in_pixels+15+10+30)),font=("FreeMono",13),anchor="w",fill=col1)

                else:

                    if songs_status[0]==1:

                        can.create_image(10,h-20-60-20-27-15+3+10+3+2+2-3+15+10-12.5,image=favourite2,anchor="nw")
                        can.create_text(10+25+10,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"FreeMono",13,(w-10)-(10+25+10)),font=("FreeMono",13),anchor="w",fill=col1)
                    else:
                        can.create_text(10,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"FreeMono",13,(w-10)-(10)),font=("FreeMono",13),anchor="w",fill=col1)
            
            except:
                pass



        can.create_line(10,h-20-60-20+10+2+5-3+10,w-10,h-20-60-20+10+2+5-3+10,fill=_theme[1][1],width=2)

        
        if st==2 and playlist_st==0 and current_playing=="":
            pass
        else:

            if not current_playing=="":
                can.create_text(w-10,h-20-60-20+20+10+5-3+5-2+2,text=tot_tm,font=("FreeMono",11),anchor="e",fill=col1)



        can.create_image(w/2-30,h-20-30-30+5+10-3, image=circle,anchor="nw")

        if play_st==0:
            can.create_image(w/2-15+2,h-20-30-15+5+10-3, image=play,anchor="nw")
        elif play_st==1:
            can.create_image(w/2-15,h-20-30-15+5+10-3, image=pause,anchor="nw")







        if st==4:
            can.create_image(10,h-20-30-15+5+10-3+2.5,image=list1,anchor="nw")
        elif st==2 and playlist_st==0:
            can.create_image(10,h-20-30-15+5+10-3+2.5,image=list1,anchor="nw")

        else:


            if lst==0:
                global sig_,sig2

                can.delete(sig_)

                try:

                    if st!=4:
                        if vid_st==0:
                            sig_=can.create_line(sig2,fill=col1)

                except:
                    pass

                can.create_image(10,h-20-30-15+5+10-3+2.5,image=list1,anchor="nw")
            elif lst==1:
                can.create_image(10,h-20-30-15+5+10-3+2.5,image=list2,anchor="nw")


        if lyric_st==1:
            can.delete(sig_)



        if songs_status[0]==3:

            can.create_image(10+25+15,h-20-30-15+5+10-3+2.5,image=sort2,anchor="nw")
        else:

            if sort_val!="":
                can.create_image(10+25+15,h-20-30-15+5+10-3+2.5,image=sort,anchor="nw")

            else:
                can.create_image(10+25+15,h-20-30-15+5+10-3+2.5,image=sort2,anchor="nw")



        if songs_status[0]==3:
            can.create_image(10+25+15+25+15,h-20-30-15+5+10-3+2.5,image=shuffle1,anchor="nw")


        else:


            if shuff==0:


                can.create_image(10+25+15+25+15,h-20-30-15+5+10-3+2.5,image=shuffle1,anchor="nw")
            elif shuff==1:
                can.create_image(10+25+15+25+15,h-20-30-15+5+10-3+2.5,image=shuffle2,anchor="nw")




        if loop==0:
            can.create_image(10+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=loop1,anchor="nw")

        elif loop==1:

            can.create_image(10+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=loop2,anchor="nw")



        if vid_st==0:

            can.create_image(10+25+15+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=vid2,anchor="nw")


        elif vid_st==1:

            can.create_image(10+25+15+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=vid1,anchor="nw")



        ar=os.listdir("videos")

        try:
            v=ar.index(current_playing.replace(".mp3",".mp4"))
            can.create_image(10+25+15+25+15+25+15+25+15+25+3,h-20-30-15+5+10-3+2.5+12.5-2,image=circle6,anchor="nw")
        except:
            pass



        can.create_line(w-10-120,h-20-30+5+10-3, w-10,h-20-30+5+10-3,fill=_theme[1][1],width=2)


        can.create_image(w-10-120-10-30+5,h-20-30-15+5+10-3+1,image=speaker,anchor="nw")



        can.delete(vol1)
        can.delete(vol2)
        can.delete(vol3)
        can.delete(vol4)

        r=(w-10)-(w-10-120)


        vol1=can.create_line(w-10-120,h-20-30+5+10-3 ,w-10-120+current_volume*r,h-20-30+5+10-3,fill=col1,width=2)

        vol2=can.create_text(w-10,h-20-30+5+10-3+12,text=str(int(current_volume*100))+"%",fill=col1,font=("FreeMono",11),anchor="e")
        vol3=can.create_image(w-10-120+current_volume*r-4,h-20-30+5+10-3-4,image=circle7,anchor="nw")
        vol4=can.create_image(w-10-120+current_volume*r-3,h-20-30+5+10-3-3,image=circle8,anchor="nw")



        can.create_image(w/2-30-30-25,h-20-30-15+5+10-3+2.5,image=previous,anchor="nw")
        can.create_image(w/2+30+30,h-20-30-15+5+10-3+2.5,image=next_,anchor="nw")

        can.create_image(w/2-30-30-25-15-25-10,h-20-30-15+5+10-3+2.5,image=backward,anchor="nw")

        can.create_image(w/2+30+30+25+15+10,h-20-30-15+5+10-3+2.5,image=forward,anchor="nw")










    if not current_playing=="":
        prog()

    
    if st==2 and playlist_st==0:
        can.delete(ctime)
        can.delete(prog1)
        can.delete(prog2)
        can.delete(prog3)

    if st==4:
        can.delete(ctime)
        can.delete(prog1)
        can.delete(prog2)
        can.delete(prog3)   






    


    if st==4:


        frame.place_forget()
        
        yv=50+(((h-121)-50)-90)/2



        can.create_image(w/2-80-15,yv, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv, w/2+80,yv+30-1,fill=col1,outline=col1)



        can.create_text(w/2,yv+15,text="Add Folder",fill="#000000",font=("FreeMono",13))






        can.create_image(w/2-80-15,yv+60, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv+60, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv+60, w/2+80,yv+30-1+60,fill=col1,outline=col1)


        can.create_text(w/2,yv+15+60,text="Add Audio File",fill="#000000",font=("FreeMono",13))

        prog()



    if select_st==1:

        length_in_pixels = get_text_length(can, playlist_select, "FreeMono", 13) 

        x=(w-(30+5+length_in_pixels))/2

        can.create_image(x,(h-121+75)+((h-1)-(h-121+75))/2-11,image=playlist2,anchor="nw")

        can.create_text(x+30+5,(h-121+75)+((h-1)-(h-121+75))/2,text=playlist_select,font=("FreeMono",13),fill=col1,anchor="w")

        can.create_image(w-10-25,(h-121+75)+((h-1)-(h-121+75)-25)/2,image=quit,anchor="nw")


    if filter_st==1:
        filter_can1["height"]=20+30*4
        filter_can1["width"]=250

        filter_can1.delete("all")

        filter_can1.create_image(-(w-10-int(filter_can1["width"])),-(40+30-10-5-5+30+10),
            image=bg2_,anchor="nw")

        draw_round_rec(filter_can1,0,0,int(filter_can1["width"])-1,int(filter_can1["height"])-1,15,_theme[0],"",1)

        filter_can2.place_forget()

        ar=[(0,"None"),(favourite2,"Favourites"),(playlist2,"Playlists"),(vid1,"With Video")]

        y=10

        for a in ar:


            filter_can1.create_text(5+25+15,y+15,text=a[1],font=("FreeMono",13),fill=_theme[0],anchor="w")

            if not a[0]==0:

                filter_can1.create_image(5,y+2.5,image=a[0],anchor="nw")

            if filter_val==a[1]:

                filter_can1.create_image(int(filter_can1["width"])-10-20,y+5,image=checked,anchor="nw")




            y+=30


        filter_can1.place(in_=root,x=w-10-int(filter_can1["width"]),y=40+30-10-5-5+30+10)


        if filter_val=="Playlists":

            l=0
            for p in playlist:

                if get_text_length(filter_can2, p, "FreeMono", 13)>l:

                    l=get_text_length(filter_can2, p, "FreeMono", 13)


            if (10+l+15+20)>300:

                filter_can2["width"]=10+l+15+20

            else:

                filter_can2["width"]=300


            filter_can2.delete("all")

            bg_f2=filter_can2.create_image(-(w-10-int(filter_can1["width"])-int(filter_can2["width"])-10),
                -(40+30-10-5-5+30+10+10+90)+filter_can2.canvasy(0),image=bg2_,anchor="nw")


            y=0
            for p in playlist:



                filter_can2.create_text(10,y+15,text=p,font=("FreeMono",13),fill=_theme[0],anchor="w")

                if filter_pl==p:
                    filter_can2.create_image(int(filter_can2["width"])-5-20,y+5,image=checked,anchor="nw")

                y+=30


            if y<=int(filter_can2["height"]):


                filter_can2["scrollregion"]=(0,0, int(filter_can2["width"]),int(filter_can2["height"]))

            else:

                filter_can2["scrollregion"]=(0,0, int(filter_can2["width"]),y)


            
            filter_can2.place(in_=root,x=w-10-int(filter_can1["width"])-int(filter_can2["width"])-10,y=40+30-10-5-5+30+10+10+90)

            f2=filter_can2.create_rectangle(0,filter_can2.canvasy(0), int(filter_can2["width"])-1,
                filter_can2.canvasy(int(filter_can2["height"])-1),outline=_theme[0])


        if st==songs_status[0]:

            if st==2:

                if current_playlist==songs_status[1]:


                    f1_=filter_val
                    f2_=filter_pl


                   


            else:
                f1_=filter_val
                f2_=filter_pl



    draw_round_rec(can,0,0,w-1,h-1,25,_theme[0],"",1)



    can.create_image(10,(50-25)/2,image=settings,anchor="nw")
    can.create_image(w-10-25,(50-25)/2,image=quit,anchor="nw")
    can.create_image(w-10-25-10-25,(50-25)/2,image=minimize,anchor="nw")



    save()

    draw_sb()

    move_bg()

f2=0

def wrap_text(canvas, text, max_width, x, y, font):
    """
    Create and wrap text on the canvas with center justification.
    Returns the canvas text ID.
    """
    # Split the text into lines
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        # Check if the width of the test line fits within max_width
        width = canvas.create_text(0, 0, text=test_line, font=font, anchor="nw")
        bbox = canvas.bbox(width)
        canvas.delete(width)
        if bbox and (bbox[2] - bbox[0]) > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line
    lines.append(current_line)

    # Join the lines and draw centered
    final_text = "\n".join(lines)
    text_id = canvas.create_text(x, y, text=final_text, font=font, anchor="center", justify="center")
    
    return text_id

def get_text_height(canvas, text_id):
    """
    Get the pixel height of the canvas text.
    """
    bbox = canvas.bbox(text_id)
    if bbox:
        return bbox[3] - bbox[1]
    return 0


lvar=0

ylyrics=0


_bg3_=None
_bg5_=None
bg3=0
def show_lyrics():
    global can,w,can_lyrics
    global current_playing,music_details

    global lst
    global lvar
    global ylyrics
    global _bg3_,note
    global _bg5_,note2
    global bg3
    global cur_can_lyrics
    global no_music



    col1=_theme[0]
    col2=_theme[1][0]



    try:

        if lst==0:


            




            if not current_playing=="":




                _lyric_=music_details[current_playing][2]

                if not _lyric_=="":




                    if lvar==0:


                        can_lyrics["scrollregion"]=(0,0,int(can_lyrics["width"]),int(can_lyrics["height"]))

                        update_details()



                        lvar=1




                    txt=str(_lyric_).replace("'","")
                    txt=txt.replace("\\n","\n")
                    txt=txt.replace("\\r","\n")
                    txt=txt.replace("\\","'")
                    txt=txt.replace('"',"'")


                    






                    can_lyrics.delete("all")

                    bg3=can_lyrics.create_image(-10,-(50)+int(can_lyrics.canvasy(0)),image=bg,anchor="nw")


                    


                    can_lyrics["bg"]="#000000"

                    can_lyrics["width"]=w-20
                    can_lyrics["height"]=(h-121-30-50/2+(50-30)/2)-50

                    

                    #can_lyrics.create_text((790-111)/2,0, text=txt,anchor="c",fill=col1,font=("FreeMono",13))


                    tt=txt.split("\n")

                    y=13

                    for l in tt:

                        can_lyrics.create_text(10+(w-20)/2,y, text=l, font=("FreeMono",13),anchor="c",fill=col1)

                        y+=13

                    ylyrics=y+13


                    if ylyrics<=int(can_lyrics["height"]):

                        can_lyrics["scrollregion"]=(0,0,int(can_lyrics["width"]),int(can_lyrics["height"]))
                    else:
                        can_lyrics["scrollregion"]=(0,0,int(can_lyrics["width"]),ylyrics)









                    can_lyrics.place(in_=root,x=10,y=50)







                else:

                    can.create_image(w/2-150,50+(((h-121)-50)-420)/2+210-150,image=no_music,anchor="nw")

                    can_lyrics.place_forget()

            else:
                can.create_image(w/2-150,50+(((h-121)-50)-420)/2+210-150,image=no_music,anchor="nw")
                can_lyrics.place_forget()



        else:
            can_lyrics.place_forget()
    except:
        pass






def draw_round_rec(c,x1,y1,x2,y2,r,col,col2,con,width=1):

    ar=[]
    ar2=[]

    ar3=[]

    a_=270

    cx,cy=x1+r,y1+r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(int(round(x,0)))
        ar.append(int(round(y,0)))



        a_-=1


    a_=180

    cx,cy=x2-r,y1+r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(int(round(x,0)))
        ar.append(int(round(y,0)))


        a_-=1
        

    a_=90

    cx,cy=x2-r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(int(round(x,0)))
        ar.append(int(round(y,0)))

        a_-=1
        


    a_=0

    cx,cy=x1+r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(int(round(x,0)))
        ar.append(int(round(y,0)))



        a_-=1

    ar.append(ar[0])
    ar.append(ar[1])



    def quadratic_bezier(t, p0, p1, p2):
        """Calculate a point on a quadratic Bezier curve at parameter t (0 to 1)."""
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        return x, y

    def get_bezier_coordinates_flat(input_coords, steps=1000):
        """Return a flat list of coordinates [x1, y1, x2, y2, ...] for continuous quadratic Bezier curves."""
        if len(input_coords) < 6 or len(input_coords) % 2 != 0:
            return []  # Need at least 3 points (6 coordinates) and even length
        
        # Convert flat list to list of (x, y) points
        points = [(input_coords[i], input_coords[i+1]) for i in range(0, len(input_coords), 2)]
        
        # Generate points for each Bezier segment
        all_points = []
        
        # Process points in groups of 3 for each quadratic Bezier segment
        for i in range(0, len(points) - 2, 1):  # Step by 1 to chain segments
            p0, p1, p2 = points[i], points[i+1], points[i+2]
            # Include start point only for the first segment
            start_t = 0 if i == 0 else 1.0 / steps  # Skip start point for continuity
            for j in range(int(start_t * steps), steps + 1):
                t = j / steps
                x, y = quadratic_bezier(t, p0, p1, p2)
                all_points.extend([x, y])
        
        return all_points


    #ar=get_bezier_coordinates_flat(ar)


    if con==0:

        c.create_polygon(ar,fill=col,outline=col2,width=width,smooth=True)
    elif con==1:    
        c.create_line(ar,fill=col,width=width,smooth=True)




note=0
note2=0

cur=0
circle7=0
circle8=0
bg=0

copy=0
circle9=0
circle11=0
cursor=0

bg2_=0
settings=0

delete3=0

crop,crop2=0,0

delete_,delete2_=0,0

vid1,vid2,vid3=0,0,0,

filter_=0

no_music=0
circle6=0
def load_im():

    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global cancel,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,checked,sort,delete,favourite1_,favourite2_,delete2,playlist3,sort2,loop1,loop2,wallpaper
    global circle2,circle3,circle4,circle5,circle6,circle4,circle7,circle8,circle9,circle5,expand,expand2,playlist4

    global minimize,quit
    global circlex
    global add,add2
    global nomusic
    global forward,backward
    global note_
    global note
    global circle6,circle7,circle8
    global bg,bg2_
    global note2
    global cur
    global copy
    global circle9,circle10
    global circle11
    global cursor
    global settings
    global delete3
    global crop,crop2
    global delete_,delete2_
    global vid1,vid2,vid3
    global filter_
    global no_music

    circle=ImageTk.PhotoImage(file="data/circle.png")
    circle2=ImageTk.PhotoImage(file="data/circle2.png")
    circle3=ImageTk.PhotoImage(file="data/circle3.png")
    circle4=ImageTk.PhotoImage(file="data/circle4.png")
    circle5=ImageTk.PhotoImage(file="data/circle5.png")
    circle6=ImageTk.PhotoImage(file="data/circle6.png")
    circle7=ImageTk.PhotoImage(file="data/circle7.png")
    circle8=ImageTk.PhotoImage(file="data/circle8.png")
    circle9=ImageTk.PhotoImage(file="data/circle9.png")
    circle10=ImageTk.PhotoImage(file="data/circle10.png")
    play=ImageTk.PhotoImage(file="data/play.png")
    play=ImageTk.PhotoImage(file="data/play.png")
    pause=ImageTk.PhotoImage(file="data/pause.png")
    favourite1=ImageTk.PhotoImage(file="data/favourite1.png")
    favourite2=ImageTk.PhotoImage(file="data/favourite2.png")
    list1=ImageTk.PhotoImage(file="data/list1.png")
    list2=ImageTk.PhotoImage(file="data/list2.png")
    musical_note1=ImageTk.PhotoImage(file="data/musical_note1.png")
    musical_note2=ImageTk.PhotoImage(file="data/musical_note2.png")
    speaker=ImageTk.PhotoImage(file="data/speaker.png")
    previous=ImageTk.PhotoImage(file="data/previous.png")
    next_=ImageTk.PhotoImage(file="data/next.png") 
    cancel=ImageTk.PhotoImage(file="data/cancel.png")
    search_im=ImageTk.PhotoImage(file="data/search.png")    
    shuffle1=ImageTk.PhotoImage(file="data/shuffle1.png")
    shuffle2=ImageTk.PhotoImage(file="data/shuffle2.png")
    playlist2=ImageTk.PhotoImage(file="data/playlist2.png")
    checked=ImageTk.PhotoImage(file="data/checked.png")
    sort=ImageTk.PhotoImage(file="data/sort.png")
    delete=ImageTk.PhotoImage(file="data/bin.png")
    favourite1_=ImageTk.PhotoImage(file="data/favourite1_.png")
    favourite2_=ImageTk.PhotoImage(file="data/favourite2_.png")
    delete2=ImageTk.PhotoImage(file="data/bin2.png")
    delete3=ImageTk.PhotoImage(file="data/bin3.png")

    playlist3=ImageTk.PhotoImage(file="data/playlist3.png")
    playlist4=ImageTk.PhotoImage(file="data/playlist4.png")
    sort2=ImageTk.PhotoImage(file="data/sort2.png")
    loop1=ImageTk.PhotoImage(file="data/loop1.png")
    loop2=ImageTk.PhotoImage(file="data/loop2.png")

    minimize=ImageTk.PhotoImage(file="data/minimize.png")
    quit=ImageTk.PhotoImage(file="data/quit.png")
    circlex=ImageTk.PhotoImage(file="data/circlex.png")
    add=ImageTk.PhotoImage(file="data/add.png")
    add2=ImageTk.PhotoImage(file="data/add2.png")


    forward=ImageTk.PhotoImage(file="data/forward.png")
    backward=ImageTk.PhotoImage(file="data/backward.png")
    bg=ImageTk.PhotoImage(file="data/bg.png")
    bg2_=ImageTk.PhotoImage(file="data/bg2.png")

    cursor=ImageTk.PhotoImage(file="data/cursor.png")
    settings=ImageTk.PhotoImage(file="data/settings.png")

    crop=ImageTk.PhotoImage(file="data/crop.png")
    crop2=ImageTk.PhotoImage(file="data/crop2.png")

    delete_=ImageTk.PhotoImage(file="data/delete.png")
    delete2_=ImageTk.PhotoImage(file="data/delete2_.png")

    vid1=ImageTk.PhotoImage(file="data/vid1.png")
    vid2=ImageTk.PhotoImage(file="data/vid2.png")
    vid3=ImageTk.PhotoImage(file="data/vid3.png")    

    filter_=ImageTk.PhotoImage(file="data/filter.png") 
    no_music=ImageTk.PhotoImage(file="data/no-music.png") 




def check_pl():
    global npl,plv,can2,playlist_st,st,_npl

    if st==2 and playlist_st==0:

        if can2.canvasy(0)!=plv:

            plv=can2.canvasy(0)

            if not can2.canvasy(0)==0:
                _npl=0
                can_npl.place_forget()


    root.after(2,check_pl)




def clipboard():

    global _lyric

    clipboard_content = pyperclip.paste()
    clipboard_content = repr(clipboard_content)

    if _lyric!=clipboard_content:
        _lyric=clipboard_content



        pyperclip.copy("")




def sync_lyrics():

    global tm, lyric_st, music_details, current_playing,tot_tm_,text,ylyrics,can_lyrics

    if lyric_st==1:

        if not music_details[current_playing][2]=="":


            height=ylyrics


            ratio=tm*height/tot_tm_


            pixel_value = ratio
            scroll_region = can_lyrics.bbox("all")  # Get the bounding box of all content
            if scroll_region:
                total_height = scroll_region[3] - scroll_region[1]  # Scrollable height
                fraction = pixel_value / total_height if total_height > 0 else 0
                can_lyrics.yview_moveto(fraction)


    root.after(2,sync_lyrics)

ang=0
def load_():
    global can,st,convert,w,h
    global load,load2
    global ang


    col1=_theme[0]
    col2=_theme[1][0]


    can.delete(load)
    can.delete(load2)


    if st==4:
        if not convert==0:



            load=can.create_arc(w/2-20,h-121-20-40, w/2+20,h-121-20,outline=col1,start=ang+180,extent=70,style="arc",width=2)

            load2=can.create_arc(w/2-20,h-121-20-40, w/2+20,h-121-20,outline=col1,start=ang,extent=70,style="arc",width=2)


            ang+=1



    root.after(2,load_)

mot_val=0
my_cursor=0
attr=[0,0,0,0]


cr_pos=[]

cur_can=0
cur_can2=0
cur_can3=0
cur_can4=0
cur_can6=0

cur_can_lyrics=0
cur_can_sort=0
cur_can_settings=0
cur_can_search=0
cur_can_npl=0
cur_can_theme_ent=0
cur_can_sel_op=0
cur_filter_can1=0
cur_filter_can2=0
cur_conf_del=0

cur_p=[]

def check_cur_on_s(x,y):


    cx,cy=w-10-5-20+10-10-25,40+5+30-10-5-5+10
    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 0


    x1,y1,x2,y2=10,40+30-10-5-5,w-10-10-25,40+30-10-5-5+30


    cx,cy=x1+15,y1+15

    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 1



    cx,cy=x2-15,y1+15

    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 1


    if x1+15<=x<=x2-15:
        if y1<=y<=y2:
            return 1




    return 0



def check_cur_on_s2(x,y):

    global can2,sb_sz


    y_=5


    cx,cy=(int(can2["width"])-sb_sz-1)-10-5-20+10,y_+5+10
    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 0


    x1,y1,x2,y2=10,y_,(int(can2["width"])-sb_sz-1)-10,y_+30


    cx,cy=x1+15,y1+15

    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 1



    cx,cy=x2-15,y1+15

    r=math.sqrt((x-cx)**2+(y-cy)**2)

    if r<=15:
        return 1


    if x1+15<=x<=x2-15:
        if y1<=y<=y2:
            return 1




    return 0

def draw_cur():


    global can,can2,can3,can4,can6,can_lyrics,can_sort,can_settings,can_search,can_npl,can_theme_ent,can_sel_op
    global filter_can1,cur_filter_can1
    global filter_can2,cur_filter_can2
    global conf_del,cur_conf_del
    global cur_can,cur_can2,cur_can3,cur_can4,cur_can6,cur_can_lyrics,cur_can_sort,cur_can_settings
    global cur_can_search,cur_can_npl,cur_can_theme_ent,cur_can_sel_op
    global circle7,circle11
    global root_st
    global cur_p
    global _search,_npl
    global lst
    global cursor
    global vid_tm
    


    x,y=pyautogui.position()


    









    con=0
    if not cur_p==[x,y]:
        vid_tm=time.time()
        con=1
        cur_p=[x,y]

        can.delete(cur_can)

    can2.delete(cur_can2)


    can3.delete(cur_can3)


    can4.delete(cur_can4)

    can6.delete(cur_can6)

    can_lyrics.delete(cur_can_lyrics)



    can_sort.delete(cur_can_sort)

    can_settings.delete(cur_can_settings)

    can_search.delete(cur_can_search)

    can_npl.delete(cur_can_npl)

    can_theme_ent.delete(cur_can_theme_ent)

    can_sel_op.delete(cur_can_sel_op)

    filter_can1.delete(cur_filter_can1)
    filter_can2.delete(cur_filter_can2)
    conf_del.delete(cur_conf_del)

    if root_st==1 and con==1:


        #str(wd-3-50)+"+"+str(ht-51-50)


        xx,yy=x-(wd-3-50),y-(ht-51-50)

        cx,cy=(wd-3-50)+25,(ht-51-50)+25

        r=math.sqrt((x-cx)**2+(y-cy)**2)


        if r<=25:


            cur_can=can.create_image(xx,yy,image=cursor,anchor="nw")

        root.after(2,draw_cur)
        return




    if con==1:




        xx,yy=x-(wd-w)/2,y-(ht-h)/2

        can_label(xx,yy)

        cur_can=can.create_image(xx,yy,image=cursor,anchor="nw")


    if lst==1:

        xx,yy=x-(wd-w)/2-10,y-(ht-h)/2-88+can2.canvasy(0)

        cur_can2=can2.create_image(xx,yy,image=cursor,anchor="nw")

        xx,yy=x-(wd-w)/2-(w-int(can3["width"]))/2,y-(ht-h)/2-(h-(int(can4["height"])+int(can3["height"])+int(can6["height"])))/2

        cur_can4=can4.create_image(xx,yy,image=cursor,anchor="nw")



        xx,yy=x-(wd-w)/2-(w-int(can3["width"]))/2,y-(ht-h)/2-(h-(int(can4["height"])+int(can3["height"])+int(can6["height"])))/2-40+can3.canvasy(0)

        cur_can3=can3.create_image(xx,yy,image=cursor,anchor="nw")


        xx,yy=x-(wd-w)/2-(w-int(can3["width"]))/2,y-(ht-h)/2-(h-(int(can4["height"])+int(can3["height"])+int(can6["height"])))/2-40-int(can3["height"])

        cur_can6=can6.create_image(xx,yy,image=cursor,anchor="nw")



    xx,yy=x-(wd-w)/2-10,y-(ht-h)/2-50+can_lyrics.canvasy(0)

    cur_can_lyrics=can_lyrics.create_image(xx,yy,image=cursor,anchor="nw")



    xx,yy=x-(wd-w)/2-(10+25+15+25),y-(ht-h)/2-(h-20-30-15+5+10+2.5-160)

    cur_can_sort=can_sort.create_image(xx,yy,image=cursor,anchor="nw")


    xx,yy=x-(wd-w)/2-(10+25+5),y-(ht-h)/2-(25+12.5+5)

    cur_can_settings=can_settings.create_image(xx,yy,image=cursor,anchor="nw")

    xx,yy=x-(wd-w)/2-(10+15),y-(ht-h)/2-(50+1)

    cur_can_search=can_search.create_image(xx,yy,image=cursor,anchor="nw")



    xx,yy=x-(wd-w)/2-(10+15+10),y-(ht-h)/2-(5+1+88)

    cur_can_npl=can_npl.create_image(xx,yy,image=cursor,anchor="nw")


    xx,yy=x-(wd-w)/2-(77-1+1+(10+25+5)),y-(ht-h)/2-(19+1+(25+12.5+5))

    cur_can_theme_ent=can_theme_ent.create_image(xx,yy,image=cursor,anchor="nw")



    xx_=10+25+5+20+get_text_length(can_settings, "Opacity (bg , select)", "FreeMono", 13)+10
    yy_=25+12.5+5+int(can_settings["height"])-65-9

    xx,yy=x-(wd-w)/2-(xx_),y-(ht-h)/2-(yy_)

    cur_can_sel_op=can_sel_op.create_image(xx,yy,image=cursor,anchor="nw")



    xx,yy=x-(wd-w)/2-(w-10-int(filter_can1["width"])),y-(ht-h)/2-(40+30-10-5-5+30+10)

    cur_filter_can1=filter_can1.create_image(xx,yy,image=cursor,anchor="nw")


    xx,yy=x-(wd-w)/2-(w-10-int(filter_can1["width"])-int(filter_can2["width"])-10),y-(ht-h)/2-(40+30-10-5-5+30+10+10+90)+filter_can2.canvasy(0)

    cur_filter_can2=filter_can2.create_image(xx,yy,image=cursor,anchor="nw")


    xx,yy=x-(wd-w)/2-((w-int(conf_del["width"]))/2),y-(ht-h)/2-((h-int(conf_del["height"]))/2)

    cur_conf_del=conf_del.create_image(xx,yy,image=cursor,anchor="nw")


    root.after(2,draw_cur)


def check_cur_pos():
    global can2,attr,current_playing,playlist,songs
    global _pl_,playlist2,playlist3,_fv_,music_details,favourite1,favourite1_,favourite2_,favourite2
    global sb_sz,_del_,delete,delete2,music_details
    global cr_pos
    global ht,h
    global st,playlist_st
    global cp_im,cp_im2,cp_im3
    global current_playlist
    global lst
    global songs2
    global cp2_im
    global add_st
    global sort_st,sort_ar,csv_im
    global search_var
    global root_st
    global lst
    global can4,can3,can6
    global vid1,vid2,vid3
    global delete_,delete2_



    if root_st==0:

        con__=1



        

        x,y=pyautogui.position()



        can2.delete(attr[0])
        can2.delete(attr[1])
        can2.delete(attr[2])
        can2.delete(attr[3])
        can2.coords(cp_im,0,-100)
        can3.coords(cp2_im,0,-100)
        can_sort.coords(csv_im,0,-100)
        can2.coords(cp_im2,0,-100)
        can2.coords(cp_im3,0,-100) 




        y_=y-int(((ht)-h)/2)-88



        if st==2 and playlist_st==0 and select_st==0 and add_st==0 and sort_st==0 and lst==1:


            if y_<0 or y_>int(can2["height"]):

                root.after(2,check_cur_pos)
                return

            if (root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2<=x<=(root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2+int(can2["width"]):

                y=95

                ar=[]

                for pl in playlist:

                    scon=0


                    sval=search_var.lower()

                    if sval.find(" ")!=-1:

                        ss=[]

                        s_ar=sval.split(" ")

                        for sv in s_ar:

                            if pl.lower().find(sv)!=-1:
                                ss.append(1)
                            else:
                                ss.append(0)

                        scon=1

                        for ss_ in ss:

                            if ss_==0:
                                scon=0
                                break

                    else:
                        if pl.lower().find(sval)!=-1:
                            scon=1

                    if scon==1:

                        ar.append([pl,y])
                        y+=50


                for p in ar:



                    if p[1]<=can2.canvasy(y_)<=p[1]+50:

                        y=p[1]

                        can2.coords(cp_im,0,y)
                        can2.coords(cp_im3,0,y)
                        if current_playlist==p[0]:

                            attr[0]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=add2,anchor="nw")
                            _del_=delete2_
                        else:

                            attr[0]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=add,anchor="nw")
                            _del_=delete_

                        attr[1]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25,y+12.5,image=_del_,anchor="nw")

                        break
            root.after(5,check_cur_pos)
            return


        elif sort_st==1:


            if (root.winfo_screenwidth()-w)/2+can_sort.winfo_x()<=x<=(root.winfo_screenwidth()-w)/2+can_sort.winfo_x()+int(can_sort["width"]):


                y=30

                ar=[]

                for s in sort_ar:


                    if y<30+30*4:

                        if y<=can_sort.canvasy(y_-(h-20-30-15+5+10+2.5-160)+88)<=y+30:

                            can_sort.coords(csv_im,0,y)

                    y+=30
            root.after(5,check_cur_pos)
            return





        elif add_st==1 and lst==1:








            y_+=88
            y_-=((h-(int(can4["height"])+int(can3["height"])+int(can6["height"])))/2)
            y_-=40


            #print(y_)








            if (root.winfo_screenwidth()-w)/2+(w-int(can3["width"]))/2<=x<=(root.winfo_screenwidth()-w)/2+(w-int(can3["width"]))/2+int(can3["width"]):

                if -40<=y_<=int(can3["height"])+40:

                    con__=0



            if y_<0 or y_>int(can3["height"]):
                pass


            else:

                if (root.winfo_screenwidth()-w)/2+(w-int(can3["width"]))/2<=x<=(root.winfo_screenwidth()-w)/2+(w-int(can3["width"]))/2+int(can3["width"]):

                    y=0

                    ar=[]

                    for pl in playlist:


                        if y<=can3.canvasy(y_)<=y+50:


                            can3.coords(cp2_im,0,y)


                        y+=50







        elif select_st==1 and lst==1:




            if y_<0 or y_>int(can2["height"]):

                root.after(2,check_cur_pos)
                return


            if (root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2<=x<=(root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2+int(can2["width"]):



                for song in songs2:

                    if song[1]<=can2.canvasy(y_)<=song[1]+50:
                        y=song[1]

                        can2.coords(cp_im,0,y)
                        break
            root.after(5,check_cur_pos)
            return

        

        if con__==1:

            y_=y-int(((ht)-h)/2)-88


            if lst==1:


                if y_<0 or y_>int(can2["height"]):

                    root.after(2,check_cur_pos)
                    return

                if (root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2<=x<=(root.winfo_screenwidth()-w)/2+(w-int(can2["width"]))/2+int(can2["width"]):


                    for song in songs:

                        if song[1]<=can2.canvasy(y_)<=song[1]+50:
                            y=song[1]

                            can2.coords(cp_im,0,y)
                            can2.coords(cp_im2,0,y)

                            if song[0]==current_playing:
                                _del_=delete2_

                            else:
                                _del_=delete_
                            
                            attr[0]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25,y+12.5,image=_del_,anchor="nw")


                            con_v=0

                            try:

                                ar=os.listdir("videos")

                                v=ar.index(song[0].replace(".mp3",".mp4"))

                                con_v=1

                            except:
                                pass


                            

                            if con_v==1:

                                if song[0]==current_playing:

                                    attr[1]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=vid3,anchor="nw")
                                else:
                                    attr[1]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=vid1,anchor="nw")

                            elif con_v==0:

                                attr[1]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25,y+12.5,image=vid2,anchor="nw")


                            con=0

                            for i in playlist:


                                try: 
                                    v=playlist[i].index(song[0])
                                except:
                                    pass


                            _pl_=playlist2




                            if song[0]==current_playing:
                                _pl_=playlist3

                                


                            attr[2]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25-15-25,y+12.5,image=_pl_,anchor="nw")




                            if music_details[song[0]][0]==0:

                                _fv_=favourite1

                                if song[0]==current_playing:
                                    _fv_=favourite1_


                            elif music_details[song[0]][0]==1:


                                _fv_=favourite2


                                if song[0]==current_playing:
                                    _fv_=favourite2_

                            attr[3]=can2.create_image((int(can2["width"])-sb_sz-1)-10-25-15-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")

                            break





    root.after(5,check_cur_pos)


def can_label(x,y):

    global can,mot_val
    global root_st


    col1=_theme[0]
    col2=_theme[1][0]

    if not root_st==1:

        


        can.delete(mot_val)


        #list

        cx,cy=10+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=x<=cx+12.5:
            if cy-12.5<=y<=cy+12.5:

                mot_val=can.create_text(10+12.5,h-20-30-15+5+10-3+2.5+25+10,text="list",fill=col1,font=("FreeMono",10),anchor="c")



        #sort

        cx,cy=10+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=x<=cx+12.5:
            if cy-12.5<=y<=cy+12.5:
                mot_val=can.create_text(10+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="sort",fill=col1,font=("FreeMono",10),anchor="c")
            



        #shuffle

        cx,cy=10+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=x<=cx+12.5:
            if cy-12.5<=y<=cy+12.5:

                mot_val=can.create_text(10+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="shuffle",fill=col1,font=("FreeMono",10),anchor="c")
            


        #loop

        cx,cy=10+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=x<=cx+12.5:
            if cy-12.5<=y<=cy+12.5:

                mot_val=can.create_text(10+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="loop",fill=col1,font=("FreeMono",10),anchor="c")
            


        #play vid

        cx,cy=10+25+15+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=x<=cx+12.5:
            if cy-12.5<=y<=cy+12.5:

                ar=os.listdir("videos")

                try:

                    v=ar.index(current_playing.replace(".mp3",".mp4"))

                    txt="play video"
                except:
                    txt="no video"

                mot_val=can.create_text(10+25+15+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text=txt,fill=col1,font=("FreeMono",10),anchor="c")
            

def convert_(file,output,col):


    im=Image.open(file)
    w,h=im.size

    rgb=hex_to_rgb(col)




    image = Image.new('RGBA', (w, h), (0,0,0,255))
    pixels = image.load()


    for y in range(h):

        for x in range(w):


            color = im.getpixel((x, y))

            mx=max(rgb)

            c_=color[1]#max(color)#color[rgb.index(mx)]



            r=int(c_*rgb[0]/mx)
            g=int(c_*rgb[1]/mx)
            b=int(c_*rgb[2]/mx)


            pixels[x,y]=(r,g,b,255)

        root.after(2,update)

    image.save(output)


circle=0
circle2=0
circle3=0
circle4=0
circle5=0
circle4=0
circle7=0
circle8=0
circle9=0
circle5=0
circle6=0
play=0
pause=0
add=0
favourite1=0
favourite2=0
list1=0
list2=0
musical_note1=0
musical_note2=0
speaker=0
previous=0
next_=0
cancel=0
cancel2=0
search_im=0
shuffle1=0
shuffle2=0
note=0
nomusic=0

songs=[]


st=0

pp,fv,lst=0,0,1

current_playing=""

tm=0

play_st=0


ctime=0
start_time=0

tot_tm=""
tot_tm_=0


prog1=0
prog2=0
tvar=0
mvar=0


search_var=""


playlist_st=0
plv=0

playlist1=0
playlist2=0
current_playlist=""
_playlist=[]
sel_playlist=[]
add_st=0

checked=0

load,load2,load3,load4=0,0,0,0
load_st=0
load_ang=90

sort=0

pl_st=0

shuff=0

delete=0

pl_var=0





favourite1_=0
favourite2_=0
delete2=0
playlist3=0

_pl_,_fv_,_del_=0,0,0

shuffle_st=0
shuffle_ar=[]

sort2=0


loop=0
loop1=0
loop2=0

wallpaper=0


yvar=0


_search=0

_npl=0




expand,expand2=0,0

playlist4=0





bg=0





lyric_st=0
_lyric=""



sa=["Date Added (Descending)","Date Added (Ascending)","Title (Ascending)","Title (Descending)"]

sort_val=sa[0]





if shuff==1 or shuff==2:
    sort_val=""

play_video_st=0


minimize,quit=0,0




root_st=0


circlex=0


select_st=0

add,add2=0,0

bg=0


_songs_=[]
songs_status=[st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing]


filter_val,filter_pl="None",None


forward=None
backward=None


note_=None

_theme=["#ffffff",[],0.5,0.15,[],1,[]]


try:

    with open("data/save.json", "r") as file:
        data = json.load(file)


    if not len(data["save"][-3][0])==7:


        data={"save":[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status,_theme,filter_val,filter_pl]}





        with open("data/save.json", "w") as file:
            json.dump(data, file, indent=4)



except:
    data={"save":[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status,_theme,filter_val,filter_pl]}





    with open("data/save.json", "w") as file:
        json.dump(data, file, indent=4)


try:


    st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status,_theme,filter_val,filter_pl=data["save"]


    st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing=songs_status


except:

    pass

f1_,f2_=filter_val,filter_pl

lst=1
if playlist_st==0 and current_playing!="":
    playlist_st=1



def update():
    pass
root=tk.Tk()

wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()
#wd,ht=1366,768
h=int(ht)
w=int(wd)



root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht)-h)/2)))
root.resizable(0,0)
#root.wm_attributes("-alpha",0.9)
root.wm_attributes("-transparentcolor","#333333")
root.wm_attributes("-topmost",True)
root.iconbitmap("data/icon.ico")
root.title("HMUSIC")

root.overrideredirect(True)


configure_theme(_theme[0])

adj_st=0

def adjust_theme():
    global _theme,theme_ent
    global adj_st
    global sel_col


    if adj_st==0:
        col=_theme[0]
        configure_theme(_theme[0])

    else:
        col=sel_col



    
    change_theme(col)
    resize_im()

    if _theme[-2]==1:

        im=Image.new("RGBA",(w,h),(0,0,0,255))
        im.save("data/bg_.png")
        im.save("data/bg.png")
        im.save("data/bg2.png")

        _theme[-1]=[0,0,0,0]

    else:


        ar=os.listdir("data")

        for i in ar:

            if i.split(".")[0]=="bg_":
                ext=i.split(".")[1]

        

        im=Image.open("data/bg_."+ext)
        x,y=im.size



        if _theme[-1]==[]:

            if w/h>x/y:

                yy=int((y-x*h/w)/2)

                im=im.crop((0,yy,x,y-yy))

                _theme[-1]=[0,yy,x,y-yy]

            elif w/h<x/y:

                xx=int((x-y*w/h)/2)

                im=im.crop((xx,0,x-xx,y))

                _theme[-1]=[xx,0,x-xx,y]
            else:
                _theme[-1]=[0,0,0,0]

        else:

            x_=_theme[-1][2]-_theme[-1][0]
            y_=_theme[-1][3]-_theme[-1][1]


            if x_/y_-0.02<=w/h<=x_/y_+0.02:

                im=im.crop((_theme[-1][0],_theme[-1][1],_theme[-1][2],_theme[-1][3]))
            else:


                if w/h>x/y:

                    yy=int((y-x*h/w)/2)

                    im=im.crop((0,yy,x,y-yy))

                    _theme[-1]=[0,yy,x,y-yy]

                elif w/h<x/y:

                    xx=int((x-y*w/h)/2)

                    im=im.crop((xx,0,x-xx,y))

                    _theme[-1]=[xx,0,x-xx,y]
                else:
                    _theme[-1]=[0,0,0,0]


        im.save("data/bg.png")

        im=Image.open("data/bg.png")

        im=im.resize((w,h))
        im.save("data/bg.png")




        convert_("data/bg.png","data/bg.png",col)





        
        darken_image("data/bg.png", "data/bg.png",(0,0,0), _theme[2])
        darken_image("data/bg.png", "data/bg2.png",(0,0,0), 0.5)




    load_im()

    root.after(2,update)
    adj_st=1


    




y1,y2,y3=0,0,0
def move_bg():

    global can2,can_lyrics,can3
    global bg2,bg3,bgp
    global sb_h,sb2_h
    global root_st
    global y1,y2,y3


    if root_st==0:

        if y1!=can2.canvasy(0):


            can2.coords(bg2,-10,-(90-2)+int(can2.canvasy(0)))


            sb_h=can2.canvasy(0)*int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])
            draw_sb()

            y1=can2.canvasy(0)


        if y2!=can_lyrics.canvasy(0):


            can_lyrics.coords(bg2,-10,-(50)+int(can_lyrics.canvasy(0)))

            y2=can_lyrics.canvasy(0)


        if y3!=can3.canvasy(0):

            

            sb2_h=can3.canvasy(0)*int(can3["height"])/int(can3["scrollregion"].split(" ")[-1])
            draw_sb2()

            y3=can3.canvasy(0)

            can3.coords(bgp,-((w-550)/2),-((h-(40+250-40+50+40))/2+40)+can3.canvasy(0))

def update_bg_pos():

    move_bg()


    root.after(2,update_bg_pos)




def _on_mousewheel(e):
    global can2,can3,yyy,h,add_st
    global ylyric,lyric_st,lst
    global music_details,current_playing,can_lyrics
    global _bg2_,_bg3_,_bg4_,_bg5_
    global w
    global select_st,transparent_im,transparent_im2
    global bg2,bg3,bgp
    global sb_h,sb2_h
    global filter_st,filter_val,filter_can2,f2
    global _theme

    if add_st==0 and lst==1 and filter_st==0:

        if int(can2["scrollregion"].split(" ")[-1])>((h-121)-80-10):

            can2.yview_scroll(int(-1*(e.delta/120)), "units")

            can2.coords(bg2,-10,-(90-2)+int(can2.canvasy(0)))

            sb_h=can2.canvasy(0)*int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])
            draw_sb()
            

     



    elif add_st==1:

        if int(can3["scrollregion"].split(" ")[-1])>210:
            can3.yview_scroll(int(-1*(e.delta/120)), "units")
            sb2_h=can3.canvasy(0)*int(can3["height"])/int(can3["scrollregion"].split(" ")[-1])

            can3.coords(bgp,-((w-550)/2),-((h-(40+250-40+50+40))/2+40)+can3.canvasy(0))
            draw_sb2()

    if lyric_st==1:
        if not music_details[current_playing][2]=="":
            can_lyrics.yview_scroll(int(-1*(e.delta/120)), "units")

            can_lyrics.coords(bg3,-10,-(50)+int(can_lyrics.canvasy(0)))


    if filter_st==1:

        if int(filter_can2["scrollregion"].split(" ")[-1])>int(filter_can2["height"]):

            filter_can2.delete(f2)



            filter_can2.yview_scroll(int(-1*(e.delta/120)), "units")
            f2=filter_can2.create_rectangle(0,filter_can2.canvasy(0), int(filter_can2["width"])-1,
                filter_can2.canvasy(int(filter_can2["height"])-1),outline=_theme[0])


            filter_can2.coords(bg_f2,-(w-10-int(filter_can1["width"])-int(filter_can2["width"])-10),
                -(40+30-10-5-5+30+10+10+90)+filter_can2.canvasy(0))

def update_song_status():
    global songs,_songs_,songs_status
    global current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing


    if not st==4:



        _songs_=songs

        songs_status=[st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing]



def play_pause(e):
    global st,playlist_st,play_st,current_playing,pp,tm,tts
    global paused
    global select_st







    if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
        pass

    else:

        if not current_playing=="":

            if pp==0:
                pp=1
                play_st=1

                tts=tm

                if tm>0:
                    play_music("music/"+current_playing,tm,1)

                else:
                    play_music("music/"+current_playing,tm)

                paused=False

                main()
            elif pp==1:
                pp=0
                play_st=0

                pygame.mixer.quit()

                main()

                paused=True



                prog()


def play_next(e):
    global st,playlist_st,play_st,current_playing,mvar,tm,loop,pp,songs,pl_st,lvar
    global play_video_st,vid_canvas,lyric_st,cap
    global select_st

    global _songs_

    global playlist_st,current_playlist,songs_status


    if st==2 and playlist_st==0 and pl_st==0:
        return

    if current_playing=="":
        return


    st_=st
    cp=current_playlist
    p=playlist_st


    st=songs_status[0]
    current_playlist=songs_status[1]
    playlist_st=1

    main()

    st=st_
    current_playlist=cp
    playlist_st=p


    if loop==0:

        if mvar+1==len(_songs_):
            mvar=0
        else:
            mvar+=1


    tm=0
    
    current_playing=_songs_[mvar][0]
    play_st=1

    play_music("music/"+current_playing,tm)

    pp=1

    get_audio_duration("music/"+current_playing)

    lvar=0

    play_video_st=0

    

    lyric_st=0

    cap=None

    main()

    if not select_st==1:

        move_to_playing()




        if st==2 and playlist_st==0:
            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))



def play_previous(e):

    global st,playlist_st,play_st,current_playing,mvar,tm,loop,pp,songs,play_video_st,vid_canvas,lyric_st
    global cap
    global select_st
    global _songs_
    global playlist_st,current_playlist,songs_status


    if st==2 and playlist_st==0 and pl_st==0:
        return

    if current_playing=="":
        return

    
    st_=st
    cp=current_playlist
    p=playlist_st


    st=songs_status[0]
    current_playlist=songs_status[1]
    playlist_st=1

    main()

    st=st_
    current_playlist=cp
    playlist_st=p


    if loop==0:

        mvar-=1



    if mvar<0:
        mvar=len(_songs_)-1



    tm=0
    
    current_playing=_songs_[mvar][0]
    play_st=1

    play_music("music/"+current_playing,tm)

    pp=1

    get_audio_duration("music/"+current_playing)

    lvar=0

    play_video_st=0

    

    lyric_st=0

    cap=None

    main()

    if not select_st==1:

        move_to_playing()

        if st==2 and playlist_st==0:
            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))


def __list(e):
    global lst,lyric_st,can_lyrics,can2,st,playlist_st,_search,search_var,frame
    global songs_status,current_playlist
    global frame2
    global vid_st,vid_st2
    global conf_del

    if e.char.lower()=="l":


        if lst==0:
            vid_st=0
            vid_st2=0
            lyric_st=0
            lst=1
            can_lyrics.place_forget()


            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

        elif lst==1:

            if st==2 and playlist_st==0:
                pass
            else:
                lst=0
                _search=0
                _npl=0

                search_var=""

                
                can_search.place_forget()
                frame.place_forget()
                frame2.place_forget()
                filter_st=0
                filter_can1.place_forget()
                filter_can2.place_forget()
                conf_del.place_forget()


        main()

        if st==songs_status[0]:

            if st==2:
                if current_playlist==songs_status[1]:
                    move_to_playing(1)

            else:
                move_to_playing(1)


def on_release_can(e):
    global play_st2,v_st


    if play_st2==1:
        play_st2=0

    if v_st==1:
        v_st=0

def drag_can(e):


    global can
    global play_st2,v_st
    global w,h
    global tm,tot_tm_
    global current_volume,volume
    global vol1,vol2,vol3,vol4
    global circle7,circle8
    global current_playing,tts,sig




    if play_st2==1:

        if 10<=e.x<=w-10:


            x=e.x-10

            tm=x*tot_tm_/(w-20)


            if play_st==1:

                tts=tm
                sig=[]

                if tm>0:
                    play_music("music/"+current_playing,tm,1)

                else:
                    play_music("music/"+current_playing,tm)


            

            prog()
            #main()

    if v_st==1:


        if w-10-120<=e.x<=w-10:



            x=e.x-(w-10-120)

            r=120

            current_volume=x/r


            volume.SetMasterVolumeLevelScalar(current_volume, None)

                
            can.delete(vol1)
            can.delete(vol2)
            can.delete(vol3)
            can.delete(vol4)        


            vol1=can.create_line(w-10-120,h-20-30+5+10-3 ,w-10-120+current_volume*r,h-20-30+5+10-3,fill=_theme[0],width=2)

            vol2=can.create_text(w-10,h-20-30+5+10-3+12,text=str(int(current_volume*100))+"%",fill=_theme[0],font=("FreeMono",11),anchor="e")

            vol3=can.create_image(w-10-120+current_volume*r-4,h-20-30+5+10-3-4,image=circle7,anchor="nw")
            vol4=can.create_image(w-10-120+current_volume*r-3,h-20-30+5+10-3-3,image=circle8,anchor="nw")






can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
can.bind("<Button-3>",can_b3)
can.bind_all("<MouseWheel>",_on_mousewheel)
can.bind("<space>",play_pause)
can.bind("<Right>",play_next)
can.bind("<Left>",play_previous)
can.bind("<KeyPress>",__list)
can.bind("<B1-Motion>",drag_can)
can.bind("<ButtonRelease-1>",on_release_can)





col1=_theme[0]
col2=_theme[1][0]




style=ttk.Style()
style.element_create("My.Vertical.TScrollbar.trough", "from", "clam")
style.element_create("My.Vertical.TScrollbar.thumb", "from", "clam")
style.element_create("My.Vertical.TScrollbar.grip", "from", "clam")

style.layout("My.Vertical.TScrollbar",
   [('My.Vertical.TScrollbar.trough',
     {'children': [('My.Vertical.TScrollbar.thumb',
                    {'unit': '1',
                     'children':
                        [('My.Vertical.TScrollbar.grip', {'sticky': ''})],
                     'sticky': 'nswe'})
                  ],
      'sticky': 'ns'})])


style.configure("My.Vertical.TScrollbar", gripcount=0, background=col1,
                troughcolor='#000000', borderwidth=0, bordercolor='#000000',
                lightcolor='#000000',relief="flat", darkcolor='#000000',
                arrowsize=6)








style2=ttk.Style()
style2.element_create("My.Vertical.TScrollbar2.trough", "from", "clam")
style2.element_create("My.Vertical.TScrollbar2.thumb", "from", "clam")
style2.element_create("My.Vertical.TScrollbar2.grip", "from", "clam")

style2.layout("My.Vertical.TScrollbar2",
   [('My.Vertical.TScrollbar2.trough',
     {'children': [('My.Vertical.TScrollbar2.thumb',
                    {'unit': '1',
                     'children':
                        [('My.Vertical.TScrollbar2.grip', {'sticky': ''})],
                     'sticky': 'nswe'})
                  ],
      'sticky': 'ns'})])





style2.configure("My.Vertical.TScrollbar2", gripcount=0, background=col1,
                troughcolor='#000000', borderwidth=0, bordercolor='#000000',
                lightcolor='#000000',relief="flat", darkcolor='#000000',
                arrowsize=6)












        


frame=tk.Frame(bg="#000000",width=w-20,height=((h-121)-80-10))



def on_release(e):
    global sb_st

    if sb_st==1:
        sb_st=0

def drag(e):

    global can2
    global sb_sz,sb_col,sb_h,sb_st

    if sb_st==1:

        if not e.y<0:


            #can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            h=int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])*int(can2["height"])

            if not e.y+h>int(can2["height"]):
                sb_move(e.y,e.y*int(can2["scrollregion"].split(" ")[-1])/int(can2["height"]))
            else:
                sb_move(int(can2["height"])-h-3,(int(can2["height"])-h-3)*int(can2["scrollregion"].split(" ")[-1])/int(can2["height"]))


            move_bg()
            draw_sb()


def update_sb():
    global can2,sb_region,sb_h,psb_h



    if can2["scrollregion"]!=sb_region:

        draw_sb()

        sb_region=can2["scrollregion"]

        move_bg()


    if sb_h!=psb_h:

        draw_sb()

        psb_h=sb_h

        move_bg()







    root.after(2,update_sb)


def draw_sb():
    global can2
    global sb,sb_sz,sb_region,sb_h,sb_col,circle10
    global _theme

    can2.delete(sb[0])
    can2.delete(sb[1])
    can2.delete(sb[2])

    sb_col=_theme[0]

    h=int(can2["height"])/int(can2["scrollregion"].split(" ")[-1])*int(can2["height"])

    #if not int(h)==int(can2["scrollregion"].split(" ")[-1]):




    sb[0]=can2.create_image(int(can2["width"])-sb_sz-1,can2.canvasy(sb_h),image=circle10,anchor="nw")
    sb[1]=can2.create_rectangle(int(can2["width"])-sb_sz-1,can2.canvasy(sb_h+sb_sz/2),int(can2["width"])-1,can2.canvasy(sb_h+h-sb_sz/2-1),fill=sb_col,outline=sb_col)
    sb[2]=can2.create_image(int(can2["width"])-sb_sz-1,can2.canvasy(sb_h+h-sb_sz-1),image=circle10,anchor="nw")

def sb_move(v1,v2):

    global can2
    global sb_h

    sb_h=v1
    can2.yview_moveto(v2/int(can2["scrollregion"].split(" ")[-1]))

    #print(can.canvasy(0))

    move_bg()


sb=[0,0,0]
sb_sz=6

sb_col=_theme[0]
sb_region=()
sb_h=0
psb_h=0
sb_st=0


can2=tk.Canvas(frame,bg="#000000",width=w-20,height=((h-121)-80-10),relief="flat",highlightthickness=0,border=0,cursor="none")
can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-1>",can2_b1)
can2.bind("<Button-3>",can_b3)
can2.bind("<space>",play_pause)
can2.bind("<Right>",play_next)
can2.bind("<Left>",play_previous)
can2.bind("<KeyPress>",__list)

can2.bind("<B1-Motion>",drag)

can2.bind("<ButtonRelease-1>",on_release)


frame2=tk.Frame(bg="#000000",width=350+100+100,height=250)

can4=tk.Canvas(frame2,bg="#000000",width=350+100+100,height=40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250),cursor="none")
can4.pack(side=tk.TOP)



frame3=tk.Frame(frame2,bg="#000000",width=350+100+100,height=250-40)


def on_release2(e):
    global sb2_st

    if sb2_st==1:
        sb2_st=0

def drag2(e):

    global can3
    global sb2_sz,sb2_col,sb2_h,sb2_st

    if sb2_st==1:

        if not e.y<0:


            #can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

            h=int(can3["height"])/int(can3["scrollregion"].split(" ")[-1])*int(can3["height"])

            if not e.y+h>int(can3["height"]):
                sb2_move(e.y,e.y*int(can3["scrollregion"].split(" ")[-1])/int(can3["height"]))
            else:
                sb2_move(int(can3["height"])-h-3,(int(can3["height"])-h-3)*int(can3["scrollregion"].split(" ")[-1])/int(can3["height"]))


            move_bg()
            draw_sb2()


def update_sb2():
    global can3,sb2_region,sb2_h,psb2_h



    if can3["scrollregion"]!=sb2_region:

        draw_sb2()

        sb2_region=can3["scrollregion"]

        move_bg()

    if sb2_h!=psb2_h:

        draw_sb2()

        psb2_h=sb2_h

        move_bg()







    root.after(2,update_sb2)


def draw_sb2():
    global can3
    global sb2,sb2_sz,sb2_region,sb2_h,sb2_col,circle10
    global _theme

    sb2_col=_theme[0]

    can3.delete(sb2[0])
    can3.delete(sb2[1])
    can3.delete(sb2[2])

    h=int(can3["height"])/int(can3["scrollregion"].split(" ")[-1])*int(can3["height"])


    sb2[0]=can3.create_image(int(can3["width"])-sb2_sz-4,can3.canvasy(sb2_h),image=circle10,anchor="nw")
    sb2[1]=can3.create_rectangle(int(can3["width"])-sb2_sz-4,can3.canvasy(sb2_h+sb2_sz/2),int(can3["width"])-4,can3.canvasy(sb2_h+h-sb2_sz/2-1),fill=sb2_col,outline=sb2_col)
    sb2[2]=can3.create_image(int(can3["width"])-sb2_sz-4,can3.canvasy(sb2_h+h-sb2_sz-1),image=circle10,anchor="nw")


def sb2_move(v1,v2):

    global can3
    global sb2_h

    sb2_h=v1
    can3.yview_moveto(v2/int(can3["scrollregion"].split(" ")[-1]))

    #print(can3.canvasy(0))

    move_bg()


sb2=[0,0,0]
sb2_sz=6
sb2_col=_theme[0]
sb2_region=()
sb2_h=0
psb2_h=0
sb2_st=0
can3=tk.Canvas(frame3,bg="#000000",width=350+100+100,height=250-40+50,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250-40),cursor="none")
can3.pack(side=tk.LEFT)
can3.bind_all("<MouseWheel>",_on_mousewheel)
can3.bind("<Button-1>",can3_b1)

can3.bind("<B1-Motion>",drag2)

can3.bind("<ButtonRelease-1>",on_release2)







frame3.pack(side=tk.TOP)


can6=tk.Canvas(frame2,bg="#000000",width=350+100+100,height=40,relief="flat",highlightthickness=0,border=0,cursor="none")
can6.pack(side=tk.TOP)








def search__():

    global search,search_var,mvar,songs,current_playing
    global st,current_playlist
    global songs_status
    global playlist_st
    

    if search.get()!=search_var:
        search_var=search.get()



        main()

        move_to_playing()








    root.after(2,search__)

def est_sz(con):
    global w

    w_=680*1.75

    if con==0:

        return int(w*123/w_)

    elif con==1:

        return int(w*122/w_)



search=tk.Entry(bg=_theme[1][1],fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=est_sz(0),font=("FreeMono",13))
npl=tk.Entry(bg=_theme[1][1],fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=est_sz(1),font=("FreeMono",13))

ls=0
def mvar_():


    global ls,current_playing,songs,mvar
    global _songs_,songs_status
    global st,current_playlist

    try:




        for s in range(len(_songs_)):
            if _songs_[s][0]==current_playing:
               

                mvar=s


    except:
        pass

    root.after(2,mvar_)



def can_sort_b1(e):

    global sort_ar,sort_val
    global sort_st,can_sort
    global can2
    global loop

    global st,current_playlist
    global songs_status


    for s in sort_ar:

        if s[1]<=e.y<=s[1]+30:

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            loop=0


            sort_val=s[0]

            main()


            if st==songs_status[0]:

                if st==2:

                    if current_playlist==songs_status[1]:

                        update_song_status()
                        move_to_playing(1)

                else:
                    update_song_status()
                    move_to_playing(1)





            sort_st=0
            can_sort.place_forget()



sort_st=0
_sort=0
can_sort=tk.Canvas(bg="#000000",width=250,height=160,relief="flat",highlightthickness=0,border=0,cursor="none")

can_sort.bind("<Button-1>",can_sort_b1)




sort_ar=[]




y=30
for _ in sa:

    sort_ar.append([_,y])

    y+=30







can_lyrics=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")

l1,l2=0,0
ang_=0
def check_up_theme():
    global up_theme,_theme,theme_ent,sel_col
    global l1,l2,ang_
    global con_theme
    global bg_region_

    if not up_theme==None:

        if up_theme.is_alive():


            can_settings.delete(l1)
            can_settings.delete(l2)

            cx,cy=int(can_settings["width"])/2+45+10+15,int(can_settings["height"])-10-15
            r=15

            l1=can_settings.create_arc(cx-r,cy-r,cx+r,cy+r,start=ang_,extent=70,style="arc",outline=_theme[0],width=2)
            l2=can_settings.create_arc(cx-r,cy-r,cx+r,cy+r,start=ang_+180,extent=70,style="arc",outline=_theme[0],width=2)
            

            ang_+=1

        else:


            _theme[0]=str(sel_col)

            configure_theme(_theme[0])

            
            main()
            draw_settings()
            up_theme=None

            can_settings.create_text(int(can_settings["width"])-20,int(can_settings["height"])-10-15,
                text="Theme Updated!",font=("FreeMono",13),fill=_theme[0],anchor="e")

            sel_col=""
            ang_=0
            con_theme=0

    root.after(2,check_up_theme)
theme_attr=[0,0]
can_sel_op_rec=0

def check_theme_attr():
    global settings_st2
    global can_settings
    global bg_region_,bg_region,bg_region2_
    global theme_ent,sel_op_ent
    global sel_col
    global theme_attr

    global can_theme_ent,te_var,can_theme_ent_rec
    global can_sel_op,op_var,can_sel_op_rec


    if settings_st2==1:


        if te_var!=theme_attr[0] or op_var!=theme_attr[1]:

            theme_attr=[te_var,op_var]

            can_settings.delete(bg_region)
            can_settings.delete(bg_region2_)


            sel_col=te_var






            can_theme_ent.delete(can_theme_ent_rec)


            try:


                can_theme_ent_rec=can_theme_ent.create_rectangle(0,0, int(can_theme_ent["width"])-1,int(can_theme_ent["height"])-1,
                    outline=sel_col)
            except:



                can_theme_ent_rec=can_theme_ent.create_rectangle(0,0, int(can_theme_ent["width"])-1,int(can_theme_ent["height"])-1,
                    outline=_theme[0])






            

            try:

                bg_region2_=can_settings.create_image(bg_region_[1][0],bg_region_[1][1],image=conf_bg(sel_col),anchor="nw")
    
            except:
                pass


            try:

                bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
            except:
                bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])









    root.after(2,check_theme_attr)



up_theme=None
sel_col=""
settings_st2=0
def can_settings_b1(e):

    global can_settings,theme_ent,sel_op_ent
    global settings_st
    global _theme
    global ar_themes
    global bg_xy
    global bg_region_,bg_region
    global _crop_,cr,cr2

    global crop,crop2

    global no_bg_st
    global up_theme
    global sel_col
    global settings_st2
    global bg_region2_
    global con_theme
    global te_var,op_var
    global cte_txt

    bg_xy=[e.x,e.y]

    #quit

    if int(can_settings["width"])-10-25<=e.x<=int(can_settings["width"])-10:
        if 10<=e.y<=10+25:
            settings_st=0
            can_settings.place_forget()
            can_theme_ent.place_forget()
            can_sel_op.place_forget()

            settings_st2=0

            return


    #save

    cx,cy=int(can_settings["width"])/2-45+15,int(can_settings["height"])-10-15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:



        ar=os.listdir("data")

        for i in ar:

            if i.split(".")[0]=="bg_":

                os.remove("data/"+i)

        im=Image.open("data/bg2_.png")
        im.save("data/bg_.png")


        
        op1,op2=str(op_var).replace(" ","").split(",")

        sel_col=str(te_var)

        con_theme=1

        _theme[2]=float(op1)
        _theme[3]=float(op2)


        im=Image.open("data/bg3.png")
        x,y=im.size

        im2=Image.open("data/bg2_.png")
        x_,y_=im2.size

        ar=[]

        bg_st=0
        for p in range(len(bg_region_[1])):

            if bg_st==0:
                ar.append(int(round((bg_region_[1][p]-bg_region_[0][0])*x_/x,0)))
                bg_st=1
            elif bg_st==1:
                ar.append(int(round((bg_region_[1][p]-bg_region_[0][1])*y_/y,0)))
                bg_st=0

        _theme[-1]=[ar[0],ar[1],ar[4],ar[5]]

        _theme[-2]=no_bg_st

        save()

        #adjust_theme()

        draw_settings()

        up_theme=threading.Thread(target=adjust_theme,daemon=True)
        up_theme.start()



        return


    cx,cy=int(can_settings["width"])/2+45-15,int(can_settings["height"])-10-15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:


        ar=os.listdir("data")

        for i in ar:

            if i.split(".")[0]=="bg_":

                os.remove("data/"+i)


        im=Image.open("data/bg2_.png")
        im.save("data/bg_.png")


        op1,op2=str(op_var).replace(" ","").split(",")

        sel_col=str(te_var)

        con_theme=1

        _theme[2]=float(op1)
        _theme[3]=float(op2)


        im=Image.open("data/bg3.png")
        x,y=im.size

        im2=Image.open("data/bg2_.png")
        x_,y_=im2.size

        ar=[]

        bg_st=0
        for p in range(len(bg_region_[1])):

            if bg_st==0:
                ar.append(int(round((bg_region_[1][p]-bg_region_[0][0])*x_/x,0)))
                bg_st=1
            elif bg_st==1:
                ar.append(int(round((bg_region_[1][p]-bg_region_[0][1])*y_/y,0)))
                bg_st=0

        _theme[-1]=[ar[0],ar[1],ar[4],ar[5]]

        _theme[-2]=no_bg_st

        save()
        #adjust_theme()

        draw_settings()

        up_theme=threading.Thread(target=adjust_theme,daemon=True)
        up_theme.start()
        return

    if int(can_settings["width"])/2-45+15<=e.x<=int(can_settings["width"])/2+45-15:
        if int(can_settings["height"])-10-30<=e.y<=int(can_settings["height"])-10:


            ar=os.listdir("data")

            for i in ar:

                if i.split(".")[0]=="bg_":

                    os.remove("data/"+i)


            im=Image.open("data/bg2_.png")
            im.save("data/bg_.png")

            op1,op2=str(op_var).replace(" ","").split(",")

            sel_col=str(te_var)

            con_theme=1

            _theme[2]=float(op1)
            _theme[3]=float(op2)

            im=Image.open("data/bg3.png")
            x,y=im.size

            im2=Image.open("data/bg2_.png")
            x_,y_=im2.size

            ar=[]

            bg_st=0
            for p in range(len(bg_region_[1])):

                if bg_st==0:
                    ar.append(int(round((bg_region_[1][p]-bg_region_[0][0])*x_/x,0)))
                    bg_st=1
                elif bg_st==1:
                    ar.append(int(round((bg_region_[1][p]-bg_region_[0][1])*y_/y,0)))
                    bg_st=0

            _theme[-1]=[ar[0],ar[1],ar[4],ar[5]]

            _theme[-2]=no_bg_st 

            save()



            #adjust_theme()

            draw_settings()

            up_theme=threading.Thread(target=adjust_theme,daemon=True)
            up_theme.start()
            return    

    # add bg 



    cx,cy=int(can_settings["width"])-20-25-15-25+15,int(can_settings["height"])-95+5+15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=12.5:

        try:

            file=filedialog.askopenfilename()

            im=Image.open(file)
            im.save("data/bg2_.png")

            settings_st=1

            no_bg_st=0

            draw_settings(1)


            

        except:
            pass

        #if file!="":



        return



    for c in ar_themes:

        cx,cy=c[-2:]

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=20:

            cx,cy=c[1]-10+10,c[2]-20+2+10

            r_=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

            if r_<=10:

                _theme[4].pop(_theme[4].index(c[0]))
                save()
                draw_settings()
                return

            te_var=c[0]


            can_theme_ent.delete(cte_txt)

            if get_text_length(can_theme_ent, te_var, "FreeMono", 13)>int(can_theme_ent["width"])-2:

                try:
                    cte_txt=can_theme_ent.create_text(int(can_theme_ent["width"])-2,10,text=te_var,fill=te_var,
                        font=("FreeMono",13),anchor="e")
                except:
                    cte_txt=can_theme_ent.create_text(int(can_theme_ent["width"])-2,10,text=te_var,fill=_theme[0],
                        font=("FreeMono",13),anchor="e")
            else:

                try:
                    cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=te_var,
                        font=("FreeMono",13),anchor="w")

                except:
                    cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=_theme[0],
                        font=("FreeMono",13),anchor="w")

            return

    #crop



    if int(can_settings["width"])-20-25-15-25-15-25<=e.x<=int(can_settings["width"])-20-25-15-25-15:
        if int(can_settings["height"])-95+5<=e.y<=int(can_settings["height"])-95+5+25:

            if no_bg_st==1:
                return


            if not settings_st==2:
                settings_st=2

                can_settings.delete(bg_region)
                can_settings.delete(bg_region2_)


                _crop_=[]
            elif settings_st==2:

                settings_st=0

                try:

                    bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
                except:
                    bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])


            can_settings.delete(cr)

            can_settings.delete(cr2)

            if settings_st==2:

                cr=can_settings.create_image(int(can_settings["width"])-20-25-15-25-15-25,int(can_settings["height"])-95+5,
                    image=crop,anchor="nw")

            else:

                cr=can_settings.create_image(int(can_settings["width"])-20-25-15-25-15-25,int(can_settings["height"])-95+5,
                    image=crop2,anchor="nw")  

            return


    if settings_st==2:


        im=Image.open("data/bg3.png")
        x,y=im.size

        if bg_region_[0][0]<=e.x<=bg_region_[0][0]+x:
            if bg_region_[0][1]<=e.y<=bg_region_[0][1]+y:


                _crop_.append(e.x)
                _crop_.append(e.y)

                if len(_crop_)==4:



                    im=Image.open("data/bg2_.png")
                    x,y=im.size

                    im2=Image.open("data/bg3.png")
                    x_,y_=im2.size


                    xx=[_crop_[0],_crop_[2]]
                    yy=[_crop_[1],_crop_[3]]

                    x1=int(round((min(xx)-bg_region_[0][0])*x/x_,0))
                    x2=int(round((max(xx)-bg_region_[0][0])*x/x_,0))

                    y1=int(round((min(yy)-bg_region_[0][1])*y/y_,0))
                    y2=int(round((max(yy)-bg_region_[0][1])*y/y_,0))



                    im=im.crop((x1,y1,x2,y2))


                    im.save("data/bg2_.png")

                    _crop_=[]



                    draw_settings(1)

                return



    if int(can_settings["width"])-20-25<=e.x<=int(can_settings["width"])-20:

        if int(can_settings["height"])-95+5<=e.y<=int(can_settings["height"])-95+5+25:


                im=Image.new("RGBA", (w,h), (0,0,0,255))

                im.save("data/bg2_.png")

                no_bg_st=1



                draw_settings(1)

                return


no_bg_st=0
    #print(e.x,e.y)



ar_themes=[]

sel_theme=0
bg_region,bg_region_=0,[]

settings_st=0
cr=0
_crop_=[]
cr2=0
bg_region2=0
def conf_bg(col):
    global _theme
    global bg_region_,bg_region2
    global op_var 

    x1=int(round(bg_region_[1][0]-bg_region_[0][0],0))
    x2=int(round(bg_region_[1][4]-bg_region_[0][0],0))

    y1=int(round(bg_region_[1][1]-bg_region_[0][1],0))
    y2=int(round(bg_region_[1][5]-bg_region_[0][1],0))

    im=Image.open("data/bg3.png")
    im=im.crop((x1,y1,x2,y2))
    im.save("data/bg3_.png")

    convert_("data/bg3_.png","data/bg3_.png",col)
    darken_image("data/bg3_.png", "data/bg3_.png",(0,0,0), float(str(op_var).replace(" ","").split(",")[0]))

    bg_region2=ImageTk.PhotoImage(file="data/bg3_.png")

    return bg_region2

bg_region2_=0
con_theme=0
bg_region_=0
bg_se=0

focus__=0
def draw_settings(con=0):

    global can_settings,theme_ent,sel_op_ent
    global settings_st,settings_st2
    global im_bg
    global _theme
    global ar_themes
    global sel_theme
    global bg_region,bg_region_
    global bg_xy
    global settings_st
    global crop,crop2
    global delete_,add
    global cr
    global no_bg_st
    global bg2_
    global bg_region2,bg_region2_
    global sel_col
    global con_theme
    global bg_region_
    global bg_se
    global can_theme_ent,te_var
    global can_theme_ent_rec,cte_txt


    global can_sel_op,op_var
    global can_sel_op_rec,cop_txt
    global focus__



    focus__=0


    if con==0:

        no_bg_st=_theme[-2]
        col_=_theme[0]
    else:


        try:
            can_settings.create_line(-1,-1,-1,-1,fill=te_var)
            col_=te_var
        except:
            col_=_theme[0]



    if con_theme==1:
        try:
            can_settings.create_line(-1,-1,-1,-1,fill=sel_col)
            col_=sel_col
        except:
            col_=_theme[0] 


    

    can_settings.delete("all")
    can_settings.place(in_=root,x=10+25+5,y=25+12.5+5)

    can_settings.create_image(-(10+25+5),-(25+12.5+5),image=bg2_,anchor="nw")


    draw_round_rec(can_settings,0,0, int(can_settings["width"])-1,int(can_settings["height"])-1,25,_theme[0],col1,1)

    can_settings.create_image(int(can_settings["width"])-10-25,10,image=quit,anchor="nw")


    can_settings.create_text(20,30,text="Theme",font=("FreeMono",13),fill=_theme[0],anchor="w")

    x_=10+25+5+20+get_text_length(can_settings, "Theme", "FreeMono", 13)+10
    y_=25+12.5+5+30-9

    

    can_theme_ent["width"]=(259+1+1)-(77-1+1)
    can_theme_ent["height"]=(42)-(20)

    can_theme_ent.delete("all")

    can_theme_ent.create_image(-(77-1+1+(10+25+5)),-(19+1+(25+12.5+5)),image=bg2_,anchor="nw")

    te_var=col_

    cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=col_,
        font=("FreeMono",13),anchor="w")

    can_theme_ent_rec=can_theme_ent.create_rectangle(0,0, int(can_theme_ent["width"])-1,int(can_theme_ent["height"])-1,
        outline=col_)


    can_theme_ent.place(in_=root,x=77-1+1+(10+25+5),y=19+1+(25+12.5+5))



    r=20
    x=259+1+1+50
    y=30-20

    ar_themes=[]

    for c in _theme[4]:

        can_settings.create_oval(x,y,x+r*2,y+r*2,fill=c,outline=c)

        ar_themes.append([c,x+r,y+r])

        x+=r*2+20



    can_settings.create_line(20+10,60, 20,60, 20,int(can_settings["height"])-95,
        int(can_settings["width"])-20,int(can_settings["height"])-95,
        int(can_settings["width"])-20,60,20+10+5+get_text_length(can_settings, "Background", "FreeMono", 13)+5,60,
        fill=_theme[0])

    can_settings.create_text(20+10+5,60,text="Background",font=("FreeMono",13),fill=_theme[0],
        anchor="w")


    ar=os.listdir("data")

    for i in ar:

        if i.split(".")[0]=="bg_":

            ext=i.split(".")[1]

    im=Image.open("data/bg_."+ext)

    if con==0:

        im.save("data/bg2_.png")

    im=Image.open("data/bg2_.png")


    x,y=im.size

    xx=(int(can_settings["width"])-20)-20-60
    yy=(int(can_settings["height"])-95)-60-60

    if xx/yy<x/y:


        x2=int(xx)
        y2=int(round(x2*y/x,0))

        im=im.resize((x2,y2))

        im.save("data/bg3.png")

    elif xx/yy>x/y:


        x2=int(round(yy*x/y,0))
        y2=int(yy)

        im=im.resize((x2,y2))

        im.save("data/bg3.png")

    else:

        x2=int(xx)
        y2=int(yy)

        im=im.resize((x2,y2))

        im.save("data/bg3.png")


    im=Image.open("data/bg3.png")
    x,y=im.size

    x_=(xx-x)/2
    y_=(yy-y)/2


    ar=os.listdir("data")

    for i in ar:

        if i.split(".")[0]=="bg_":
            ext=i.split(".")[1]

    

    im=Image.open("data/bg_."+ext)
    _x,_y=im.size



    if w/h>x/y:

        __x=x
        __y=x*h/w

    elif w/h<x/y:

        __y=y
        __x=y*w/h
    else:

        __x=x
        __y=y

    xy=[0,0]


    if settings_st==0:

        if _theme[-1]==[]:




            if w/h>_x/_y:

                yy_=int((_y-_x*h/w)/2)

                xy=[0,yy_]

                _theme[-1]=[0,yy_,_x,_y-yy_]

            elif w/h<_x/_y:

                xx_=int((_x-_y*w/h)/2)


                xy=[xx_,0]

                _theme[-1]=[xx_,0,_x-xx_,_y]

            else:
                xy=[0,0]

        else:

            xy=_theme[-1][:2]

    else:
        im=Image.open("data/bg2_.png")
        _x,_y=im.size


        if w/h>_x/_y:

            yy_=int((_y-_x*h/w)/2)

            xy=[0,yy_]


        elif w/h<_x/_y:

            xx_=int((_x-_y*w/h)/2)


            xy=[xx_,0]

        else:

            xy=[0,0]


        settings_st=0



    if no_bg_st==1:
        xy=[0,0]




    im_bg=ImageTk.PhotoImage(file="data/bg3.png")

    can_settings.create_image(20+30+x_,60+30+y_,image=im_bg,anchor="nw")


    can_settings.create_rectangle(20+30,60+30,20+30+xx,60+30+yy,outline=_theme[1][0])



    x1=20+30+xy[0]*x/_x
    y1=60+30+xy[1]*y/_y

    if no_bg_st==1:

        x2=x1+x
        y2=y1+y

    else:


        if w/h>x/y:

            x2=20+30+x+xy[0]*x/_x
            y2=60+30+x*h/w+xy[1]*y/_y
        elif w/h<x/y:

            y2=60+30+y+xy[1]*y/_y
            x2=20+30+y*w/h+xy[0]*x/_x




    sz=90
    can_settings.create_image(int(can_settings["width"])-20-25,int(can_settings["height"])-95+5,
        image=delete_,anchor="nw")

    can_settings.create_image(int(can_settings["width"])-20-25-15-25,int(can_settings["height"])-95+5,
        image=add,anchor="nw")

    if settings_st==2:

        cr=can_settings.create_image(int(can_settings["width"])-20-25-15-25-15-25,int(can_settings["height"])-95+5,
            image=crop,anchor="nw")

    else:

        cr=can_settings.create_image(int(can_settings["width"])-20-25-15-25-15-25,int(can_settings["height"])-95+5,
            image=crop2,anchor="nw")    





    can_settings.create_text(20,int(can_settings["height"])-65,text="Opacity (bg , select)",
        fill=_theme[0],font=("FreeMono",13),anchor="w")




    xx_=10+25+5+20+get_text_length(can_settings, "Opacity (bg , select)", "FreeMono", 13)+10
    yy_=25+12.5+5+int(can_settings["height"])-65-9


    can_sel_op["width"]=(259+1+1)-(77-1+1)
    can_sel_op["height"]=(42)-(20)

    can_sel_op.delete("all")

    can_sel_op.create_image(-(xx_),-(yy_),image=bg2_,anchor="nw")

    op_var=str(_theme[2])+","+str(_theme[3])

    cop_txt=can_sel_op.create_text(0,10,text=op_var,fill=_theme[0],
        font=("FreeMono",13),anchor="w")

    can_sel_op_rec=can_sel_op.create_rectangle(0,0, int(can_sel_op["width"])-1,int(can_sel_op["height"])-1,
        outline=_theme[0])


    can_sel_op.place(in_=root,x=xx_,y=yy_)






    xx_=20+get_text_length(can_settings, "Opacity (bg , select)", "FreeMono", 13)+10
    yy_=int(can_settings["height"])-65-9


    can_settings.create_image(int(can_settings["width"])/2-sz/2,int(can_settings["height"])-40,
        image=circle3,anchor="nw")
    can_settings.create_image(int(can_settings["width"])/2+sz/2-30,int(can_settings["height"])-40,
        image=circle3,anchor="nw")

    can_settings.create_rectangle(int(can_settings["width"])/2-sz/2+15,int(can_settings["height"])-40,
        int(can_settings["width"])/2+sz/2-15,int(can_settings["height"])-40+30-1,
        fill=_theme[0],outline=_theme[0])

    can_settings.create_text(int(can_settings["width"])/2,int(can_settings["height"])-40+15,text="Save",
        fill="#000000",font=("FreeMono",13),anchor="c")


    bg_region_=[[20+30+x_,60+30+y_],[x1+x_,y1+y_, x2+x_,y1+y_, x2+x_,y2+y_,
        x1+x_,y2+y_, x1+x_,y1+y_]]


    try:
        bg_region2_=can_settings.create_image(bg_region_[1][0],bg_region_[1][1],image=conf_bg(col_),anchor="nw")
    except:
        pass

    try:

        bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
    except:
        bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])

    settings_st2=1

del_theme=0
def can_settings_m(e):
    global can_settings
    global ar_themes
    global delete3
    global del_theme
    global _crop_,cr2
    global bg_region_
    global settings_st

    global no_bg_st
    global te_var

    can_settings.delete(del_theme)

    for c in ar_themes:

        cx,cy=c[1:]

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=20:

            del_theme=can_settings.create_image(c[1]-10,c[2]-20+2,
                image=delete3,anchor="nw")
            return


    im=Image.open("data/bg3.png")
    x,y=im.size

    if bg_region_[0][0]<=e.x<=bg_region_[0][0]+x:
        if bg_region_[0][1]<=e.y<=bg_region_[0][1]+y:


            if settings_st==2:

                can_settings.delete(cr2)


                if len(_crop_)==2:

                    try:

                        cr2=can_settings.create_rectangle(*_crop_,e.x,e.y,outline=te_var)

                    except:
                        cr2=can_settings.create_rectangle(*_crop_,e.x,e.y,outline=_theme[0])

bg_xy=[]
def can_settings_drag(e):
    global can_settings
    global bg_region,bg_region_,bg_region2_
    global bg_xy
    global te_var



    if bg_region_[1][0]<=e.x<=bg_region_[1][4]:
        if bg_region_[1][1]<=e.y<=bg_region_[1][5]:

            im=Image.open("data/bg3.png")
            xx,yy=im.size

            ar=[]

            for p in bg_region_[1]:
                ar.append(p)

            bg_st=0
            for p in range(len(ar)):

                if bg_st==0:

                    ar[p]-=bg_xy[0]-e.x
                    bg_st=1
                elif bg_st==1:

                    ar[p]-=bg_xy[1]-e.y
                    bg_st=0

            bg_xy=[e.x,e.y]


            if bg_region_[0][0]<=ar[0] and ar[4]<=bg_region_[0][0]+xx:


                bg_st=0
                for p in range(len(ar)):

                    if bg_st==0:

                        bg_region_[1][p]=ar[p]
                        bg_st=1

                    elif bg_st==1:
                        bg_st=0



                can_settings.delete(bg_region)
                can_settings.delete(bg_region2_)

                try:

                    bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
                except:
                    bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])



            if bg_region_[0][1]<=ar[1] and ar[5]<=bg_region_[0][1]+yy:

                    bg_st=0
                    for p in range(len(ar)):

                        if bg_st==0:

                            
                            bg_st=1

                        elif bg_st==1:

                            bg_region_[1][p]=ar[p]
                            bg_st=0

                    can_settings.delete(bg_region)
                    can_settings.delete(bg_region2_)

                    try:

                        bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
                    except:
                        bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])


def on_release_s(e):

    global bg_region_
    global settings_st
    global bg_region,bg_region2_
    global can_settings
    global sel_col
    global theme_ent
    global te_var


    if bg_region_[1][0]<=e.x<=bg_region_[1][4]:
        if bg_region_[1][1]<=e.y<=bg_region_[1][5]:

            if not settings_st==2:
                can_settings.delete(bg_region)
                can_settings.delete(bg_region2_)

                try:

                    bg_region2_=can_settings.create_image(bg_region_[1][0],bg_region_[1][1],image=conf_bg(te_var),anchor="nw")
                except:
                    pass

                try:

                    bg_region=can_settings.create_line(bg_region_[1],fill=te_var)
                except:
                    bg_region=can_settings.create_line(bg_region_[1],fill=_theme[0])


settings_st=0

can_settings=tk.Canvas(width=w-100,height=h-200,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can_settings.bind("<Button-1>",can_settings_b1)
can_settings.bind("<Motion>",can_settings_m)
can_settings.bind("<B1-Motion>",can_settings_drag)
can_settings.bind("<ButtonRelease-1>",on_release_s)

theme_ent=tk.Entry(width=20,font=("FreeMono",13),bg="#000000",fg=_theme[0],relief="flat",highlightthickness=0,
    border=0,insertbackground=_theme[0],selectbackground=_theme[0],selectforeground="#000000")

sel_op_ent=tk.Entry(width=20,font=("FreeMono",13),bg="#000000",fg=_theme[0],relief="flat",highlightthickness=0,
    border=0,insertbackground=_theme[0],selectbackground=_theme[0],selectforeground="#000000")

can2.focus_set()


def filter1_b1(e):

    global filter_val,filter_pl
    global current_playing
    global _songs_

    ar=["None","Favourites","Playlists","With Video"]


    y=10

    for a in ar:


        if y<=e.y<=y+30:

            filter_val=a

            filter_pl=None

            draw_can()

            main()

            if not a=="Playlists":

                con=0


                for s in _songs_:

                    if s[0]==current_playing:
                        con=1


                if con==0:

                    if play_st==1:

                        pygame.mixer.quit()
                    current_playing=""

            main()
            move_to_playing()

            

            return

        y+=30
def filter2_b1(e):
    global filter_pl
    global current_playing
    global _songs_

    y=0


    for pl in playlist:
        if y<=filter_can2.canvasy(e.y)<=y+30:

            filter_pl=pl


            draw_can()
            main()
            con=0


            for s in _songs_:

                if s[0]==current_playing:
                    con=1

            if con==0:

                pygame.mixer.quit()
                current_playing=""

            main()
            move_to_playing()

            return

        y+=30


filter_can1=tk.Canvas(width=250,height=30*4,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
filter_can1.bind("<Button-1>",filter1_b1)

filter_can2=tk.Canvas(width=250,height=30*7,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
filter_can2.bind("<Button-1>",filter2_b1)
filter_can2.bind_all("<MouseWheel>",_on_mousewheel)


del_info=["",""]
def conf_del_b1(e):

    global del_info
    global conf_del
    global songs_status,play_st,current_playing,st,_songs_,mvar
    global can2,current_playlist,tm

    #song

    if int(conf_del["height"])-35<=e.y<=int(conf_del["height"]):

        if 0<=e.x<=int(conf_del["width"])/2:



            if del_info[1]=="music":
            

            


                song_=del_info[0].split("/")[-1]



                p_=play_st
                

                if songs_status[0]==st:
                    if songs_status[1]==current_playlist:

                        if current_playing==song_:
                            play_st=0
                            pygame.mixer.quit() 
                    else:
                        
                        if current_playing==song_:
                            play_st=0
                            pygame.mixer.quit() 


                os.remove(del_info[0])


                play_st=p_




                conn=0


                if current_playing==song_:



                    if len(_songs_)==1:
                        mvar=0
                    elif mvar==len(_songs_)-1:
                        mvar=0
                    else:
                        mvar=mvar+1


                    current_playing=_songs_[mvar][0]

                    tm=0



                    if len(_songs_)==1:
                        pygame.mixer.quit()
                        current_playing=""

                    else:


                        if play_st==0:

                            play_music("music/"+current_playing,tm,1)
                            pygame.mixer.quit()
                        elif play_st==1:

                            play_music("music/"+current_playing,tm)




                    
                    songs_status[-1]=current_playing


                    conn=1







                
                del_wave()

                main()

                if conn==1:
                    move_to_playing()

            elif del_info[1]=="video":

                os.remove(del_info[0])

                main()


            elif del_info[1]=="playlist":


                    can2["scrollregion"]=(0,0,(int(can2["width"])-sb_sz-1),int(can2["height"]))

                    if st==songs_status[0]:
                        if st==2:
                            if del_info[0]==songs_status[1]:

                                try:
                                    play_music("music/"+current_playing,tm,1)
                                    pygame.mixer.quit()
                                except:
                                    pass


                                current_playing=""
                                current_playlist=""

                                update_song_status()


                    create_playlist(del_info[0],con=3)



                    main()

                    if st==songs_status[0]:
                        if st==2:
                            if current_playlist==songs_status[1]:
                                update_song_status()

            elif del_info[1]=="lyrics":



                update_details(del_info[0],2,"")
                main()
        conf_del.place_forget()


def conf_del_(file,con):
    global conf_del
    global del_info
    global bg2_
    global _theme
    global w,h


    conf_del.delete("all")

    conf_del.create_image(-(w-int(conf_del["width"]))/2,-(h-int(conf_del["height"]))/2,
        image=bg2_,anchor="nw")

    draw_round_rec(conf_del,0,0, int(conf_del["width"])-1,int(conf_del["height"])-1,15,_theme[0],"",1)

    conf_del.create_line(0,int(conf_del["height"])-35,int(conf_del["width"]),int(conf_del["height"])-35,
        fill=_theme[0])

    conf_del.create_line(int(conf_del["width"])/2,int(conf_del["height"])-35,
        int(conf_del["width"])/2,int(conf_del["height"]),fill=_theme[0])

    xx=int(conf_del["width"])/4
    conf_del.create_text(xx,int(conf_del["height"])-35/2,text="Confirm",font=("FreeMono",13),fill=_theme[0])
    conf_del.create_text(int(conf_del["width"])-xx,int(conf_del["height"])-35/2,text="Cancel",font=("FreeMono",13),fill=_theme[0])

    conf_del.place(in_=root,x=(w-int(conf_del["width"]))/2,y=(h-int(conf_del["height"]))/2)

    del_info=[file,con]

    #song

    if con=="music":


        if get_text_length(can3, "Delete Song : "+file.split("/")[-1], "FreeMono", 13)>int(conf_del["width"])-20:

            l=get_text_length(can3, "...", "FreeMono", 13)
            txt=_text_(can2,"Delete Song : "+file.split("/")[-1],"FreeMono",13,int(conf_del["width"])-20-l)+"..."

        else:
            txt="Delete Song : "+file.split("/")[-1]

        conf_del.create_text(10,(int(conf_del["height"])-35)/2,text=txt,
            fill=_theme[0],font=("FreeMono",13),anchor="w")









    #video

    if con=="video":


        if get_text_length(can3, "Delete Video : "+file.split("/")[-1], "FreeMono", 13)>int(conf_del["width"])-20:

            l=get_text_length(can3, "...", "FreeMono", 13)
            txt=_text_(can2,"Delete Video : "+file.split("/")[-1],"FreeMono",13,int(conf_del["width"])-20-l)+"..."

        else:
            txt="Delete Video : "+file.split("/")[-1]


        conf_del.create_text(10,(int(conf_del["height"])-35)/2,text=txt,
            fill=_theme[0],font=("FreeMono",13),anchor="w")



    #playlist

    if con=="playlist":



        if get_text_length(can3, "Delete Playlist : "+file, "FreeMono", 13)>int(conf_del["width"])-20:

            l=get_text_length(can3, "...", "FreeMono", 13)
            txt=_text_(can2,"Delete Playlist : "+file,"FreeMono",13,int(conf_del["width"])-20-l)+"..."

        else:
            txt="Delete Playlist : "+file


        conf_del.create_text(10,(int(conf_del["height"])-35)/2,text=txt,
            fill=_theme[0],font=("FreeMono",13),anchor="w")


    #lyrics


    if con=="lyrics":




        if get_text_length(can3, "Delete Lyrics : "+file, "FreeMono", 13)>int(conf_del["width"])-20:

            l=get_text_length(can3, "...", "FreeMono", 13)
            txt=_text_(can2,"Delete Lyrics : "+file,"FreeMono",13,int(conf_del["width"])-20-l)+"..."

        else:
            txt="Delete Lyrics : "+file


        conf_del.create_text(10,(int(conf_del["height"])-35)/2,text=txt,
            fill=_theme[0],font=("FreeMono",13),anchor="w")


conf_del=tk.Canvas(width=600,height=150,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")

conf_del.bind("<Button-1>",conf_del_b1)

cs_txt=0
def can_search_kp(e):
    global search_var
    global can_search
    global cs_txt

    search_var+=e.char


    can_search.delete(cs_txt)

    if get_text_length(can_search, search_var, "FreeMono", 13)>int(can_search["width"])-2:

        
        cs_txt=can_search.create_text(int(can_search["width"])-2,14,text=search_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cs_txt=can_search.create_text(0,14,text=search_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")

    main()


cs_i=0
cs_i_st=0
def can_search_insert():
    global cs_i,cs_i_st
    global search_var
    global can_search

    if cs_i_st==1:

        can_search.delete(cs_i)

        cs_i_st=0

    elif cs_i_st==0:

        if get_text_length(can_search, search_var, "FreeMono", 13)>int(can_search["width"])-2:

            
            cs_i=can_search.create_line(int(can_search["width"])-1,2, int(can_search["width"])-1,26,
                fill=_theme[0])
        else:
            l=get_text_length(can_search, search_var, "FreeMono", 13)

            cs_i=can_search.create_line(l+1,2, l+1,26,
                fill=_theme[0])

        cs_i_st=1

    root.after(250,can_search_insert)

def can_search_b1(e):
    global can_search

    can_search.focus_set()

def can_search_bs(e):
    global search_var
    global can_search
    global cs_txt



    search_var=search_var[:-1]


    can_search.delete(cs_txt)

    if get_text_length(can_search, search_var, "FreeMono", 13)>int(can_search["width"])-2:

        
        cs_txt=can_search.create_text(int(can_search["width"])-2,14,text=search_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cs_txt=can_search.create_text(0,14,text=search_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")

    main()

def can_search_r(e):
    pass



can_search=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can_search.bind("<Button-1>",can_search_b1)
can_search.bind("<Return>",can_search_r)
can_search.bind("<BackSpace>",can_search_bs)

can_search.bind("<KeyPress>",can_search_kp)



can_search_insert()


cnpl_txt=0

npl_var=""
def can_npl_kp(e):
    global npl_var
    global can_npl
    global cnpl_txt



    npl_var+=e.char


    can_npl.delete(cnpl_txt)

    if get_text_length(can_npl, npl_var, "FreeMono", 13)>int(can_npl["width"])-2:

        
        cnpl_txt=can_npl.create_text(int(can_npl["width"])-2,14,text=npl_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cnpl_txt=can_npl.create_text(0,14,text=npl_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")

    main()


cnpl_i=0
cnpl_i_st=0
def can_npl_insert():
    global cnpl_i,cnpl_i_st
    global npl_var
    global can_npl

    if cnpl_i_st==1:

        can_npl.delete(cnpl_i)

        cnpl_i_st=0

    elif cnpl_i_st==0:

        if get_text_length(can_npl, npl_var, "FreeMono", 13)>int(can_npl["width"])-2:

            
            cnpl_i=can_npl.create_line(int(can_npl["width"])-1,2, int(can_npl["width"])-1,26,
                fill=_theme[0])
        else:
            l=get_text_length(can_npl, npl_var, "FreeMono", 13)

            cnpl_i=can_npl.create_line(l+1,2, l+1,26,
                fill=_theme[0])

        cnpl_i_st=1

    root.after(250,can_npl_insert)

def can_npl_b1(e):
    global can_npl

    can_npl.focus_set()

def can_npl_bs(e):
    global npl_var
    global can_npl
    global cnpl_txt



    npl_var=npl_var[:-1]


    can_npl.delete(cnpl_txt)

    if get_text_length(can_npl, npl_var, "FreeMono", 13)>int(can_npl["width"])-2:

        
        cnpl_txt=can_npl.create_text(int(can_npl["width"])-2,14,text=npl_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cnpl_txt=can_npl.create_text(0,14,text=npl_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")

    main()
def can_npl_r(e):
    pass

can_npl=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can_npl.bind("<Button-1>",can_npl_b1)
can_npl.bind("<Return>",can_npl_r)
can_npl.bind("<BackSpace>",can_npl_bs)

can_npl.bind("<KeyPress>",can_npl_kp)



can_npl_insert()














cte_txt=0

te_var=""
def can_theme_ent_kp(e):
    global te_var
    global can_theme_ent
    global cte_txt



    te_var+=e.char


    can_theme_ent.delete(cte_txt)

    if get_text_length(can_theme_ent, te_var, "FreeMono", 13)>int(can_theme_ent["width"])-2:

        try:
            cte_txt=can_theme_ent.create_text(int(can_theme_ent["width"])-2,10,text=te_var,fill=te_var,
                font=("FreeMono",13),anchor="e")
        except:
            cte_txt=can_theme_ent.create_text(int(can_theme_ent["width"])-2,10,text=te_var,fill=_theme[0],
                font=("FreeMono",13),anchor="e")
    else:

        try:
            cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=te_var,
                font=("FreeMono",13),anchor="w")

        except:
            cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=_theme[0],
                font=("FreeMono",13),anchor="w")



cte_i=0
cte_i_st=0
def can_theme_ent_insert():
    global cte_i,cte_i_st
    global te_var
    global can_theme_ent
    global sel_col
    global focus__

    if focus__==1:

        if cte_i_st==1:

            can_theme_ent.delete(cte_i)

            cte_i_st=0

        elif cte_i_st==0:

            if get_text_length(can_theme_ent, te_var, "FreeMono", 13)>int(can_theme_ent["width"])-2:

                try:
                    cte_i=can_theme_ent.create_line(int(can_theme_ent["width"])-1,2, int(can_theme_ent["width"])-1,26,
                        fill=sel_col)
                except:
                    cte_i=can_theme_ent.create_line(int(can_theme_ent["width"])-1,2, int(can_theme_ent["width"])-1,26,
                        fill=_theme[0])
            else:
                l=get_text_length(can_theme_ent, te_var, "FreeMono", 13)

                try:

                    cte_i=can_theme_ent.create_line(l+1,2, l+1,26,
                        fill=sel_col)

                except:
                    cte_i=can_theme_ent.create_line(l+1,2, l+1,26,
                        fill=_theme[0])

            cte_i_st=1
    else:
        can_theme_ent.delete(cte_i)

    root.after(250,can_theme_ent_insert)

def can_theme_ent_b1(e):
    global can_theme_ent
    global focus__


    focus__=1

    can_theme_ent.focus_set()

def can_theme_ent_bs(e):
    global te_var
    global can_theme_ent
    global cte_txt



    te_var=te_var[:-1]


    can_theme_ent.delete(cte_txt)

    if get_text_length(can_theme_ent, te_var, "FreeMono", 13)>int(can_theme_ent["width"])-2:

        
        cte_txt=can_theme_ent.create_text(int(can_theme_ent["width"])-2,10,text=te_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cte_txt=can_theme_ent.create_text(0,10,text=te_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")


def can_theme_ent_r(e):
    pass

can_theme_ent=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can_theme_ent.bind("<Button-1>",can_theme_ent_b1)
can_theme_ent.bind("<Return>",can_theme_ent_r)
can_theme_ent.bind("<BackSpace>",can_theme_ent_bs)

can_theme_ent.bind("<KeyPress>",can_theme_ent_kp)



can_theme_ent_insert()
















cop_txt=0

op_var=""
def can_sel_op_kp(e):
    global op_var
    global can_sel_op
    global cop_txt



    op_var+=e.char


    can_sel_op.delete(cop_txt)

    if get_text_length(can_sel_op, op_var, "FreeMono", 13)>int(can_sel_op["width"])-2:

        cop_txt=can_sel_op.create_text(int(can_sel_op["width"])-2,10,text=op_var,fill=_theme[0],
                font=("FreeMono",13),anchor="e")
    else:

        cop_txt=can_sel_op.create_text(0,10,text=op_var,fill=_theme[0],
                font=("FreeMono",13),anchor="w")



cop_i=0
cop_i_st=0
def can_sel_op_insert():
    global cop_i,cop_i_st
    global op_var
    global can_sel_op
    global sel_col
    global focus__


    if focus__==2:


        if cop_i_st==1:

            can_sel_op.delete(cop_i)

            cop_i_st=0

        elif cop_i_st==0:

            if get_text_length(can_sel_op, op_var, "FreeMono", 13)>int(can_sel_op["width"])-2:

                cop_i=can_sel_op.create_line(int(can_sel_op["width"])-1,2, int(can_sel_op["width"])-1,26,
                        fill=_theme[0])
            else:
                l=get_text_length(can_sel_op, op_var, "FreeMono", 13)

                cop_i=can_sel_op.create_line(l+1,2, l+1,26,
                        fill=_theme[0])

            cop_i_st=1
    else:
        can_sel_op.delete(cop_i)


    root.after(250,can_sel_op_insert)

def can_sel_op_b1(e):
    global can_sel_op
    global focus__

    focus__=2

    can_sel_op.focus_set()

def can_sel_op_bs(e):
    global op_var
    global can_sel_op
    global cop_txt



    op_var=op_var[:-1]


    can_sel_op.delete(cop_txt)

    if get_text_length(can_sel_op, op_var, "FreeMono", 13)>int(can_sel_op["width"])-2:

        
        cop_txt=can_sel_op.create_text(int(can_sel_op["width"])-2,10,text=op_var,fill=_theme[0],
            font=("FreeMono",13),anchor="e")
    else:
        cop_txt=can_sel_op.create_text(0,10,text=op_var,fill=_theme[0],
            font=("FreeMono",13),anchor="w")

def can_sel_op_r(e):
    pass


can_sel_op=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="none")
can_sel_op.bind("<Button-1>",can_sel_op_b1)
can_sel_op.bind("<Return>",can_sel_op_r)
can_sel_op.bind("<BackSpace>",can_sel_op_bs)

can_sel_op.bind("<KeyPress>",can_sel_op_kp)



can_sel_op_insert()





adjust_theme()





main()


timer()

#search__()
check_volume()

mvar_()


check_pl()



draw_wave()


try:

    update_song_status()

except:
    pass

pygame.mixer.init()
try:
    if not current_playing=="":
        tm=0
        tts=0
        mvar=0
        play_music("music/"+current_playing,tm,1)
        get_audio_duration("music/"+current_playing)

        play_st=0
        pygame.mixer.quit()
        main()
        prog()
except:
    pass


move_to_playing(1)
if playlist_st==0:
    pass#can2["scrollregion"]=(0,0,w-7,((h-121)-80-10))


default_font = tk.Label(root, text="Sample Text").cget("font")


load_()
update_bg_pos()


check_sound_device()

update_sb()
update_sb2()

check_cur_pos()
move_bg()
draw_cur()

#draw_sel_theme()







#update()
check_up_theme()
play_vid()
vid_timer()
check_theme_attr()

root.mainloop()
