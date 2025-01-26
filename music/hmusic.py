
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
import pygame
import subprocess
from mutagen.mp3 import MP3
from PIL import Image,ImageTk
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




"""

im=Image.open("data/red/play.png")
im=im.resize((30,30))
im.save("data/red/play.png")
"""



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


vid_im=0
vid_im_=0
vid_bg=0



vid_im2=0

cap = None
paused = False
vid_label = None

def initialize_ui(root, video_path):
    """Set up the Tkinter UI components."""
    global vid_label,can



    # Label for displaying the video

    vid_label.place(in_=root,x=10,y=47+30-20-5)


def play_video(video_path, start_time=0):
    """Play the video from the specified start time."""
    global cap, paused

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


def update_frame():
    """Update the video frame in the Tkinter window."""
    global cap, paused, vid_label, w,play_video_st,play_st


    if play_video_st==1 and play_st==1:

        try:

            if cap is not None and cap.isOpened() and not paused:
                ret, frame = cap.read()
                if ret:
                    # Resize the frame to the specified width and height
                    frame = cv2.resize(frame, (w-20-5, 494+5+20+5))

                    # Convert the frame to RGB for Tkinter compatibility
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)

                    # Update the label with the current frame
                    vid_label.imgtk = imgtk
                    vid_label.configure(image=imgtk)
                else:
                    cap=None
     
        except:
            pass

    # Schedule the next frame update
    root.after(20, update_frame)



paused=False
def play_vid(time_=0):
    
    global lst,frame,vid_label,cap,play_video_st,play_st


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




sig=[]
sig_=0
sig2=[]
tts=0

def draw_wave():

    global lst,can,st,sig,sig_,sig2,tm,tts,play_st,current_playing,w,h


    global theme

    global lyric_st

    global play_video_st

    global root_st


    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"





    xv=4

    if play_st==1:



        can.delete(sig_)

        if play_video_st==0:

            try:






                sig2=[]
                x=10
                for a in sig:

                    sig2.append(x)
                    sig2.append(a+(80-30+40-10-30)+(int(460*(h-30)/680)+10+30)/2+30)

                    x+=xv

                try:

                    if lst==0 and st!=4 and lyric_st==0 and root_st==0:

                        sig_=can.create_line(sig2,fill=col1)
                except:
                    pass









            except:
                pass

    root.after(10,draw_wave)





def gen_wave():
    global lst,can,st,sig,sig_,sig2,tm,tts,play_st,current_playing,w,h







    amp=150
    xv=4


    if play_st==1:




        try:

            amplitude = get_amplitude_at_time("waves/"+current_playing[:-3]+"wav", tts)





            sig.append(-amplitude*amp)


            xn=int((w-20)/xv)

            if len(sig)>xn:
                sig.pop(0)



            tts+=0.01
        except:
            pass


    root.after(10,gen_wave)

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





    global theme


    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"



    if convert==1:



        ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
        sample_rate=44100
        channels=2
        bitrate="192k"


        if st==4:


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill=col1)

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

                    if st==4:

                        can.delete(load)

                        load=can.create_text(10,h-20-60-60,text=i,font=("FreeMono",13),fill=col1,anchor="w")
                    main()

                except:
                    pass






        except:
            pass

        if st==4:


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            load2=can.create_oval(w/2-50,493-20-40-30-15+100, w/2-50+30,493-20-40-30+15+100,fill=col1,outline=col1)
            load3=can.create_oval(w/2+50-30,493-20-40-30-15+100, w/2+50,493-20-40-30+15+100,fill=col1,outline=col1)
            load4=can.create_rectangle(w/2-50+15,493-20-40-30-15+100, w/2+50-15,493-20-40-30+15+100,fill=col1,outline=col1)

            load=can.create_text(w/2,493-20-40-30+100,text="Done!",font=("FreeMono",13),fill="#000000")
        convert=0
        update_waves()


    root.after(1,convert_folder_to_audio)

def convert_file_to_audio():

    global can,load,load2,load3,load4,w,h
    global convert,input_file,st


    global theme


    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"



    if convert==2:




        ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
        sample_rate=44100
        channels=2
        bitrate="192k"



        if st==4:



            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill=col1)


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

                main()

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
                    main()

                    if st==4:

                        can.delete(load)

                        load=can.create_text(10,h-20-60-60,text=i,font=("FreeMono",13),fill=col1,anchor="w")
                    

                except:
                    pass


        except:
            pass


        if st==4:

            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            load2=can.create_oval(w/2-50,493-20-40-30-15+100, w/2-50+30,493-20-40-30+15+100,fill=col1,outline=col1)
            load3=can.create_oval(w/2+50-30,493-20-40-30-15+100, w/2+50,493-20-40-30+15+100,fill=col1,outline=col1)
            load4=can.create_rectangle(w/2-50+15,493-20-40-30-15+100, w/2+50-15,493-20-40-30+15+100,fill=col1,outline=col1)

            load=can.create_text(w/2,493-20-40-30+100,text="Done!",font=("FreeMono",13),fill="#000000")

        convert=0
        update_waves()

    root.after(1,convert_file_to_audio)

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
                data[song]=[0,0,"",False]



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




        vids = os.listdir("videos")
        all_songs = os.listdir("music")









        for s_ in all_songs:

            try:

                x=vids.index(s_[:-3]+"mp4")
                data[s_][3]=True

            except:
                data[s_][3]=False

        


        for v in vids:

            try:
                a=all_songs.index(v[:-3]+"mp3")

            except:
                os.remove("videos/"+v)












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


            for v in ar2:
                ar.pop(v)

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

    global st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,theme,save_,shuffle_ar,shuffle_st


    try:

        with open("data/save.json", "r") as file:
            data = json.load(file)


    except:
        data={"save":[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,theme,shuffle_ar,shuffle_st]}




    data["save"]=[st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,theme,shuffle_ar,shuffle_st]





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





def prog():

    global play_st,tm,start_time,can
    global ctime,tot_tm_
    global prog1,prog2
    global tvar
    global w



    global theme


    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"




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

    ctime=can.create_text(10,h-20-60-20+20+10+5,text=tt,font=("FreeMono",13),fill=col1,anchor="w")


    can.delete(prog1)
    can.delete(prog2)

    x_=tm*(w-20)/tot_tm_

    prog1=can.create_line(10,h-20-60-20+10+2+5, x_+10,h-20-60-20+10+2+5,fill=col1,width=4)



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
    global vid_label
    global lyric_st

    if play_st==1:




        prog()

        tm+=1

        if tm>=tot_tm_:

            play_video_st=0
            vid_label.place_forget()

            if loop==0:
                mvar+=1
            add_st=0
            frame2.place_forget()
            can2.focus_set()


            if mvar+1>len(songs):
                mvar=0

                can2["scrollregion"]=(0,0,w-7,h-240+30)


            tm=0
            
            current_playing=songs[mvar][0]
            play_st=1

            play_music("music/"+current_playing,tm)

            pp=1

            get_audio_duration("music/"+current_playing)

            #update_details(current_playing,1)

            lvar=0

            play_video_st=0
            lyric_st=0

            main()

    root.after(1000,timer)


