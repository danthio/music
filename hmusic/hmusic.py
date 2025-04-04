
#pyinstaller --noconfirm --onefile --windowed --icon C:\Users\admin\Desktop\my projects\hmusic\data\icon.ico C:\Users\admin\Desktop\my projects\hmusic\hmusic.py --distpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh\application --workpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh\build --specpath C:\Users\admin\AppData\Local\Temp\tmppm9ol7uh


import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
import pygame
import subprocess
from mutagen.mp3 import MP3
from PIL import Image,ImageTk,ImageGrab
import os
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
import cv2

import ctypes
from ctypes import wintypes

import threading
import pyautogui


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


"""


im=Image.open("data/nomusic.png")
im=im.resize((300,300))
im.save("data/nomusic.png")


"""

"""
    im=Image.open("data/"+c+"/note.png")

    x,y=im.size

    nh=x*(680)/int(680*1.618)

    yy=int((y-nh)/2)

    print(yy)


    im=im.crop((0,yy,x,y-yy))

    im=im.resize((int(680*1.618),(680)))

    im.save("data/"+c+"/note.png")"""








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



"""

directory_path = Path("videos")

if directory_path.is_dir():
    pass
else:
    os.makedirs("videos", exist_ok=True)
"""


def minimize_window():
    root.iconify()

def close_window():
    root.destroy()


vid_im=0
vid_im_=0
vid_bg=0



vid_im2=0

cap = None
paused = False
vid_canvas = None

def initialize_ui(root, video_path):
    """Set up the Tkinter UI components."""
    global vid_canvas,can



    # Label for displaying the video

    vid_canvas["width"]=w-20
    vid_canvas["height"]=(h-121)-50

    vid_canvas.place(in_=root,x=10,y=50)

fps=30
def play_video(video_path, start_time=0):
    """Play the video from the specified start time."""
    global cap, paused,fps

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: File not found at {video_path}")
        return

    # Release previous capture if already open
    if cap is not None and cap.isOpened():
        cap.release()

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file: {video_path}")
        return

    # Validate and set the start time
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_duration = video_length / fps * 1000  # Convert to milliseconds


    cap.set(cv2.CAP_PROP_POS_MSEC, start_time)
    paused = False

imgtk=None
def update_frame():
    """Update the video frame in the Tkinter window."""
    global cap, paused, vid_canvas, w,h,play_video_st,play_st
    global sort_st,can_sort,imgtk
    global fps


    if play_video_st==1 and play_st==1:

        try:

            if cap is not None and cap.isOpened() and not paused:
                ret, frame = cap.read()
                if ret:
                    # Resize the frame to the specified width and height
                    frame = cv2.resize(frame, (w-20, (h-121)-50))

                    # Convert the frame to RGB for Tkinter compatibility
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)

                    # Update the label with the current frame
                    #vid_canvas.imgtk = imgtk
                    #vid_canvas.configure(image=imgtk)

                    vid_canvas.delete("all")

                    vid_canvas.create_image(0,0, image=imgtk,anchor="nw")

                    r=20
                    cx,cy=r,r
                    a_=270

                    ar=[]

                    for a in range(90):

                        x=r*math.sin(math.radians(a_))+cx
                        y=r*math.cos(math.radians(a_))+cy

                        a_-=1

                        ar.append(x)
                        ar.append(y)

                    ar.append(0)
                    ar.append(0)

                    vid_canvas.create_polygon(ar,fill="#000000",outline="#000000")



                    cx,cy=int(vid_canvas["width"])-r,r
                    a_=180

                    ar=[]

                    for a in range(90):

                        x=r*math.sin(math.radians(a_))+cx
                        y=r*math.cos(math.radians(a_))+cy

                        a_-=1

                        ar.append(x)
                        ar.append(y)

                    ar.append(int(vid_canvas["width"]))
                    ar.append(0)

                    vid_canvas.create_polygon(ar,fill="#000000",outline="#000000")









                    cx,cy=int(vid_canvas["width"])-r,int(vid_canvas["height"])-r
                    a_=90

                    ar=[]

                    for a in range(90):

                        x=r*math.sin(math.radians(a_))+cx
                        y=r*math.cos(math.radians(a_))+cy

                        a_-=1

                        ar.append(x)
                        ar.append(y)

                    ar.append(int(vid_canvas["width"]))
                    ar.append(int(vid_canvas["height"]))

                    vid_canvas.create_polygon(ar,fill="#000000",outline="#000000")







                    cx,cy=r,int(vid_canvas["height"])-r
                    a_=0

                    ar=[]

                    for a in range(90):

                        x=r*math.sin(math.radians(a_))+cx
                        y=r*math.cos(math.radians(a_))+cy

                        a_-=1

                        ar.append(x)
                        ar.append(y)

                    ar.append(0)
                    ar.append(int(vid_canvas["height"]))

                    vid_canvas.create_polygon(ar,fill="#000000",outline="#000000")




                    if sort_st==1:
                        can_sort.place(in_=root,x=10+30+20+30,y=h-20-30-15+5+10-160)

                else:
                    cap=None
     
        except:
            pass

    # Schedule the next frame update

    #delay = int(1000 / fps)
    root.after(15, update_frame)



paused=False
def play_vid(time_=0):
    
    global lst,frame,vid_canvas,cap,play_video_st,play_st


    if play_video_st==1 and play_st==1:


        lst=0
        main()
        frame.place_forget()



        # Example usage:
        video_path = "videos/"+current_playing[:-3]+"mp4"  # Replace with your video file path
        time_in_seconds = time_  # Time in seconds where you want to capture the frame
        output_image_path = "data/vid_im.png"  # Output image file path

        get_frame_at_time(video_path, time_in_seconds, output_image_path)


        



        im=Image.open("data/vid_im.png")
        x,y=im.size

        if x/y>w/494:

            nx=w
            ny=nx*y/x


            im=im.resize((int(nx),int(ny)))

        elif x/y<w/494:

            ny=494
            nx=ny*x/y

            im=im.resize((int(nx),int(ny)))

        elif x/y==w/494:

            nx=w
            ny=494


            im=im.resize((int(nx),int(ny)))

        im.save("data/vid_im.png")



        im=Image.open("data/vid_im.png")
        x,y=im.size

        y_=(494-y)/2


        paused=False

        cap = None

        initialize_ui(root, "videos/"+current_playing[:-3]+"mp4")
        play_video("videos/"+current_playing[:-3]+"mp4",time_*1000)





def get_frame_at_time(video_path, time_in_seconds, output_image_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Get the frames per second (FPS) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate the frame number at the given time
    frame_number = int(fps * time_in_seconds)
    
    # Set the video capture to the specific frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    # Read the frame at the specified time
    ret, frame = cap.read()
    
    if ret:
        # Save the frame as an image file
        cv2.imwrite(output_image_path, frame)
    
    # Release the video capture object
    cap.release()



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



    col1="#00ffff"
    col2="#005555"





    xv=2
    amp=150

    if play_st==1:



        can.delete(sig_)

        if play_video_st==0:

            try:






                amplitude = get_amplitude_at_time("waves/"+current_playing[:-3]+"wav", get_playback_time()+tts)





                sig.append(-amplitude*amp)


                xn=int((w-20)/xv)


                if len(sig)>=xn:
                    sig.pop(0)




                sig2=[]
                x=10
                for a in sig:

                    sig2.append(x)
                    sig2.append(a+50+((h-121)-50)/2)

                    x+=xv




                try:

                    if lst==0 and st!=4 and lyric_st==0 and root_st==0:

                        if not tts>tot_tm_:
                            sig_=can.create_line(sig2,fill=col1)
                except:
                    pass












            except:
                pass

    root.after(2,draw_wave)





def gen_wave():
    global lst,can,st,sig,sig_,sig2,tm,tts,play_st,current_playing,w,h









    amp=150
    xv=1


    if play_st==1:






        try:

            

            amplitude = get_amplitude_at_time("waves/"+current_playing[:-3]+"wav", get_playback_time())





            sig.append(-amplitude*amp)


            xn=int((w-20)/xv)


            if len(sig)>=xn:
                sig.pop(0)




        except:
            pass


    #root.after(1,gen_wave)

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
        
        # Set the read position to the desi#00ffff frame
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



def convert_folder_to_audio():

    global can,load,load2,load3,load4,w,h
    global input_folder,convert,st




    col1="#00ffff"
    col2="#005555"



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
                    root.after(0,dummy)


                except:
                    root.after(0,dummy)
                    






        except:
            pass

        convert=0
        update_waves()





def convert_file_to_audio():

    global can,load,load2,load3,load4,w,h
    global convert,input_file,st



    col1="#00ffff"
    col2="#005555"



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

                    root.after(0,dummy)
                    

                except:
                    root.after(0,dummy)
                    


        except:
            pass


        convert=0
        update_waves()



def dummy():
    pass


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


    try:

        with open("data/save.json", "r") as file:
            data = json.load(file)


    except:
        data={"save":[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status]}




    data["save"]=[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status]




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
    global w



    global select_st
    global current_playing
    global circle9,circle5



    if not select_st==1:


        if not tot_tm_==0:

            if not current_playing=="":


                col1="#00ffff"
                col2="#005555"




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

                ctime=can.create_text(10,h-20-60-20+20+10+5-3+5-2,text=tt,font=("TkDefaultFont",11),fill=col1,anchor="w")


                can.delete(prog1)
                can.delete(prog2)
                can.delete(prog3)

                x_=tm*(w-20)/tot_tm_

                prog1=can.create_line(10,h-20-60-20+10+2+5-3+10, x_+10,h-20-60-20+10+2+5-3+10,fill=col1,width=2)

                #prog2=can.create_image(x_+10-3,h-20-60-20+10+2+5-3-3+10,image=circle5,anchor="nw")
                #prog3=can.create_image(x_+10-2,h-20-60-20+10+2+5-3-2+10,image=circle9,anchor="nw")


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
                vid_canvas.place_forget()

                if loop==0:
                    mvar+=1
                add_st=0
                frame2.place_forget()
                can2.focus_set()


                if mvar+1>len(_songs_):
                    mvar=0

                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))


                tm=0
                
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

    root.after(4,timer)


def can3_b1(e):
    global sel_playlist,can3,frame2,add_st,current_playing,current_playlist,playlist,songs,mvar,tm
    global st,songs_status,_songs_


    #add_st=0
    #frame2.place_forget()

    for p in sel_playlist:

        if p[2]<=can3.canvasy(e.y)<=p[2]+50:

            if not current_playing=="":
                create_playlist(p[0],1,p[1])
                main()


                if current_playing==p[1]:

                    if not songs_status[1]=="":

                        try:
                            v=playlist[songs_status[1]].index(current_playing)
                        except:




                            cp=p[1]


                            

                            if len(_songs_)-1==mvar:
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






                            
                            songs_status[-1]=current_playing



                            ar=[]
                            for s in range(len(_songs_)):

                                if cp==_songs_[s][0]:

                                    if p[1]==_songs_[s][0]:
                                        ar.append(s)

                            for p in ar:
                                _songs_.pop(p)




                            if len(_songs_)==0:
                                current_playing=""


                move_to_playing()


            #add_st=0
            #frame2.place_forget()

            add_playlist()
            can2.focus_set()

            main()


