
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


im=Image.open("data/playlist1.png")
im=im.resize((30,30))
im.save("data/playlist1.png")


"""

im=Image.open("data/next.png")
im=im.resize((30,30))
im.save("data/next.png")
"""
sig=[]
sig_=0
sig2=[]
tts=0
def gen_wave():
    global lst,can,st,sig,sig_,sig2,tm,tts,play_st,current_playing,w,h

    xv=2
    amp=150


    if play_st==1:



        can.delete(sig_)

        try:

            amplitude = get_amplitude_at_time("waves/"+current_playing[:-3]+"wav", tts)





            sig.append(-amplitude*amp)


            xn=int((w-20)/xv)

            if len(sig)>xn:
                sig.pop(0)



            sig2=[]
            x=10
            for a in sig:

                sig2.append(x)
                sig2.append(a+(80-30+40-10-30)+((440*h/680)+10+30)/2)

                x+=xv

            try:

                if lst==0 and st!=4:

                    sig_=can.create_line(sig2,fill="#32fca7")
            except:
                pass









            tts+=0.025
        except:
            pass


    root.after(25,gen_wave)

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
        
        # Set the read position to the desired frame
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

            load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill="#32fca7")

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

                        load=can.create_text(10,h-20-60-60,text=i,font=("FreeMono",13),fill="cyan",anchor="w")
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

            load2=can.create_oval(w/2-50,493-20-40-30-15, w/2-50+30,493-20-40-30+15,fill="#32fca7",outline="#32fca7")
            load3=can.create_oval(w/2+50-30,493-20-40-30-15, w/2+50,493-20-40-30+15,fill="#32fca7",outline="#32fca7")
            load4=can.create_rectangle(w/2-50+15,493-20-40-30-15, w/2+50-15,493-20-40-30+15,fill="#32fca7",outline="#32fca7")

            load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#000000")
        convert=0
        update_waves()


    root.after(1,convert_folder_to_audio)

def convert_file_to_audio():

    global can,load,load2,load3,load4,w,h
    global convert,input_file,st



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

            load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill="#32fca7")


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

                        load=can.create_text(10,h-20-60-60,text=i,font=("FreeMono",13),fill="cyan",anchor="w")
                    

                except:
                    pass


        except:
            pass


        if st==4:

            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            load2=can.create_oval(w/2-50,493-20-40-30-15, w/2-50+30,493-20-40-30+15,fill="#32fca7",outline="#32fca7")
            load3=can.create_oval(w/2+50-30,493-20-40-30-15, w/2+50,493-20-40-30+15,fill="#32fca7",outline="#32fca7")
            load4=can.create_rectangle(w/2-50+15,493-20-40-30-15, w/2+50-15,493-20-40-30+15,fill="#32fca7",outline="#32fca7")

            load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#000000")

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



def update_details(s="",con=-1):
    global music_details



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
            data[song]=[0,0]



    if con==0:
        f=data[s][0]

        if f==0:
            f=1
        elif f==1:
            f=0

        data[s][0]=f

    elif con==1:

        n=data[s][-1]

        n+=1



        data[s][-1]=n

    elif con==2:

        data.pop(s)


    music_details=data







    with open("data/music_details.json", "w") as file:
        json.dump(data, file, indent=4) 


update_details()



playlist={}


def create_playlist(pl="",con="",song=""):
    global playlist


    try:

        with open("data/playlist.json", "r") as file:
            data = json.load(file)


    except:
        data={}


    all_songs = os.listdir("music")

    for i in data:

        ar=data[i]
        ar2=[]

        for v in ar:

            try:
                all_songs.index(v)

            except:
                ar2.append(v)


        for v in range(len(ar2)):
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

create_playlist()



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

    ctime=can.create_text(10,h-20-60-20+20,text=tt,font=("FreeMono",13),fill="#32fca7",anchor="w")


    can.delete(prog1)
    can.delete(prog2)

    x_=tm*(w-20)/tot_tm_

    prog1=can.create_line(10,h-20-60-20, x_+10,h-20-60-20,fill="#32fca7",width=4)
    prog2=can.create_oval(x_+10-5,h-20-60-20-5, x_+10+5,h-20-60-20+5,fill="#000000",outline="#32fca7")



def timer():
    global play_st,tm,start_time,can
    global ctime,tot_tm_
    global prog1,prog2
    global tvar
    global mvar
    global current_playing,songs
    global w,h,add_st,frame2,can2
    global loop

    if play_st==1:




        prog()

        tm+=1

        if tm>=tot_tm_:

            if loop==0:
                mvar+=1
            add_st=0
            frame2.place_forget()
            can2.focus_set()


            if mvar+1>len(songs):
                mvar=0

                can2["scrollregion"]=(0,0,w-20-7,h-240+30)


            tm=0
            
            current_playing=songs[mvar][0]
            play_st=1

            play_music("music/"+current_playing,tm)

            pp=1

            get_audio_duration("music/"+current_playing)

            #update_details(current_playing,1)

            main()

    root.after(1000,timer)


