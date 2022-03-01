from pytube import Playlist
from hashlib import sha1
from os import getcwd, listdir, mkdir
import json
from time import sleep

def download_playlist(path):

    p = Playlist(path)

    tracker = {
        'lastFile': ''
    }

    if p.title not in listdir(getcwd()):
        mkdir(f'{getcwd()}/{p.title}')
        with open(f'{getcwd()}/{p.title}/lastFile.json', 'w') as file:
            json.dump(tracker, file)

    with open(f'{getcwd()}/{p.title}/lastFile.json', 'r') as file:
        tracker = json.load(file)
    
    hash_first_music = sha1(p.videos[0].title.encode()).hexdigest()

    if tracker['lastFile'] != hash_first_music:

        test_list = p.videos
        print('Iniciando Download...')
        video_i = 0
        indice = 0

        while indice < len(test_list):
            try:
                video_i = indice
                video_title = sha1(test_list[indice].title.encode()).hexdigest()
                
                if video_title != tracker['lastFile']:
                    print(f'Baixando {test_list[indice].title}...')
                    a = test_list[indice].streams.filter(only_audio=True).first()
                    extension = a.mime_type.split('/')
                    a.download(output_path=f'{getcwd()}/{p.title}', filename=f'{video_title}.{extension[1]}')
                    print('Concluido!')
                    indice += 1
                else:
                    break
            except Exception as ex:
                print(f'Erro: {ex.__class__.__name__}')
                print('Tentando Denovo...')
                indice = video_i
                sleep(1)

        tracker['lastFile'] = hash_first_music   
        with open(f'{getcwd()}/{p.title}/lastFile.json', 'w') as file:
            json.dump(tracker, file)
        
        print('Fim do Download!')
    else:
        print('Tudo Atualizado')

    