song_add_pl=0
def add_playlist():
    global can4,can3,can5,can6
    global sel_playlist,playlist,playlist2,checked
    global songs
    global song_add_pl




    col1="#00ffff"
    col2="#005555"



    can4.delete("all")
    can3.delete("all")
    can5.delete("all")
    can6.delete("all")


    can4.create_text(450/2,20,text="Playlists",font=("TkDefaultFont",12),fill=col1)
    can4.create_line(2,38,450-2,38,fill=col2)

    draw_round_rec(can4,2,2 ,450-2,80,15,col1,"",1)

    draw_round_rec(can6,2,-15 ,450-2,15,15,col1,"",1)






    can3.delete("all")

    y=0
    
    sel_playlist=[]

    for p in playlist:

        ar=playlist[p]

        can3.create_image(10,y+10+4,image=playlist2,anchor="nw")
        can3.create_text(10+30+10,y+25,text=p,font=("TkDefaultFont",12),anchor="w",fill=col1)
        #can3.create_line(0,y+50,450-7,y+50,fill="#000000")

        try:
            v=ar.index(song_add_pl)



            can3.create_image(450-7-10-20,y+15, image=checked,anchor="nw")
            
        except:
            pass




        sel_playlist.append([p,song_add_pl,y])
        pl_var=[p,song_add_pl,y]



        y+=50



    if y<250-40:


        can3.create_line(2,0, 2,250-40,fill=col1)
        can5.create_line(0,0, 0,250-40,fill=col1)
    else:

        can3.create_line(2,0, 2,y,fill=col1)
        can5.create_line(0,0, 0,y,fill=col1)


    if len(playlist)==0:
        can3.create_text(10+30+10,(250-40)/2,text="No record",font=("TkDefaultFont",12),anchor="w")



    if y<=int(can3["height"]):

        can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))
    else:
        can3["scrollregion"]=(0,0,int(can3["width"]),y)



def can2_b1(e):
    global current_playing,songs,play_st
    global pp
    global start_time
    global tot_tm
    global tm
    global mvar
    global can2
    global st,npl,playlist_st,_playlist,current_playlist,playlist
    global search,_search,frame
    global add_st,frame2,can3,can4,can5,can6
    global sel_playlist
    global _npl,npl
    global can_sort
    global shuffle_st,shuff,sort_val,sort_ar

    global playlist_select,select_st
    global songs2

    global songs_status
    global loop
    global lyric_st
    global song_add_pl
    global _songs__





    if select_st==1:


        for a in range(len(songs2)):


            if songs2[a][-1]<=can2.canvasy(e.y)<=songs2[a][-1]+50:

                create_playlist(playlist_select,1,songs2[a][0])


                main()



                if current_playing==songs2[a][0]:

                    if not songs_status[1]=="":

                        try:
                            v=playlist[songs_status[1]].index(current_playing)
                        except:




                            cp=songs2[a][0]


                            

                            if len(_songs_)-1==mvar:
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






                            
                            songs_status[-1]=current_playing



                            ar=[]
                            for s in range(len(_songs_)):

                                if cp==_songs_[s][0]:

                                    if songs2[a][0]==_songs_[s][0]:
                                        ar.append(s)

                            for p in ar:
                                _songs_.pop(p)




                            if len(_songs_)==0:
                                current_playing=""

                main()

                move_to_playing()


                            












        return




    _search=0
    _npl=0

    #search.delete(0,tk.END)

    #search.place_forget()
    npl.place_forget()

    main()   



    can_sort.place_forget()

    frame2.place_forget()





    if st==2 and playlist_st==0:


        cx,cy=int(can2["width"])-10-5-20+10,5+10

        if cx-10<=e.x<=cx+10:
            if cy-10<=e.y<=cy+10:

            
                _npl=0
                npl.delete(0,tk.END)
                npl.place_forget()

                main()
                return



        if 10<=e.x<=int(can2["width"])-10:
            if 5<=e.y<=35:

                can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
                npl.delete(0,tk.END)
                _npl=1
                npl.place(in_=root,x=10+15+10,y=90+15-5-1-1)
                npl.focus_set()
                main()

                return

        # create new playlist


        cx,cy=int(can2["width"])/2-100,45+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            if not npl.get()=="":
                create_playlist(npl.get(),0)
                npl.delete(0,tk.END)
                npl.place_forget()
                _npl=0

                main()
            return


        cx,cy=int(can2["width"])/2+100,45+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            if not npl.get()=="":
                create_playlist(npl.get(),0)
                npl.delete(0,tk.END)
                _npl=0
                npl.place_forget()
                main()

            return


        if int(can2["width"])/2-100<=e.x<=int(can2["width"])/2+100:
            if 45<=e.y<=45+30:

                if not npl.get()=="":
                    create_playlist(npl.get(),0)
                    _npl=0
                    npl.delete(0,tk.END)
                    npl.place_forget()
                    main()
                return


        for _pl in _playlist:

            
            cx,cy=int(can2["width"])-10-25-15-25+12.5,_pl[1]+12.5+12.5
            r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
            if r<=12.5:

                playlist_select=_pl[0]
                select_st=1

                can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

                main()

                return






            cx,cy=int(can2["width"])-10-25+12.5,_pl[1]+12.5+12.5
            if cx-12.5<=e.x<=cx+12.5:
                if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

                    if st==songs_status[0]:
                        if st==2:
                            if current_playlist==songs_status[1]:

                                try:
                                    play_music("music/"+current_playing,tm,1)
                                    pygame.mixer.quit()
                                except:
                                    pass


                                current_playing=""
                                current_playlist=""

                                update_song_status()


                    create_playlist(_pl[0],con=3)



                    main()

                    if st==songs_status[0]:
                        if st==2:
                            if current_playlist==songs_status[1]:
                                update_song_status()



                    return


            if _pl[1]<=can2.canvasy(e.y)<=_pl[1]+50:
                can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

                
                current_playlist=_pl[0]
                playlist_st=1

                shuffle_st=0
                sort_val=sort_ar[0][0]






                main()


                search.delete(0,tk.END)
                search.place_forget()
                frame.place_forget()



                main()
                return




        return




    #favourite

    for s in songs:


        y=s[-1]

        cx,cy=int(can2["width"])-10-25-15-25-15-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                update_details(s[0],0)
                


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

        cx,cy=int(can2["width"])-10-25-15-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:

                if add_st==0:
                    add_st=1
                elif add_st==1:
                    add_st=0


                if add_st==1:



                    song_add_pl=s[0]

                    can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

                    add_playlist()

                    frame2.place(in_=root,x=(w-450)/2,y=(h-(40+250-40+10))/2)

                    #can3.focus_set()

                    main()

                return

    """
    #add video


    for s in songs:
        y=s[1]
    
        cx,cy=int(can2["width"])-10-25-15-25+12.5,y+12.5+12.5
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

    #delete file


    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=int(can2["width"])-10-25+12.5,y+12.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=can2.canvasy(e.y)<=cy+12.5:


                try:
                    if play_st==0:


                        if current_playing==s[0]:



                            if len(_songs_)==1:
                                mvar=0
                            elif mvar==len(_songs_)-1:
                                mvar=0
                            else:
                                mvar=mvar+1


                            current_playing=_songs_[mvar][0]

                            tm=0

                            play_music("music/"+current_playing,tm,1)
                            pygame.mixer.quit()





                            if len(_songs_)==1:
                                current_playing=""
                            
                            songs_status[-1]=current_playing







                        os.remove("music/"+s[0])
                        del_wave()
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

                        move_to_playing()


                    return

                except:
                    pass

                main()
                return




    #play song
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

            loop=0

            songs_status[-2]=0

            lyric_st=0



            main()

            if not st==2:
                current_playlist=""

            

            

            update_song_status()

            main()


            move_to_playing()

            return



def move_to_playing(con_=0):
    global current_playing,can2
    global songs,_songs_
    global select_st
    global playlist_st,can2

    global st,current_playlist,songs_status


    try:

        if select_st==1:
            return

        if playlist_st==0:
            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            main()
            return

        if not current_playing=="":


            if st==songs_status[0]:

                if st==2:
                    if current_playlist==songs_status[1]:
                        con=1

                else:
                    con=1


            if con==1:


                for s in _songs_:

                    if s[0]==current_playing:


                        t=len(_songs_)*50


                        v=s[1]

                        if con_==0:

                            if can2.canvasy(0)<=v<=can2.canvasy(0)+int(can2["height"])-50:
                                main()
                                return

                        if s[1]+int(can2["height"])/2-25<t:
                            v=s[1]-(int(can2["height"])/2-25)

                        pixel_value = int(v)
                        scroll_region = can2.bbox("all")  # Get the bounding box of all content
                        if scroll_region:
                            total_height = scroll_region[3] - scroll_region[1]  # Scrollable height
                            fraction = pixel_value / total_height if total_height > 0 else 0
                            can2.yview_moveto(fraction)
                            main()
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

    #get_pixel_color(e.x, e.y)

    #capture_canvas()
    move_to_playing()


convert=0
input_file=""
input_folder=""
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






    if select_st==1:

        

        cx,cy=w-10-25+12.5,(h-121+75)+((h-1)-(h-121+75)-25)/2+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:
                select_st=0

                main()
                return


    if root_st==1:



        root_st=0


        root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))

        main()

        move_to_playing()

        return



    _search=0
    _npl=0

    search.delete(0,tk.END)
    search.place_forget()
    npl.place_forget()

    main()   





    col1="#00ffff"
    col2="#005555"









    can_sort.place_forget()
    main()




    add_st=0
    frame2.place_forget()

    xv=w/6




    if xv-60<=e.x<=xv+60:
        if 50/2-15<=e.y<=50/2+15:

            lyric_st=0

            select_st=0

            play_video_st=0
            vid_canvas.place_forget()

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))
            
            lst=1
            current_playlist=""

            add_st=0
            frame2.place_forget()

            can2.focus_set()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()



            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass                
            


            st=0
            main()


            
            return


    if xv*2-60<=e.x<=xv*2+60:
        if 50/2-15<=e.y<=50/2+15:

            lyric_st=0

            select_st=0




            play_video_st=0
            vid_canvas.place_forget()

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()


            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()


            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))

            
            lst=1
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()
            


            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass   


            st=1
            main()




            return

    if xv*3-60<=e.x<=xv*3+60:
        if 50/2-15<=e.y<=50/2+15:

            lyric_st=0

            select_st=0


            play_video_st=0
            vid_canvas.place_forget()

            lst=1
            main()

            _search=0
            sort_st=0
            can_sort.place_forget()


            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

            main()


            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))

            
            playlist_st=0
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()

            




            main()


            if st==2:
                pl_st=1

            else:
                pl_st=0


            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass   
                

            st=2

            main()

            return


    if xv*4-60<=e.x<=xv*4+60:
        if 50/2-15<=e.y<=50/2+15:

            lyric_st=0

            select_st=0



            play_video_st=0
            vid_canvas.place_forget()


            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()




            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))

            
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()

            if st==4:

                try:

                    current_playing=songs_status[-1]
                    current_playlist=songs_status[1]

                    get_audio_duration("music/"+current_playing)
                except:
                    pass   

            st=3
            main()




            return


    if xv*5-60<=e.x<=xv*5+60:
        if 50/2-15<=e.y<=50/2+15:

            lyric_st=0




            st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing=songs_status

            if st==2:
                if current_playlist!="":
                    playlist_st=1

            main()

            move_to_playing(1)


            select_st=0



            play_video_st=0
            vid_canvas.place_forget()


            lst=1
            _search=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
            main()


            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))

            st=4
            main()
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()




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



                if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
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

                vid_canvas.place_forget()



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



                if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
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


                vid_canvas.place_forget()

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
                    can_lyrics.place_forget()

                    play_video_st=0
                    cap=None
                    vid_canvas.place_forget()

                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

                elif lst==1:

                    if st==2 and playlist_st==0:
                        pass
                    else:
                        lst=0
                        _search=0

                        frame.place_forget()

                main()

                if st==songs_status[0]:

                    if st==2:
                        if current_playlist==songs_status[1]:
                            move_to_playing()

                    else:
                        move_to_playing()



        #volume
        if w-10-100-10<=e.x<=w-10+10:
            if h-20-30+5-10+10-3<=e.y<=h-20-30+5+10+10-3:

                if e.x<w-10-100:
                    current_volume=0
                    volume.SetMasterVolumeLevelScalar(current_volume, None)
                elif e.x>w-10:
                    current_volume=1
                    volume.SetMasterVolumeLevelScalar(current_volume, None)
                elif w-10-100<=e.x<=w-10:

                    x=e.x-(w-10-100)

                    r=100

                    current_volume=x/r





                    volume.SetMasterVolumeLevelScalar(current_volume, None)



                main()


        #sort

        cx,cy=10+25+15+12.5,h-20-30-15+5+12.5+10-3+2.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:


                if sort_st==0:
                    sort_st=1
                elif sort_st==1:
                    sort_st=0




                if sort_st==1:

                    if sort_val=="":
                        sort_val=sort_ar[0][0]



                    col1="#00ffff"
                    col2="#005555"






                    can_sort.delete("all")

                    draw_round_rec(can_sort,2,2, 250-2,160-2,15,"#000000",col1,0)

                    can_sort.create_text(125,15,text="Sort",font=("TkDefaultFont",12),fill=col1)


                    can_sort.create_line(3,30, 250-2,30,fill=col2 )
                    y=30
                    for _ in sa:

                        can_sort.create_text(10,y+15,text=_,font=("TkDefaultFont",12),fill=col1,anchor="w")

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

                return



        #shuffle




        cx,cy=10+25+15+25+15+12.5,h-20-30-15+5+12.5+10-3+2.5


        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

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

        #lyrics


        if not st==4:

            x=w/2
            y=h-121+5-30



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


                cx,cy=x+40+10-5+12.5,y+2.5+12.5


                if cx-12.5<=e.x<=cx+12.5:
                    if cy-12.5<=e.y<=cy+12.5:


                        if not current_playing=="":
                            update_details(current_playing,2,_lyric)

                            lvar=0

                            main()
                            prog()




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
                    search.place_forget()
                    npl.place_forget()
                    play_vid(tm)


            elif play_video_st==1:
                cap=None
                play_video_st=0
                vid_canvas.place_forget()
                main()

        """





        


    #search

    cx,cy=w-10-5-20+10,45+10+30

    if cx-10<=e.x<=cx+10:
        if cy-10<=e.y<=cy+10:


            search.delete(0,tk.END)
            search.place_forget()
            can.focus_set()
            _search=0

            main()


            return

    if 10<=e.x<=w-10-5-30:
        if 40+30-10-5<=e.y<=40+30+30-10-5:

            _search=1


            search.place(in_=root,x=10+15,y=45+30-10-5-5)
            search.focus_set()

            main()

            return






    #add songs

    if st==4:

        yv=50+(((h-121)-50)-90)/2+20



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


                
                if con==0 or lst==0:
                    can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))





                lst=1

                

                main()

                move_to_playing()


                return


            except:
                pass



    