def can3_b1(e):
    global sel_playlist,can3,frame2,add_st,current_playing



    add_st=0
    frame2.place_forget()

    for p in sel_playlist:

        if p[2]<=can3.canvasy(e.y)<=p[2]+50:

            if not current_playing=="":
                create_playlist(p[0],1,p[1])

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
    global search,frame,can2
    global add_st,frame2,can3
    global sel_playlist
    global _npl,npl

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

                can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
                npl.delete(0,tk.END)
                _npl=1
                npl.place(in_=root,x=10+20,y=80-30+40+5+5)
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
                npl.plac

                e_forget()
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
                can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
                create_playlist(_pl[0],con=3)

                main()
                return

            if _pl[1]<=can2.canvasy(e.y)<=_pl[1]+50:
                can2["scrollregion"]=(0,0,w-20-7,(440*h/680))

                
                con=0
                if current_playlist==_pl[0]:
                    con=1
                current_playlist=_pl[0]
                playlist_st=1





                main()

                if con==0:


                    
                    try:

                        
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

        cx,cy=w-20-7-10-30-20-30-20-30+15,y+10+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:


            update_details(s[0],0)
            main()
            return

    #playlist

    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=w-20-7-10-30-20-30+15,y+10+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

                if add_st==0:
                    add_st=1
                elif add_st==1:
                    add_st=0


                if add_st==1:




                    can3.delete("all")

                    y=0
                    can3["scrollregion"]=(0,0,300-7,250-40)
                    sel_playlist=[]

                    for p in playlist:

                        ar=playlist[p]

                        can3.create_image(10,y+10,image=playlist2,anchor="nw")
                        can3.create_text(10+30+10,y+25,text=p,font=("FreeMono",13),anchor="w",fill="#32fca7")
                        can3.create_line(0,y+50,350-7,y+50,fill="#000000")

                        try:
                            v=ar.index(s[0])



                            can3.create_image(350-7-10-20,y+15, image=checked,anchor="nw")
                            
                        except:
                            pass




                        sel_playlist.append([p,s[0],y])
                        pl_var=[p,s[0],y]



                        y+=50

                    if len(playlist)==0:
                        can3.create_text(10+30+10,(250-40)/2,text="No record",font=("FreeMono",13),anchor="w")

                    can3["scrollregion"]=(0,0,300-7,y)
                    frame2.place(in_=root,x=(w-350)/2,y=(h-(40+250-40+10))/2)

                    can3.focus_set()

                    main()

                return

    #delete file


    for s in songs:

        #print(s[0])

        y=s[-1]

        cx,cy=w-20-7-10-30+15,y+10+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            os.remove("music/"+s[0])
            del_wave()
            main()
            return




    for a in range(len(songs)):

        cx,cy=w-20-7-10-30+10,songs[a][-1]+15+10

        r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

        if r<=10:
            # remove

            main()

            return


        if songs[a][-1]<=can2.canvasy(e.y)<=songs[a][-1]+50:


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



