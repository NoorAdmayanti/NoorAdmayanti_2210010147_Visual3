import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.theme_text_color("#FF0000")

window = sg.Window(title="Profile",
                   layout=[[sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="center")],
                           [sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="left")],
                           [sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="right")],
                           [sg.Text("TEKNOLOGI INFORMASI " + ' ' * 2, size=(25, 2), justification="center")],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FF0000")]],
                   size=(400, 250),
                   font=("Arial", 18))

window.read()
window.close()