vol1,vol2,vol3,vol4=0,0,0,0
def check_volume():
    global current_volume
    global can,vol1,vol2,vol3,vol4

    global circle9,circle5




    col1="#00ffff"
    col2="#005555"


    if volume.GetMasterVolumeLevelScalar()!=current_volume:

        current_volume=volume.GetMasterVolumeLevelScalar()

        can.delete(vol1)
        can.delete(vol2)

        r=(w-10)-(w-10-100)

        vol1=can.create_line(w-10-100,h-20-30+5+10-3 ,w-10-100+current_volume*r,h-20-30+5+10-3,fill=col1,width=2)

        vol2=can.create_text(w-10,h-20-30+5+10-3+12,text=str(int(current_volume*100))+"%",fill=col1,font=("TkDefaultFont",11),anchor="e")

        #vol3=can.create_image(w-10-100+current_volume*r-3,h-20-30+5+10-3-3,image=circle5,anchor="nw")
        #vol4=can.create_image(w-10-100+current_volume*r-2,h-20-30+5+10-3-2,image=circle9,anchor="nw")


    root.after(500,check_volume)






def play_music(file,time,con=0):
    global current_playing
    global sig,tts
    global play_st


    if play_st==1:

        if time==0:


            sig=[]
            tts=0



        # Initialize Pygame Mixer
        pygame.mixer.init()


        # Load the audio file
        pygame.mixer.music.load(file)  # Replace with your audio file path

        if con==0:

            update_details(current_playing,1)

        # Start playing the audio from a specific position (in seconds)
        start_time = time  # Replace with the desi#00ffff starting time in seconds
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
            text=text[-1]


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
def main():

    global can,st,w,h,wd,ht
    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global pp,fv,lst
    global frame,can2
    global current_playing
    global yyy

    global songs
    global search,search_var
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




    col1="#00ffff"
    col2="#007777"
    col3="#002020"



    can["bg"]="#333333"

    can2["bg"]="#000000"


    if root_st==1:

        root.geometry(str(50)+"x"+str(50)+"+"+str(wd-3-50)+"+"+str(ht-51-50))

        can.delete("all")

        can.create_image(0,0, image=circlex, anchor="nw")

        can.create_image(10,10, image=musical_note2, anchor="nw")

        frame.place_forget()
        search.place_forget()
        vid_canvas.place_forget()
        play_video_st=0


        return



    update_details()
    create_playlist()




    if shuff==1 or shuff==2:
        sort_val=""






    style.configure("My.Vertical.TScrollbar", gripcount=0, background=col1,
                    troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                    lightcolor="#000000",relief="flat", darkcolor="#000000",
                    arrowsize=6)


    style2.configure("My.Vertical.TScrollbar2", gripcount=0, background=col1,
                    troughcolor='#000000', borderwidth=0, bordercolor='#000000',
                    lightcolor='#000000',relief="flat", darkcolor='#000000',
                    arrowsize=6)





    frame["width"]=w-20
    frame["height"]=((h-121)-80-10)

    can2["width"]=w-3-20-2+1
    can2["height"]=((h-121)-80-10)


    can["width"]=w
    can["height"]=h







    
    #create_rectangle(can,0, 0, w, h, fill='#000000', alpha=.65)


    






    def sort_data_added(directory: str, descending: bool = True):


        from pathlib import Path
        # Get the list of all files and directories
        items = [Path(directory) / item for item in os.listdir(directory)]

        # Filter only valid paths (ignores broken symbolic links)
        items = [item for item in items if item.exists()]

        # Sort by modification time (or creation time, platform-dependent)
        sorted_items = sorted(items, key=lambda x: x.stat().st_mtime, reverse=descending)

        return sorted_items


    def sort_title(directory: str, descending: bool = False):
        # Get the list of all items in the directory
        items = os.listdir(directory)

        # Sort the items alphabetically (case-insensitive)x
        sorted_items = sorted(items, key=str.lower, reverse=descending)

        return sorted_items     


    can2.delete("all")


    _bg2_=can2.create_image(-10,-(90-1-1)+can2.canvasy(0),image=bg,anchor="nw")
    can2_cur=can2.create_image(-200,-200,image=cur,anchor="nw")
    _bg4_=can2.create_image((w-450)/2-10,50+((h-121-50)-450)/2-(90-1-1)+can2.canvasy(0),image=note,anchor="nw")

    
    


 



            





    if select_st==1:


        y=1

        

        all_songs = os.listdir("music")

        all_songs = sort_data_added("music", descending=True)


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

            """
            if scon==0:

                scon2=1

                for p in playlist:



                    if sval.find(" ")!=-1:

                        s_ar=sval.split(" ")

                        for sv in s_ar:

                            if p.lower().find(sv)==-1:
                                scon2=0
                                break

                        if scon2==0:
                            break
                    else:
                        if p.lower().find(sval)==-1:
                            scon2=0

                    if scon2==0:
                        break


                scon=scon2
            """









            if scon==1:

                can2.create_image(5,y+10,image=musical_note2,anchor="nw")
                col=col1


                can2.create_text(50,y+25,text=_text_(can2,song[:-4],"TkDefaultFont",12,(int(can2["width"])-20-20-20)-50),font=("TkDefaultFont",12),fill=col,anchor="w")
                
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

            can2.create_image((int(can2["width"])-300)/2,(int(can2["height"])-300)/2,image=nomusic,anchor="nw")
            #can2.create_text((w-7)/2,((h-121)-80-10)/2,text="No Record!",font=("TkDefaultFont",12),fill=col1)


            style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                            troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                            lightcolor="#000000",relief="flat", darkcolor="#000000",
                            arrowsize=6)




        if y+1<=int(can2["height"]):

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
        else:
            can2["scrollregion"]=(0,0,int(can2["width"]),y+1)





    else:


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
                all_songs = sort_data_added("music", descending=True)

            elif sort_val=="Date Added (Ascending)":
                all_songs = sort_data_added("music", descending=False)

            elif sort_val=="Title (Descending)":
                all_songs= sort_title("music", descending=True)

            elif sort_val=="Title (Ascending)":
                all_songs= sort_title("music", descending=False)



            ar=[]
            for i in all_songs:
                try:
                
                    ar.append(str(i).split("\\")[1])
                except:
                    ar.append(i)
                    pass




            all_songs=ar

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

                """
                if scon==0:

                    scon2=1

                    for p in playlist:



                        if sval.find(" ")!=-1:

                            s_ar=sval.split(" ")

                            for sv in s_ar:

                                if p.lower().find(sv)==-1:
                                    scon2=0
                                    break

                            if scon2==0:
                                break
                        else:
                            if p.lower().find(sval)==-1:
                                scon2=0

                        if scon2==0:
                            break


                    scon=scon2
                """









                if scon==1:



                    if song==current_playing:

                        can2.create_line(2,y, int(can2["width"]),y,fill="#000000")


                        #can2.create_rectangle(2,y, int(can2["width"]),y+50-1,fill=col1,outline=col1)

                        #draw_round_rec(can2,2,y, int(can2["width"]),y+50,10,col1,col1,0)

                        draw_active(can2,0,y,int(can2["width"])-1,51,col1)
                        can2.create_image(5,y+10,image=musical_note1,anchor="nw")
                        col="#000000"

                        _del_=delete2


                    else:



                        can2.create_image(5,y+10,image=musical_note2,anchor="nw")
                        col="#00ffff"

                        _del_=delete

                    n=music_details[song][1]



                    if n<1000:
                        t=str(n)
                    elif 1000<=n<1000000:


                        t=str(round(n/1000,2))+" K"
                    elif 1000000<=n<1000000000:


                        t=str(round(n/1000000,2))+" M"
                    elif n>=1000000000:


                        t=str(round(n/1000000000,2))+" B"

                    if n==1:
                        vw="View"
                    else:
                        vw="Views"


                    can2.create_text(50,y+50/3,text=_text_(can2,song[:-4],"TkDefaultFont",12,(int(can2["width"])-25*3-15*3-10)-50),font=("TkDefaultFont",12),fill=col,anchor="w")
                    can2.create_text(50,y+50*2.3/3,text=t+" "+vw,font=("TkDefaultFont",10),fill=col2,anchor="w")



                    can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")



                    """

                    if music_details[song][3]==True:

                        if song==current_playing:
                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video3,anchor="nw")
                        else:

                           can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video2,anchor="nw")
                    elif music_details[song][3]==False:

                        can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video1,anchor="nw")

                    """





                    con=0

                    for i in playlist:


                        try:
                            v=playlist[i].index(song)
                            con=1
                        except:
                            pass


                    if con==0:

                        _pl_=playlist1




                    elif con==1:

                        
                        _pl_=playlist2



                        if song==current_playing:
                            _pl_=playlist3
                        


                    can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=_pl_,anchor="nw")




                    if music_details[song][0]==0:

                        _fv_=favourite1


                        if song==current_playing:
                            _fv_=favourite1_


                    elif music_details[song][0]==1:


                        _fv_=favourite2

                        if song==current_playing:
                            _fv_=favourite2_



                    can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")




                    #if not song==current_playing:

                    #    can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col3)

                    ar=[song,y]

                    songs.append(ar)

                    y+=50

            if len(songs)==0:
                



                can2.create_image((int(can2["width"])-300)/2,(int(can2["height"])-300)/2,image=nomusic,anchor="nw")
                

                #can2.create_text(int(can2["width"])/2,((h-121)-80-10)/2,text="No Record!",font=("TkDefaultFont",12),fill=col1)



                style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                                troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                                lightcolor="#000000",relief="flat", darkcolor="#000000",
                                arrowsize=6)


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

                    if music_details[song][0]==1:

                        if song==current_playing:
                            can2.create_line(2,y, int(can2["width"]),y,fill="#000000")

                            #can2.create_rectangle(2,y, int(can2["width"]),y+50-1,fill=col1,outline=col1)
                            #draw_round_rec(can2,2,y, int(can2["width"]),y+50,10,col1,col1,0)

                            draw_active(can2,0,y,int(can2["width"])-1,51,col1)

                            col="#000000"

                            can2.create_image(5,y+10,image=musical_note1,anchor="nw")
                            _del_=delete2
                        else:
                            col=col1
                            can2.create_image(5,y+10,image=musical_note2,anchor="nw")
                            _del_=delete

                        n=music_details[song][1]


                        if n<1000:
                            t=str(n)
                        elif 1000<=n<1000000:


                            t=str(round(n/1000,2))+" K"
                        elif 1000000<=n<1000000000:


                            t=str(round(n/1000000,2))+" M"
                        elif n>=1000000000:


                            t=str(round(n/1000000000,2))+" B"

                        if n==1:
                            vw="View"
                        else:
                            vw="Views"


                        can2.create_text(50,y+50/3,text=_text_(can2,song[:-4],"TkDefaultFont",12,(int(can2["width"])-25*3-15*3-10)-50),font=("TkDefaultFont",12),fill=col,anchor="w")
                        can2.create_text(50,y+50*2.3/3,text=t+" "+vw,font=("TkDefaultFont",10),fill=col2,anchor="w")
                        

                        can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")


                        """


                        if music_details[song][3]==True:

                            if song==current_playing:
                                can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video3,anchor="nw")
                            else:

                               can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video2,anchor="nw")
                        elif music_details[song][3]==False:

                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video1,anchor="nw")

                        """



                        con=0

                        for i in playlist:


                            try:
                                v=playlist[i].index(song)
                                con=1
                            except:
                                pass


                        if con==0:

                            _pl_=playlist1



                        elif con==1:

                            
                            _pl_=playlist2

                            if song==current_playing:
                                _pl_=playlist3
                            


                        can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=_pl_,anchor="nw")




                        if music_details[song][0]==0:

                            _fv_=favourite1


                            if song==current_playing:
                                _fv_=favourite1_


                        elif music_details[song][0]==1:


                            _fv_=favourite2

                            if song==current_playing:
                                _fv_=favourite2_


                        can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")



                        #if not song==current_playing:

                        #    can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col3)





                        ar=[song,y]

                        songs.append(ar)

                        y+=50


            if len(songs)==0:


                can2.create_image((int(can2["width"])-300)/2,(int(can2["height"])-300)/2,image=nomusic,anchor="nw")
                
                #can2.create_text(int(can2["width"])/2,((h-121)-80-10)/2,text="No Record!",font=("TkDefaultFont",12),fill=col1)


                style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                                troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                                lightcolor="#000000",relief="flat", darkcolor="#000000",
                                arrowsize=6)




        elif st==2:




            if playlist_st==0:
                y=0

                if _search==1:

                    can.create_oval(10,40, 10+30,40+30,fill="#000000",outline="#000000")
                    can.create_oval(w-10-30,40, w-10,40+30,fill="#000000",outline="#000000")

                    can.create_rectangle(10+15,40, w-10-15,40+30,fill="#000000",outline="#000000")






                can.create_arc(10,40, 10+30,40+30, style=tk.ARC,start=90,extent=180,outline=col1)
                can.create_arc(w-10-30,40, w-10,40+30, style=tk.ARC,start=270,extent=180,outline=col1)

                can.create_line(10+15,40, w-10-15,40, fill=col1)
                can.create_line(10-1+15,40+30, w-10-15,40+30, fill=col1)



                can.create_text(30+20+5,40+15,text="Search",font=("TkDefaultFont",12),fill=col1,anchor="w")



                can.create_image(w-10-5-20,40+5,image=cancel,anchor="nw")

                can.create_image(30,40+5,image=search_im,anchor="nw")





                #can.create_line(10,70,w-10,70,fill=col1)
                #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill=col1)

                frame.place(in_=root,x=11,y=80-30+40)







                #can2.create_rectangle(0,0, int(can2["width"]),95,fill=col3,outline=col3)





                y=5



                if _npl==1:

                    can2.create_oval(10,y, 10+30,y+30, fill="#000000",outline="#000000")
                    can2.create_oval(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30,fill="#000000",outline="#000000")

                    can2.create_rectangle(10+15,y, int(can2["width"])-10-15,y+30,fill="#000000",outline="#000000")



                can2.create_arc(10,y, 10+30,y+30, style=tk.ARC,start=90,extent=180,outline=col1)
                can2.create_arc(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30, style=tk.ARC,start=270,extent=180,outline=col1)

                can2.create_line(10+15,y, int(can2["width"])-10-15,y, fill=col1)
                can2.create_line(10-1+15,y+30, int(can2["width"])-10-15,y+30, fill=col1)







                can2.create_text(30,y+15,text="New Playlist",font=("TkDefaultFont",12),fill=col1,anchor="w")



                can2.create_image(int(can2["width"])-10-5-20,y+5,image=cancel,anchor="nw")


                y+=40






                #can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30, outline=col1)

                can2.create_image(int(can2["width"])/2-100-15,y,image=circle3,anchor="nw")
                can2.create_image(int(can2["width"])/2+100-15,y,image=circle3,anchor="nw")

                can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30-1,fill=col1,outline=col1)


                can2.create_text(int(can2["width"])/2,y+15,text="Create New Playlist",font=("TkDefaultFont",12),fill="#000000")

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
                        if pl.lower().find(sval)!=-1:
                            scon=1


                    if scon==1:
                        
                        if conx==0:

                            #can2.create_line(2,y, int(can2["width"])-3,y,fill=col3)


                            conx=1




                        if current_playlist==pl:
                            can2.create_line(2,y, int(can2["width"]),y,fill="#000000")

                            #can2.create_rectangle(2,y, int(can2["width"]),y+50-1,fill=col1,outline=col1)
                            #draw_round_rec(can2,2,y, int(can2["width"]),y+50,10,col1,col1,0)

                            draw_active(can2,0,y,int(can2["width"])-1,51,col1)

                            col="#000000"
                            _pl_=playlist3
                            _del_=delete2

                        else:

                            col=col1

                            _pl_=playlist2
                            _del_=delete

                        if current_playlist==pl:

                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add2,anchor="nw")

                        else:

                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add,anchor="nw")

                        can2.create_image(10,y+12.5+2,image=_pl_,anchor="nw")




                        can2.create_text(50,y+25,text=_text_(can2,pl,"TkDefaultFont",12,(int(can2["width"])-25*2-15*2-10)-50),font=("TkDefaultFont",12),fill=col,anchor="w")

                        can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")

                        #if current_playlist!=pl:
                        #    can2.create_line(0,y+50, int(can2["width"]),y+50,fill=col3)

                        _playlist.append([pl,y])



                        y+=50

                if len(_playlist)==0:

                    y_=y-20

                    can2.create_image((int(can2["width"])-300)/2,y_+(int(can2["height"])-300-y_)/2,image=nomusic,anchor="nw")
                    
                    #can2.create_text(int(can2["width"])/2,y+(((h-121)-80-10)-y)/2,text="No Record",font=("TkDefaultFont",12),fill=col1)


                    style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                                    troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                                    lightcolor="#000000",relief="flat", darkcolor="#000000",
                                    arrowsize=6)




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

                        try:
                            v=ar.index(song)

                        
                            if song==current_playing:
                                can2.create_line(2,y, int(can2["width"]),y,fill="#000000")

                                #can2.create_rectangle(2,y, int(can2["width"]),y+50-1,fill=col1,outline=col1)
                                #draw_round_rec(can2,2,y, int(can2["width"]),y+50,10,col1,col1,0)

                                draw_active(can2,0,y,int(can2["width"])-1,51,col1)

                                _del_=delete2

                                can2.create_image(5,y+10,image=musical_note1,anchor="nw")
                                col="#000000"

                            else:



                                can2.create_image(5,y+10,image=musical_note2,anchor="nw")
                                col=col1

                                _del_=delete



                            n=music_details[song][1]


                            if n<1000:
                                t=str(n)
                            elif 1000<=n<1000000:


                                t=str(round(n/1000,2))+" K"
                            elif 1000000<=n<1000000000:


                                t=str(round(n/1000000,2))+" M"
                            elif n>=1000000000:


                                t=str(round(n/1000000000,2))+" B"


                            if n==1:
                                vw="View"
                            else:
                                vw="Views"


                            can2.create_text(50,y+50/3,text=_text_(can2,song[:-4],"TkDefaultFont",12,(int(can2["width"])-25*3-15*3-10)-50),font=("TkDefaultFont",12),fill=col,anchor="w")
                            can2.create_text(50,y+50*2.3/3,text=t+" "+vw,font=("TkDefaultFont",10),fill=col2,anchor="w")


                            can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")




                            """
                            if music_details[song][3]==True:

                                if song==current_playing:
                                    can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video3,anchor="nw")
                                else:

                                   can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video2,anchor="nw")
                            elif music_details[song][3]==False:

                                can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=video1,anchor="nw")
                            """




                            con=0

                            for i in playlist:


                                try:
                                    v=playlist[i].index(song)
                                    con=1
                                except:
                                    pass


                            if con==0:

                                _pl_=playlist1



                            elif con==1:

                                
                                _pl_=playlist2


                                if song==current_playing:
                                    _pl_=playlist3

                                


                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=_pl_,anchor="nw")




                            if music_details[song][0]==0:

                                _fv_=favourite1

                                if song==current_playing:
                                    _fv_=favourite1_


                            elif music_details[song][0]==1:


                                _fv_=favourite2


                                if song==current_playing:
                                    _fv_=favourite2_

                            can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")




                            #if not song==current_playing:

                            #    can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col3)


                            songs.append([song,y])

                            y+=50
                        except:
                            pass
                if len(songs)==0:


                    can2.create_image((int(can2["width"])-300)/2,(int(can2["height"])-300)/2,image=nomusic,anchor="nw")
                    
                    #can2.create_text(int(can2["width"])/2,((h-121)-80-10)/2,text="No Record!",font=("TkDefaultFont",12),fill=col1)


                    style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                                    troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                                    lightcolor="#000000",relief="flat", darkcolor="#000000",
                                    arrowsize=6)



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

                    n=music_details[song][1]

                    if n>=1:
                        ar_.append([song,n])


            ar_=sorted(ar_, key=lambda row: row[1], reverse=True)



            for song in ar_:



                if song[0]==current_playing:
                    can2.create_line(2,y, int(can2["width"]),y,fill="#000000")

                    #can2.create_rectangle(2,y, int(can2["width"]),y+50-1,fill=col1,outline=col1)

                    #draw_round_rec(can2,2,y, int(can2["width"]),y+50,10,col1,col1,0)

                    draw_active(can2,0,y,int(can2["width"])-1,51,col1)

                    col="#000000"
                    _del_=delete2

                    can2.create_image(5,y+10,image=musical_note1,anchor="nw")

                else:


                    can2.create_image(5,y+10,image=musical_note2,anchor="nw")
                    col=col1

                    _del_=delete



                n=music_details[song[0]][1]


                if n<1000:
                    t=str(n)
                elif 1000<=n<1000000:


                    t=str(round(n/1000,2))+" K"
                elif 1000000<=n<1000000000:


                    t=str(round(n/1000000,2))+" M"
                elif n>=1000000000:


                    t=str(round(n/1000000000,2))+" B"


                if n==1:
                    vw="View"
                else:
                    vw="Views"
                



                can2.create_text(50,y+50/3,text=_text_(can2,song[0][:-4],"TkDefaultFont",12,(int(can2["width"])-25*3-15*3-10)-50),font=("TkDefaultFont",12),fill=col,anchor="w")
                can2.create_text(50,y+50*2.3/3,text=t+" "+vw,font=("TkDefaultFont",10),fill=col2,anchor="w")
                



                can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")

                """

                if music_details[song[0]][3]==True:

                    if song[0]==current_playing:
                        can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=video3,anchor="nw")
                    else:

                       can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=video2,anchor="nw")
                elif music_details[song[0]][3]==False:

                    can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=video1,anchor="nw")

                """






                con=0

                for i in playlist:


                    try:
                        v=playlist[i].index(song[0])
                        con=1
                    except:
                        pass


                if con==0:

                    _pl_=playlist1



                elif con==1:

                    
                    _pl_=playlist2

                    if song[0]==current_playing:
                        _pl_=playlist3

                    


                can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=_pl_,anchor="nw")




                if music_details[song[0]][0]==0:

                    _fv_=favourite1

                    if song[0]==current_playing:
                        _fv_=favourite1_


                elif music_details[song[0]][0]==1:


                    _fv_=favourite2


                    if song[0]==current_playing:
                        _fv_=favourite2_



                can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")



                #if not song[0]==current_playing:

                #    can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col3)


                ar=[song[0],y]

                songs.append(ar)

                y+=50

            if len(songs)==0:





                    

                can2.create_image((int(can2["width"])-300)/2,(int(can2["height"])-300)/2,image=nomusic,anchor="nw")
                
                #can2.create_text(int(can2["width"])/2,((h-121)-80-10)/2,text="No Record!",font=("TkDefaultFont",12),fill=col1)


                style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                                troughcolor="#000000", borderwidth=0, bordercolor="#000000",
                                lightcolor="#000000",relief="flat", darkcolor="#000000",
                                arrowsize=6)

        """
        if y<=((h-121)-80-10):
            hex(can2,-30,-30,w+60,int(can2["height"])+60,30,"#390200","#000000")


        else:

            hex(can2,-30,-30,w+60,y+60,30,"#390200","#000000")

        """


        if lst==0:

            if not playlist_st==0:

                _search=0
                search.place_forget()



                _npl=0
                npl.place_forget()

        
        if lyric_st==0:
            can_lyrics.place_forget()

        if _search==0 and _npl==0:
            can.focus_set()



        if y+1<=int(can2["height"]):

            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
        else:
            can2["scrollregion"]=(0,0,int(can2["width"]),y+1)


    if st==songs_status[0]:

        if st==2:

            if current_playlist==songs_status[1]:

                if search_var=="":

                    _songs_=songs

               


        else:

            if search_var=="":
                _songs_=songs



    draw_can()


    
    #"#1c7e53"


    draw_round_rec(can,0,0,w-1,h-1,15,col1,"",1)

    """
        r=10

        can.create_line(1+r,1, w-2-r,1, w-2,1+r, w-2,h-2-r, w-2-r,h-2, 1+r,h-2, 1,h-2-r, 1,1+r, 1+r,1, fill=col1 )

    """


    can.create_image(w-10-25,(50-25)/2,image=quit,anchor="nw")
    can.create_image(w-10-25-10-25,(50-25)/2,image=minimize,anchor="nw")

    #mv=can2.canvasy(0)

    save()







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
def draw_can():

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
    global circle2,circle3,circle4,circle5,circle7,circle8,circle9,circle5

    global expand,expand2,expand_st

    global playlist4

    global style,style2

    global lyric_st

    global play_video_st


    global select_st
    global songs_status
    global quit
    global forward,backward
    global _bg_

    global transparent_im,transparent_im2,transparent_im3

    global note
    global circle6
    global bg
    global favourite2
    global can_cur,cur

    can.delete("all")

    #hex(can,-40,-40,w+40,h+40,40,"#000000","#000000")






    if shuff==1 or shuff==2:
        sort_val=""



    col1="#00ffff"
    col2="#005555"
    col3="#001618"




    can["bg"]="#000000"



    


    _bg_=can.create_image(0,0,image=bg,anchor="nw")
    can_cur=can.create_image(-200,-200,image=cur,anchor="nw")

    can.create_image((w-450)/2,50+((h-121-50)-450)/2,image=note,anchor="nw" )



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

    #can.create_rectangle(0,h-20-30-15+5+10-3+2.5-5, 10+25+15+25+15+25+15+25+10,h-20-30-15+5+10-3+2.5-5+35,fill="#000000",outline="#000000")
    
    if select_st==0:
        create_rectangle_(can,0,int(h-20-30-15+5+10-3+2.5-5), int(10+25+15+25+15+25+15+25+10),int(h-20-30-15+5+10-3+2.5-5+35), fill='#000000', alpha=.8)

    draw_round_rec2(can,0,0,w-1,h-1,15,"#333333")




    search["fg"]=col1
    search["insertbackground"]=col1


    npl["fg"]=col1
    npl["insertbackground"]=col1
 





    #lyrics

    if lst==0:

        if not st==4:

            x=w/2
            y=h-121+5-30



            if lyric_st==0:

                

                can.create_image(x-40,y,image=circle6,anchor="nw")
                can.create_image(x+40-30,y,image=circle6,anchor="nw")


                can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col2,outline=col2)

                #draw_round_rec(can,x-40,y,x+40,y+30,15,col1,"",1)

                can.create_text(x,y+15,text="Lyrics",font=("TkDefaultFont",12),fill="#00ffff")


                try:


                    if not music_details[current_playing][2]=="":


                        can.create_image(x+40+5,y+15-3, image=circle5,anchor="nw")
                except:
                    pass

            elif lyric_st==1:


                can.create_image(x-40,y,image=circle3,anchor="nw")
                can.create_image(x+40-30,y,image=circle3,anchor="nw")


                can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col1,outline=col1)

                can.create_text(x,y+15,text="Lyrics",font=("TkDefaultFont",12),fill="#000000")


                can.create_image(x+40+10-5,y+2.5,image=add,anchor="nw")






    if lst==1:


        if st==4:
            pass

        else:



            can.create_image(10,50,image=transparent_im3,anchor="nw")
            
            if _search==1:

                can.create_oval(10,40+30-10-5-5, 10+30,40+30+30-10-5-5,fill="#000000",outline="#000000")
                can.create_oval(w-10-30-1,40+30-10-5-5, w-10-1,40+30+30-10-5-5,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40+30-10-5-5, w-10-15-1,40+30+30-10-5-5,fill="#000000",outline="#000000")
            



            can.create_arc(10,40+30-10-5-5, 10+30,40+30+30-10-5-5, style=tk.ARC,start=90,extent=180,outline=col1)
            can.create_arc(w-10-30,40+30-10-5-5, w-10,40+30+30-10-5-5, style=tk.ARC,start=270,extent=180,outline=col1)

            can.create_line(10+15,40+30-10-5-5, w-10-15,40+30-10-5-5, fill=col1)
            can.create_line(10-1+15,40+30+30-10-5-5, w-10-15,40+30+30-10-5-5, fill=col1)



            can.create_image(w-10-5-20,40+5+30-10-5-5,image=cancel,anchor="nw")

            #draw_round_rec(can,10,40, w-10,40+30,10,"#000000",col1,0)

            can.create_text(30+20+5,40+15+30-10-5-5,text="Search",font=("TkDefaultFont",12),fill=col1,anchor="w")



            can.create_image(30,45+30-10-5-5,image=search_im,anchor="nw")

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





                #can.create_polygon(ar,fill=col3,outline=col3)




            """
            if select_st==1:
                draw_round_rec(can,10,90,w-10-1,h-121+75,15,col1,col1,1,1)
            else:
                draw_round_rec(can,10,90,w-10-1,h-121,15,col1,col1,1,1)

            """


            #can.create_line(10,89-2,w-10,89-2,fill=col2)
            can.create_line(10,90+int(can2["height"]),w-10,90+int(can2["height"]),fill=col1,width=2)

            frame.place(in_=root,x=10,y=90-1-1)


    

    if lyric_st==1:
        show_lyrics()



















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









        #can.create_rectangle(x-50,20-10, x+50,20+10, outline=col1)



        can.create_text(x,50/2,text=label[l],fill=col,font=("TkDefaultFont",12),anchor="c")



        x+=xv







    if select_st==1:

        pass


    else:

        if playlist_st==0 and st==2 and pl_st==0 and current_playing=="":

            pass

        else:

            #can.create_text(10,h-20-60-20-27,text=current_playlist,font=("TkDefaultFont",13),anchor="w",fill=col1)


            #can.create_text(10,h-20-60-20-27-30,text=current_playlist,font=("TkDefaultFont",13),anchor="w",fill=col1)


            try:


                if songs_status[1]!="":

                        current_playlist_=songs_status[1]

                        
                        length_in_pixels = get_text_length(can, current_playlist_, "TkDefaultFont", 12) 

                        can.create_image(10,h-20-60-20-27-15+3+10+3+2+2-3+1+10,image=circle3,anchor="nw")
                        can.create_image(10+15+length_in_pixels+30-15,h-20-60-20-27-15+3+10+3+2+2-3+1+10,image=circle3,anchor="nw")

                        can.create_rectangle(10+15,h-20-60-20-27-15+3+10+3+2+2-3+1+10, 10+15+length_in_pixels+30,h-20-60-20-27-15+3+10+3+2+2-3+30-1+1+10,
                            fill=col1,outline=col1)


                        can.create_image(10+15,h-20-60-20-27-15+3+10+5+3+2+2-3+2+10, image=playlist4,anchor="nw")

                        can.create_text(10+15+30,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=current_playlist_,font=("TkDefaultFont",12,),anchor="w",fill="#000000")
                              
                        can.create_text(10+15+length_in_pixels+15+10+30,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"TkDefaultFont",12,(w-10)-(10+15+length_in_pixels+15+10+30)),font=("TkDefaultFont",12),anchor="w",fill=col1)

                else:

                    if songs_status[0]==1:

                        can.create_image(10,h-20-60-20-27-15+3+10+3+2+2-3+15+10-12.5,image=favourite2,anchor="nw")
                        can.create_text(10+25+10,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"TkDefaultFont",12,(w-10)-(10+25+10)),font=("TkDefaultFont",12),anchor="w",fill=col1)
                    else:
                        can.create_text(10,h-20-60-20-27-15+3+10+3+2+2-3+15+10,text=_text_(can2,current_playing[:-4],"TkDefaultFont",12,(w-10)-(10)),font=("TkDefaultFont",12),anchor="w",fill=col1)
            
            except:
                pass


            """
            if not current_playing=="":

                    n=music_details[current_playing][1]


                    if n<1000:
                        t=str(n)
                    elif 1000<=n<1000000:


                        t=str(round(n/1000,2))+" K"
                    elif 1000000<=n<1000000000:


                        t=str(round(n/1000000,2))+" M"
                    elif n>=1000000000:


                        t=str(round(n/1000000000,2))+" B"
                    else:

                        t=str(n)



                    l=get_text_length(can, t, "TkDefaultFont", 13)

                    can.create_rectangle(w-10-26-5-l-10, h-20-60-20-27-15+3+10+3+2+2-3+15-13, w, h-20-60-20-27-15+3+10+3+2+2-3+15+13,fill="#000000",outline="#000000")

                    can.create_text(w-10-26-5,h-20-60-20-27-15+3+10+3+2+2-3+15,text=t,font=("TkDefaultFont",12),anchor="e",fill=col1)

                    can.create_image(w-10-26,h-20-60-20-27-15+3+10+3+2+2-3+15-13,image=eye,anchor="nw")"""




        can.create_line(10,h-20-60-20+10+2+5-3+10,w-10,h-20-60-20+10+2+5-3+10,fill=col2,width=2)

        
        if st==2 and playlist_st==0 and current_playing=="":
            pass
        else:

            if not current_playing=="":
                can.create_text(w-10,h-20-60-20+20+10+5-3+5-2,text=tot_tm,font=("TkDefaultFont",11),anchor="e",fill=col1)



        can.create_image(w/2-30,h-20-30-30+5+10-3, image=circle,anchor="nw")

        if play_st==0:
            can.create_image(w/2-15+2,h-20-30-15+5+10-3, image=play,anchor="nw")
        elif play_st==1:
            can.create_image(w/2-15,h-20-30-15+5+10-3, image=pause,anchor="nw")













        if lst==0:
            global sig_,sig2

            can.delete(sig_)

            try:

                if st!=4:
                    sig_=can.create_line(sig2,fill=col1)

            except:
                pass

            can.create_image(10,h-20-30-15+5+10-3+2.5,image=list1,anchor="nw")
        elif lst==1:
            can.create_image(10,h-20-30-15+5+10-3+2.5,image=list2,anchor="nw")


        if lyric_st==1:
            can.delete(sig_)




        if sort_val!="":
            can.create_image(10+25+15,h-20-30-15+5+10-3+2.5,image=sort,anchor="nw")

        else:
            can.create_image(10+25+15,h-20-30-15+5+10-3+2.5,image=sort2,anchor="nw")

        if shuff==0:


            can.create_image(10+25+15+25+15,h-20-30-15+5+10-3+2.5,image=shuffle1,anchor="nw")
        elif shuff==1:
            can.create_image(10+25+15+25+15,h-20-30-15+5+10-3+2.5,image=shuffle2,anchor="nw")




        if loop==0:
            can.create_image(10+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=loop1,anchor="nw")

        elif loop==1:

            can.create_image(10+25+15+25+15+25+15,h-20-30-15+5+10-3+2.5,image=loop2,anchor="nw")



        can.create_line(w-10-100,h-20-30+5+10-3, w-10,h-20-30+5+10-3,fill=col2,width=2)


        can.create_image(w-10-100-10-30+5,h-20-30-15+5+10-3+1,image=speaker,anchor="nw")



        can.delete(vol1)
        can.delete(vol2)
        can.delete(vol3)
        can.delete(vol4)

        r=(w-10)-(w-10-100)


        vol1=can.create_line(w-10-100,h-20-30+5+10-3 ,w-10-100+current_volume*r,h-20-30+5+10-3,fill=col1,width=2)

        vol2=can.create_text(w-10,h-20-30+5+10-3+12,text=str(int(current_volume*100))+"%",fill=col1,font=("TkDefaultFont",11),anchor="e")

        #vol3=can.create_image(w-10-100+current_volume*r-3,h-20-30+5+10-3-3,image=circle5,anchor="nw")
        #vol4=can.create_image(w-10-100+current_volume*r-2,h-20-30+5+10-3-2,image=circle9,anchor="nw")

        can.create_image(w/2-30-30-25,h-20-30-15+5+10-3+2.5,image=previous,anchor="nw")
        can.create_image(w/2+30+30,h-20-30-15+5+10-3+2.5,image=next_,anchor="nw")

        can.create_image(w/2-30-30-25-15-25-10,h-20-30-15+5+10-3+2.5,image=backward,anchor="nw")

        can.create_image(w/2+30+30+25+15+10,h-20-30-15+5+10-3+2.5,image=forward,anchor="nw")





        """

        if play_video_st==1:
            can.create_image(10+25*3+15*3,h-20-30-15+5+10-3+2.5,image=circle5,anchor="nw")
            can.create_image(10+25*3+15*3,h-20-30-15+5+10-3+2.5,image=video2,anchor="nw")

        elif play_video_st==0:

            can.create_image(10+25*3+15*3,h-20-30-15+5+10-3+2.5,image=circle5,anchor="nw")
            can.create_image(10+25*3+15*3,h-20-30-15+5+10-3+2.5,image=video1,anchor="nw")

        """






    try:
        if not lyric_st==1:
            prog()
    except:
        pass

    
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



        #draw_polygon(can,7,0,w/2,50+(((h-121)-50)-420)/2+210,210,col2,10,2,"#000000",10)
        frame.place_forget()
        
        yv=50+(((h-121)-50)-90)/2+20



        can.create_image(w/2-80-15,yv, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv, w/2+80,yv+30-1,fill=col1,outline=col1)



        can.create_text(w/2,yv+15,text="Add Folder",fill="#000000",font=("TkDefaultFont",12))






        can.create_image(w/2-80-15,yv+60, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv+60, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv+60, w/2+80,yv+30-1+60,fill=col1,outline=col1)


        can.create_text(w/2,yv+15+60,text="Add Audio File",fill="#000000",font=("TkDefaultFont",12))

        prog()



    if select_st==1:

        length_in_pixels = get_text_length(can, playlist_select, "TkDefaultFont", 13) 

        x=(w-(30+5+length_in_pixels))/2

        can.create_image(x,(h-121+75)+((h-1)-(h-121+75))/2-11,image=playlist2,anchor="nw")

        can.create_text(x+30+5,(h-121+75)+((h-1)-(h-121+75))/2,text=playlist_select,font=("TkDefaultFont",12),fill=col1,anchor="w")

        can.create_image(w-10-25,(h-121+75)+((h-1)-(h-121+75)-25)/2,image=quit,anchor="nw")



    #can.create_text(w/4,h-15,text="hepta7 ©",font=("TkDefaultFont",12),anchor="c",fill=col2)








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
def show_lyrics():
    global can,w,can_lyrics
    global current_playing,music_details

    global lst
    global lvar
    global ylyrics
    global _bg3_,note
    global _bg5_,note2
    global cur,can_lyrics_cur



    col1="#00ffff"
    col2="#005555"



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


                    
                    _bg3_=can_lyrics.create_image(-10,-(50)+can_lyrics.canvasy(0),image=bg,anchor="nw")
                    can_lyrics_cur=can_lyrics.create_image(-200,-200,image=cur,anchor="nw")
                    _bg5_=can_lyrics.create_image((w-450)/2-10,50+((h-121-50)-450)/2-(50)+can_lyrics.canvasy(0),image=note,anchor="nw")
                    
                    


                    can_lyrics["bg"]="#000000"

                    can_lyrics["width"]=w-20
                    can_lyrics["height"]=(h-121+5-30-50/2+(50-30)/2)-50

                    

                    #can_lyrics.create_text((790-111)/2,0, text=txt,anchor="c",fill=col1,font=("TkDefaultFont",13))


                    tt=txt.split("\n")

                    y=13

                    for l in tt:

                        can_lyrics.create_text(10+(w-20)/2,y, text=l, font=("TkDefaultFont",13),anchor="c",fill=col1)

                        y+=13

                    ylyrics=y+13


                    if ylyrics<=int(can_lyrics["height"]):

                        can_lyrics["scrollregion"]=(0,0,int(can_lyrics["width"]),int(can_lyrics["height"]))
                    else:
                        can_lyrics["scrollregion"]=(0,0,int(can_lyrics["width"]),ylyrics)





                    #text.tag_configure("center", justify="center")

                    # Apply the tag to the inserted text
                    #text.tag_add("center", "1.0", "end")






                    can_lyrics.place(in_=root,x=10,y=50)



                    #draw_round_rec(can,0,h-145-30-5-450-10 ,w,h-145-30-5,10,"#000000","#000000",0)






                else:
                    can.create_text(w/2,50+(((h-121)-50)-420)/2+210,text="Nothing to show!",fill=col1,font=("TkDefaultFont",12))

                    can_lyrics.place_forget()

            else:
                can.create_text(w/2,50+(((h-121)-50)-420)/2+210,text="Nothing to show!",fill=col1,font=("TkDefaultFont",12))
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

        ar.append(x)
        ar.append(y)


        ar2.append(x)
        ar2.append(y)


        a_-=1


    a_=180

    cx,cy=x2-r,y1+r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        ar2.append(x)
        ar2.append(y)


        a_-=1
        

    a_=90

    cx,cy=x2-r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        ar3.append(x)
        ar3.append(y)

        a_-=1
        


    a_=0

    cx,cy=x1+r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        ar3.append(x)
        ar3.append(y)


        a_-=1

    ar.append(ar[0])
    ar.append(ar[1])


    if con==0:

        c.create_polygon(ar,fill=col,outline=col2,width=width)
    elif con==1:    
        c.create_line(ar,fill=col,width=width)

    elif con==2:

        c.create_line(ar2,fill=col,width=width)

        c.create_line(ar3,fill=col,width=width)