def can_b3(e):
    global current_playing,can2
    global songs

    if not current_playing=="":

        for s in songs:

            if s[0]==current_playing:

                t=len(songs)*50


                v=s[1]

                if s[1]+(440*h/680)/2-25<t:
                    v=s[1]-((440*h/680)/2-25)

                pixel_value = int(v)
                scroll_region = can2.bbox("all")  # Get the bounding box of all content
                if scroll_region:
                    total_height = scroll_region[3] - scroll_region[1]  # Scrollable height
                    fraction = pixel_value / total_height if total_height > 0 else 0
                    can2.yview_moveto(fraction)
                    main()

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
    global current_volume,vol1,vol2,vol3
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


    add_st=0
    frame2.place_forget()

    xv=w/6




    if xv-60<=e.x<=xv+60:
        if 0<=e.y<=35:

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()

            if shuffle_st==2:
                shuffle_st=1



            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=680
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")
            
            lst=1
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            current_playlist=""

            add_st=0
            frame2.place_forget()

            can2.focus_set()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()




            

            if st!=4:

                st=0
                main()



                try:
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

            st=0
            main()


            
            return


    if xv*2-60<=e.x<=xv*2+60:
        if 0<=e.y<=35:

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()


            if shuffle_st==2:
                shuffle_st=1



            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=680
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            
            lst=1
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()
            



            if st!=4:

                st=1
                main()



                try:
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


            st=1
            main()

            return

    if xv*3-60<=e.x<=xv*3+60:
        if 0<=e.y<=35:
            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()


            if shuffle_st==2 and current_playlist=="":
                shuffle_st=1




            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)

            h=680
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            
            playlist_st=0
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()




            if not st==4:
                st=2
                main()


                if st==2:
                    pl_st=1

                else:
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
        if 0<=e.y<=35:

            lst=1

            _search=0
            sort_st=0
            can_sort.place_forget()



            if shuffle_st==2:
                shuffle_st=1


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=680
            can["height"]=h

            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()



            if st!=4:
                st=3
                main()



                try:
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

            st=3
            main()

            return


    if xv*5-60<=e.x<=xv*5+60:
        if 0<=e.y<=35:
            _search=0
            sort_st=0
            can_sort.place_forget()


            if shuffle_st==2:
                shuffle_st=1


            can.delete(load)
            can.delete(load2)
            can.delete(load3)
            can.delete(load4)
            h=680
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            st=4
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            main()
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            _npl=0
            npl.place_forget()









            return



    if h-20-60-20-10<=e.y<=h-20-60-20+10:



        if e.x<10:
            tm=0
        elif e.x>w-10:
            tm=tot_tm_

        elif 10<=e.x<=w-10:

            x=e.x-10

            tm=x*tot_tm_/(w-20)

        if play_st==1:

            tts=tm
            sig=[]

            play_music("music/"+current_playing,tm)

        prog()

        return


    #play/pause

    cx,cy=w/2,h-20-30+5

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=30:

        if st==2 and playlist_st==0 and pl_st==0:
            pass
        else:

            if pp==0:
                pp=1
                play_st=1

                play_music("music/"+current_playing,tm)

                main()
            elif pp==1:
                pp=0
                play_st=0

                pygame.mixer.quit()

                main()



                prog()

        return

    #previous

    cx,cy=w/2-30-30-30+15,h-20-30-15+15+5
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

        if st==2 and playlist_st==0 and pl_st==0:
            return


        if loop==0:

            mvar-=1


        tm=0
        
        current_playing=songs[mvar][0]
        play_st=1

        play_music("music/"+current_playing,tm)

        pp=1

        get_audio_duration("music/"+current_playing)

        main()
        return

    #next

    cx,cy=w/2+30+30+15,h-20-30-15+15+5
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:




        if st==2 and playlist_st==0 and pl_st==0:
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

        main()
        return



    


    #search

    cx,cy=w-10-5-20+10,45+10

    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=10:
        search.delete(0,tk.END)
        search.place_forget()
        can.focus_set()
        _search=0

        main()


        return

    if 10<=e.x<=w-10-5-30:
        if 40<=e.y<=40+30:

            _search=1





            can.create_arc(10,40, 10+30,40+30, style=tk.ARC,start=90,extent=180,outline="#32fca7")
            can.create_arc(w-10-30,40, w-10,40+30, style=tk.ARC,start=270,extent=180,outline="#32fca7")

            can.create_line(10+15,40, w-10-15,40, fill="#32fca7")
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill="#32fca7")





            search.place(in_=root,x=10+15,y=45)
            search.focus_set()

            main()

            return


    #list

    cx,cy=10+15,h-20-30-15+5+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:

        if lst==0:
            lst=1
        elif lst==1:
            lst=0
            frame.place_forget()

        main()


    #volume
    if w-10-100-10<=e.x<=w-10+10:
        if h-20-30+5-10<=e.y<=h-20-30+5+10:

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



            can.delete(vol1)
            can.delete(vol2)
            can.delete(vol3)

            r=(w-10)-(w-10-100)

            vol1=can.create_line(w-10-100,h-20-30+5 ,w-10-100+current_volume*r,h-20-30+5,fill="#32fca7",width=2)
            vol2=can.create_oval(w-10-100+current_volume*r-5,h-20-30+5-5, w-10-100+current_volume*r+5,h-20-30+5+5,fill="#000000",outline="#32fca7")

            vol3=can.create_text(w-10-100+50,h-20-30+5+20,text=str(int(current_volume*100))+" %",fill="#32fca7",font=("FreeMono",13))


    #sort

    cx,cy=10+30+20+15,h-20-30-15+5+15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:

        if sort_st==0:
            sort_st=1
        elif sort_st==1:
            sort_st=0


        can_sort.delete(_sort)


        for s in sort_ar:

            if s[0]==sort_val:

                _sort=can_sort.create_image(250-5-20,s[1]+5,image=checked,anchor="nw")

        if sort_st==1:

            can_sort.place(in_=root,x=10+30+20+30,y=h-20-30-15+5-160)

            shuff=0
            shuffle_st=0
        else:
            can_sort.place_forget()

        return



    #shuffle




    cx,cy=10+30+20+30+20+15,h-20-30-15+5+15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:
        loop=0

        if shuffle_st==0:
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            mvar=0
            shuffle_st=1
            shuff=1

            sort_val=""

            main()
        elif shuffle_st==1:
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            shuffle_st=0
            shuff=0

            sort_val=sort_ar[0][0]
            main()

        elif shuffle_st==2:
            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))
            shuffle_st=0
            shuff=0
            sort_val=sort_ar[0][0]            
            main()
        




    #loop

    cx,cy=w/2+30+30+30+20+10+15,h-20-30-15+5+15

    r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

    if r<=15:



        if loop==0:
            if current_playing!="":
                loop=1
        elif loop==1:
            loop=0

        main()










    #add to playlist

    

    cx,cy=10+30+20+15,h-20-30-15+5+15
    r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
    if r<=15:
        create_playlist()

        if add_st==0:

            if current_playing=="":
                return
            add_st=1
            can3.delete("all")

            y=0
            can3["scrollregion"]=(0,0,300-7,250-40)
            sel_playlist=[]

            for p in playlist:

                ar=playlist[p]

                can3.create_image(10,y+10,image=playlist2,anchor="nw")
                can3.create_text(10+30+10,y+25,text=p,font=("FreeMono",13),anchor="w",fill="#32fca7")
                can3.create_line(0,y+50,350-7,y+50,fill="#888888")

                try:
                    v=ar.index(current_playing)



                    can3.create_image(350-7-10-20,y+15, image=checked,anchor="nw")
                    
                except:
                    pass




                sel_playlist.append([p,current_playing,y])



                y+=50

            if len(playlist)==0:
                can3.create_text(10+30+10,(250-40)/2,text="No record",font=("FreeMono",13),anchor="w")

            can3["scrollregion"]=(0,0,300-7,y)
            frame2.place(in_=root,x=(w-350)/2,y=(h-(40+250-40+10))/2)

            can3.focus_set()

            return



        elif add_st==1:
            add_st=0
            frame2.place_forget()
            can2.focus_set()
            return

    #add songs

    if st==4:


        yv=((493-39)-(30+30+30))/2
        yv+=39


        #can.create_rectangle(w/2-150,yv, w/2+150,yv+30, fill="#32fca7")


        cx,cy=w/2-150,yv+15

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


        cx,cy=w/2+150,yv+15

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


        if w/2-150<=e.x<=w/2+150:
            if yv<=e.y<=yv+30:
                can.delete(load)
                can.delete(load2)
                can.delete(load3)
                can.delete(load4)
                input_folder=filedialog.askdirectory(title="Select a Folder")

                if not input_folder=="":
                    convert=1


                return


















        cx,cy=w/2-150,yv+15+60

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



        cx,cy=w/2+150,yv+15+60

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



        if w/2-150<=e.x<=w/2+150:
            if yv+60<=e.y<=yv+30+60:
                can.delete(load)
                can.delete(load2)
                can.delete(load3)
                can.delete(load4)
                input_file=filedialog.askopenfilename()

                if not input_file=="":
                    convert=2


                return





        #file=filedialog.askopenfilename()
        #folder=filedialog.askdirectory(title="Select a Folder")





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



            root.wm_attributes("-fullscreen",0)
            root.geometry("950x680+208+0")
            main()


    #play_music("music/24.mp3",30.556)


vol1,vol2,vol3=0,0,0
def check_volume():
    global current_volume
    global can,vol1,vol2,vol3

    if volume.GetMasterVolumeLevelScalar()!=current_volume:

        current_volume=volume.GetMasterVolumeLevelScalar()

        can.delete(vol1)
        can.delete(vol2)
        can.delete(vol3)

        r=(w-10)-(w-10-100)

        vol1=can.create_line(w-10-100,h-20-30+5 ,w-10-100+current_volume*r,h-20-30+5,fill="#32fca7",width=3)
        vol2=can.create_oval(w-10-100+current_volume*r-5,h-20-30+5-5, w-10-100+current_volume*r+5,h-20-30+5+5,fill="#000000",outline="#32fca7")

        vol3=can.create_text(w-10-100+50,h-20-30+5+20,text=str(int(current_volume*100))+" %",fill="#32fca7",font=("FreeMono",13))


    root.after(500,check_volume)






