import PySimpleGUI as sg

sg.theme('DarkBlue3')
sg.theme_text_color("#FF0000")

window = sg.Window("Contoh Button",
    layout=[[sg.Text("Contoh Button", text_color="#FF0000")],
            [sg.Button("Button Simpan")],
            [sg.Button("Button Keluar")]],
    size=(400, 200),
    font=("Arial", 20))

kejadian, nilai = window.read()
print(kejadian, "=", nilai)

# Menutup window
window.close()