def hex_to_rgb(hex_color: str) -> tuple:
    # Remove the '#' if it exists
    hex_color = hex_color.lstrip('#')
    # Convert to RGB
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

note=0
note2=0

cur=0
def load_im():

    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global cancel,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,checked,sort,delete,favourite1_,favourite2_,delete2,playlist3,sort2,loop1,loop2,wallpaper
    global circle2,circle3,circle4,circle5,circle4,circle7,circle8,circle9,circle5,expand,expand2,playlist4

    global minimize,quit
    global circlex
    global add,add2
    global nomusic
    global forward,backward
    global note_
    global note
    global circle6
    global bg
    global note2
    global cur

    circle=ImageTk.PhotoImage(file="data/circle.png")
    circle2=ImageTk.PhotoImage(file="data/circle2.png")
    circle3=ImageTk.PhotoImage(file="data/circle3.png")
    circle4=ImageTk.PhotoImage(file="data/circle4.png")
    circle5=ImageTk.PhotoImage(file="data/circle5.png")
    circle6=ImageTk.PhotoImage(file="data/circle6.png")
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
    #note=ImageTk.PhotoImage(file="data/note.png")
    #note_=ImageTk.PhotoImage(file="data/note_.png")
    nomusic=ImageTk.PhotoImage(file="data/nomusic.png")
    playlist1=ImageTk.PhotoImage(file="data/playlist1.png")
    playlist2=ImageTk.PhotoImage(file="data/playlist2.png")
    checked=ImageTk.PhotoImage(file="data/checked.png")
    sort=ImageTk.PhotoImage(file="data/sort.png")
    delete=ImageTk.PhotoImage(file="data/bin.png")
    favourite1_=ImageTk.PhotoImage(file="data/favourite1_.png")
    favourite2_=ImageTk.PhotoImage(file="data/favourite2_.png")
    delete2=ImageTk.PhotoImage(file="data/bin2.png")
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
    note=ImageTk.PhotoImage(file="data/note.png")
    bg=ImageTk.PhotoImage(file="data/bg.png")
    cur=ImageTk.PhotoImage(file="data/cursor.png")




