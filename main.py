import os, shutil
# replace my path with yours.
download_path = 'c:/users/harsh/downloads'
image_path = 'c:/users/harsh/downloads/images'
video_path = 'c:/users/harsh/downloads/videos'
exe_path = 'c:/users/harsh/downloads/exe'
document_path = 'c:/users/harsh/downloads/document'
zip_path = 'c:/users/harsh/downloads/zip'
music_path = 'c:/users/harsh/downloads/music'
# first we will create filter folders like img txt etc.

if not os.path.exists(image_path):
    os.mkdir(image_path)

if not os.path.exists(video_path):
    os.mkdir(video_path)

if not os.path.exists(exe_path):
    os.mkdir(exe_path)

if not os.path.exists(document_path):
    os.mkdir(document_path)

if not os.path.exists(zip_path):
    os.mkdir(zip_path)

if not os.path.exists(music_path):
    os.mkdir(music_path)

# now here we will start a infinite loop that will check extension of every file in downloads and move them
# replace my path with yours
# add as many extension you want
while True:
    for file in os.listdir(download_path):
        if file.endswith('.jpg') or file.endswith('.bmp') or file.endswith('.webp') or file.endswith(
                '.png') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.JPG') or file.endswith(
            '.JPG'):
            shutil.move(download_path+'/'+ file, image_path)

        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mov'):
            shutil.move(download_path+'/'+ file, video_path)

        if file.endswith('.txt') or file.endswith('.docx') or file.endswith('.pdf') or file.endswith(
                '.ppt') or file.endswith('.pptx') or file.endswith('.xls') or file.endswith('.xlsx'):
            shutil.move(download_path+'/'+ file, document_path)

        if file.endswith('.exe') or file.endswith('.msi'):
            shutil.move(download_path+'/'+ file, exe_path)

        if file.endswith('.zip') or file.endswith('.rar') or file.endswith('.7z'):
            shutil.move(download_path+'/'+ file, zip_path)

        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.m4a') or file.endswith('.aac'):
            shutil.move(download_path+'/'+ file, music_path)
