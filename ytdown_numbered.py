from pytube import YouTube
SAVE_PATH = "E:/VIDEOS/PLAYLIST/"
links = open('list_name.txt','r')
i = 1
for l in links:
	get_true = True
	yt = YouTube(l)
			
	while get_true:
		try:
			yt = YouTube(l)
			get_true = False
		except:
			print("Connection Error, Retrying")
			continue
	mp4files = yt.filter('mp4')
	try:
		file_name = str(i)+" - "+str(yt.filename)
		yt.set_filename(file_name)
		print(file_name)
		print(mp4files[-1])
	except:
		pass
	video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		video.download(SAVE_PATH)
		i = i+1
	except:
		print("Error, Maybe Duplicate File")
		continue