def can3_b1(e):
    global sel_playlist,can3,frame2,add_st,current_playing,current_playlist,playlist,songs,mvar,tm



    add_st=0
    frame2.place_forget()

    for p in sel_playlist:

        if p[2]<=can3.canvasy(e.y)<=p[2]+50:

            if not current_playing=="":
                create_playlist(p[0],1,p[1])
                main()

                try:

                    v=playlist[p[0]].index(p[1])

                except:

                    if p[0]==current_playlist and st==2:

                        if len(songs)>0:
                            if mvar==len(songs):
                                mvar=0
                                current_playing=songs[mvar][0]
                                tm=0

                                play_music("music/"+current_playing,tm)
                                get_audio_duration("music/"+current_playing)

                                move_to_playing()
                            else:

                                current_playing=songs[mvar][0]
                                tm=0

                                play_music("music/"+current_playing,tm)
                                get_audio_duration("music/"+current_playing)
                        else:
                            current_playing=""
                            tm=0

                            play_music("music/"+current_playing,tm)
                            get_audio_duration("music/"+current_playing)




            add_st=0
            frame2.place_forget()
            can2.focus_set()

            main()



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
    global theme
    global shuffle_st,shuff,sort_val,sort_ar



    _search=0
    _npl=0


    search.place_forget()
    npl.place_forget()

    main()   



    can_sort.place_forget()

    frame2.place_forget()
    npl.place_forget()





    if st==2 and playlist_st==0:


        cx,cy=int(can2["width"])-10-5-20+10,5+10

        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:
            
            _npl=0
            npl.delete(0,tk.END)
            npl.place_forget()

            main()
            return



        if 10<=e.x<=int(can2["width"])-10:
            if 5<=e.y<=35:

                can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
                npl.delete(0,tk.END)
                _npl=1
                npl.place(in_=root,x=10+15+10,y=80-30+40+5+5+30-10)
                npl.focus_set()
                main()

                return

        # create new playlist


        cx,cy=int(can2["width"])/2-100,45+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:
            print("")

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
            

            cx,cy=int(can2["width"])-10-30+15,_pl[1]+10+15
            r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
            if r<=10:
                can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
                create_playlist(_pl[0],con=3)

                main()
                return

            if _pl[1]<=can2.canvasy(e.y)<=_pl[1]+50:
                can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))

                
                con=0
                if current_playlist==_pl[0]:
                    con=1
                current_playlist=_pl[0]
                playlist_st=1




                main()

                if con==0:


                    
                    try:




                        shuffle_st=0
                        shuff=0

                        sort_val=sort_ar[0][0]

                        main()


                        
                        current_playing=songs[0][0]
                        tm=0
                        mvar=0
                        play_music("music/"+current_playing,tm,1)
                        get_audio_duration("music/"+current_playing)

                        play_st=0
                        pygame.mixer.quit()
                        pp=0
                        main()
                        prog()
                    except:
                        pass

                search.delete(0,tk.END)
                search.place_forget()
                frame.place_forget()



                main()
                return




    #favourite

    for s in songs:


        y=s[-1]

        cx,cy=int(can2["width"])-10-25-15-25-15-25-15-25+12.5,y+12.5+12.5
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=12.5:


            update_details(s[0],0)
            main()
            return

    #playlist

    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=int(can2["width"])-10-25-15-25-15-25+12.5,y+12.5+12.5
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=12.5:

                if add_st==0:
                    add_st=1
                elif add_st==1:
                    add_st=0


                if add_st==1:



                    if theme=="red":
                        col1="#ff4137"
                        col2="#590400"

                    if theme=="mint":
                        col1="#32fca7"
                        col2="#003927"

                    elif theme=="cyan":
                        col1="#00ffff"
                        col2="#003538"



                    can4.delete("all")
                    can3.delete("all")
                    can5.delete("all")
                    can6.delete("all")


                    can4.create_text(450/2,20,text="Playlists",font=("FreeMono",13),fill=col1)
                    can4.create_line(2,38,450-2,38,fill=col2)

                    draw_round_rec(can4,2,2 ,450-2,80,15,col1,"",1)

                    draw_round_rec(can6,2,-10 ,450-2,15,15,col1,"",1)






                    can3.delete("all")

                    y=0
                    can3["scrollregion"]=(0,0,300-7,250-40)
                    sel_playlist=[]

                    for p in playlist:

                        ar=playlist[p]

                        can3.create_image(10,y+10,image=playlist2,anchor="nw")
                        can3.create_text(10+30+10,y+25,text=p,font=("FreeMono",13),anchor="w",fill=col1)
                        #can3.create_line(0,y+50,450-7,y+50,fill="#000000")

                        try:
                            v=ar.index(s[0])



                            can3.create_image(450-7-10-20,y+15, image=checked,anchor="nw")
                            
                        except:
                            pass




                        sel_playlist.append([p,s[0],y])
                        pl_var=[p,s[0],y]



                        y+=50



                    if y<250-40:


                        can3.create_line(2,0, 2,250-40,fill=col1)
                        can5.create_line(0,0, 0,250-40,fill=col1)
                    else:

                        can3.create_line(2,0, 2,y,fill=col1)
                        can5.create_line(0,0, 0,y,fill=col1)


                    if len(playlist)==0:
                        can3.create_text(10+30+10,(250-40)/2,text="No record",font=("FreeMono",13),anchor="w")

                    can3["scrollregion"]=(0,0,300-7,y)
                    frame2.place(in_=root,x=(w-450)/2,y=(h-(40+250-40+10))/2)

                    #can3.focus_set()

                    main()

                return


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

    #delete file


    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=int(can2["width"])-10-25+12.5,y+12.5+12.5
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=12.5:

            if current_playing==s[0]:

                try:

                    os.remove("music/"+s[0])
                    del_wave()
                    main()

                    if mvar==len(songs):

                        if not len(songs)==0:


                            mvar=0

                            current_playing=songs[mvar][0]



                            tm=0

                            play_music("music/"+current_playing,tm)
                            get_audio_duration("music/"+current_playing)




                            move_to_playing()

                    else:

                        if not len(songs)==0:
                            current_playing=songs[mvar][0]
                            tm=0

                            play_music("music/"+current_playing,tm)
                            get_audio_duration("music/"+current_playing)





                    if len(songs)==0:
                        current_playing=""
                except:
                    pass

            else:
                os.remove("music/"+s[0])
                del_wave()
                main()

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


            main()

            return



def move_to_playing():
    global current_playing,can2
    global songs

    if not current_playing=="":

        for s in songs:

            if s[0]==current_playing:

                t=len(songs)*50


                v=s[1]

                if s[1]+int(460*(h-30)/680)/2-25<t:
                    v=s[1]-(int(460*(h-30)/680)/2-25)

                pixel_value = int(v)
                scroll_region = can2.bbox("all")  # Get the bounding box of all content
                if scroll_region:
                    total_height = scroll_region[3] - scroll_region[1]  # Scrollable height
                    fraction = pixel_value / total_height if total_height > 0 else 0
                    can2.yview_moveto(fraction)
                    main()

