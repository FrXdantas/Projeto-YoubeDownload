#biblioteca que trabalha com youtube
from pytube import YouTube 
#biblioteca que trabalha com caminhos e arquivos
from pathlib import Path

#função para baixar o video na pasta Downloads
def Download (link):
    youtubeObjeto = YouTube(link)
    youtubeObjeto = youtubeObjeto.streams.get_highest_resolution()
    youtubeObjeto = youtubeObjeto
    caminho_video = (Path.home() / 'Downloads')
    
    
    try:
        youtubeObjeto.download(caminho_video)
    except:
        print('Erro ao baixar video')
    print('Download do Video do Youtube Completo')
    print(f'Salvo em : {caminho_video}')
#Interação com usuário
link = input ('Cole aqui o Link do Vídeo: ')
#execução da função
Download(link)

#sugestão de melhoria { implantar em um ambiente com janelas / pegar lista de videos em txt } 