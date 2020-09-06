import os, shutil

# first we will create filter folders like img txt etc.
# replace my path with yours.
if not os.path.exists('c:/users/harsh/downloads/images'):
    os.mkdir('c:/users/harsh/downloads/images')

if not os.path.exists('c:/users/harsh/downloads/videos'):
    os.mkdir('c:/users/harsh/downloads/videos')

if not os.path.exists('c:/users/harsh/downloads/exe'):
    os.mkdir('c:/users/harsh/downloads/exe')

if not os.path.exists('c:/users/harsh/downloads/text'):
    os.mkdir('c:/users/harsh/downloads/text')

if not os.path.exists('c:/users/harsh/downloads/zip'):
    os.mkdir('c:/users/harsh/downloads/zip')

if not os.path.exists('c:/users/harsh/downloads/music'):
    os.mkdir('c:/users/harsh/downloads/music')

# now here we will start a infinite loop that will check extension of every file in downloads and move them
# replace my path with yours
# add as many extension you want
while True:
    for file in os.listdir('c:/users/harsh/downloads'):
        if file.endswith('.jpg') or file.endswith('.bmp') or file.endswith('.dng') or file.endswith(
                '.png') or file.endswith('.jpeg') or file.endswith('.gif'):
            shutil.move('c:/users/harsh/downloads/' + file, 'c:/users/harsh/downloads/images')

        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mov'):
            shutil.move('c:/users/harsh/downloads/' + file, 'c:/users/harsh/downloads/videos')

        if file.endswith('.txt') or file.endswith('.docx') or file.endswith('.pdf'):
            shutil.move('c:/users/harsh/downloads/' + file, 'c:/users/harsh/downloads/text')
