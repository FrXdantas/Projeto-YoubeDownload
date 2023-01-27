#biblioteca que trabalha com youtube
from pytube import YouTube 

def Download (link):
    youtubeObjeto = YouTube(link)
    youtubeObjeto = youtubeObjeto.streams.get_highest_resolution()
    youtubeObjeto = youtubeObjeto.
    
    try:
        youtubeObjeto.download()
    except:
        print('Erro ao baixar video')
    print('Download do Video do Youtube Completo')
        
   