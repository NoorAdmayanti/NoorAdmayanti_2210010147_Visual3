import PySimpleGUI as sg
sg.theme('DarkBlue3')
sg.theme_text_color("#FF0000")

susunan = [
    [sg.Text("UNISKA MAAB", font=("Arial", 24), text_color="#FF0000")],
    [sg.Text("BANJARMASIN", font=("Arial", 18), text_color="#FF0000")]
]

window = sg.Window(
    title="New Icon",
    layout=susunan,
    element_justification="center",
    icon="favicon.ico",  # Pastikan "favicon.ico" ada di direktori yang sama
    size=(430, 200)
)

window.read()
window.close()