transparent_im=None
transparent_im2=None
transparent_im3=None

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
    global transparent_im,transparent_im2,transparent_im3
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        image2 = Image.new('RGBA', (x2-x1, (y2+75)-y1), fill)
        image3 = Image.new('RGBA', ((w-10)-10, 80-50), fill)

        transparent_im=ImageTk.PhotoImage(image)
        transparent_im2=ImageTk.PhotoImage(image2)
        transparent_im3=ImageTk.PhotoImage(image3)



        #can.create_image(x1, y1, image=images1[-1], anchor='nw')




def check_pl():
    global npl,plv,can2,playlist_st,st,_npl

    if st==2 and playlist_st==0:

        if can2.canvasy(0)!=plv:

            plv=can2.canvasy(0)

            if not can2.canvasy(0)==0:
                _npl=0
                npl.place_forget()


    root.after(1,check_pl)

def load_():
    global can,load,load_ang,load_st
    global st,w


    if st==4 and load_st==1:

        can.delete(load)

        load=can.create_arc(w/2-20,493-20-40, w/2+20,493-20,outline=col1,width=2,style=tk.ARC,start=load_ang,extent=270)

        load_ang-=30

    root.after(100,load_)



def clipboard():

    global _lyric

    clipboard_content = pyperclip.paste()
    clipboard_content = repr(clipboard_content)

    if _lyric!=clipboard_content:
        _lyric=clipboard_content

    root.after(1,clipboard)




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


    root.after(1,sync_lyrics)

