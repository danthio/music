import subprocess
import os

import shutil



def convert_to_mp3(input_folder, ffmpeg_path=None, sample_rate=44100, channels=2, bitrate="192k"):


	all_items = os.listdir(input_folder)
	saved=os.listdir("music")





	for i in all_items:
		print(i)

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


convert_to_mp3(
	input_folder=r"C:\Users\admin\Desktop\download",
	ffmpeg_path=r"ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
)

print("\ndone")
