from pytube import YouTube
from PyQt5 import  uic,QtWidgets
import os

#direotio para salvar os arquivos
dirAudio='Audios'
dirVideo='Videos'

def downloadAudio():

    #limpando mensagens
    telaDowload.textInfo.setText(" ")
    telaDowload.textInfoMotiv.setText(" ")

    # recebendo url do youtube
    try:
        yt = YouTube(str(telaDowload.lineEditLink.text()))   
    except:
        telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
        return
    
    # extraindo audio
    try:
        audio = yt.streams.filter(only_audio=True).first()
    except:
        telaDowload.textInfoMotiv.setText("URL Inválido para extração de aúdio.")
        return
    # diretorio do arquivo
    #diretorio=str('Audios')
    #diretorio = str(input("Onde você deseja salvar o arquivo? (deixe em branco para o diretorio atual)\n"))
    
    # download do arquivo
    try:
        out_file = audio.download(output_path=dirAudio)
    except:
        telaDowload.textInfoMotiv.setText("Erro no download, verifique o link.")
        return
    # salvando arquivo
    try:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Salvando")
        # resultado
        telaDowload.textInfo.setText(yt.title[0:50] + "  |  Download - MP3 - concluído.")
    except:
        telaDowload.textInfoMotiv.setText("Download não realizado, Arquivo já existe.")
        return

def downloadVideo():

    #limpando mensagens
    telaDowload.textInfo.setText(" ")
    telaDowload.textInfoMotiv.setText(" ")
    
    # recebendo url do video
    try:
        yt = YouTube(str(telaDowload.lineEditLink.text()))
    except:
        telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
        return
    
    # extraindo video de alta qualidade
    try:
        video = yt.streams.get_highest_resolution()
    except:
        telaDowload.textInfoMotiv.setText("URL Inválido para Download de Video.")
        return
    # diretorio do arquivo
    #diretorio=str('Videos')
    #diretorio = str(input("Onde você deseja salvar o arquivo? (deixe em branco para o diretorio atual)\n"))
    
    # download do arquivo
    try:
        telaDowload.textInfo.setText("Carregando...")
        out_file = video.download(output_path=dirVideo)
    except:
        telaDowload.textInfoMotiv.setText("Erro no download, verifique o link.")
        return
    
    # salvando arquivo
    try:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        print("Salvando")
         # resultado
        telaDowload.textInfo.setText(yt.title[0:50] + "  |  Download - MP4 - concluído.")
    except:
        telaDowload.textInfo.setText("Download não realizado, Arquivo já existe.")
        return


app=QtWidgets.QApplication([])
telaDowload=uic.loadUi("telaYtDownload.ui")
telaDowload.btnMP3.clicked.connect(downloadAudio)
telaDowload.btnMP4.clicked.connect(downloadVideo)
telaDowload.btn_close.clicked.connect(exit)

telaDowload.show()
app.exec()