def can_b3(e):
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

    global theme,theme_st
    global sa

    global theme
    global lyric_st,_lyric
    global text,lvar

    global play_video_st
    global music_details
    global vid_label
    global paused
    global cap
    global root_st




    if root_st==1:

        root_st=0

        w,h=1100,710

        root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")

        main()

        return



    _search=0
    _npl=0


    search.place_forget()
    npl.place_forget()

    main()   




    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"






    

    if theme_st==1:



        cx,cy=10+10+15,5+30+5+15

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=15:

            theme="red"
            load_im()

            theme_st=0

            main()
            return

        cx,cy=10+10+30+10+15,5+30+5+15

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=15:

            theme="mint"
            load_im()

            theme_st=0

            main()
            return


        cx,cy=10+10+30+10+30+10+15,5+30+5+15

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=15:

            theme="cyan"
            load_im()

            theme_st=0

            main()
            return




    


    cx,cy=10+15,5+15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:

        if theme_st==0:
            theme_st=1
        elif theme_st==1:
            theme_st=0
        main()


    can_sort.place_forget()
    main()




    add_st=0
    frame2.place_forget()

    xv=w/6




    if xv-60<=e.x<=xv+60:
        if 1<=e.y<=36:

            play_video_st=0
            vid_label.place_forget()

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()

            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=710
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")
            
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




            

            st=0
            main()



            try:


                current_playing=songs[0][0]
                tm=0
                tts=0
                mvar=0
                play_music("music/"+current_playing,tm,1)
                get_audio_duration("music/"+current_playing)

                play_st=0
                pygame.mixer.quit()
                pp=0
                main()
                prog()
            except:
                pass

            st=0
            main()


            
            return


    if xv*2-60<=e.x<=xv*2+60:
        if 1<=e.y<=36:




            play_video_st=0
            vid_label.place_forget()

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()


            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=710
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")

            
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
            



            st=1
            main()



            try:
                current_playing=songs[0][0]
                tm=0
                tts=0
                mvar=0
                play_music("music/"+current_playing,tm,1)
                get_audio_duration("music/"+current_playing)

                play_st=0
                pygame.mixer.quit()
                pp=0
                main()
                prog()
            except:
                pass


            st=1
            main()

            return

    if xv*3-60<=e.x<=xv*3+60:
        if 1<=e.y<=36:


            play_video_st=0
            vid_label.place_forget()

            lst=1
            main()

            _search=0
            sort_st=0
            can_sort.place_forget()


            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))

            main()

            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            h=710
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")

            
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
                current_playing=""
                pl_st=0


                
                try:
                    current_playing=""
                    play_st=0
                    pygame.mixer.quit()
                    pp=0
                    main()
                except:
                    pass
                

            st=2

            main()

            return


    if xv*4-60<=e.x<=xv*4+60:
        if 1<=e.y<=36:



            play_video_st=0
            vid_label.place_forget()


            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()



            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=710
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")

            
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()


            st=3
            main()



            try:
                current_playing=songs[0][0]
                tm=0
                tts=0
                mvar=0
                play_music("music/"+current_playing,tm,1)
                get_audio_duration("music/"+current_playing)

                play_st=0
                pygame.mixer.quit()
                pp=0
                main()
                prog()
            except:
                pass

            st=3
            main()

            return


    if xv*5-60<=e.x<=xv*5+60:
        if 1<=e.y<=36:



            play_video_st=0
            vid_label.place_forget()


            lst=1
            _search=0
            sort_st=0
            can_sort.place_forget()

            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=710
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")

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

            current_playlist=""



            try:
                current_playing=""
                play_st=0
                pygame.mixer.quit()
                pp=0
                main()
            except:
                pass





            return



    if h-20-60-20+10+2+5-10<=e.y<=h-20-60-20+10+2+5+10:



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


    #play/pause


    cx,cy=w/2,h-20-30-30+5+10+30

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=30:

        if st==2 and playlist_st==0 and pl_st==0:
            pass
        else:

            if not current_playing=="":

                if pp==0:
                    pp=1
                    play_st=1

                    paused=False

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

    cx,cy=w/2-30-30-30+15,h-20-30-15+5+10+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

        if st==2 and playlist_st==0 and pl_st==0:
            return

        if st==4:
            return


        if loop==0:

            mvar-=1


        tm=0
        
        current_playing=songs[mvar][0]
        play_st=1

        play_music("music/"+current_playing,tm)

        pp=1

        get_audio_duration("music/"+current_playing)


        play_video_st=0

        vid_label.place_forget()



        lvar=0
        lyric_st=0

        main()

        move_to_playing()
        return

    #next


    cx,cy=w/2+30+30+15,h-20-30-15+5+10+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:




        if st==2 and playlist_st==0 and pl_st==0:
            return

        if st==4:
            return


        if loop==0:

            if mvar+1==len(songs):
                mvar=0
            else:
                mvar+=1


        tm=0
        
        current_playing=songs[mvar][0]
        play_st=1

        play_music("music/"+current_playing,tm)

        pp=1

        get_audio_duration("music/"+current_playing)

        lvar=0
        play_video_st=0
        lyric_st=0


        vid_label.place_forget()

        main()

        move_to_playing()
        return



    


    #search

    cx,cy=w-10-5-20+10,45+10+30

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=10:
        search.delete(0,tk.END)
        search.place_forget()
        can.focus_set()
        _search=0

        main()


        return

    if 10<=e.x<=w-10-5-30:
        if 40+30-10-5<=e.y<=40+30+30-10-5:

            _search=1


            search.place(in_=root,x=10+15,y=45+30-10-5)
            search.focus_set()

            main()

            return


    #list

    cx,cy=10+15,h-20-30-15+5+15+10
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

        if lst==0:
            lst=1
            text.place_forget()

            play_video_st=0
            vid_label.place_forget()

        elif lst==1:


            lst=0
            _search=0
            frame.place_forget()
        main()


    #volume
    if w-10-100-10<=e.x<=w-10+10:
        if h-20-30+5-10+10<=e.y<=h-20-30+5+10+10:

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

    cx,cy=10+30+20+15,h-20-30-15+5+15+10

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:

        if sort_st==0:
            sort_st=1
        elif sort_st==1:
            sort_st=0




        if sort_st==1:

            if sort_val=="":
                sort_val=sort_ar[0][0]



            if theme=="red":
                col1="#ff4137"
                col2="#590400"

            if theme=="mint":
                col1="#32fca7"
                col2="#003927"

            elif theme=="cyan":
                col1="#00ffff"
                col2="#003538"






            can_sort.delete("all")

            draw_round_rec(can_sort,2,2, 250-2,160-2,15,"#000000",col1,0)

            can_sort.create_text(125,15,text="Sort",font=("FreeMono",13),fill=col1)


            can_sort.create_line(2,30, 250-2,30,fill=col2 )
            y=30
            for _ in sa:

                can_sort.create_text(10,y+15,text=_,font=("FreeMono",13),fill=col1,anchor="w")

                #can_sort.create_line(0,y+30,250,y+30,fill="#000000")

                sort_ar.append([_,y])

                y+=30



            for s in sort_ar:

                if s[0]==sort_val:

                    _sort=can_sort.create_image(250-5-20,s[1]+5,image=checked,anchor="nw")


            can_sort.place(in_=root,x=10+30+20+30,y=h-20-30-15+5+10-160)

            shuff=0
            shuffle_st=0

            main()
        else:
            can_sort.place_forget()

        return



    #shuffle




    cx,cy=10+30+20+30+20+15,h-20-30-15+5+15+10

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:
        loop=0

        if shuffle_st==0:
            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            mvar=0
            shuffle_st=1
            shuff=1

            sort_val=""
            sort_st=0

            main()
        elif shuffle_st==1:
            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()

        elif shuffle_st==2:
            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))
            shuffle_st=0
            shuff=0
            sort_val=sort_ar[0][0]            
            main()
        




    #loop

    cx,cy=w/2+30+30+30+20+10+15,h-20-30-15+5+15+10

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:



        if loop==0:
            if current_playing!="":
                loop=1
        elif loop==1:
            loop=0

        main()










    #add songs

    if st==4:

        yv=((int(460*(h-30)/680)+10+30)-(30+30+30))/2
        yv+=39+30+15



        #can.create_rectangle(w/2-150,yv, w/2+150,yv+30, fill=col1)


        cx,cy=w/2-80,yv+15

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:

            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            input_folder=filedialog.askdirectory(title="Select a Folder")

            if not input_folder=="":
                convert=1



            return


        cx,cy=w/2+80,yv+15

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            input_folder=filedialog.askdirectory(title="Select a Folder")

            if not input_folder=="":
                convert=1

            return


        if w/2-80<=e.x<=w/2+80:
            if yv<=e.y<=yv+30:
                can.delete(load)
                can.delete(load2)
                can.delete(load3)
                can.delete(load4)
                input_folder=filedialog.askdirectory(title="Select a Folder")

                if not input_folder=="":
                    convert=1


                return


















        cx,cy=w/2-80,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            input_file=filedialog.askopenfilename()

            if not input_file=="":
                convert=2



            return



        cx,cy=w/2+80,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            input_file=filedialog.askopenfilename()
            if not input_file=="":
                convert=2


            return



        if w/2-80<=e.x<=w/2+80:
            if yv+60<=e.y<=yv+30+60:
                can.delete(load)
                can.delete(load2)
                can.delete(load3)
                can.delete(load4)
                input_file=filedialog.askopenfilename()

                if not input_file=="":
                    convert=2


                return




    #lyrics

    x=w/2
    y=520+30



    cx,cy=x-40+15,y+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

        if lyric_st==0:
            lyric_st=1
        elif lyric_st==1:
            lyric_st=0
            text.place_forget()

        lvar=0

        main()
        return


    if play_video_st==0:

        cx,cy=x+40-30+15,y+15
        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:

            if lyric_st==0:
                lyric_st=1
            elif lyric_st==1:
                lyric_st=0
                text.place_forget()

            lvar=0

            main()
            return


        if x-40+15<=e.x<=x+40-15:
            if y<=e.y<=y+30:


                if lyric_st==0:
                    lyric_st=1
                elif lyric_st==1:
                    lyric_st=0
                    text.place_forget()

                lvar=0

                main()
                return


        if lyric_st==1:


            cx,cy=x+40+10-5+12.5,y+2.5+12.5
            r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
            if r<=12.5:

                if not current_playing=="":
                    update_details(current_playing,2,_lyric)

                    lvar=0

                    main()




                return



    #play_video

    cx,cy=10+90+60+15,h-20-30-15+5+10+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

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
            play_video_st=0
            vid_label.place_forget()
            main()




    #minimize

    cx,cy=w-10-25-15-25+12.5,5+2.5+12.5

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

    if r<=12.5:

        root_st=1

        main()


    #quit

    cx,cy=w-10-25+12.5,5+2.5+12.5

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

    if r<=12.5:

        root.destroy()

        



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


    