def play_music(file,time,con=0):
    global current_playing
    global sig,tts

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
    start_time = time  # Replace with the desired starting time in seconds
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

    global can,st,w,h
    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global pp,fv,lst
    global frame,can2
    global current_playing
    global yyy

    global songs
    global search,search_var
    global cancel1,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,sort,delete,favourite1_,favourite2_,delete2,playlist3
    global music_details
    global vol1,vol2,vol3,current_volume
    global playlist,playlist_st
    global can2
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
    global circle2,circle3

    global expand,expand2,expand_st



    if root.wm_attributes("-fullscreen")==1:



        frame["width"]=w-20
        frame["height"]=(440*h/680)+30

        can2["width"]=w-20-7
        can2["height"]=(440*h/680)+30
    else:

        frame["width"]=w-20
        frame["height"]=(440*h/680)

        can2["width"]=w-20-7
        can2["height"]=(440*h/680)


    can["width"]=w
    can["height"]=h


    can.delete("all")

    #can.create_image(0,0, image=wallpaper,anchor="nw")
    #create_rectangle(can,0, 0, w, h, fill='#111111', alpha=.65)

    if expand_st==0:
        can.create_image(w-10-20,10,image=expand,anchor="nw")
    elif expand_st==1:
        can.create_image(w-10-20,10,image=expand2,anchor="nw")




    update_details()
    create_playlist()

    



    xv=w/6
    x=xv


    label=["All Songs","Favourites","Playlist","Most Played","Add Song"]

    for l in range(len(label)):

        col="#32fca7"

        if l==st:
            col="#000000"


            can.create_image(x-60,5,image=circle3,anchor="nw")
            can.create_image(x+60-30,5,image=circle3,anchor="nw")


            can.create_rectangle(x-60+15,5, x+60-15,35-1, fill="#32fca7",outline="#32fca7")









        #can.create_rectangle(x-50,20-10, x+50,20+10, outline="red")



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





















    can2.delete("all")
    #can2.create_image(-10,can2.canvasy(-(80-30+40))-h,image=wallpaper,anchor="nw")
    #can2.create_image(-10,can2.canvasy(-(80-30+40)),image=wallpaper,anchor="nw",tags="fixed_image")
    #can2.create_image(-10,can2.canvasy(-(80-30+40))+h,image=wallpaper,anchor="nw")
    #create_rectangle(can2,0, int(can2.canvasy(0))-h, int(can2["width"]), int(can2.canvasy(int(can2["height"])))+h, fill='#111111', alpha=.65)

    y=0

    if st==0:

        songs=[]
        

        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                if song==current_playing:

                    can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                    can2.create_image(0,y,image=circle2,anchor="nw")
                    can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                    can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill="#32fca7",outline="#32fca7")

                    can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                    col="#000000"
                else:
                    can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                    col="#888888"


                can2.create_text(10+30+20,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                if song==current_playing:
                    can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7-30,y+45,fill="#32fca7",outline="#32fca7")
                    can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                else:
                    can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7,y+45,fill="#000000",outline="#000000")


                _del_=delete
                if song==current_playing:
                    _del_=delete2

                can2.create_image(w-20-7-10-30,y+10,image=_del_,anchor="nw")


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
                    


                can2.create_image(w-20-7-10-30-20-30,y+10,image=_pl_,anchor="nw")




                if music_details[song][0]==0:

                    _fv_=favourite1

                    if song==current_playing:
                        _fv_=favourite1_


                elif music_details[song][0]==1:


                    _fv_=favourite2

                    if song==current_playing:
                        _fv_=favourite2_


                can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=_fv_,anchor="nw")



                if not song==current_playing:

                    can2.create_line(0,y+50,w-20-7,y+50,fill="#323232")

                ar=[song,y]

                songs.append(ar)

                y+=50

        if len(songs)==0:
            current_playing=""
            can2.create_text((w-20-7)/2,(440*h/680)/2,text="No Record!",font=("FreeMono",13),fill="#888888")
    elif st==1:
        songs=[]


        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                if music_details[song][0]==1:

                    if song==current_playing:
                        can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                        can2.create_image(0,y,image=circle2,anchor="nw")
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                        can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill="#32fca7",outline="#32fca7")
                        can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                        col="#000000"
                    else:
                        can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                        col="#888888"



                    can2.create_text(10+30+20,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                    if song==current_playing:
                        can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7-30,y+45,fill="#32fca7",outline="#32fca7")
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                    else:
                        can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7,y+45,fill="#000000",outline="#000000")



                    _del_=delete
                    if song==current_playing:
                        _del_=delete2

                    can2.create_image(w-20-7-10-30,y+10,image=_del_,anchor="nw")


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
                        


                    can2.create_image(w-20-7-10-30-20-30,y+10,image=_pl_,anchor="nw")




                    if music_details[song][0]==0:

                        _fv_=favourite1

                        if song==current_playing:
                            _fv_=favourite1_


                    elif music_details[song][0]==1:


                        _fv_=favourite2

                        if song==current_playing:
                            _fv_=favourite2_


                    can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=_fv_,anchor="nw")



                    if not song==current_playing:

                        can2.create_line(0,y+50,w-20-7,y+50,fill="#323232")





                    ar=[song,y]

                    songs.append(ar)

                    y+=50


        if len(songs)==0:
            current_playing=""
            can2.create_text((w-20-7)/2,(440*h/680)/2,text="No Record!",font=("FreeMono",13),fill="#888888")
    elif st==2:

        create_playlist()

        if playlist_st==0:

            if _search==1:

                can.create_oval(10,40, 10+30,40+30,fill="#000000",outline="#000000")
                can.create_oval(w-10-30,40, w-10,40+30,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40, w-10-15,40+30,fill="#000000",outline="#000000")






            can.create_arc(10,40, 10+30,40+30, style=tk.ARC,start=90,extent=180,outline="#32fca7")
            can.create_arc(w-10-30,40, w-10,40+30, style=tk.ARC,start=270,extent=180,outline="#32fca7")

            can.create_line(10+15,40, w-10-15,40, fill="#32fca7")
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill="#32fca7")



            can.create_text(30+20+5,40+15,text="Search",font=("FreeMono",13),fill="#32fca7",anchor="w")



            can.create_image(w-10-5-20,40+5,image=cancel1,anchor="nw")

            can.create_image(30,40+5,image=search_im,anchor="nw")






            #draw_round_rec(can,10-2,80-10-30+40,w-10,80-30+40+(440*h/680)+10,15,"#137345","",1)
            #can.create_line(10,70,w-10,70,fill="#888888")
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill="#888888")

            frame.place(in_=root,x=10,y=80-30+40)













            y=5



            if _npl==1:

                can2.create_oval(10,y, 10+30,y+30, fill="#000000",outline="#000000")
                can2.create_oval(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30,fill="#000000",outline="#000000")

                can2.create_rectangle(10+15,y, int(can2["width"])-10-15,y+30,fill="#000000",outline="#000000")



            can2.create_arc(10,y, 10+30,y+30, style=tk.ARC,start=90,extent=180,outline="#32fca7")
            can2.create_arc(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30, style=tk.ARC,start=270,extent=180,outline="#32fca7")

            can2.create_line(10+15,y, int(can2["width"])-10-15,y, fill="#32fca7")
            can2.create_line(10-1+15,y+30, int(can2["width"])-10-15,y+30, fill="#32fca7")







            can2.create_text(30,y+15,text="New Playlist",font=("FreeMono",13),fill="#32fca7",anchor="w")



            can2.create_image(int(can2["width"])-10-5-20,y+5,image=cancel1,anchor="nw")


            y+=40






            #can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30, outline="#32fca7")

            can2.create_image(int(can2["width"])/2-100-15,y,image=circle3,anchor="nw")
            can2.create_image(int(can2["width"])/2+100-15,y,image=circle3,anchor="nw")

            can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30-1,fill="#32fca7",outline="#32fca7")


            can2.create_text(int(can2["width"])/2,y+15,text="Create New Playlist",font=("FreeMono",13),fill="#111111")

            y+=30+20

            can2.create_line(0,y, int(can2["width"]),y,fill="#323232")

            _playlist=[]

            for pl in playlist:

                if not pl.lower().find(search_var.lower())==-1:
                    

                    if current_playlist==pl:
                        col="#000000"
                        can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                        can2.create_image(0,y,image=circle2,anchor="nw")
                        can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                        can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill="#32fca7",outline="#32fca7")
                        _pl_=playlist3
                        _del_=delete2
                    else:
                        col="#888888"

                        _pl_=playlist1
                        _del_=delete



                    can2.create_image(10,y+10,image=_pl_,anchor="nw")




                    can2.create_text(10+30+10,y+25,text=pl,font=("FreeMono",13),fill=col,anchor="w")

                    can2.create_image(int(can2["width"])-10-30,y+10,image=_del_,anchor="nw")

                    if current_playlist!=pl:
                        can2.create_line(0,y+50, int(can2["width"]),y+50,fill="#323232")

                    _playlist.append([pl,y])



                    y+=50

            if len(_playlist)==0:
                current_playing=""
                can2.create_text(int(can2["width"])/2,y+((440*h/680)-y)/2,text="No Record",font=("FreeMono",13),fill="#888888")



        elif playlist_st==1:

            songs=[]


            ar=playlist[current_playlist]




            for song in all_songs:

                if not song.lower().find(search_var.lower())==-1:

                    try:
                        v=ar.index(song)

                    


                        if song==current_playing:
                            can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                            can2.create_image(0,y,image=circle2,anchor="nw")
                            can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                            can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill="#32fca7",outline="#32fca7")
                            can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                            col="#000000"
                        else:
                            can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                            col="#888888"



                        can2.create_text(10+30+20,y+25,text=song,font=("FreeMono",13),fill=col,anchor="w")
                        if song==current_playing:
                            can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7-30,y+45,fill="#32fca7",outline="#32fca7")
                            can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
                        else:
                            can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7,y+45,fill="#000000",outline="#000000")



                        _del_=delete
                        if song==current_playing:
                            _del_=delete2

                        can2.create_image(w-20-7-10-30,y+10,image=_del_,anchor="nw")


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
                            


                        can2.create_image(w-20-7-10-30-20-30,y+10,image=_pl_,anchor="nw")




                        if music_details[song][0]==0:

                            _fv_=favourite1

                            if song==current_playing:
                                _fv_=favourite1_


                        elif music_details[song][0]==1:


                            _fv_=favourite2

                            if song==current_playing:
                                _fv_=favourite2_


                        can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=_fv_,anchor="nw")




                        if not song==current_playing:

                            can2.create_line(0,y+50,w-20-7,y+50,fill="#323232")


                        songs.append([song,y])

                        y+=50
                    except:
                        pass
            if len(songs)==0:
                current_playing=""
                can2.create_text((w-20-7)/2,(440*h/680)/2,text="No Record!",font=("FreeMono",13),fill="#888888")

    elif st==3:
        songs=[]

        ar_=[]
        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                n=music_details[song][-1]

                if n>=5:
                    ar_.append([song,n])


        ar_=sorted(ar_, key=lambda row: row[1], reverse=True)



        for song in ar_:


            if song[0]==current_playing:
                can2.create_line(0,y, int(can2["width"]),y,fill="#000000")

                can2.create_image(0,y,image=circle2,anchor="nw")
                can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")

                can2.create_rectangle(25,y, int(can2["width"])-25,y+50-1,fill="#32fca7",outline="#32fca7")
                can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                col="#000000"
            else:
                can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                col="#888888"



            can2.create_text(10+30+20,y+25,text=song[0],font=("FreeMono",13),fill=col,anchor="w")
            if song[0]==current_playing:
                can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7-30,y+45,fill="#32fca7",outline="#32fca7")
                can2.create_image(int(can2["width"])-50,y,image=circle2,anchor="nw")
            else:
                can2.create_rectangle(w-20-7-10-30-20-30-20-30-10,y+5, w-20-7,y+45,fill="#000000",outline="#000000")




            _del_=delete
            if song[0]==current_playing:
                _del_=delete2

            can2.create_image(w-20-7-10-30,y+10,image=_del_,anchor="nw")


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
                


            can2.create_image(w-20-7-10-30-20-30,y+10,image=_pl_,anchor="nw")




            if music_details[song[0]][0]==0:

                _fv_=favourite1

                if song[0]==current_playing:
                    _fv_=favourite1_


            elif music_details[song[0]][0]==1:


                _fv_=favourite2

                if song[0]==current_playing:
                    _fv_=favourite2_


            can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=_fv_,anchor="nw")



            if not song[0]==current_playing:

                can2.create_line(0,y+50,w-20-7,y+50,fill="#323232")


            ar=[song[0],y]

            songs.append(ar)

            y+=50

        if len(songs)==0:
            current_playing=""
            can2.create_text((w-20-7)/2,(440*h/680)/2,text="No Record!",font=("FreeMono",13),fill="#888888")

    elif st==4:
        frame.place_forget()
        
        yv=(((440*h/680)+10+30)-(30+30+30))/2
        yv+=39


        #can.create_rectangle(w/2-150,yv, w/2+150,yv+30, fill="#32fca7")

        can.create_image(w/2-150-15,yv, image=circle3,anchor="nw")
        can.create_image(w/2+150-15,yv, image=circle3,anchor="nw")

        can.create_rectangle(w/2-150,yv, w/2+150,yv+30-1,fill="#32fca7",outline="#32fca7")



        can.create_text(w/2,yv+15,text="Add Folder",fill="#111111",font=("FreeMono",13))






        can.create_image(w/2-150-15,yv+60, image=circle3,anchor="nw")
        can.create_image(w/2+150-15,yv+60, image=circle3,anchor="nw")

        can.create_rectangle(w/2-150,yv+60, w/2+150,yv+30-1+60,fill="#32fca7",outline="#32fca7")


        can.create_text(w/2,yv+15+60,text="Add Audio File",fill="#111111",font=("FreeMono",13))


    can2["scrollregion"]=(0,0,w-20-7,y)

    yyy=y



    if lst==1:


        if st==2 and playlist_st==0 and pl_st==0:
            pass
        elif st==4:
            pass

        else:





            if _search==1:

                can.create_oval(10,40, 10+30,40+30,fill="#000000",outline="#000000")
                can.create_oval(w-10-30,40, w-10,40+30,fill="#000000",outline="#000000")

                can.create_rectangle(10+15,40, w-10-15,40+30,fill="#000000",outline="#000000")




            can.create_arc(10,40, 10+30,40+30, style=tk.ARC,start=90,extent=180,outline="#32fca7")
            can.create_arc(w-10-30,40, w-10,40+30, style=tk.ARC,start=270,extent=180,outline="#32fca7")

            can.create_line(10+15,40, w-10-15,40, fill="#32fca7")
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill="#32fca7")



            can.create_image(w-10-5-20,40+5,image=cancel1,anchor="nw")

            #draw_round_rec(can,10,40, w-10,40+30,10,"#000000","#32fca7",0)

            can.create_text(30+20+5,40+15,text="Search",font=("FreeMono",13),fill="#32fca7",anchor="w")



            can.create_image(30,45,image=search_im,anchor="nw")





            #draw_round_rec(can,10-2,80-10-30+40,w-10,80-30+40+(440*h/680)+10,15,"#137345","",1)
            #can.create_line(10,70,w-10,70,fill="#888888")
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill="#888888")

            frame.place(in_=root,x=10,y=80-30+40)
    else:
        
        if playlist_st==0 and st==2:
            pass
        elif st==4:
            pass
        else:
            can.create_image((w-400)/2,70,image=note,anchor="nw")

        



    if playlist_st==0 and st==2 and pl_st==0 :

        pass

    else:

        #can.create_text(10,h-20-60-20-27,text=current_playlist,font=("FreeMono",13),anchor="w",fill="cyan")


        #can.create_text(10,h-20-60-20-27-30,text=current_playlist,font=("FreeMono",13),anchor="w",fill="cyan")

        if len(current_playlist)>0:
            def get_text_length(canvas, text, font_name, font_size):
                # Create a tkinter font object with the given font name and size
                text_font = font.Font(family=font_name, size=font_size)

                # Measure the width of the text in pixels
                text_width = text_font.measure(text)
                return text_width  

            can.create_text(10,h-20-60-20-27+5,text="("+current_playlist+") ",font=("FreeMono",13,),anchor="w",fill="cyan")
            length_in_pixels = get_text_length(can, "("+current_playlist+") ", "FreeMono", 13)        
            can.create_text(10+length_in_pixels,h-20-60-20-27+5,text=current_playing,font=("FreeMono",13),anchor="w",fill="#32fca7")
        else:
            can.create_text(10,h-20-60-20-27+5,text=current_playing,font=("FreeMono",13),anchor="w",fill="#32fca7")


    can.create_line(10,h-20-60-20,w-10,h-20-60-20,fill="#888888",width=4)

    
    if st==2 and playlist_st==0:
        pass
    elif st==4:
        pass
    else:
        can.create_text(w-10,h-20-60-20+20,text=tot_tm,font=("FreeMono",13),anchor="e",fill="#32fca7")



    can.create_image(w/2-30,h-20-30-30+5, image=circle,anchor="nw")

    if pp==0:
        can.create_image(w/2-15,h-20-30-15+5, image=play,anchor="nw")
    elif pp==1:
        can.create_image(w/2-15,h-20-30-15+5, image=pause,anchor="nw")










    if lst==0:
        global sig_,sig2

        can.delete(sig_)

        try:

            if st!=4:
                sig_=can.create_line(sig2,fill="#32fca7")

        except:
            pass

        can.create_image(10,h-20-30-15+5,image=list1,anchor="nw")
    elif lst==1:
        can.create_image(10,h-20-30-15+5,image=list2,anchor="nw")



    if sort_val!="":

        can.create_image(10+30+20,h-20-30-15+5,image=sort,anchor="nw")

    else:
        can.create_image(10+30+20,h-20-30-15+5,image=sort2,anchor="nw")

    if shuff==0:

        can.create_image(10+30+20+30+20,h-20-30-15+5,image=shuffle1,anchor="nw")
    elif shuff==1:
        can.create_image(10+30+20+30+20,h-20-30-15+5,image=shuffle2,anchor="nw")





    can.create_line(w-10-100,h-20-30+5, w-10,h-20-30+5,fill="#888888",width=3)

    can.create_image(w-10-100-10-30,h-20-30-15+5,image=speaker,anchor="nw")



    can.delete(vol1)
    can.delete(vol2)
    can.delete(vol3)

    r=(w-10)-(w-10-100)


    vol1=can.create_line(w-10-100,h-20-30+5 ,w-10-100+current_volume*r,h-20-30+5,fill="#32fca7",width=3)
    vol2=can.create_oval(w-10-100+current_volume*r-5,h-20-30+5-5, w-10-100+current_volume*r+5,h-20-30+5+5,fill="#000000",outline="#32fca7")

    vol3=can.create_text(w-10-100+50,h-20-30+5+20,text=str(int(current_volume*100))+" %",fill="#32fca7",font=("FreeMono",13))



    can.create_image(w/2-30-30-30,h-20-30-15+5,image=previous,anchor="nw")
    can.create_image(w/2+30+30,h-20-30-15+5,image=next_,anchor="nw")


    if loop==0:
        can.create_image(w/2+30+30+30+20+10,h-20-30-15+5,image=loop1,anchor="nw")

    elif loop==1:
        can.create_image(w/2+30+30+30+20+10,h-20-30-15+5,image=loop2,anchor="nw")




    try:
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
    global cancel1,cancel2,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,checked,sort,delete,favourite1_,favourite2_,delete2,playlist3,sort2,loop1,loop2,wallpaper
    global circle2,circle3,expand,expand2

    circle=ImageTk.PhotoImage(file="data/circle.png")
    circle2=ImageTk.PhotoImage(file="data/circle2.png")
    circle3=ImageTk.PhotoImage(file="data/circle3.png")
    play=ImageTk.PhotoImage(file="data/play.png")
    play=ImageTk.PhotoImage(file="data/play.png")
    pause=ImageTk.PhotoImage(file="data/pause.png")
    add=ImageTk.PhotoImage(file="data/add.png")
    favourite1=ImageTk.PhotoImage(file="data/favourite1.png")
    favourite2=ImageTk.PhotoImage(file="data/favourite2.png")
    list1=ImageTk.PhotoImage(file="data/list1.png")
    list2=ImageTk.PhotoImage(file="data/list2.png")
    musical_note1=ImageTk.PhotoImage(file="data/musical_note1.png")
    musical_note2=ImageTk.PhotoImage(file="data/musical_note2.png")
    remove=ImageTk.PhotoImage(file="data/remove.png")
    rename=ImageTk.PhotoImage(file="data/rename.png")
    speaker=ImageTk.PhotoImage(file="data/speaker.png")
    previous=ImageTk.PhotoImage(file="data/previous.png")
    next_=ImageTk.PhotoImage(file="data/next.png") 
    cancel1=ImageTk.PhotoImage(file="data/cancel1.png")
    cancel2=ImageTk.PhotoImage(file="data/cancel2.png")
    search_im=ImageTk.PhotoImage(file="data/search.png")    
    shuffle1=ImageTk.PhotoImage(file="data/shuffle1.png")
    shuffle2=ImageTk.PhotoImage(file="data/shuffle2.png")
    dots=ImageTk.PhotoImage(file="data/dots.png")
    note=ImageTk.PhotoImage(file="data/note.png")
    playlist1=ImageTk.PhotoImage(file="data/playlist1.png")
    playlist2=ImageTk.PhotoImage(file="data/playlist2.png")
    checked=ImageTk.PhotoImage(file="data/checked.png")
    sort=ImageTk.PhotoImage(file="data/sort.png")
    delete=ImageTk.PhotoImage(file="data/bin.png")
    favourite1_=ImageTk.PhotoImage(file="data/favourite1_.png")
    favourite2_=ImageTk.PhotoImage(file="data/favourite2_.png")
    delete2=ImageTk.PhotoImage(file="data/bin2.png")
    playlist3=ImageTk.PhotoImage(file="data/playlist3.png")
    sort2=ImageTk.PhotoImage(file="data/sort2.png")
    loop1=ImageTk.PhotoImage(file="data/loop1.png")
    loop2=ImageTk.PhotoImage(file="data/loop2.png")
    #wallpaper=ImageTk.PhotoImage(file="data/wallpaper.png")

    expand=ImageTk.PhotoImage(file="data/expand.png")
    expand2=ImageTk.PhotoImage(file="data/expand2.png")



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

        load=can.create_arc(w/2-20,493-20-40, w/2+20,493-20,outline="#32fca7",width=2,style=tk.ARC,start=load_ang,extent=270)

        load_ang-=30

    root.after(100,load_)







