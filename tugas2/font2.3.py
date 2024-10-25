import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.theme_text_color("#FF0000")

window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA", font=("Arial", 24), text_color="#FF0000")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Arial", 18, "italic", "bold", "underline"))],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FF0000")]],
                   size=(430, 200),
                   font=("Arial", 18))

window.read()
window.close()