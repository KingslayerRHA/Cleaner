import PySimpleGUI as sg
import subprocess
import sys

def Clean():
    text_elem = window['-text-']
    text_elem.update("Trash found! {}".format(r))

sg.theme('DarkAmber')

layout = [[sg.Text('Cleaner (GNU)\t\t\t\t\t\t', font="30"), sg.Text('(c)K丨|-|Ꮆ丂ㄥ卂ㄚ乇尺', font="Ubuntu")],
           [sg.Text('Click on punkt "Clobal clean" if you want to do full clear')],[sg.Checkbox('Global clean', default=False)],
           [sg.Button('Clean'), sg.Button('Cancel')]]


window = sg.Window('Cleaner (GNU)', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if sg.Checkbox == True:
        print(sys._clear_type_cache())
        subprocess.call('sudo -i')
        subprocess.call('sync; echo 1 > /proc/sys/vm/drop_caches')
        subprocess.call('swapoff -a && swapon -a')
        subprocess.call('sync; echo 3 > /proc/sys/vm/drop_caches')
        break
    print(sys._clear_type_cache())
    layout2 = [[sg.Text('Cleaner (GNU)')],[sg.Text('All info in this dir: /proc/sys/vm/drop_caches')] ,[sg.Text('Done!')], [sg.Button('Exit')]]

    window = sg.Window('Done', layout2)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
