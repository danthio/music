
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



im=Image.open("data/search.png")
im=im.resize((20,20))
im.save("data/search.png")
"""

im=Image.open("data/next.png")
im=im.resize((30,30))
im.save("data/next.png")
"""




def convert_folder_to_audio(input_folder, ffmpeg_path=None, sample_rate=44100, channels=2, bitrate="192k"):

    global can,load,w



    can.delete(load)

    load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill="#32fca7")





    try:
    



        all_items = os.listdir(input_folder)
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
            except:
                pass

    except:
        pass


    can.delete(load)

    load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#32fca7")

def convert_file_to_audio(input_file, ffmpeg_path=None, sample_rate=44100, channels=2, bitrate="192k"):

    global can,load,w



    can.delete(load)

    load=can.create_text(w/2,493-20-40-30,text="...",font=("FreeMono",25),fill="#32fca7")


    try:

    


        saved=os.listdir("music")






        i=input_file.split("/")[-1]

        con=0

        for i_ in saved:

            if i[:-3]==i_[:-3]:
                con=1
        if con==1:
            can.delete(load)

            load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#32fca7")
            return


        if i[-3:]=="mp3":

            destination_file = os.path.join("music", os.path.basename(input_file))
            shutil.copy(input_file, "music")

            can.delete(load)

            load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#32fca7")

            return




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
        except:
            pass


    except:
        pass

    can.delete(load)

    load=can.create_text(w/2,493-20-40-30,text="Done!",font=("FreeMono",13),fill="#32fca7")


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

    prog1=can.create_line(10,h-20-60-20, x_+10,h-20-60-20,fill="#32fca7",width=2)
    prog2=can.create_oval(x_+10-5,h-20-60-20-5, x_+10+5,h-20-60-20+5,fill="#000000",outline="#32fca7")



