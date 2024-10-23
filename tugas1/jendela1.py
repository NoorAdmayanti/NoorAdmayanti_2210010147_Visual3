import PySimpleGUI as sg
sg.theme("DarkBlue6")
sg.theme_text_color("#ac4d99")
window = sg.Window(title="Profile",
    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
            font=("Arial",25,"italic","bold","underline"))],
            [sg.Text("NPM        : 2210010147 ")],
            [sg.Text("Nama       : Noor Admayanti ")],
            [sg.Text("Kelas      : 5B NonRegular Banjarmasin ")],
            ],
    size=(510,200),
    font=("Times", 18))

window()
window.close()