ang=0
def load_():
    global can,st,convert,w,h
    global load,load2
    global ang


    col1="#00ffff"
    col2="#005555"


    can.delete(load)
    can.delete(load2)


    if st==4:
        if not convert==0:



            load=can.create_arc(w/2-20,h-121-20-40, w/2+20,h-121-20,outline=col1,start=ang+180,extent=70,style="arc",width=2)

            load2=can.create_arc(w/2-20,h-121-20-40, w/2+20,h-121-20,outline=col1,start=ang,extent=70,style="arc",width=2)


            ang+=1



    root.after(1,load_)

mot_val=0
my_cursor=0
def can_motion(e):

    global can,mot_val
    global root_st



    col1="#00ffff"
    col2="#005555"

    if not root_st==1:

        


        can.delete(mot_val)


        #list

        cx,cy=10+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                mot_val=can.create_text(10+12.5,h-20-30-15+5+10-3+2.5+25+10,text="list",fill=col1,font=("TkDefaultFont",10),anchor="c")



        #sort

        cx,cy=10+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:
                mot_val=can.create_text(10+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="sort",fill=col1,font=("TkDefaultFont",10),anchor="c")
            



        #shuffle

        cx,cy=10+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                mot_val=can.create_text(10+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="shuffle",fill=col1,font=("TkDefaultFont",10),anchor="c")
            


        #loop

        cx,cy=10+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+12.5

        if cx-12.5<=e.x<=cx+12.5:
            if cy-12.5<=e.y<=cy+12.5:

                mot_val=can.create_text(10+25+15+25+15+25+15+12.5,h-20-30-15+5+10-3+2.5+25+10,text="loop",fill=col1,font=("TkDefaultFont",10),anchor="c")
            