def timer():
    global play_st,tm,start_time,can
    global ctime,tot_tm_
    global prog1,prog2
    global tvar
    global mvar
    global current_playing,songs
    global w,h,add_st,frame2,can2

    if play_st==1:




        prog()

        tm+=1

        if tm>=tot_tm_:
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


    add_st=0
    frame2.place_forget()





    if st==2 and playlist_st==0:


        cx,cy=int(can2["width"])-10-5-20+10,5+10

        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:
            npl.delete(0,tk.END)
            npl.place_forget()

            main()
            return



        if 10<=e.x<=int(can2["width"])-10:
            if 5<=e.y<=35:

                can2["scrollregion"]=(0,0,w-20-7,390)
                npl.delete(0,tk.END)
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
                npl.place_forget()
                main()

            return


        if int(can2["width"])/2-100<=e.x<=int(can2["width"])/2+100:
            if 45<=e.y<=45+30:

                if not npl.get()=="":
                    create_playlist(npl.get(),0)
                    npl.delete(0,tk.END)
                    npl.place_forget()
                    main()
                return


        for _pl in _playlist:
            

            cx,cy=int(can2["width"])-10-20+10,_pl[1]+15+10
            r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
            if r<=10:
                can2["scrollregion"]=(0,0,w-20-7,390)
                create_playlist(_pl[0],con=3)

                main()
                return

            if _pl[1]<=can2.canvasy(e.y)<=_pl[1]+50:

                
                con=0
                if current_playlist==_pl[0]:
                    con=1
                current_playlist=_pl[0]
                playlist_st=1





                main()

                if con==0:


                    
                    try:

                        can2["scrollregion"]=(0,0,w-20-7,390)
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




            add_st=1
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

        cx,cy=w-20-7-10-30+15,y+15+15
        r=math.sqrt((e.x-cx)**2+(can2.canvasy(e.y)-cy)**2)
        if r<=15:

            os.remove("music/"+s[0])
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
    global load


    add_st=0
    frame2.place_forget()

    xv=w/6




    if xv-60<=e.x<=xv+60:
        if 0<=e.y<=35:

            can.delete(load)

            h=640
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")
            st=0
            lst=1
            can2["scrollregion"]=(0,0,w-20-7,390)
            current_playlist=""

            add_st=0
            frame2.place_forget()

            can2.focus_set()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            npl.place_forget()




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


            
            return


    if xv*2-60<=e.x<=xv*2+60:
        if 0<=e.y<=35:

            can.delete(load)

            h=640
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            st=1
            lst=1
            can2["scrollregion"]=(0,0,w-20-7,390)
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            npl.place_forget()
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

            return

    if xv*3-60<=e.x<=xv*3+60:
        if 0<=e.y<=35:

            can.delete(load)
            h=670
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            
            playlist_st=0
            can2["scrollregion"]=(0,0,w-20-7,390)
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            npl.place_forget()
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
            can.delete(load)
            h=640
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            st=3
            can2["scrollregion"]=(0,0,w-20-7,390)
            current_playlist=""
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
            npl.place_forget()
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

            return


    if xv*5-60<=e.x<=xv*5+60:
        if 0<=e.y<=35:

            can.delete(load)

            h=640
            can["height"]=h
            root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")

            st=4
            can2["scrollregion"]=(0,0,w-20-7,390)
            main()
            can2.focus_set()
            add_st=0
            frame2.place_forget()
            search.delete(0,tk.END)
            search.place_forget()
            npl.delete(0,tk.END)
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
        #search_var=""

        main()


        return

    if 10<=e.x<=w-10-5-30:
        if 40<=e.y<=40+30:
            search.place(in_=root,x=20,y=45)
            search.focus_set()

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
    #shuffle



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
                can3.create_line(0,y+50,350-7,y+50,fill="#777777")

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
            folder=filedialog.askdirectory(title="Select a Folder")



            convert_folder_to_audio(
                input_folder=folder,
                ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
            )


        cx,cy=w/2+150,yv+15

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            folder=filedialog.askdirectory(title="Select a Folder")


            convert_folder_to_audio(
                input_folder=folder,
                ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
            )


        if w/2-150<=e.x<=w/2+150:
            if yv<=e.y<=yv+30:
                can.delete(load)
                folder=filedialog.askdirectory(title="Select a Folder")


                convert_folder_to_audio(
                    input_folder=folder,
                    ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
                )


















        cx,cy=w/2-150,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            file=filedialog.askopenfilename()
            convert_file_to_audio(
                input_file=file,
                ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
            )



        cx,cy=w/2+150,yv+15+60

        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
        if r<=15:
            can.delete(load)
            file=filedialog.askopenfilename()


            convert_file_to_audio(
                input_file=file,
                ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
            )



        if w/2-150<=e.x<=w/2+150:
            if yv+60<=e.y<=yv+30+60:
                can.delete(load)
                file=filedialog.askopenfilename()
                convert_file_to_audio(
                    input_file=file,
                    ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
                )





        #file=filedialog.askopenfilename()
        #folder=filedialog.askdirectory(title="Select a Folder")





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

        vol1=can.create_line(w-10-100,h-20-30+5 ,w-10-100+current_volume*r,h-20-30+5,fill="#32fca7",width=2)
        vol2=can.create_oval(w-10-100+current_volume*r-5,h-20-30+5-5, w-10-100+current_volume*r+5,h-20-30+5+5,fill="#000000",outline="#32fca7")

        vol3=can.create_text(w-10-100+50,h-20-30+5+20,text=str(int(current_volume*100))+" %",fill="#32fca7",font=("FreeMono",13))


    root.after(500,check_volume)


def b3(e):
    pygame.mixer.quit()




def play_music(file,time,con=0):
    global current_playing



    # Initialize Pygame Mixer
    pygame.mixer.init()


    # Load the audio file
    pygame.mixer.music.load(file)  # Replace with your audio file path

    if con==0:

        update_details(current_playing,1)

    # Start playing the audio from a specific position (in seconds)
    start_time = time  # Replace with the desired starting time in seconds
    pygame.mixer.music.play(start=round(start_time))  # Use round for an integer value








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



