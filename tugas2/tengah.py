import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.theme_text_color("#FF0000")

susunan = [
    [sg.Text("UNISKA MAAB", font=("Arial", 24), text_color="#FF0000")],
    [sg.Text("BANJARMASIN", font=("Arial", 18), text_color="#FF0000")]
]

window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   element_justification="center",
                   size=(430, 200),
                   font=("Arial", 18))

window.read()
window.close()