circle=0
circle2=0
circle3=0
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
cancel1=0
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


w,h=950,680
root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")
root.resizable(0,0)
#root.wm_attributes("-alpha",0.92)

root.iconbitmap("data/icon.ico")
root.title("HMUSIC")



can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
can.bind("<Button-3>",can_b3)












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


style.configure("My.Vertical.TScrollbar", gripcount=0, background="#32fca7",
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


style2.configure("My.Vertical.TScrollbar2", gripcount=0, background="#32fca7",
                troughcolor='#111111', borderwidth=0, bordercolor='#111111',
                lightcolor='#111111',relief="flat", darkcolor='#111111',
                arrowsize=7)







def _on_mousewheel(e):
    global can2,can3,yyy,h,add_st

    if add_st==0:

        if int(can2["scrollregion"].split(" ")[-1])>(440*h/680):

            can2.yview_scroll(int(-1*(e.delta/120)), "units")
            #main()


    elif add_st==1:

        if int(can3["scrollregion"].split(" ")[-1])>210:
            can3.yview_scroll(int(-1*(e.delta/120)), "units")

yy=0

def on_canvas_scroll():
    global yy
    
    if can2.canvasy(0)!=yy:


        yy=can2.canvasy(0)
        #main()

    root.after(1,on_canvas_scroll)
        






frame=tk.Frame(bg="#000000",width=w-20,height=(440*h/680))

can2=tk.Canvas(frame,bg="#000000",width=w-20-7,height=(440*h/680),relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,w-20-7,(440*h/680)))
can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-1>",can2_b1)
can2.bind("<Button-3>",can_b3)