def main():

    global can,st,w,h
    global circle,play,pause,add,favourite1,favourite2,list1,list2,musical_note1,musical_note2,remove,rename,speaker,previous,next_
    global pp,fv,lst
    global frame,can2
    global current_playing
    global yyy

    global songs
    global search,search_var
    global cancel,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,sort
    global music_details
    global vol1,vol2,vol3,current_volume
    global playlist,playlist_st
    global can2
    global current_playlist
    global _playlist
    global ctime,prog1,prog2
    global pl_st
    global shuff



    update_details()
    create_playlist()

    can.delete("all")

    search["width"]=77

    xv=w/6
    x=xv


    label=["All Songs","Favourites","Playlist","Most Played","Add Song"]

    for l in range(len(label)):

        col="#777777"

        if l==st:
            col="#32fca7"


            can.create_arc(x-60,5, x-60+30,5+30, style="arc",start=90,extent=180,outline="#32fca7")
            can.create_arc(x+60,5, x+60-30,5+30, style="arc",start=270,extent=180,outline="#32fca7")

            can.create_line(x-60+15,5, x+60-15,5, fill="#32fca7")
            can.create_line(x-60+15-1,35, x+60-15,35, fill="#32fca7")








        #can.create_rectangle(x-50,20-10, x+50,20+10, outline="red")



        can.create_text(x,20,text=label[l],fill=col,font=("FreeMono",13),anchor="c")



        x+=xv





    


    all_songs = os.listdir("music")

    can2.delete("all")

    y=0

    

    if st==0:

        songs=[]
        

        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                if song==current_playing:
                    can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                    col="#32fca7"
                else:
                    can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                    col="#777777"

                ex=""

                if len(song)>70:
                    ex="..."

                can2.create_text(10+30+20,y+25,text=song[:70]+ex,font=("FreeMono",13),fill=col,anchor="w")

                can2.create_image(w-20-7-10-30,y+15,image=remove,anchor="nw")


                con=0

                for i in playlist:


                    try:
                        v=playlist[i].index(song)
                        con=1
                    except:
                        pass


                if con==0:

                    can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist1,anchor="nw")
                elif con==1:
                    can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist2,anchor="nw")




                if music_details[song][0]==0:

                    can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite1,anchor="nw")
                elif music_details[song][0]==1:
                    can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite2,anchor="nw")



                can2.create_line(0,y+50,w-20-7,y+50,fill="#222222")

                ar=[song,y]

                songs.append(ar)

                y+=50

        if len(songs)==0:
            can2.create_text((w-20-7)/2,390/2,text="No Record!",font=("FreeMono",13),fill="#777777")
    elif st==1:
        songs=[]


        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                if music_details[song][0]==1:

                    if song==current_playing:
                        can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                        col="#32fca7"
                    else:
                        can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                        col="#777777"

                    ex=""

                    if len(song)>70:
                        ex="..."

                    can2.create_text(10+30+20,y+25,text=song[:70]+ex,font=("FreeMono",13),fill=col,anchor="w")


                    can2.create_image(w-20-7-10-30,y+15,image=remove,anchor="nw")


                    con=0

                    for i in playlist:


                        try:
                            v=playlist[i].index(song)
                            con=1
                        except:
                            pass


                    if con==0:

                        can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist1,anchor="nw")
                    elif con==1:
                        can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist2,anchor="nw")




                    if music_details[song][0]==0:

                        can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite1,anchor="nw")
                    elif music_details[song][0]==1:
                        can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite2,anchor="nw")


                    can2.create_line(0,y+50,w-20-7,y+50,fill="#222222")





                    ar=[song,y]

                    songs.append(ar)

                    y+=50


        if len(songs)==0:
            can2.create_text((w-20-7)/2,390/2,text="No Record!",font=("FreeMono",13),fill="#777777")
    elif st==2:

        create_playlist()

        if playlist_st==0:




            can.create_arc(10,40, 10+30,40+30, style="arc",start=90,extent=180,outline="#32fca7")
            can.create_arc(w-10-30,40, w-10,40+30, style="arc",start=270,extent=180,outline="#32fca7")

            can.create_line(10+15,40, w-10-15,40, fill="#32fca7")
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill="#32fca7")



            can.create_text(30+20+5,40+15,text="Search",font=("FreeMono",13),fill="#32fca7",anchor="w")



            can.create_image(w-10-5-20,40+5,image=cancel,anchor="nw")
            can.create_image(30,40+5,image=search_im,anchor="nw")






            draw_round_rec(can,10-1,80-10-30+40,w-10,80-30+40+390+10,10,"#000000","#32fca7",0)
            #can.create_line(10,70,w-10,70,fill="#777777")
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill="#777777")

            frame.place(in_=root,x=10,y=80-30+40)













            y=5

            can2.delete("all")




            can2.create_arc(10,y, 10+30,y+30, style="arc",start=90,extent=180,outline="#32fca7")
            can2.create_arc(int(can2["width"])-10-30,y, int(can2["width"])-10,y+30, style="arc",start=270,extent=180,outline="#32fca7")

            can2.create_line(10+15,y, int(can2["width"])-10-15,y, fill="#32fca7")
            can2.create_line(10-1+15,y+30, int(can2["width"])-10-15,y+30, fill="#32fca7")







            can2.create_text(30,y+15,text="New Playlist",font=("FreeMono",13),fill="#32fca7",anchor="w")

            can2.create_image(int(can2["width"])-10-5-20,y+5,image=cancel,anchor="nw")


            y+=40






            #can2.create_rectangle(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y+30, outline="#32fca7")

            can2.create_arc(int(can2["width"])/2-100-15,y, int(can2["width"])/2-100+15,y+30, style="arc",start=90,extent=180,outline="#32fca7")
            can2.create_arc(int(can2["width"])/2+100-15,y, int(can2["width"])/2+100+15,y+30, style="arc",start=270,extent=180,outline="#32fca7")

            can2.create_line(int(can2["width"])/2-100,y, int(can2["width"])/2+100,y, fill="#32fca7")
            can2.create_line(int(can2["width"])/2-100-1,y+30, int(can2["width"])/2+100,y+30, fill="#32fca7")

            can2.create_text(int(can2["width"])/2,y+15,text="Create New Playlist",font=("FreeMono",13),fill="#32fca7")

            y+=30+20

            can2.create_line(0,y, int(can2["width"]),y,fill="#777777")

            _playlist=[]

            for pl in playlist:

                if not pl.lower().find(search_var.lower())==-1:
                    col="#777777"

                    con=0

                    if pl==current_playlist:
                        col="#32fca7"
                        con=1

                    if con==0:
                        can2.create_image(10,y+10,image=playlist1,anchor="nw")
                    elif con==1:
                        can2.create_image(10,y+10,image=playlist2,anchor="nw")




                    can2.create_text(10+30+10,y+25,text=pl,font=("FreeMono",13),fill=col,anchor="w")

                    can2.create_image(int(can2["width"])-10-20,y+15,image=remove,anchor="nw")


                    can2.create_line(0,y+50, int(can2["width"]),y+50,fill="#777777")

                    _playlist.append([pl,y])



                    y+=50

            if len(_playlist)==0:
                can2.create_text(int(can2["width"])/2,y+(390-y)/2,text="No Record",font=("FreeMono",13),fill="#777777")



        elif playlist_st==1:

            songs=[]


            ar=playlist[current_playlist]




            for song in all_songs:

                if not song.lower().find(search_var.lower())==-1:

                    try:
                        v=ar.index(song)

                    


                        if song==current_playing:
                            can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                            col="#32fca7"
                        else:
                            can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                            col="#777777"

                        ex=""

                        if len(song)>70:
                            ex="..."

                        can2.create_text(10+30+20,y+25,text=song[:70]+ex,font=("FreeMono",13),fill=col,anchor="w")


                        can2.create_image(w-20-7-10-30,y+15,image=remove,anchor="nw")


                        con=0

                        for i in playlist:


                            try:
                                v=playlist[i].index(song)
                                con=1
                            except:
                                pass


                        if con==0:

                            can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist1,anchor="nw")
                        elif con==1:
                            can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist2,anchor="nw")




                        if music_details[song][0]==0:

                            can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite1,anchor="nw")
                        elif music_details[song][0]==1:
                            can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite2,anchor="nw")



                        can2.create_line(0,y+50,w-20-7,y+50,fill="#222222")


                        songs.append([song,y])

                        y+=50
                    except:
                        pass
            if len(songs)==0:
                can2.create_text((w-20-7)/2,390/2,text="No Record!",font=("FreeMono",13),fill="#777777")

    elif st==3:
        songs=[]

        ar_=[]
        for song in all_songs:

            if not song.lower().find(search_var.lower())==-1:

                n=music_details[song][-1]

                if n>0:
                    ar_.append([song,n])


        ar_=sorted(ar_, key=lambda row: row[1], reverse=True)



        for song in ar_:


            if song[0]==current_playing:
                can2.create_image(10,y+10,image=musical_note2,anchor="nw")
                col="#32fca7"
            else:
                can2.create_image(10,y+10,image=musical_note1,anchor="nw")
                col="#777777"

            ex=""

            if len(song[0])>70:
                ex="..."

            can2.create_text(10+30+20,y+25,text=song[0][:70]+ex,font=("FreeMono",13),fill=col,anchor="w")


            can2.create_image(w-20-7-10-30,y+15,image=remove,anchor="nw")


            con=0

            for i in playlist:


                try:
                    v=playlist[i].index(song)
                    con=1
                except:
                    pass


            if con==0:

                can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist1,anchor="nw")
            elif con==1:
                can2.create_image(w-20-7-10-30-20-30,y+10,image=playlist2,anchor="nw")




            if music_details[song[0]][0]==0:

                can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite1,anchor="nw")
            elif music_details[song[0]][0]==1:
                can2.create_image(w-20-7-10-30-20-30-20-30,y+10,image=favourite2,anchor="nw")



            can2.create_line(0,y+50,w-20-7,y+50,fill="#222222")

            ar=[song[0],y]

            songs.append(ar)

            y+=50

        if len(songs)==0:
            can2.create_text((w-20-7)/2,390/2,text="No Record!",font=("FreeMono",13),fill="#777777")

    elif st==4:
        frame.place_forget()
        
        yv=((493-39)-(30+30+30))/2
        yv+=39


        #can.create_rectangle(w/2-150,yv, w/2+150,yv+30, fill="#32fca7")
        can.create_arc(w/2-150-15,yv, w/2-150+15,yv+30,start=90,extent=180,style="arc",outline="#32fca7")
        can.create_arc(w/2+150-15,yv, w/2+150+15,yv+30,start=270,extent=180,style="arc",outline="#32fca7")

        can.create_line(w/2-150,yv, w/2+150,yv, fill="#32fca7")
        can.create_line(w/2-150-1,yv+30, w/2+150,yv+30, fill="#32fca7")


        can.create_text(w/2,yv+15,text="Add Folder",fill="#32fca7",font=("FreeMono",13))






        #can.create_rectangle(w/2-150,yv+60, w/2+150,yv+30+60, fill="#32fca7")
        can.create_arc(w/2-150-15,yv+60, w/2-150+15,yv+30+60,start=90,extent=180,style="arc",outline="#32fca7")
        can.create_arc(w/2+150-15,yv+60, w/2+150+15,yv+30+60,start=270,extent=180,style="arc",outline="#32fca7")

        can.create_line(w/2-150,yv+60, w/2+150,yv+60, fill="#32fca7")
        can.create_line(w/2-150-1,yv+30+60, w/2+150,yv+30+60, fill="#32fca7")

        can.create_text(w/2,yv+15+60,text="Add Audio File",fill="#32fca7",font=("FreeMono",13))


    can2["scrollregion"]=(0,0,w-20-7,y)

    yyy=y



    if lst==1:


        if st==2 and playlist_st==0 and pl_st==0:
            pass
        elif st==4:
            pass

        else:



            can.create_arc(10,40, 10+30,40+30, style="arc",start=90,extent=180,outline="#32fca7")
            can.create_arc(w-10-30,40, w-10,40+30, style="arc",start=270,extent=180,outline="#32fca7")

            can.create_line(10+15,40, w-10-15,40, fill="#32fca7")
            can.create_line(10-1+15,40+30, w-10-15,40+30, fill="#32fca7")



            #draw_round_rec(can,10,40, w-10,40+30,10,"#000000","#32fca7",0)

            can.create_text(30+20+5,40+15,text="Search",font=("FreeMono",13),fill="#32fca7",anchor="w")



            can.create_image(w-10-5-20,40+5,image=cancel,anchor="nw")
            can.create_image(30,45,image=search_im,anchor="nw")





            draw_round_rec(can,10-1,80-10-30+40,w-10,80-30+40+390+10,10,"#000000","#32fca7",0)
            #can.create_line(10,70,w-10,70,fill="#777777")
            #can.create_line(10,80+h-240+10,w-10,80+h-240+10,fill="#777777")

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


        can.create_text(10,h-20-60-20-27-30,text=current_playlist,font=("FreeMono",13),anchor="w",fill="cyan")
        
        can.create_text(10,h-20-60-20-27,text=current_playing,font=("FreeMono",13),anchor="w",fill="#32fca7")



    can.create_line(10,h-20-60-20,w-10,h-20-60-20,fill="#777777",width=2)

    
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
        can.create_image(10,h-20-30-15+5,image=list1,anchor="nw")
    elif lst==1:
        can.create_image(10,h-20-30-15+5,image=list2,anchor="nw")




    can.create_image(10+30+20,h-20-30-15+5,image=sort,anchor="nw")

    if shuff==0:

        can.create_image(10+30+20+30+20,h-20-30-15+5,image=shuffle1,anchor="nw")
    elif shuff==1:
        can.create_image(10+30+20+30+20,h-20-30-15+5,image=shuffle2,anchor="nw")

    can.create_line(w-10-100,h-20-30+5, w-10,h-20-30+5,fill="#777777",width=2)

    can.create_image(w-10-100-10-30,h-20-30-15+5,image=speaker,anchor="nw")



    can.delete(vol1)
    can.delete(vol2)
    can.delete(vol3)

    r=(w-10)-(w-10-100)


    vol1=can.create_line(w-10-100,h-20-30+5 ,w-10-100+current_volume*r,h-20-30+5,fill="#32fca7",width=2)
    vol2=can.create_oval(w-10-100+current_volume*r-5,h-20-30+5-5, w-10-100+current_volume*r+5,h-20-30+5+5,fill="#000000",outline="#32fca7")

    vol3=can.create_text(w-10-100+50,h-20-30+5+20,text=str(int(current_volume*100))+" %",fill="#32fca7",font=("FreeMono",13))



    can.create_image(w/2-30-30-30,h-20-30-15+5,image=previous,anchor="nw")
    can.create_image(w/2+30+30,h-20-30-15+5,image=next_,anchor="nw")

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
    global cancel,search_im,shuffle1,shuffle2,dots,note,playlist1,playlist2,checked,sort

    circle=ImageTk.PhotoImage(file="data/circle.png")
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
    cancel=ImageTk.PhotoImage(file="data/cancel.png")
    search_im=ImageTk.PhotoImage(file="data/search.png")    
    shuffle1=ImageTk.PhotoImage(file="data/shuffle1.png")
    shuffle2=ImageTk.PhotoImage(file="data/shuffle2.png")
    dots=ImageTk.PhotoImage(file="data/dots.png")
    note=ImageTk.PhotoImage(file="data/note.png")
    playlist1=ImageTk.PhotoImage(file="data/playlist1.png")
    playlist2=ImageTk.PhotoImage(file="data/playlist2.png")
    checked=ImageTk.PhotoImage(file="data/checked.png")
    sort=ImageTk.PhotoImage(file="data/sort.png")