def draw_polygon(canvas,n,st_ang,cx,cy,r,col,width,con,col2="",d=10):








    if con==1:


        a=180+st_ang

        ar=[]

        for _ in range(n):


            x=r*math.sin(math.radians(a))+cx
            y=r*math.cos(math.radians(a))+cy

            ar.append(x)
            ar.append(y)


            a+=360/n

        canvas.create_polygon(ar,fill=col,outline=col)





        a=180+st_ang

        ar=[]

        r-=d

        

        for _ in range(n):

            a_=a+360/n

            x=r*math.sin(math.radians(a))+cx
            y=r*math.cos(math.radians(a))+cy

            for aa in range(n-1):



                x2=r*math.sin(math.radians(a_))+cx
                y2=r*math.cos(math.radians(a_))+cy

                canvas.create_line(x,y, x2,y2, fill=col2,width=width)


                a_+=360/n







            a+=360/n
    elif con==2:



        a=180+st_ang

        ar=[]


        

        for _ in range(n):

            a_=a+360/n

            x=r*math.sin(math.radians(a))+cx
            y=r*math.cos(math.radians(a))+cy

            for aa in range(n-1):



                x2=r*math.sin(math.radians(a_))+cx
                y2=r*math.cos(math.radians(a_))+cy

                canvas.create_line(x,y, x2,y2, fill=col,width=width)


                a_+=360/n







            a+=360/n


can_cur=0
can2_cur=0
can_lyrics_cur=0

def adjust_cursor(x,y,con=0):
    global can,can2,can_lyrics
    global can_cur,can2_cur,can_lyrics_cur
    global cur
    global hex_ar

    def is_point_in_hexagon(px, py, hex_points):
        from matplotlib.path import Path
        path = Path(hex_points)
        return path.contains_point((px, py))


    for v in hex_ar:

        ar=v[0]
        cx,cy=v[1],v[2]


        if con==0:




            if is_point_in_hexagon(x, y, ar):




                x_=cx-65
                y_=cy-56-4


                can.coords(can_cur,x_,y_)

                can2.coords(can2_cur,x_-10,y_-(90-1-1)+can2.canvasy(0))

                can_lyrics.coords(can_lyrics_cur,x_-10,y_-50+can_lyrics.canvasy(0))


        else:

            can.coords(can_cur,-200,-200)

            can2.coords(can2_cur,-200,-200)

            can_lyrics.coords(can_lyrics_cur,-200,-200)




def update_cursor_pos():
    global root_st,can

    if not root_st==1:

        x,y = pyautogui.position()

        p=root.geometry().split("+")

        xx,yy=int(p[1]),int(p[2])


        con=1
        if xx<=x<=xx+int(can["width"]):
            con=0

        if con==0:
            if yy<=y<=yy+int(can["height"]):
                pass
            else:
                con=1

        adjust_cursor(x-xx,y-yy,con)

    root.after(4,update_cursor_pos)





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

try:

    with open("data/save.json", "r") as file:
        data = json.load(file)
except:
    pass




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
songs_status=[]




forward=None
backward=None


note_=None

try:


    st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,shuffle_ar,shuffle_st,songs_status=data["save"]


    st,current_playlist,shuffle_st,sort_val,shuffle_ar,loop,current_playing=songs_status


except:

    pass
lst=1
if playlist_st==0 and current_playing!="":
    playlist_st=1




root=tk.Tk()

wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()

w,h=int(680*1.618),680
"""
im=Image.open("hp.jpg")
x,y=im.size

im=im.resize((w,int(w*y/x)))
x,y=im.size
yy=int((y-680)/2)

im=im.crop((0,yy,x,y-yy))

im.save("hp.png")"""



root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int(((ht-get_taskbar_height())-h)/2)))
root.resizable(0,0)
#root.wm_attributes("-alpha",0.9)
root.wm_attributes("-transparentcolor","#333333")
root.wm_attributes("-topmost",True)
root.iconbitmap("data/icon.ico")
root.title("HMUSIC")

root.overrideredirect(True)