sb=ttk.Scrollbar(frame,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

sb.config(command=can2.yview)

can2.config(yscrollcommand=sb.set)
sb.pack(side=tk.LEFT,fill=tk.Y)


frame2=tk.Frame(bg="#111111",width=350,height=250)

can4=tk.Canvas(frame2,bg="#111111",width=350,height=40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can4.pack(side=tk.TOP)



a_=180
ar=[]

cx,cy=10,10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(0)
ar.append(0)

can4.create_polygon(ar,fill="#000000",outline="#000000")


a_=180
ar=[]

cx,cy=350-10,10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_-=1

ar.append(350)
ar.append(0)

can4.create_polygon(ar,fill="#000000",outline="#000000")









can4.create_text(350/2,20,text="Playlists",font=("FreeMono",13),fill="#32fca7")
can4.create_line(0,38,350,38,fill="#000000")

frame3=tk.Frame(frame2,bg="#111111",width=350,height=250-40)

can3=tk.Canvas(frame3,bg="#111111",width=350-7,height=250-40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250-40))
can3.pack(side=tk.LEFT)
can3.bind_all("<MouseWheel>",_on_mousewheel)
can3.bind("<Button-1>",can3_b1)




sb2=ttk.Scrollbar(frame3,orient=tk.VERTICAL,style="My.Vertical.TScrollbar2")

sb2.config(command=can3.yview)

can3.config(yscrollcommand=sb2.set)
sb2.pack(side=tk.LEFT,fill=tk.Y)

frame3.pack(side=tk.TOP)


can5=tk.Canvas(frame2,bg="#111111",width=350,height=10,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can5.pack(side=tk.TOP)




a_=270
ar=[]

cx,cy=10,0
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(0)
ar.append(10)

can5.create_polygon(ar,fill="#000000",outline="#000000")





a_=0
ar=[]

cx,cy=350-10,0
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(350)
ar.append(10)

can5.create_polygon(ar,fill="#000000",outline="#000000")











def search__():

    global search,search_var,mvar,songs,current_playing

    

    if search.get()!=search_var:
        search_var=search.get()



        main()

    root.after(1,search__)

search=tk.Entry(bg="#000000",fg="#32fca7",insertbackground="#32fca7",relief="flat",highlightthickness=0,border=0,width=86,font=("FreeMono",13))
#search.bind("<KeyPress>",search_keypress)
npl=tk.Entry(bg="#000000",fg="#32fca7",insertbackground="#32fca7",relief="flat",highlightthickness=0,border=0,width=85,font=("FreeMono",13))

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

            can2["scrollregion"]=(0,0,w-20-7,(440*h/680))

            loop=0


            sort_val=s[0]

            main()










            sort_st=0
            can_sort.place_forget()



sort_st=0
_sort=0
can_sort=tk.Canvas(bg="#111111",width=250,height=160,relief="flat",highlightthickness=0,border=0)

can_sort.bind("<Button-1>",can_sort_b1)



a_=180
ar=[]

cx,cy=10,10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(0)
ar.append(0)

can_sort.create_polygon(ar,fill="#000000",outline="#000000")




a_=180
ar=[]

cx,cy=250-10,10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_-=1

ar.append(250)
ar.append(0)

can_sort.create_polygon(ar,fill="#000000",outline="#000000")






a_=270
ar=[]

cx,cy=10,160-10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(0)
ar.append(160)

can_sort.create_polygon(ar,fill="#000000",outline="#000000")





a_=0
ar=[]

cx,cy=250-10,160-10
for a in range(90):

    x=10*math.sin(math.radians(a_))+cx
    y=10*math.cos(math.radians(a_))+cy

    ar.append(x)
    ar.append(y)

    a_+=1

ar.append(250)
ar.append(160)

can_sort.create_polygon(ar,fill="#000000",outline="#000000")









can_sort.create_text(125,15,text="Sort",font=("FreeMono",13),fill="#32fca7")


can_sort.create_line(0,30, 250,30,fill="#000000" )

sort_ar=[]


a=["Date Added (Descending)","Date Added (Ascending)","Title (Ascending)","Title (Descending)"]

sort_val=a[0]

y=30
for _ in a:

    can_sort.create_text(20,y+15,text=_,font=("FreeMono",13),fill="#32fca7",anchor="w")

    can_sort.create_line(0,y+30,250,y+30,fill="#000000")

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










can2.focus_set()
load_im()


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


check_geometry()

try:
    current_playing=songs[0][0]
    tm=0
    mvar=0
    play_music("music/"+current_playing,tm,1)
    get_audio_duration("music/"+current_playing)

    play_st=0
    pygame.mixer.quit()
    main()
    prog()
except:
    pass
root.mainloop()