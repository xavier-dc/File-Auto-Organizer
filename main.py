from os import listdir
from os.path import isfile, join
from shutil import move

print('Enter your windows user name....')
YOUR_USER_NAME = input()
downloads_path = 'C:/Users/' + YOUR_USER_NAME + '/Downloads'

videos_path = f'C:/Users/{YOUR_USER_NAME}/Videos'
images_path = f'C:/Users/{YOUR_USER_NAME}/Images'
docs_path = f'C:/Users/{YOUR_USER_NAME}/Docs'
music_path = f'C:/Users/{YOUR_USER_NAME}/Music'
misc_path = f'C:/Users/{YOUR_USER_NAME}/Misc'

files = [f for f in listdir(downloads_path) if isfile(join(downloads_path, f))]

for file in files:
    if (file.endswith('.mp4') or file.endswith('.mkv') or file.endswith('.avi') or file.endswith('.mov')):
        print(file)
        move(join(downloads_path, file), join(videos_path, file))
    elif (file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.gif')):
        print(file)
        move(join(downloads_path, file), join(images_path, file))
    elif (file.endswith('.pdf') or file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xls') or file.endswith('.xlsx') or file.endswith('.ppt') or file.endswith('.pptx')):
        print(file)
        move(join(downloads_path, file), join(docs_path, file))
    elif (file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.flac') or file.endswith('.aac') or file.endswith('.m4a') or file.endswith('.wma')):
        print(file)
        move(join(downloads_path, file), join(music_path, file))
    else:
        print(file)
        move(join(downloads_path, file), join(misc_path, file))

print("Complete")