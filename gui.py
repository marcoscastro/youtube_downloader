from tkinter import *
from downloader import *

window = Tk() # cria uma janela
window.title('Youtube Downloader') # seta o título da janela
window.geometry('500x200') # seta o tamanho da janela
window.resizable(0,0) # não permite redimensionamento da janela

# label do título do programa
title = Label(window, text='Youtube Downloader', font=('Arial', 25), fg='Blue')
title.pack()

# label da mensagem de execução do programa
msg = Label(window, text='', font=('Arial', 15))

entry_url = Entry(window, width=60, justify='center') # cria uma entrada de texto
entry_url.insert(0, 'Enter the url') # seta o texto
entry_url.pack() # gerenciador de geometria
entry_url.focus_set() # obtém o foco para a entrada de texto

entry_name_video = Entry(window, width=60, justify='center')
entry_name_video.insert(0, 'Enter the name video')
entry_name_video.pack()

# função para o evento de clique do botão
def click_button():

	# obtém os textos
	url = entry_url.get()
	name_video = entry_name_video.get()

	if download_video(url, name_video):
		msg['fg'] = 'Green'
		msg['text'] = 'Download feito com sucesso!'
	else:
		msg['fg'] = 'Red'
		msg['text'] = 'Ocorreu alguma falha... :('

# cria um botão
btn = Button(window, text='Download now', width=20, command=click_button)
btn.pack()

# exibe a mensagem
msg.pack()

# loop principal da aplicação
window.mainloop()