vol1,vol2=0,0
def check_volume():
    global current_volume
    global can,vol1,vol2


    global theme


    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"


    if volume.GetMasterVolumeLevelScalar()!=current_volume:

        current_volume=volume.GetMasterVolumeLevelScalar()

        can.delete(vol1)
        can.delete(vol2)

        r=(w-10)-(w-10-100)

        vol1=can.create_line(w-10-100,h-20-30+5+10 ,w-10-100+current_volume*r,h-20-30+5+10,fill=col1,width=3)

        vol2=can.create_text(w-10,h-20-30+5+20+10-2,text=str(int(current_volume*100))+" %",fill=col1,font=("FreeMono",13),anchor="e")


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
def main():

    global can,st,w,h,wd
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
    global circle2,circle3,circle4

    global expand,expand2,expand_st

    global playlist4

    global theme,theme_,theme_st
    global style,style2

    global red,mint,cyan
    global paste
    global lyric_st
    global add_video1,add_video2,add_video3
    global play_video_st
    global text
    global quit,minimize
    global root_st

    global vid_label,play_video_st
    global circlex



    if theme=="red":
        col1="#ff4137"
        col2="#590400"
        col3="#390200"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"
        col3="#002016"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"
        col3="#001e20"




    can["bg"]="#333333"


    if root_st==1:

        root.geometry(str(50)+"x"+str(50)+"+"+str(wd-3-50)+"+"+str(ht-51-50))

        can.delete("all")

        can.create_image(0,0, image=circlex, anchor="nw")

        can.create_image(10,10, image=musical_note2, anchor="nw")

        frame.place_forget()
        search.place_forget()
        vid_label.place_forget()
        play_video_st=0

        return



    update_details()
    create_playlist()




    if shuff==1 or shuff==2:
        sort_val=""






    style.configure("My.Vertical.TScrollbar", gripcount=0, background=col1,
                    troughcolor='#000000', borderwidth=0, bordercolor='#000000',
                    lightcolor='#000000',relief="flat", darkcolor='#000000',
                    arrowsize=7)


    style2.configure("My.Vertical.TScrollbar2", gripcount=0, background=col1,
                    troughcolor='#000000', borderwidth=0, bordercolor='#000000',
                    lightcolor='#000000',relief="flat", darkcolor='#000000',
                    arrowsize=7)



    if root.wm_attributes("-fullscreen")==1:



        frame["width"]=w-20-2
        frame["height"]=int(460*(h-30)/680)+30

        can2["width"]=w-7-20-2
        can2["height"]=int(460*(h-30)/680)+30
    else:

        frame["width"]=w-20-2
        frame["height"]=int(460*(h-30)/680)

        can2["width"]=w-7-20-2
        can2["height"]=int(460*(h-30)/680)


    can["width"]=w
    can["height"]=h







    
    #create_rectangle(can,0, 0, w, h, fill='#111111', alpha=.65)


    



    xv=w/6
    x=xv


    label=["All Songs","Favourites","Playlist","Most Played","Add Song"]

    for l in range(len(label)):

        col=col1

        if l==st:
            col="#000000"


            can.create_image(x-60,5,image=circle3,anchor="nw")
            can.create_image(x+60-30,5,image=circle3,anchor="nw")


            can.create_rectangle(x-60+15,5, x+60-15,35-1, fill=col1,outline=col1)









        #can.create_rectangle(x-50,20-10, x+50,20+10, outline=col1)



        can.create_text(x,20,text=label[l],fill=col,font=("FreeMono",13),anchor="c")



        x+=xv





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

        # Sort the items alphabetically (case-insensitive)
        sorted_items = sorted(items, key=str.lower, reverse=descending)

        return sorted_items     



    


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







    can2.delete("all")
    #can2.create_image(-10,can2.canvasy(-(80-30+40))-h,image=wallpaper,anchor="nw")
    #can2.create_image(-10,can2.canvasy(-(80-30+40)),image=wallpaper,anchor="nw",tags="fixed_image")
    #can2.create_image(-10,can2.canvasy(-(80-30+40))+h,image=wallpaper,anchor="nw")
    #create_rectangle(can2,0, int(can2.canvasy(0))-h, int(can2["width"]), int(can2.canvasy(int(can2["height"])))+h, fill='#111111', alpha=.65)



    if lst==1 and st!=4:

        
        pass
        #can.create_line(10,80-30+40+5+int(can2["height"]),w-10,80-30+40+5+int(can2["height"]),fill=col2)

    y=0


    if st==0:

        songs=[]
        

        for song in all_songs:

            scon=0


            sval=search_var.lower()

            if sval.find(" ")!=-1:

                s_ar=sval.split(" ")

                for sv in s_ar:

                    if song.lower().find(sv)!=-1:
                        scon=1
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

                    can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                    can2.create_image(0,y,image=circle2,anchor="nw")
                    can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                    can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill=col1,outline=col1)

                    can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                    col="#000000"
                else:
                    can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                    col=col1


                can2.create_text(10+30,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                if song==current_playing:
                    can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"])-40,y+45,fill=col1,outline=col1)
                    can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                else:
                    can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"]),y+45,fill="#000000",outline="#000000")


                _del_=delete
                if song==current_playing:
                    _del_=delete2

                can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")


                if music_details[song][3]==True:

                    if song==current_playing:
                        can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video3,anchor="nw")
                    else:

                       can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video2,anchor="nw")
                elif music_details[song][3]==False:

                    can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video1,anchor="nw")





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
                    


                can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_pl_,anchor="nw")




                if music_details[song][0]==0:

                    _fv_=favourite1

                    if song==current_playing:
                        _fv_=favourite1_


                elif music_details[song][0]==1:


                    _fv_=favourite2

                    if song==current_playing:
                        _fv_=favourite2_


                can2.create_image(int(can2["width"])-10-25-15-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")



                if not song==current_playing:

                    can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col2)

                ar=[song,y]

                songs.append(ar)

                y+=50

        if len(songs)==0:
            
            if search_var=="":

                current_playing=""
            

            can2.create_text((w-7)/2,int(460*(h-30)/680)/2,text="No Record!",font=("FreeMono",13),fill=col1)

    elif st==1:
        songs=[]


        for song in all_songs:


            scon=0


            sval=search_var.lower()

            if sval.find(" ")!=-1:

                s_ar=sval.split(" ")

                for sv in s_ar:

                    if song.lower().find(sv)!=-1:
                        scon=1
                        break
            else:
                if song.lower().find(sval)!=-1:
                    scon=1

            if scon==1:

                if music_details[song][0]==1:

                    if song==current_playing:
                        can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                        can2.create_image(0,y,image=circle2,anchor="nw")
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                        can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill=col1,outline=col1)
                        can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                        col="#000000"
                    else:
                        can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                        col=col1



                    can2.create_text(10+30,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                    if song==current_playing:
                        can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"])-40,y+45,fill=col1,outline=col1)
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                    else:
                        can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"]),y+45,fill="#000000",outline="#000000")



                    _del_=delete
                    if song==current_playing:
                        _del_=delete2

                    can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")





                    if music_details[song][3]==True:

                        if song==current_playing:
                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video3,anchor="nw")
                        else:

                           can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video2,anchor="nw")
                    elif music_details[song][3]==False:

                        can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video1,anchor="nw")



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
                        


                    can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_pl_,anchor="nw")




                    if music_details[song][0]==0:

                        _fv_=favourite1

                        if song==current_playing:
                            _fv_=favourite1_


                    elif music_details[song][0]==1:


                        _fv_=favourite2

                        if song==current_playing:
                            _fv_=favourite2_


                    can2.create_image(int(can2["width"])-10-25-15-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")



                    if not song==current_playing:

                        can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col2)





                    ar=[song,y]

                    songs.append(ar)

                    y+=50


        if len(songs)==0:

            if search_var=="":
                current_playing=""
            
            can2.create_text((w-7)/2,int(460*(h-30)/680)/2,text="No Record!",font=("FreeMono",13),fill=col1)
    elif st==2:


        if playlist_st==0:

            if _search==1:

                can.create_oval(10,40, 10+30,40+30,fill="#000000",outline="#000000")
                can.create_oval(w-10-30,40, w-10,40+30,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40, w-10-15,40+30,fill="#000000",outline="#000000")






            can.create_arc(10,40, 10+30,40+30, style=tk.ARC,start=90,extent=180,outline=col1)
            can.create_arc(w-10-30,40, w-10,40+30, style=tk.ARC,start=270,extent=180,outline=col1)

            can.create_line(10+15,40, w-10-15,40, fill=col1)
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill=col1)



            can.create_text(30+20+5,40+15,text="Search",font=("FreeMono",13),fill=col1,anchor="w")



            can.create_image(w-10-5-20,40+5,image=cancel,anchor="nw")

            can.create_image(30,40+5,image=search_im,anchor="nw")





            #can.create_line(10,70,w-10,70,fill=col1)
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill=col1)

            frame.place(in_=root,x=11,y=80-30+40)







            can2.create_rectangle(0,0, int(can2["width"]),95,fill=col3,outline=col3)





            y=5



            if _npl==1:

                can2.create_oval(10,y, 10+30,y+30, fill="#000000",outline="#000000")
                can2.create_oval(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30,fill="#000000",outline="#000000")

                can2.create_rectangle(10+15,y, int(can2["width"])-10-15,y+30,fill="#000000",outline="#000000")



            can2.create_arc(10,y, 10+30,y+30, style=tk.ARC,start=90,extent=180,outline=col1)
            can2.create_arc(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30, style=tk.ARC,start=270,extent=180,outline=col1)

            can2.create_line(10+15,y, int(can2["width"])-10-15,y, fill=col1)
            can2.create_line(10-1+15,y+30, int(can2["width"])-10-15,y+30, fill=col1)







            can2.create_text(30,y+15,text="New Playlist",font=("FreeMono",13),fill=col1,anchor="w")



            can2.create_image(int(can2["width"])-10-5-20,y+5,image=cancel,anchor="nw")


            y+=40






            #can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30, outline=col1)

            can2.create_image(int(can2["width"])/2-100-15,y,image=circle3,anchor="nw")
            can2.create_image(int(can2["width"])/2+100-15,y,image=circle3,anchor="nw")

            can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30-1,fill=col1,outline=col1)


            can2.create_text(int(can2["width"])/2,y+15,text="Create New Playlist",font=("FreeMono",13),fill="#111111")

            y+=30+20

            can2.create_line(0,y, int(can2["width"])-3,y,fill=col2)

            _playlist=[]

            for pl in playlist:


                scon=0


                sval=search_var.lower()

                if sval.find(" ")!=-1:

                    s_ar=sval.split(" ")

                    for sv in s_ar:

                        if pl.lower().find(sv)!=-1:
                            scon=1
                            break
                else:
                    if pl.lower().find(sval)!=-1:
                        scon=1


                if scon==1:
                    

                    if current_playlist==pl:
                        col="#000000"
                        can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                        can2.create_image(0,y,image=circle2,anchor="nw")
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                        can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill=col1,outline=col1)
                        _pl_=playlist3
                        _del_=delete2
                    else:
                        col=col1

                        _pl_=playlist2
                        _del_=delete



                    can2.create_image(10,y+10,image=_pl_,anchor="nw")




                    can2.create_text(10+30+5,y+25,text=pl,font=("FreeMono",13),fill=col,anchor="w")

                    can2.create_image(int(can2["width"])-10-30,y+10,image=_del_,anchor="nw")

                    if current_playlist!=pl:
                        can2.create_line(0,y+50, int(can2["width"]),y+50,fill=col2)

                    _playlist.append([pl,y])



                    y+=50

            if len(_playlist)==0:
                
                can2.create_text(int(can2["width"])/2,y+(int(460*(h-30)/680)-y)/2,text="No Record",font=("FreeMono",13),fill=col1)



        elif playlist_st==1:

            songs=[]


            ar=playlist[current_playlist]




            for song in all_songs:



                scon=0


                sval=search_var.lower()

                if sval.find(" ")!=-1:

                    s_ar=sval.split(" ")

                    for sv in s_ar:

                        if song.lower().find(sv)!=-1:
                            scon=1
                            break
                else:
                    if song.lower().find(sval)!=-1:
                        scon=1


                if scon==1:

                    try:
                        v=ar.index(song)

                    


                        if song==current_playing:
                            can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                            can2.create_image(0,y,image=circle2,anchor="nw")
                            can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                            can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill=col1,outline=col1)
                            can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                            col="#000000"
                        else:
                            can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                            col=col1



                        can2.create_text(10+30,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                        if song==current_playing:
                            can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"])-40,y+45,fill=col1,outline=col1)
                            can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                        else:
                            can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"]),y+45,fill="#000000",outline="#000000")



                        _del_=delete
                        if song==current_playing:
                            _del_=delete2

                        can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")




                        if music_details[song][3]==True:

                            if song==current_playing:
                                can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video3,anchor="nw")
                            else:

                               can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video2,anchor="nw")
                        elif music_details[song][3]==False:

                            can2.create_image(int(can2["width"])-10-25-15-25,y+12.5,image=add_video1,anchor="nw")




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
                            


                        can2.create_image(int(can2["width"])-10-25-15-25-15-25,y+12.5,image=_pl_,anchor="nw")




                        if music_details[song][0]==0:

                            _fv_=favourite1

                            if song==current_playing:
                                _fv_=favourite1_


                        elif music_details[song][0]==1:


                            _fv_=favourite2

                            if song==current_playing:
                                _fv_=favourite2_


                        can2.create_image(int(can2["width"])-10-25-15-25-15-25-15-25,y+12.5,image=_fv_,anchor="nw")




                        if not song==current_playing:

                            can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col2)


                        songs.append([song,y])

                        y+=50
                    except:
                        pass
            if len(songs)==0:
                if search_var=="":
                    current_playing=""
                
                can2.create_text((w-7)/2,int(460*(h-30)/680)/2,text="No Record!",font=("FreeMono",13),fill=col1)

    elif st==3:
        songs=[]

        ar_=[]
        for song in all_songs:

            scon=0


            sval=search_var.lower()

            if sval.find(" ")!=-1:

                s_ar=sval.split(" ")

                for sv in s_ar:

                    if song.lower().find(sv)!=-1:
                        scon=1
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
                can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                can2.create_image(0,y,image=circle2,anchor="nw")
                can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill=col1,outline=col1)
                can2.create_image(0,y+10,image=musical_note1,anchor="nw")
                col="#000000"
            else:
                can2.create_image(0,y+10,image=musical_note2,anchor="nw")
                col=col1



            can2.create_text(10+30,y+25,text=song[0],font=("FreeMono",13),fill=col,anchor="w")
            if song[0]==current_playing:
                can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"])-40,y+45,fill=col1,outline=col1)
                can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
            else:
                can2.create_rectangle(int(can2["width"])-25*4-15*4,y+5, int(can2["width"]),y+45,fill="#000000",outline="#000000")







            _del_=delete
            if song[0]==current_playing:
                _del_=delete2

            can2.create_image(int(can2["width"])-10-25,y+12.5,image=_del_,anchor="nw")

            if music_details[song[0]][3]==True:

                if song[0]==current_playing:
                    can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=add_video3,anchor="nw")
                else:

                   can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=add_video2,anchor="nw")
            elif music_details[song[0]][3]==False:

                can2.create_image(int(can2["width"])-10-25-20-25,y+12.5,image=add_video1,anchor="nw")






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
                


            can2.create_image(int(can2["width"])-10-25-20-25-20-25,y+12.5,image=_pl_,anchor="nw")




            if music_details[song[0]][0]==0:

                _fv_=favourite1

                if song[0]==current_playing:
                    _fv_=favourite1_


            elif music_details[song[0]][0]==1:


                _fv_=favourite2

                if song[0]==current_playing:
                    _fv_=favourite2_


            can2.create_image(int(can2["width"])-10-25-20-25-20-25-20-25,y+12.5,image=_fv_,anchor="nw")



            if not song[0]==current_playing:

                can2.create_line(0,y+50,int(can2["width"]),y+50,fill=col2)


            ar=[song[0],y]

            songs.append(ar)

            y+=50

        if len(songs)==0:

            if search_var=="":
                current_playing=""
            
            can2.create_text((w-7)/2,int(460*(h-30)/680)/2,text="No Record!",font=("FreeMono",13),fill=col1)



    """
    if y<=int(460*(h-30)/680):
        hex(can2,-30,-30,w+60,int(can2["height"])+60,30,"#390200","#000000")


    else:

        hex(can2,-30,-30,w+60,y+60,30,"#390200","#000000")

    """

    can2["scrollregion"]=(0,0,w-7,y)



    yyy=y

    draw_can()

    if play_video_st==1:
        pass
        #can.create_rectangle(0,46, w,550,fill="#000000",outline="#000000")

        #draw_round_rec(can,10,46,w-10-1,550,15,"#000000",col1,0)


    draw_round_rec(can,1,1,w-1-1,h-1-1,20,col1,"",1)


    if lst==0:

        if not playlist_st==0:

            _search=0
            search.place_forget()



            _npl=0
            npl.place_forget()

    
    if lyric_st==0:
        text.place_forget()

    if _search==0 and _npl==0:
        can.focus_set()



    can.create_image(w-10-25,5+2.5,image=quit,anchor="nw")
    can.create_image(w-10-25-15-25,5+2.5,image=minimize,anchor="nw")












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
    global _search,_npl,npl
    global circle2,circle3,circle4

    global expand,expand2,expand_st

    global playlist4

    global theme,theme_,theme_st
    global style,style2

    global red,mint,cyan
    global paste
    global lyric_st

    global play_video1,play_video2,play_video_st

    global eye


    can.delete("all")

    #hex(can,-40,-40,w+40,h+40,40,"#111111","#000000")






    if shuff==1 or shuff==2:
        sort_val=""



    if theme=="red":
        col1="#ff4137"
        col2="#590400"
        col3="#390200"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"
        col3="#002016"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"
        col3="#001e20"


    draw_round_rec(can,0,0,w-1,h-1,20,"#000000","#000000",0)






    ar=[]





    a_=90
    r=20

    cx,cy=w-r,40+r



    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy


        a_+=1


        ar.append(x)
        ar.append(y)



    a_=180

    cx,cy=r,40+r



    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy


        a_+=1


        ar.append(x)
        ar.append(y)

    #can.create_line(ar,fill=col1)






    search["fg"]=col1
    search["insertbackground"]=col1


    npl["fg"]=col1
    npl["insertbackground"]=col1
 





    #lyrics

    if lst==0:

        x=w/2
        y=520+30



        if lyric_st==0:


            can.create_image(x-40,y,image=circle4,anchor="nw")
            can.create_image(x+40-30,y,image=circle4,anchor="nw")


            can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col2,outline=col2)

            can.create_text(x,y+15,text="Lyrics",font=("FreeMono",13),fill=col1)

        elif lyric_st==1:


            can.create_image(x-40,y,image=circle3,anchor="nw")
            can.create_image(x+40-30,y,image=circle3,anchor="nw")


            can.create_rectangle(x-40+15,y, x+40-15,y+30-1, fill=col1,outline=col1)

            can.create_text(x,y+15,text="Lyrics",font=("FreeMono",13),fill="#000000")


            can.create_image(x+40+10-5,y+2.5,image=paste,anchor="nw")




    if lst==1:


        if st==4:
            pass

        else:





            if _search==1:

                can.create_oval(10,40+30-10-5, 10+30,40+30+30-10-5,fill="#000000",outline="#000000")
                can.create_oval(w-10-30,40+30-10-5, w-10,40+30+30-10-5,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40+30-10-5, w-10-15,40+30+30-10-5,fill="#000000",outline="#000000")




            can.create_arc(10,40+30-10-5, 10+30,40+30+30-10-5, style=tk.ARC,start=90,extent=180,outline=col1)
            can.create_arc(w-10-30,40+30-10-5, w-10,40+30+30-10-5, style=tk.ARC,start=270,extent=180,outline=col1)

            can.create_line(10+15,40+30-10-5, w-10-15,40+30-10-5, fill=col1)
            can.create_line(10-1+15,40+30+30-10-5, w-10-15,40+30+30-10-5, fill=col1)



            can.create_image(w-10-5-20,40+5+30-10-5,image=cancel,anchor="nw")

            #draw_round_rec(can,10,40, w-10,40+30,10,"#000000",col1,0)

            can.create_text(30+20+5,40+15+30-10-5,text="Search",font=("FreeMono",13),fill=col1,anchor="w")



            can.create_image(30,45+30-10-5,image=search_im,anchor="nw")

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





                can.create_polygon(ar,fill=col3,outline=col3)





            draw_round_rec(can,10,80-10-30+40+30-10,w-10,80-30+40+int(460*(h-30)/680)+10+30-10,15,col1,"",1)


            #can.create_line(10,70,w-10,70,fill=col1)
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill=col1)

            frame.place(in_=root,x=11,y=80-30+40+30-10)
    else:
        
        if playlist_st==0 and st==2:
            if _search==1:

                can.create_oval(10,40+30-10-5, 10+30,40+30+30-10-5,fill="#000000",outline="#000000")
                can.create_oval(w-10-30,40+30-10-5, w-10,40+30+30-10-5,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40+30-10-5, w-10-15,40+30+30-10-5,fill="#000000",outline="#000000")







            can.create_arc(10,40+30-10-5, 10+30,40+30+30-10-5, style=tk.ARC,start=90,extent=180,outline=col1)
            can.create_arc(w-10-30,40+30-10-5, w-10,40+30+30-10-5, style=tk.ARC,start=270,extent=180,outline=col1)

            can.create_line(10+15,40+30-10-5, w-10-15,40+30-10-5, fill=col1)
            can.create_line(10-1+15,40+30+30-10-5, w-10-15,40+30+30-10-5, fill=col1)



            can.create_image(w-10-5-20,40+5+30-10-5,image=cancel,anchor="nw")

            #draw_round_rec(can,10,40, w-10,40+30,10,"#000000",col1,0)

            can.create_text(30+20+5,40+15+30-10-5,text="Search",font=("FreeMono",13),fill=col1,anchor="w")



            can.create_image(30,45+30-10-5,image=search_im,anchor="nw")


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





                can.create_polygon(ar,fill=col3,outline=col3)


            draw_round_rec(can,10,80-10-30+40+30-10,w-10,80-30+40+int(460*(h-30)/680)+10+30-10,20,col1,"",0)


            #can.create_line(10,70,w-10,70,fill=col1)
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill=col1)

            frame.place(in_=root,x=11,y=80-30+40+30-10)
        elif st==4:
            pass
        else:

            can.create_image((w-420)/2,39+(int(460*(h-30)/680)+10+30)/2-210+10+15,image=note,anchor="nw")

    

    if lyric_st==1:
        show_lyrics()











    can.create_image(10,5, image=theme_,anchor="nw")








    xv=w/6
    x=xv


    label=["All Songs","Favourites","Playlist","Most Played","Add Song"]

    for l in range(len(label)):

        col=col1

        if l==st:
            col="#000000"


            can.create_image(x-60,5+1,image=circle3,anchor="nw")
            can.create_image(x+60-30,5+1,image=circle3,anchor="nw")


            can.create_rectangle(x-60+15,5+1, x+60-15,35-1+1, fill=col1,outline=col1)









        #can.create_rectangle(x-50,20-10, x+50,20+10, outline=col1)



        can.create_text(x,20+1,text=label[l],fill=col,font=("FreeMono",13),anchor="c")



        x+=xv






    if playlist_st==0 and st==2 and pl_st==0 :

        pass

    else:

        #can.create_text(10,h-20-60-20-27,text=current_playlist,font=("FreeMono",13),anchor="w",fill=col1)


        #can.create_text(10,h-20-60-20-27-30,text=current_playlist,font=("FreeMono",13),anchor="w",fill=col1)



        def get_text_length(canvas, text, font_name, font_size):
            # Create a tkinter font object with the given font name and size
            text_font = font.Font(family=font_name, size=font_size)

            # Measure the width of the text in pixels
            text_width = text_font.measure(text)
            return text_width  
        if len(current_playlist)>0:


            
            length_in_pixels = get_text_length(can, current_playlist, "FreeMono", 13) 

            can.create_image(10,h-20-60-20-27-15+3+10+3+2+2, image=circle3,anchor="nw")
            can.create_image(10+15+length_in_pixels-15+30,h-20-60-20-27-15+3+10+3+2+2, image=circle3,anchor="nw")
            can.create_rectangle(10+15,h-20-60-20-27-15+3+10+3+2+2, 10+15+length_in_pixels+30,h-20-60-20-27+14+3+10+3+2+2,fill=col1,outline=col1)
            can.create_image(10+15,h-20-60-20-27-15+3+10+5+3+2+2, image=playlist4,anchor="nw")

            can.create_text(10+15+30,h-20-60-20-27+3+10+3+2+2,text=current_playlist,font=("FreeMono",13,),anchor="w",fill="#000000")
                  
            can.create_text(10+15+length_in_pixels+15+10+30,h-20-60-20-27+3+10+3+2+2,text=current_playing,font=("FreeMono",13),anchor="w",fill=col1)
        else:
            can.create_text(10,h-20-60-20-27+3+10+3+2+2,text=current_playing,font=("FreeMono",13),anchor="w",fill=col1)


        if not current_playing=="":

            try:

                n=music_details[current_playing][1]


                if n==1:
                    t=str(n)
                elif n>1000:


                    t=str(round(n/1000,2))+"K"
                elif n>10000000:


                    t=str(round(n/1000000,2))+"M"
                elif n>10000000000:


                    t=str(round(n/1000000000,2))+"B"
                else:

                    t=str(n)


                l=get_text_length(can, t, "FreeMono", 13)

                can.create_rectangle(w-10-26-5-l-10, h-20-60-20-27+3-13+10+3+2, w, h-20-60-20-27+3+13+10+3+2,fill="#000000",outline="#000000")

                can.create_text(w-10-26-5,h-20-60-20-27+3+10+3+2,text=t,font=("FreeMono",13),anchor="e",fill=col1)

                can.create_image(w-10-26,h-20-60-20-27+3-13+10+3+2,image=eye,anchor="nw")

            except:
                pass

    can.create_line(10,h-20-60-20+10+2+5,w-10,h-20-60-20+10+2+5,fill=col2,width=4)

    
    if st==2 and playlist_st==0:
        pass
    elif st==4:
        pass
    else:
        can.create_text(w-10,h-20-60-20+20+10+5,text=tot_tm,font=("FreeMono",13),anchor="e",fill=col1)



    can.create_image(w/2-30,h-20-30-30+5+10, image=circle,anchor="nw")

    if pp==0:
        can.create_image(w/2-15+2,h-20-30-15+5+10, image=play,anchor="nw")
    elif pp==1:
        can.create_image(w/2-15,h-20-30-15+5+10, image=pause,anchor="nw")










    if lst==0:
        global sig_,sig2

        can.delete(sig_)

        try:

            if st!=4:
                sig_=can.create_line(sig2,fill=col1)

        except:
            pass

        can.create_image(10,h-20-30-15+5+10,image=list1,anchor="nw")
    elif lst==1:
        can.create_image(10,h-20-30-15+5+10,image=list2,anchor="nw")


    if lyric_st==1:
        can.delete(sig_)




    if sort_val!="":

        can.create_image(10+30+20,h-20-30-15+5+10,image=sort,anchor="nw")

    else:
        can.create_image(10+30+20,h-20-30-15+5+10,image=sort2,anchor="nw")

    if shuff==0:

        can.create_image(10+30+20+30+20,h-20-30-15+5+10,image=shuffle1,anchor="nw")
    elif shuff==1:
        can.create_image(10+30+20+30+20,h-20-30-15+5+10,image=shuffle2,anchor="nw")





    can.create_line(w-10-100,h-20-30+5+10, w-10,h-20-30+5+10,fill=col2,width=3)

    can.create_image(w-10-100-10-30+5,h-20-30-15+5+10,image=speaker,anchor="nw")



    can.delete(vol1)
    can.delete(vol2)

    r=(w-10)-(w-10-100)


    vol1=can.create_line(w-10-100,h-20-30+5+10 ,w-10-100+current_volume*r,h-20-30+5+10,fill=col1,width=3)

    vol2=can.create_text(w-10,h-20-30+5+20+10-2,text=str(int(current_volume*100))+" %",fill=col1,font=("FreeMono",13),anchor="e")



    can.create_image(w/2-30-30-30,h-20-30-15+5+10,image=previous,anchor="nw")
    can.create_image(w/2+30+30,h-20-30-15+5+10,image=next_,anchor="nw")


    if loop==0:
        can.create_image(w/2+30+30+30+20+10,h-20-30-15+5+10,image=loop1,anchor="nw")

    elif loop==1:
        can.create_image(w/2+30+30+30+20+10,h-20-30-15+5+10,image=loop2,anchor="nw")




    try:
        if not lyric_st==1:
            prog()
    except:
        pass

    
    if st==2 and playlist_st==0:
        can.delete(ctime)
        can.delete(prog1)
        can.delete(prog2)

    if st==4:
        can.delete(ctime)
        can.delete(prog1)
        can.delete(prog2)   
   


    if theme_st==1:

        can.create_oval(10,5+30, 10+40,5+30+40,fill=col2,outline=col2)
        can.create_oval(10+130-40,5+30, 10+130,5+30+40,fill=col2,outline=col2)
        can.create_rectangle(10+20,5+30, 10+130-20,5+30+40,fill=col2,outline=col2)


        can.create_image(10+10,5+30+5,image=red,anchor="nw")
        can.create_image(10+10+30+10,5+30+5,image=mint,anchor="nw")
        can.create_image(10+10+30+10+30+10,5+30+5,image=cyan,anchor="nw")



    save()


    if st==4:


        can.create_image((w-420)/2,39+(int(460*(h-30)/680)+10+30)/2-210+10+15,image=note,anchor="nw")
        frame.place_forget()
        
        yv=((int(460*(h-30)/680)+10+30)-(30+30+30))/2
        yv+=39+30+15



        can.create_image(w/2-80-15,yv, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv, w/2+80,yv+30-1,fill=col1,outline=col1)



        can.create_text(w/2,yv+15,text="Add Folder",fill="#111111",font=("FreeMono",13))






        can.create_image(w/2-80-15,yv+60, image=circle3,anchor="nw")
        can.create_image(w/2+80-15,yv+60, image=circle3,anchor="nw")

        can.create_rectangle(w/2-80,yv+60, w/2+80,yv+30-1+60,fill=col1,outline=col1)


        can.create_text(w/2,yv+15+60,text="Add Audio File",fill="#111111",font=("FreeMono",13))




    if play_video_st==1:

        can.create_image(10+30*3+20*3,h-20-30-15+5+10,image=play_video2,anchor="nw")

    elif play_video_st==0:

        can.create_image(10+30*3+20*3,h-20-30-15+5+10,image=play_video1,anchor="nw")