def check_pl():
    global npl,plv,can2,playlist_st,st

    if st==2 and playlist_st==0:

        if can2.canvasy(0)!=plv:

            plv=can2.canvasy(0)

            if not can2.canvasy(0)==0:
                npl.place_forget()


    root.after(1,check_pl)

def load_():
    global can,load,load_ang,load_st
    global st,w


    if st==4 and load_st==1:

        can.delete(load)

        load=can.create_arc(w/2-20,493-20-40, w/2+20,493-20,outline="#32fca7",width=2,style="arc",start=load_ang,extent=270)

        load_ang-=30

    root.after(100,load_)






circle=0
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

load=0
load_st=0
load_ang=90

sort=0

pl_st=0

shuff=0

root=tk.Tk()

wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()

w,h=900,640

root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+0")
root.resizable(0,0)
root.wm_attributes("-alpha",0.92)




can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
#can.bind("<Button-3>",b3)












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
                troughcolor='#323232', borderwidth=0, bordercolor='#323232',
                lightcolor='#323232',relief="flat", darkcolor='#323232',
                arrowsize=7)







def _on_mousewheel(e):
    global can2,can3,yyy,h,add_st

    if add_st==0:

        if int(can2["scrollregion"].split(" ")[-1])>390:

            can2.yview_scroll(int(-1*(e.delta/120)), "units")
    elif add_st==1:

        if int(can3["scrollregion"].split(" ")[-1])>210:
            can3.yview_scroll(int(-1*(e.delta/120)), "units")






