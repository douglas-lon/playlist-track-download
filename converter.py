from os import system, getcwd, scandir, listdir

def convert_to_ogg():
    dirs = []
    a = scandir(getcwd())
    for entry in a:
        if entry.is_dir() and entry.name != '__pycache__':
            dirs.append(entry.name)
    a.close()
    if dirs:
        dirs.sort()

        for d in dirs:
            print(f'Dir: {d}')
            files = listdir(d)
            if '.mp4' in ', '.join(listdir(d)):
                for f in files:
                    if '.mp4' in f:
                        in_f = f'./{d}/{f}'
                        out_f = f'./{d}/{f.replace(".mp4", ".ogg")}'
                        can_remove = system(f'ffmpeg -i "{in_f}" -c:v libtheora -c:a libvorbis -q:a 4 "{out_f}"')
                        if can_remove == 0:
                            system(f'rm -rf "{in_f}" ')
                    if '.mp4' not in ', '.join(files):
                        break
            else:
                print('Tudo convertido')
    else:
        print('Não existe nenhum diretorio')