lvar=0

def show_lyrics():
    global can,w,text
    global current_playing,music_details


    global theme
    global lst
    global lvar



    if theme=="red":
        col1="#ff4137"
        col2="#590400"

    if theme=="mint":
        col1="#32fca7"
        col2="#003927"

    elif theme=="cyan":
        col1="#00ffff"
        col2="#003538"



    try:

        if lst==0:


            




            if not current_playing=="":




                _lyric_=music_details[current_playing][2]

                if not _lyric_=="":

                    text["state"]="normal"


                    text["fg"]="#000000"
                    text["bg"]=col1

                    text["state"]="disabled"

                    if lvar==0:

                        update_details()


                        txt=str(_lyric_).replace("'","")
                        txt=txt.replace("\\n","\n")
                        txt=txt.replace("\\r","\n")
                        txt=txt.replace("\\","'")


                        text["state"]="normal"


                        

                        text.delete(0.0,tk.END)

                        text.insert(tk.END,txt)
                        text["fg"]="#000000"
                        text["bg"]=col1

                        text["selectbackground"]=col2
                        text["selectforeground"]=col1

                        text["cursor"]="arrow"

                        text["state"]="disabled"

                        lvar=1

                    text.place(in_=root,x=(w-(790-111))/2,y=75-10+30)



                    draw_round_rec(can,(w-(820-126))/2,64+3-10+30 ,(w-(820-126))/2+(820-126),520-3-10+30,15,col1,col1,0)






                else:
                    can.create_text(w/2,71+(513-71)/2+30,text="Nothing to show!",fill=col1,font=("FreeMono",13))

                    text.place_forget()

            else:
                can.create_text(w/2,71+(513-71)/2+30,text="Nothing to show!",fill=col1,font=("FreeMono",13))
                text.place_forget()



        else:
            text.place_forget()
    except:
        pass
