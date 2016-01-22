from pytube import YouTube
import os

def download_video(url, name):

	try:

		# cria uma instância de YouTube
		yt = YouTube(url)

		# seta o nome do vídeo
		yt.set_filename(name)

		# obtém o diretório corrente
		curr_dir = os.path.dirname(os.path.abspath(__file__))

		# seleciona por mp4 e pela mais alta resolução
		video = yt.filter('mp4')[-1]

		# salva o vídeo no diretório corrente
		video.download(curr_dir)

		return True

	except:

		return False