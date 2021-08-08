import PySimpleGUI as sg

layout = [[sg.Text("You are in a forest, where do you want to go?", text_color="#343434", background_color="#f2f2f2", key='-head-')],
        # [sg.Input(key='-INPUT-')],
        [sg.Text(size=(40, 1), background_color="#f2f2f2", key='-OUTPUT-')],
        [sg.Button('Left', button_color=('black', 'orange')), sg.Button('Right', button_color=('black', 'red')), sg.Button('Quit', button_color=('black', 'yellow'))]]

window = sg.Window('Adventure Game', auto_size_text=True,
            background_color="#f2f2f2", default_element_size=(40, 1)).Layout(layout)
#userInput = window['-INPUT-']
header = window['-head-']

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # window['-OUTPUT-'].update("You arrived at your destination")
    if event == 'Left':
        header.update(
            value="You are now at a castle, where do you want to go?")
    if event == 'Right':
        header.update(value="You are now at a house, where do you want to go?")
        # userInput.update(value="")

window.close()
