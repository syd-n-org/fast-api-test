# # import PySimpleGUI as sg
# # sg.theme("DarkPurple2")
# # layout = [[sg.Text("Text")],
# #           [sg.Text("Text2"),sg.InputText()],
# #           [sg.Text("OUTPUT"),sg.Text(" ",key="op")],
# #           [sg.Button("HI",bind_return_key=True),sg.Button("BYE")]]


# # window = sg.Window("Title",layout,titlebar_background_color="Blue")

# # while True:
# #     event,values = window.read()
# #     if event == sg.WIN_CLOSED or event == "BYE":
# #         break
# #     window["op"].update(values[0])
# # window.close()

# ####################################################################33

# # import PySimpleGUI as sg

# # """
# #     Demo - Element List

# #     All elements shown in 1 window as simply as possible.

# #     Copyright 2022 PySimpleGUI
# # """


# # use_custom_titlebar = True if sg.running_trinket() else False

# # def make_window(theme=None):

# #     NAME_SIZE = 23


# #     def name(name):
# #         dots = NAME_SIZE-len(name)-2
# #         return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

# #     sg.theme(theme)

# #     # NOTE that we're using our own LOCAL Menu element
# #     if use_custom_titlebar:
# #         Menu = sg.MenubarCustom
# #     else:
# #         Menu = sg.Menu

# #     treedata = sg.TreeData()

# #     treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
# #     treedata.Insert("", '_B_', 'B', [])
# #     treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

# #     layout_l = [
# #                 [name('Text'), sg.Text('Text')],
# #                 [name('Input'), sg.Input(s=15)],
# #                 [name('Multiline'), sg.Multiline(s=(15,2))],
# #                 [name('Output'), sg.Output(s=(15,2))],
# #                 [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
# #                 [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
# #                 [name('Checkbox'), sg.Checkbox('Checkbox')],
# #                 [name('Radio'), sg.Radio('Radio', 1)],
# #                 [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
# #                 [name('Button'), sg.Button('Button')],
# #                 [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
# #                 [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
# #                 [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
# #                 [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
# #                 [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

# #     layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,40))],
# #                 [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
# #                 [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
# #                 [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
# #                 [name('Horizontal Separator'), sg.HSep()],
# #                 [name('Vertical Separator'), sg.VSep()],
# #                 [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
# #                 [name('Column'), sg.Column([[sg.T(s=15)]])],
# #                 [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
# #                 [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
# #                 [name('Push'), sg.Push(), sg.T('Pushed over')],
# #                 [name('VPush'), sg.VPush()],
# #                 [name('Sizer'), sg.Sizer(1,1)],
# #                 [name('StatusBar'), sg.StatusBar('StatusBar')],
# #                 [name('Sizegrip'), sg.Sizegrip()]  ]

# #     # Note - LOCAL Menu element is used (see about for how that's defined)
# #     layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
# #               [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c', expand_x=True)],
# #               [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-', p=0)],
# #               [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)]]

# #     window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

# #     window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
# #     window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

# #     return window


# # window = make_window()

# # while True:
# #     event, values = window.read()
# #     # sg.Print(event, values)
# #     if event == sg.WIN_CLOSED or event == 'Exit':
# #         break

# #     if values['-COMBO-'] != sg.theme():
# #         sg.theme(values['-COMBO-'])
# #         window.close()
# #         window = make_window()
# #     if event == '-USE CUSTOM TITLEBAR-':
# #         use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
# #         sg.set_options(use_custom_titlebar=use_custom_titlebar)
# #         window.close()
# #         window = make_window()
# #     if event == 'Edit Me':
# #         sg.execute_editor(__file__)
# #     elif event == 'Version':
# #         sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)
# # window.close()

# #!/usr/bin/env python


# """
#     Example of (almost) all Elements, that you can use in PySimpleGUI.
#     Shows you the basics including:
#         Naming convention for keys
#         Menubar format
#         Right click menu format
#         Table format
#         Running an async event loop
#         Theming your application (requires a window restart)
#         Displays the values dictionary entry for each element
#         And more!

#     Copyright 2021, 2022, 2023 PySimpleGUI
# """

# import PySimpleGUI as sg

# def make_window(theme):
#     sg.theme(theme)
#     menu_def = [['&Application', ['E&xit']],
#                 ['&Help', ['&About']] ]
#     right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing','More Nothing','Exit']]
#     graph_right_click_menu_def = [[], ['Erase','Draw Line', 'Draw',['Circle', 'Rectangle', 'Image'], 'Exit']]

#     # Table Data
#     data = [["John", 10], ["Jen", 5]]
#     headings = ["Name", "Score"]

#     input_layout =  [

#                 # [sg.Menu(menu_def, key='-MENU-')],
#                 [sg.Text('Anything that requires user-input is in this tab!')], 
#                 [sg.Input(key='-INPUT-')],
#                 [sg.Slider(orientation='h', key='-SKIDER-'),
#                  sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'),],
#                 [sg.Checkbox('Checkbox', default=True, k='-CB-')],
#                 [sg.Radio('Radio1', "RadioDemo", default=True, size=(10,1), k='-R1-'), sg.Radio('Radio2', "RadioDemo", default=True, size=(10,1), k='-R2-')],
#                 [sg.Combo(values=('Combo 1', 'Combo 2', 'Combo 3'), default_value='Combo 1', readonly=False, k='-COMBO-'),
#                  sg.OptionMenu(values=('Option 1', 'Option 2', 'Option 3'),  k='-OPTION MENU-'),],
#                 [sg.Spin([i for i in range(1,11)], initial_value=10, k='-SPIN-'), sg.Text('Spin')],
#                 [sg.Multiline('Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.', size=(45,5), expand_x=True, expand_y=True, k='-MLINE-')],
#                 [sg.Button('Button'), sg.Button('Popup'), sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-')]]