# Function to draw a single circle
def draw_circle(canvas, x,y, radius, col):

    canvas.create_oval(
        x - radius, y - radius,
        x + radius, y + radius,
        outline=col, width=1.2
    )

# Function to draw the Flower of Life pattern
def draw_flower_of_life(canvas, x, y, radius, col):


    xx=int(round(1366/radius,0))+10
    yy=int(round(768/radius,0))+10



 


    y2=0


    _x=0

    st=0

    for x_ in range(xx):



        if st==0:
            _y=0

        elif st==1:
            _y=-25


        for y_ in range(yy):



            can.create_oval(_x-radius,_y-radius, _x+radius,_y+radius,outline=col)








            _y+=radius


        if st==0:
            st=1

        elif st==1:
            st=0



        _x+=43






    
def hex(c,x,y,wd,ht,sz,col1,col2):

    global cursor

    c.delete("all")


    #c.create_rectangle(x,y, x+wd,y+ht, fill=col1,outline=col1)


    x1=sz/2*math.sin(math.radians(180-360/6))

    xv=x1*2

    y1=sz/2*math.cos(math.radians(180+360/6*2))
    yv=sz/2+y1

    _y=y

    _st=0

    for y_ in range(int(ht/(sz-6))+1):

        if _st==0:
            _x=x
        elif _st==1:
            _x=x+xv/2
        for x_ in range(int(wd/(sz-2))+1):

            """


            if y_==1:
                if x_==1 or x_==2:
                    col="#00ffff"
                    hexagon(c,_x,_y,sz,col2,col)
                else:

                    hexagon(c,_x,_y,sz,col2,col1)

            elif y_==2:
                if x_==1 or x_==2 or x_==3:
                    col="#00ffff"
                    hexagon(c,_x,_y,sz,col2,col)
                else:

                    hexagon(c,_x,_y,sz,col2,col1)

            elif y_==3:
                if x_==1 or x_==2:
                    col="#00ffff"
                    hexagon(c,_x,_y,sz,col2,col)
                else:

                    hexagon(c,_x,_y,sz,col2,col1)

            else:

                hexagon(c,_x,_y,sz,col2,col1)

            """

            hexagon(c,_x,_y,sz,col2,col1)




            _x+=xv

        if _st==0:
            _st=1
        elif _st==1:
            _st=0

        _y+=yv



        #can["width"]=int(xv*5)
        #can["height"]=int(yv*5)

        #root.geometry(str(int(xv*5))+"x"+str(int(yv*5)))

hex_ar=[]
def hexagon(c,x,y,sz,col1,col2):
    global hex_ar

    x1=sz/2*math.sin(math.radians(180-360/6))

    xv=x1*2

    cx,cy=x+xv/2,y+sz/2

    h=360/6

    a_=180

    ar=[]
    ar2=[]
    for a in range(6):

        x_=sz/2*math.sin(math.radians(a_))+cx
        y_=sz/2*math.cos(math.radians(a_))+cy

        ar.append(x_)
        ar.append(y_)

        ar2.append((x_,y_))



        a_+=h

    hex_ar.append([ar2,cx,cy])


    ar.append(ar[0])
    ar.append(ar[1])
    #c.create_polygon(ar,fill=col1,outline=col2)
















can2_y, lyrics_y=0,0

def move_bg():
    global can2,_bg2_,_bg4_,_bg5_
    global can_lyrics,_bg3_,lyric_st,_lyric_
    global w
    global music_details,current_playing
    global can2_y,lyrics_y
    global select_st,transparent_im_,transparent_im2_




    try:

        if not can2_y==can2.canvasy(0):
            

            can2.coords(_bg2_,-10,-(90-1-1)+can2.canvasy(0))
            can2.coords(_bg4_,(w-450)/2-10,50+((h-121-50)-450)/2-(90-1-1)+can2.canvasy(0))

            

            can2_y=can2.canvasy(0)

    except:
        pass



    try:
        if lyric_st==1:
            if not music_details[current_playing][2]=="":

                if not lyrics_y==can_lyrics.canvasy(0):


                    can_lyrics.coords(_bg3_,-10,-(50)+can_lyrics.canvasy(0))
                    can_lyrics.coords(_bg5_,(w-450)/2-10,50+((h-121-50)-450)/2-(50)+can_lyrics.canvasy(0))
                    

                    lyrics_y=can_lyrics.canvasy(0)




    except:
        pass


    root.after(1,move_bg)



def _on_mousewheel(e):
    global can2,can3,yyy,h,add_st
    global ylyric,lyric_st,lst
    global music_details,current_playing,can_lyrics
    global _bg2_,_bg3_,_bg4_,_bg5_
    global w
    global select_st,transparent_im,transparent_im2

    if add_st==0 and lst==1:

        if int(can2["scrollregion"].split(" ")[-1])>((h-121)-80-10):

            can2.yview_scroll(int(-1*(e.delta/120)), "units")
            


            can2.coords(_bg2_,-10,-(90-1-1)+can2.canvasy(0))
            can2.coords(_bg4_,(w-450)/2-10,50+((h-121-50)-450)/2-(90-1-1)+can2.canvasy(0))
     



    elif add_st==1:

        if int(can3["scrollregion"].split(" ")[-1])>210:
            can3.yview_scroll(int(-1*(e.delta/120)), "units")

    if lyric_st==1:
        if not music_details[current_playing][2]=="":
            can_lyrics.yview_scroll(int(-1*(e.delta/120)), "units")

            can_lyrics.coords(_bg3_,-10,-(50)+can_lyrics.canvasy(0))
            can_lyrics.coords(_bg5_,(w-450)/2-10,50+((h-121-50)-450)/2-(50)+can_lyrics.canvasy(0))



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


    if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
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

    vid_canvas.place_forget()

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


    if st==2 and playlist_st==0 and pl_st==0 and current_playing=="":
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

    vid_canvas.place_forget()

    lyric_st=0

    cap=None

    main()

    if not select_st==1:

        move_to_playing()

        if st==2 and playlist_st==0:
            can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))


def __list(e):
    global lst,lyric_st,can_lyrics,can2,st,playlist_st,_search,frame
    global songs_status,current_playlist

    if e.char.lower()=="l":


        if lst==0:
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

                frame.place_forget()

        main()

        if st==songs_status[0]:

            if st==2:
                if current_playlist==songs_status[1]:
                    move_to_playing(1)

            else:
                move_to_playing(1)



can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0,cursor="arrow")
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
can.bind("<Button-3>",can_b3)
can.bind_all("<MouseWheel>",_on_mousewheel)
can.bind("<space>",play_pause)
can.bind("<Right>",play_next)
can.bind("<Left>",play_previous)
can.bind("<Motion>",can_motion)
can.bind("<KeyPress>",__list)





hex(can,0,0,1330,715+30,30,"#003333","#000000")

col1="#00ffff"
col2="#005555"




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

can2=tk.Canvas(frame,bg="#000000",width=w-20,height=((h-121)-80-10),relief="flat",highlightthickness=0,border=0)
can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-1>",can2_b1)
can2.bind("<Button-3>",can_b3)
can2.bind("<space>",play_pause)
can2.bind("<Right>",play_next)
can2.bind("<Left>",play_previous)
can2.bind("<KeyPress>",__list)


sb=ttk.Scrollbar(frame,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")
sb.config(command=can2.yview)

can2.config(yscrollcommand=sb.set)
sb.pack(side=tk.LEFT,fill=tk.Y)


frame2=tk.Frame(bg="#000000",width=350+100,height=250)

can4=tk.Canvas(frame2,bg="#000000",width=350+100,height=40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can4.pack(side=tk.TOP)



frame3=tk.Frame(frame2,bg="#000000",width=350+100,height=250-40)

can3=tk.Canvas(frame3,bg="#000000",width=350+100-5-2-1,height=250-40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250-40))
can3.pack(side=tk.LEFT)
can3.bind_all("<MouseWheel>",_on_mousewheel)
can3.bind("<Button-1>",can3_b1)




sb2=ttk.Scrollbar(frame3,orient=tk.VERTICAL,style="My.Vertical.TScrollbar2")

sb2.config(command=can3.yview)

can3.config(yscrollcommand=sb2.set)
sb2.pack(side=tk.LEFT,fill=tk.Y)


can5=tk.Canvas(frame3,bg="#000000",width=2,height=250-40,relief="flat",highlightthickness=0,border=0)
can5.pack(side=tk.LEFT)




frame3.pack(side=tk.TOP)


can6=tk.Canvas(frame2,bg="#000000",width=350+100,height=17,relief="flat",highlightthickness=0,border=0)
can6.pack(side=tk.TOP)








def search__():

    global search,search_var,mvar,songs,current_playing
    global st,current_playlist
    global songs_status
    global playlist_st
    

    if search.get()!=search_var:
        search_var=search.get()



        main()








    root.after(1,search__)

search=tk.Entry(bg="#000000",fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=115,font=("TkDefaultFont",13))
#search.bind("<KeyPress>",search_keypress)
npl=tk.Entry(bg="#000000",fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=112,font=("TkDefaultFont",13))

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

    root.after(1,mvar_)



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
can_sort=tk.Canvas(bg="#000000",width=250,height=160,relief="flat",highlightthickness=0,border=0)

can_sort.bind("<Button-1>",can_sort_b1)




sort_ar=[]




y=30
for _ in sa:

    sort_ar.append([_,y])

    y+=30




"""

def check_geometry():
    global w,h
    global root


    if root.geometry().find("+")!=-1:

        x,y=root.geometry().split("+")[0].split("x")

    else:
        x,y=root.geometry().split("x")


    x=int(x)
    y=int(y)


    if x!=w or y!=h:

        w=x
        h=y

        main()



    root.after(1,check_geometry)
"""




can_lyrics=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0)



vid_canvas = tk.Canvas(relief="flat",highlightthickness=0,border=0)
vid_canvas["bg"]="#000000"



def darken_image(image_path, factor=0.5, output_path="darkened_image.png"):
    """
    Darkens an image by reducing its brightness.
    
    :param image_path: Path to the input image.
    :param factor: Brightness factor (0.0 = fully black, 1.0 = original brightness).
    :param output_path: Path to save the darkened image.
    """
    # Open Image
    img = Image.open(image_path)

    # Enhance Brightness
    enhancer = ImageEnhance.Brightness(img)
    darkened_img = enhancer.enhance(factor)  # Reduce brightness

    # Save and Show Image
    darkened_img.save(output_path)
    darkened_img.show()

# Example Usage
#darken_image("note_.png", factor=0.3)  # Adjust factor to control darkness




can2.focus_set()
load_im()

clipboard()


try:
    main()
except:
    pass

timer()

search__()
check_volume()

mvar_()


check_pl()



#gen_wave()
draw_wave()

#check_geometry()

try:

    update_song_status()

except:
    pass

#sync_lyrics()
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


move_to_playing()
if playlist_st==0:
    pass#can2["scrollregion"]=(0,0,w-7,((h-121)-80-10))


default_font = tk.Label(root, text="Sample Text").cget("font")


update_frame()
load_()
move_bg()
update_cursor_pos()

root.mainloop()
