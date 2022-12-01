from pytube import YouTube,Playlist
from PyQt5 import  uic,QtWidgets
import os

#direotio para salvar os arquivos
dirAudio='C:\YtDownload\Media\Musicas'
dirVideo='C:\YtDownload\Media\Videos'

def downloadAudio():
    """Realiza o download do aúdio"""

    #limpando mensagens
    telaDowload.textInfo.setText(" ")
    telaDowload.textInfoMotiv.setText(" ")

    # recebendo url do youtube
    try:
        yt = YouTube(str(telaDowload.lineEditLink.text())) 
    except:
        telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
        return


    #verificando se arquivp já exixte
    arquivo=dirAudio+'\\'+yt.title+'.mp3'
    
    if os.path.isfile(arquivo):
        telaDowload.textInfoMotiv.setText("Download não realizado, Arquivo já existe.")
        return
    
    # extraindo audio
    try:
        audio = yt.streams.filter(only_audio=True).first()
    except:
        telaDowload.textInfoMotiv.setText("URL Inválido para extração de aúdio.")
        return
    
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
        os.remove(base+'.mp4')
        return

def downloadVideo():
    """Realiza o download do vídeo"""

    #limpando mensagens
    telaDowload.textInfo.setText(" ")
    telaDowload.textInfoMotiv.setText(" ")
    
    # recebendo url do video
    try:
        yt = YouTube(str(telaDowload.lineEditLink.text()))
    except Exception as e:
        
        print(e)
        telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
        return
        
    
    playlist = Playlist(yt)
    
    print(len(playlist))

    #verificando se arquivo já exixte
    arquivo=dirVideo+'\\'+yt.title+'.mp4'
    
    if os.path.isfile(arquivo):
        telaDowload.textInfoMotiv.setText("Download não realizado, Arquivo já existe.")
        return

    # extraindo video de alta qualidade
    try:
        video = yt.streams.get_highest_resolution()
    except:
        telaDowload.textInfoMotiv.setText("URL Inválido para Download de Video.")
        return

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
        # mostra resultado
        telaDowload.textInfo.setText(yt.title[0:50] + "  |  Download - MP4 - concluído.")
    except:
        telaDowload.textInfo.setText("Download não realizado, Arquivo já existe.")
        return

def playlistVideo():
    """Realiza o download do vídeo"""

    #limpando mensagens
    telaDowload.textInfo.setText(" ")
    telaDowload.textInfoMotiv.setText(" ")
    
    # recebendo url do video

    try:
        try:
            yt = YouTube(str(telaDowload.lineEditLink.text()))
        except:
            yt_playlist = Playlist(str(telaDowload.lineEditLink.text()))
    except Exception as e:
        
        print(e)
        telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
        return
        
    
    print(len(yt_playlist))
    if len(yt_playlist)>0:
        

        for yt_url in yt_playlist:
            yt = YouTube(str(yt_url))
            #verificando se arquivo já exixte
            arquivo=dirVideo+'\\'+yt.title+'.mp4'
            
            if os.path.isfile(arquivo):
                telaDowload.textInfoMotiv.setText("Download não realizado, Arquivo já existe.")
                return

            # extraindo video de alta qualidade
            try:
                video = yt.streams.get_highest_resolution()
            except:
                telaDowload.textInfoMotiv.setText("URL Inválido para Download de Video.")
                return

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
                # mostra resultado
                telaDowload.textInfo.setText(yt.title[0:50] + "  |  Download - MP4 - concluído.")
            except:
                telaDowload.textInfo.setText("Download não realizado, Arquivo já existe.")
                return
    else:
         # recebendo url do video
        try:
            yt = YouTube(str(telaDowload.lineEditLink.text()))
        except Exception as e:
            
            print(e)
            telaDowload.textInfoMotiv.setText("Entre com um URL de Youtube válido.")
            return
            
        
        playlist = Playlist(yt)
        
        print(len(playlist))

        #verificando se arquivo já exixte
        arquivo=dirVideo+'\\'+yt.title+'.mp4'
        
        if os.path.isfile(arquivo):
            telaDowload.textInfoMotiv.setText("Download não realizado, Arquivo já existe.")
            return

        # extraindo video de alta qualidade
        try:
            video = yt.streams.get_highest_resolution()
        except:
            telaDowload.textInfoMotiv.setText("URL Inválido para Download de Video.")
            return

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
            # mostra resultado
            telaDowload.textInfo.setText(yt.title[0:50] + "  |  Download - MP4 - concluído.")
        except:
            telaDowload.textInfo.setText("Download não realizado, Arquivo já existe.")
            return
            



def sair():
    """Sair do programa"""
    exit()

app=QtWidgets.QApplication([])
telaDowload=uic.loadUi("telaYtDownload.ui")
telaDowload.btnMP3.clicked.connect(downloadAudio)
telaDowload.btnMP4.clicked.connect(playlistVideo)
telaDowload.btn_close.clicked.connect(sair)

telaDowload.show()
app.exec()

