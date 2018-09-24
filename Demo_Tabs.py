import PySimpleGUI as sg

tab1_layout = [[sg.T('This is inside tab 1')]]
tab2_layout = [[sg.T('This is inside tab 2'), sg.In(key='in')]]

tab3_layout = [[sg.T('This is inside tab 3')]]
tab4_layout = [[sg.T('This is inside tab 4')]]

tab5_layout = [[sg.T('This is inside tab 5')]]
tab6_layout = [[sg.T('This is inside tab 6')],
               [sg.T('How about a second row of stuff in tab 6?')]]

layout = [[sg.T('My Window!')],
    [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]]), sg.TabGroup([[sg.Tab('Tab 3', tab3_layout), sg.Tab('Tab 4', tab4_layout)]])],
    [sg.T('Text in the middle of the mess')],
    [sg.TabGroup([[sg.Tab('Tab 5', tab5_layout), sg.Tab('Tab 6', tab6_layout)]])],
          [sg.RButton('Read')],
          ]

window = sg.Window('My window with tabs').Layout(layout)

while True:
    b, v = window.Read()
    print(b,v)
    if b is None:           # always,  always give a way out!
        break