def draw_round_rec(c,x1,y1,x2,y2,r,col,col2,con):

    ar=[]

    a_=270

    cx,cy=x1+r,y1+r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        a_-=1


    a_=180

    cx,cy=x2-r,y1+r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        a_-=1
        

    a_=90

    cx,cy=x2-r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        a_-=1
        


    a_=0

    cx,cy=x1+r,y2-r
    for a in range(90):

        x=r*math.sin(math.radians(a_))+cx
        y=r*math.cos(math.radians(a_))+cy

        ar.append(x)
        ar.append(y)

        a_-=1

    ar.append(ar[0])
    ar.append(ar[1])


    if con==0:

        c.create_polygon(ar,fill=col,outline=col2)
    elif con==1:    
        c.create_line(ar,fill=col)


def load_im():

    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global cancel,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,checked,sort,delete,favourite1_,favourite2_,delete2,playlist3,sort2,loop1,loop2,wallpaper
    global circle2,circle3,circle4,expand,expand2,playlist4


    global theme,theme_
    global red,mint,cyan
    global paste

    global add_video1,add_video2,add_video3
    global play_video1,play_video2
    global eye
    global minimize,quit
    global circlex


    circle=ImageTk.PhotoImage(file="data/"+theme+"/circle.png")
    circle2=ImageTk.PhotoImage(file="data/"+theme+"/circle2.png")
    circle3=ImageTk.PhotoImage(file="data/"+theme+"/circle3.png")
    circle4=ImageTk.PhotoImage(file="data/"+theme+"/circle4.png")
    play=ImageTk.PhotoImage(file="data/"+theme+"/play.png")
    play=ImageTk.PhotoImage(file="data/"+theme+"/play.png")
    pause=ImageTk.PhotoImage(file="data/"+theme+"/pause.png")
    favourite1=ImageTk.PhotoImage(file="data/"+theme+"/favourite1.png")
    favourite2=ImageTk.PhotoImage(file="data/"+theme+"/favourite2.png")
    list1=ImageTk.PhotoImage(file="data/"+theme+"/list1.png")
    list2=ImageTk.PhotoImage(file="data/"+theme+"/list2.png")
    musical_note1=ImageTk.PhotoImage(file="data/"+theme+"/musical_note1.png")
    musical_note2=ImageTk.PhotoImage(file="data/"+theme+"/musical_note2.png")
    speaker=ImageTk.PhotoImage(file="data/"+theme+"/speaker.png")
    previous=ImageTk.PhotoImage(file="data/"+theme+"/previous.png")
    next_=ImageTk.PhotoImage(file="data/"+theme+"/next.png") 
    cancel=ImageTk.PhotoImage(file="data/"+theme+"/cancel.png")
    search_im=ImageTk.PhotoImage(file="data/"+theme+"/search.png")    
    shuffle1=ImageTk.PhotoImage(file="data/"+theme+"/shuffle1.png")
    shuffle2=ImageTk.PhotoImage(file="data/"+theme+"/shuffle2.png")
    note=ImageTk.PhotoImage(file="data/"+theme+"/note.png")
    playlist1=ImageTk.PhotoImage(file="data/"+theme+"/playlist1.png")
    playlist2=ImageTk.PhotoImage(file="data/"+theme+"/playlist2.png")
    checked=ImageTk.PhotoImage(file="data/"+theme+"/checked.png")
    sort=ImageTk.PhotoImage(file="data/"+theme+"/sort.png")
    delete=ImageTk.PhotoImage(file="data/"+theme+"/bin.png")
    favourite1_=ImageTk.PhotoImage(file="data/"+theme+"/favourite1_.png")
    favourite2_=ImageTk.PhotoImage(file="data/"+theme+"/favourite2_.png")
    delete2=ImageTk.PhotoImage(file="data/"+theme+"/bin2.png")
    playlist3=ImageTk.PhotoImage(file="data/"+theme+"/playlist3.png")
    playlist4=ImageTk.PhotoImage(file="data/"+theme+"/playlist4.png")
    sort2=ImageTk.PhotoImage(file="data/"+theme+"/sort2.png")
    loop1=ImageTk.PhotoImage(file="data/"+theme+"/loop1.png")
    loop2=ImageTk.PhotoImage(file="data/"+theme+"/loop2.png")
    theme_=ImageTk.PhotoImage(file="data/"+theme+"/theme.png")

    red=ImageTk.PhotoImage(file="data/"+theme+"/red.png")
    mint=ImageTk.PhotoImage(file="data/"+theme+"/mint.png")
    cyan=ImageTk.PhotoImage(file="data/"+theme+"/cyan.png")

    paste=ImageTk.PhotoImage(file="data/"+theme+"/paste.png")

    add_video1=ImageTk.PhotoImage(file="data/"+theme+"/add_video1.png")
    add_video2=ImageTk.PhotoImage(file="data/"+theme+"/add_video2.png")
    add_video3=ImageTk.PhotoImage(file="data/"+theme+"/add_video3.png")
    play_video1=ImageTk.PhotoImage(file="data/"+theme+"/play_video1.png")
    play_video2=ImageTk.PhotoImage(file="data/"+theme+"/play_video2.png")
    eye=ImageTk.PhotoImage(file="data/"+theme+"/eye.png")

    minimize=ImageTk.PhotoImage(file="data/"+theme+"/minimize.png")
    quit=ImageTk.PhotoImage(file="data/"+theme+"/quit.png")
    circlex=ImageTk.PhotoImage(file="data/"+theme+"/circlex.png")



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



