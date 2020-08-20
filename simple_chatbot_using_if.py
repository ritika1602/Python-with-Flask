import os

while True:
    query = input('Tell me what do you want? ')
    list_not = ['dont', "don't", 'no', 'not']
    for i in list_not:
        if i in query:
            print('okay, sure')
    if 'run' in query or 'open' in query:
        if 'notepad' in query or 'edit' in query:
            os.system('notepad')
        if 'chrome' in query or 'browser' in query:
            os.system('start chrome')
        if 'media' in query or 'player' in query:
            os.chdir('C:\Program Files\VideoLAN\VLC')
            os.system('vlc')
    elif 'exit' in query or 'terminate' in query or 'stop' in query:
        break
    else:
        print('Please try again')