#     asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
#                [sg.Image(data=sg.DEFAULT_BASE64_ICON,  k='-IMAGE-')],
#                [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'), sg.Button('Test Progress bar')]]

#     logging_layout = [[sg.Text("Anything printed will display here!")],
#                       [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
#                                     reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
#                       # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
#                       ]
    
#     graphing_layout = [[sg.Text("Anything you would use to graph will display here!")],
#                       [sg.Graph((200,200), (0,0),(200,200),background_color="black", key='-GRAPH-', enable_events=True,
#                                 right_click_menu=graph_right_click_menu_def)],
#                       [sg.T('Click anywhere on graph to draw a circle')],
#                       [sg.Table(values=data, headings=headings, max_col_width=25,
#                                 background_color='black',
#                                 auto_size_columns=True,
#                                 display_row_numbers=True,
#                                 justification='right',
#                                 num_rows=2,
#                                 alternating_row_color='black',
#                                 key='-TABLE-',
#                                 row_height=25)]]

#     popup_layout = [[sg.Text("Popup Testing")],
#                     [sg.Button("Open Folder")],
#                     [sg.Button("Open File")]]
    
#     theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
#                     [sg.Listbox(values = sg.theme_list(), 
#                       size =(20, 12), 
#                       key ='-THEME LISTBOX-',
#                       enable_events = True)],
#                       [sg.Button("Set Theme")]]
    
#     layout = [ [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
#                 [sg.Text('Demo Of (Almost) All Elements', size=(38, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
#     layout +=[[sg.TabGroup([[  sg.Tab('Input Elements', input_layout),
#                                sg.Tab('Asthetic Elements', asthetic_layout),
#                                sg.Tab('Graphing', graphing_layout),
#                                sg.Tab('Popups', popup_layout),
#                                sg.Tab('Theming', theme_layout),
#                                sg.Tab('Output', logging_layout)
#                                ]], key='-TAB GROUP-', expand_x=True, expand_y=True),
#                ]]
#     layout[-1].append(sg.Sizegrip())
#     window = sg.Window('All Elements Demo', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
#     window.set_min_size(window.size)
#     return window

# def main():
#     window = make_window(sg.theme())

#     # This is an Event Loop 
#     while True:
#         event, values = window.read(timeout=100)
#         # keep an animation running so show things are happening
#         if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
#             print('============ Event = ', event, ' ==============')
#             print('-------- Values Dictionary (key=value) --------')
#             for key in values:
#                 print(key, ' = ',values[key])
#         if event in (None, 'Exit'):
#             print("[LOG] Clicked Exit!")
#             break

#         window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
#         if event == 'About':
#             print("[LOG] Clicked About!")
#             sg.popup('PySimpleGUI Demo All Elements',
#                      'Right click anywhere to see right click menu',
#                      'Visit each of the tabs to see available elements',
#                      'Output of event and values can be see in Output tab',
#                      'The event and values dictionary is printed after every event', keep_on_top=True)
#         elif event == 'Popup':
#             print("[LOG] Clicked Popup Button!")
#             sg.popup("You pressed a button!", keep_on_top=True)
#             print("[LOG] Dismissing Popup!")
#         elif event == 'Test Progress bar':
#             print("[LOG] Clicked Test Progress Bar!")
#             progress_bar = window['-PROGRESS BAR-']
#             for i in range(100):
#                 print("[LOG] Updating progress bar by 1 step ("+str(i)+")")
#                 progress_bar.update(current_count=i + 1)
#             print("[LOG] Progress bar complete!")
#         elif event == "-GRAPH-":
#             graph = window['-GRAPH-']       # type: sg.Graph
#             graph.draw_circle(values['-GRAPH-'], fill_color='yellow', radius=20)
#             print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
#         elif event == "Open Folder":
#             print("[LOG] Clicked Open Folder!")
#             folder_or_file = sg.popup_get_folder('Choose your folder', keep_on_top=True)
#             sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
#             print("[LOG] User chose folder: " + str(folder_or_file))
#         elif event == "Open File":
#             print("[LOG] Clicked Open File!")
#             folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
#             sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
#             print("[LOG] User chose file: " + str(folder_or_file))
#         elif event == "Set Theme":
#             print("[LOG] Clicked Set Theme!")
#             theme_chosen = values['-THEME LISTBOX-'][0]
#             print("[LOG] User Chose Theme: " + str(theme_chosen))
#             window.close()
#             window = make_window(theme_chosen)
#         elif event == 'Edit Me':
#             sg.execute_editor(__file__)
#         elif event == 'Versions':
#             sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)

#     window.close()
#     exit(0)

# if __name__ == '__main__':
#     sg.theme('black')
#     sg.theme('dark red')
#     sg.theme('dark green 7')
#     # sg.theme('DefaultNoMoreNagging')
#     main()


url = "http://127.0.0.1:5511/api/v1/all-pets/all-records"
  
# code
import requests
try:
    r = requests.get(url, timeout=1, verify=True)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])
except requests.exceptions.ReadTimeout as errrt:
    print("Time out")
except requests.exceptions.ConnectionError as conerr:
    print("Connection error")
except requests.exceptions.RequestException as errex:
    print("Exception request")