circle=0
circle2=0
circle3=0
circle4=0
play=0
pause=0
add=0
favourite1=0
favourite2=0
list1=0
list2=0
musical_note1=0
musical_note2=0
remove=0
rename=0
speaker=0
previous=0
next_=0
cancel=0
cancel2=0
search_im=0
shuffle1=0
shuffle2=0
dots=0
note=0

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




theme="mint"
theme_=0
theme_st=0


lyric_st=0
_lyric=""


red,mint,cyan=0,0,0

sa=["Date Added (Descending)","Date Added (Ascending)","Title (Ascending)","Title (Descending)"]

sort_val=sa[0]

with open("data/save.json", "r") as file:
    data = json.load(file)


st,current_playing,current_playlist,playlist_st,lst,sort_val,shuff,loop,theme,shuffle_ar,shuffle_st=data["save"]


add_video1,add_video2,add_video3=0,0,0
play_video1,play_video2=0,0





if shuff==1 or shuff==2:
    sort_val=""

paste=0

play_video_st=0
eye=0


minimize,quit=0,0




root_st=0


circlex=0












root=tk.Tk()

wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()



"""
im=Image.open("data/wallpaper.jpg")
x,y=im.size

r=x/y

im=im.resize((int(680*r),680))
im.save("data/wallpaper.png")
"""