frame=tk.Frame(bg="#000000",width=w-20,height=390)

can2=tk.Canvas(frame,bg="#000000",width=w-20-7,height=390,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,w-20-7,390))
can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-1>",can2_b1)




sb=ttk.Scrollbar(frame,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

sb.config(command=can2.yview)

can2.config(yscrollcommand=sb.set)
sb.pack(side=tk.LEFT,fill=tk.Y)


frame2=tk.Frame(bg="#323232",width=350,height=250)

can4=tk.Canvas(frame2,bg="#323232",width=350,height=40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can4.pack(side=tk.TOP)



a_=270

ar=[]

for a in range(90):

    x=10*math.sin(math.radians(a_))+10
    y=10*math.cos(math.radians(a_))+10

    a_-=1

    ar.append(x)
    ar.append(y)

ar.append(0)
ar.append(0)

can4.create_polygon(ar,fill="#000000",outline="#000000")


a_=180

ar=[]

for a in range(90):

    x=10*math.sin(math.radians(a_))+350-10
    y=10*math.cos(math.radians(a_))+10

    a_-=1

    ar.append(x)
    ar.append(y)

ar.append(350)
ar.append(0)

can4.create_polygon(ar,fill="#000000",outline="#000000")



can4.create_text(350/2,20,text="Playlists",font=("FreeMono",13),fill="#32fca7")
can4.create_line(0,38,350,38,fill="#32fca7")

frame3=tk.Frame(frame2,bg="#323232",width=350,height=250-40)

can3=tk.Canvas(frame3,bg="#323232",width=350-7,height=250-40,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250-40))
can3.pack(side=tk.LEFT)
can3.bind_all("<MouseWheel>",_on_mousewheel)
can3.bind("<Button-1>",can3_b1)




sb2=ttk.Scrollbar(frame3,orient=tk.VERTICAL,style="My.Vertical.TScrollbar2")

sb2.config(command=can3.yview)

can3.config(yscrollcommand=sb2.set)
sb2.pack(side=tk.LEFT,fill=tk.Y)

frame3.pack(side=tk.TOP)


can5=tk.Canvas(frame2,bg="#323232",width=350,height=10,relief="flat",highlightthickness=0,border=0,
    scrollregion=(0,0,300-7,250))
can5.pack(side=tk.TOP)


a_=0

ar=[]

for a in range(90):

    x=10*math.sin(math.radians(a_))+10
    y=10*math.cos(math.radians(a_))+0

    a_-=1

    ar.append(x)
    ar.append(y)

ar.append(0)
ar.append(10)

can5.create_polygon(ar,fill="#000000",outline="#000000")



a_=90

ar=[]

for a in range(90):

    x=10*math.sin(math.radians(a_))+350-10
    y=10*math.cos(math.radians(a_))+0

    a_-=1

    ar.append(x)
    ar.append(y)

ar.append(350)
ar.append(10)

can5.create_polygon(ar,fill="#000000",outline="#000000")



def search__():

    global search,search_var,mvar,songs,current_playing

    

    if search.get()!=search_var:
        search_var=search.get()



        main()

    root.after(1,search__)

search=tk.Entry(bg="#000000",fg="#32fca7",insertbackground="#32fca7",relief="flat",highlightthickness=0,border=0,width=77,font=("FreeMono",13))
#search.bind("<KeyPress>",search_keypress)
npl=tk.Entry(bg="#000000",fg="#32fca7",insertbackground="#32fca7",relief="flat",highlightthickness=0,border=0,width=78,font=("FreeMono",13))

ls=0
def mvar_():


    global ls,current_playing,songs,mvar

    if len(songs)!=ls:

        ls=len(songs)


        try:
            for s in range(len(songs)):
                if songs[s][0]==current_playing:
                   

                    mvar=s


        except:
            pass

    root.after(1,mvar_)



can2.focus_set()
load_im()

main()
timer()

search__()
check_volume()

mvar_()


check_pl()



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