#im=Image.open("data/wallpaper.png")
#w,h=im.size


w,h=1100,710
root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+5")
root.resizable(0,0)
#root.wm_attributes("-alpha",0.9)
root.wm_attributes("-transparentcolor","#333333")
root.wm_attributes("-topmost",True)
root.iconbitmap("data/icon.ico")
root.title("HMUSIC")

root.overrideredirect(True)






    

def hex(c,x,y,wd,ht,sz,col1,col2):

    global cursor

    c.delete("all")


    c.create_rectangle(x,y, x+wd,y+ht, fill=col1,outline=col1)



    _y=y-(sz-6)

    _st=0

    for y_ in range(int(ht/(sz-6))+1):

        if _st==0:
            _x=x
        elif _st==1:
            _x=x+sz/2-1
        for x_ in range(int(wd/(sz-2))+1):

            hexagon(c,_x,_y,sz,col2,col2)


            _x+=sz-2

        if _st==0:
            _st=1
        elif _st==1:
            _st=0

        _y+=sz-6


def hexagon(c,x,y,sz,col1,col2):



    cx,cy=x+sz/2,y+sz/2

    h=360/6

    a_=180

    ar=[]
    for a in range(6):

        x_=sz/2*math.sin(math.radians(a_))+cx
        y_=sz/2*math.cos(math.radians(a_))+cy

        ar.append(x_)
        ar.append(y_)

        a_+=h

    ar.append(ar[0])
    ar.append(ar[1])
    c.create_polygon(ar,fill=col1,outline=col2)






def _on_mousewheel(e):
    global can2,can3,yyy,h,add_st
    global ylyric,lyric_st,lst

    if add_st==0 and lst==1:

        if int(can2["scrollregion"].split(" ")[-1])>int(460*(h-30)/680):

            can2.yview_scroll(int(-1*(e.delta/120)), "units")
            #main()


    elif add_st==1:

        if int(can3["scrollregion"].split(" ")[-1])>210:
            can3.yview_scroll(int(-1*(e.delta/120)), "units")




def play_pause(e):
    global st,playlist_st,play_st,current_playing,pp,tm
    global paused



    if st==2 and playlist_st==0 and pl_st==0:
        pass
    else:

        if not current_playing=="":

            if pp==0:
                pp=1
                play_st=1

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
    global play_video_st,vid_label,lyric_st


    if st==2 and playlist_st==0 and pl_st==0:
        return

    if st==4:
        return


    if loop==0:

        if mvar+1==len(songs):
            mvar=0
        else:
            mvar+=1


    tm=0
    
    current_playing=songs[mvar][0]
    play_st=1

    play_music("music/"+current_playing,tm)

    pp=1

    get_audio_duration("music/"+current_playing)

    lvar=0

    play_video_st=0

    vid_label.place_forget()

    lyric_st=0

    main()

    move_to_playing()


def play_previous(e):

    global st,playlist_st,play_st,current_playing,mvar,tm,loop,pp,songs,play_video_st,vid_label,lyric_st


    if st==2 and playlist_st==0 and pl_st:
        return

    if st==4:
        return


    if loop==0:

        mvar-=1


    tm=0
    
    current_playing=songs[mvar][0]
    play_st=1

    play_music("music/"+current_playing,tm)

    pp=1

    get_audio_duration("music/"+current_playing)

    lvar=0

    play_video_st=0

    vid_label.place_forget()

    lyric_st=0

    main()

    move_to_playing()


can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
can.bind("<Button-3>",can_b3)
can.bind_all("<MouseWheel>",_on_mousewheel)
can.bind("<space>",play_pause)
can.bind("<Right>",play_next)
can.bind("<Left>",play_previous)






if theme=="red":
    col1="#ff4137"
    col2="#590400"

if theme=="mint":
    col1="#32fca7"
    col2="#003927"

elif theme=="cyan":
    col1="#00ffff"
    col2="#003538"




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
                arrowsize=7)








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
                arrowsize=7)












yy=0

def on_canvas_scroll():
    global yy
    
    if can2.canvasy(0)!=yy:


        yy=can2.canvasy(0)
        #main()

    root.after(1,on_canvas_scroll)
        






frame=tk.Frame(bg="#000000",width=w-20-2,height=int(460*(h-30)/680))

can2=tk.Canvas(frame,bg="#000000",width=w-7-20-2,height=int(460*(h-30)/680),relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,w-7-2,int(460*(h-30)/680)))
can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-1>",can2_b1)
can2.bind("<Button-3>",can_b3)
can2.bind("<space>",play_pause)
can2.bind("<Right>",play_next)
can2.bind("<Left>",play_previous)



sb=ttk.Scrollbar(frame,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

sb.config(command=can2.yview)

can2.config(yscrollcommand=sb.set)
sb.pack(side=tk.LEFT,fill=tk.Y)


frame2=tk.Frame(bg="#000000",width=350+100,height=250)

can4=tk.Canvas(frame2,bg="#000000",width=350+100,height=40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can4.pack(side=tk.TOP)



frame3=tk.Frame(frame2,bg="#000000",width=350+100,height=250-40)

can3=tk.Canvas(frame3,bg="#000000",width=350+100-7-2,height=250-40,relief="flat",highlightthickness=0,border=0,
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


can6=tk.Canvas(frame2,bg="#000000",width=350+100,height=16,relief="flat",highlightthickness=0,border=0)
can6.pack(side=tk.TOP)








def search__():

    global search,search_var,mvar,songs,current_playing

    

    if search.get()!=search_var:
        search_var=search.get()



        main()

    root.after(1,search__)

search=tk.Entry(bg="#000000",fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=86,font=("FreeMono",13))
#search.bind("<KeyPress>",search_keypress)
npl=tk.Entry(bg="#000000",fg=col1,insertbackground=col1,relief="flat",highlightthickness=0,border=0,width=84,font=("FreeMono",13))

ls=0
def mvar_():


    global ls,current_playing,songs,mvar

    try:
        for s in range(len(songs)):
            if songs[s][0]==current_playing:
               

                mvar=s


    except:
        pass

    root.after(1,mvar_)



def can_sort_b1(e):

    global sort_ar,sort_val
    global sort_st,can_sort
    global can2
    global loop


    for s in sort_ar:

        if s[1]<=e.y<=s[1]+30:

            can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))

            loop=0


            sort_val=s[0]

            main()










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




text=tk.Text(bg="#000000",fg=col1,width=75,height=23,relief="flat",highlightthickness=0,border=0,font=("FreeMono",13))

text.config(wrap=tk.WORD)


vid_label = tk.Label()
vid_label["bg"]="#000000"


can2.focus_set()
load_im()

clipboard()

main()
timer()

search__()
check_volume()

mvar_()


check_pl()

on_canvas_scroll()

convert_folder_to_audio()
convert_file_to_audio()

gen_wave()
draw_wave()

check_geometry()

try:
    if current_playing=="":
        current_playing=songs[0][0]
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
    pass#can2["scrollregion"]=(0,0,w-7,int(460*(h-30)/680))


update_frame()
root.mainloop()