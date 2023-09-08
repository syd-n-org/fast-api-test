import PySimpleGUIWeb as sg
import requests
import json
import pandas as pd

def get_requests(func,payload:dict|None={}):
        if func == "all-records":
            headers = {'accept': 'application/json',}
            try:
                response = requests.get('http://127.0.0.1:5511/api/v1/all-pets/all-records', headers=headers,timeout=2)
                response.raise_for_status()
                # return pd.DataFrame(response.json()["content"]).values.tolist()
            except requests.exceptions.ConnectionError as connerror:
                print("Connection Error")
                return "Connection Error"
                
        elif func == "add-records":
            try:
                headers = {'accept': 'application/json','Content-Type': 'application/json'}
                response = requests.post('http://127.0.0.1:5511/api/v1/all-pets/add-records', headers=headers, json=payload)
                # return response.json()
            except requests.exceptions.ConnectionError as connerror:
                print("Connection Error")
                return "Connection Error"
        return response.json()

# print(get_requests("add-records",payload={"pet_id": 0,"name": "string","animal": "string","breed": "string"}))

def make_window():
    sg.theme("black")
    headings =  ["pet_id","name","animal","breed"]
    data = [["Nothing"],["To"],["See"],["Yet"]],
    # menu_def = [['&Application', ['E&xit']],['&Help', ['&About']] ]
    display_records_layout = [
        [   sg.Text("Get All Records", size=(45, 1), justification="center")],
        [   sg.Table(values=data, headings=headings, max_col_width=25,
                background_color='black',
                auto_size_columns=True,
                display_row_numbers=True,
                justification='right',
                num_rows=15,
                col_widths=[20, 15],
                expand_x=True, expand_y=True,
                alternating_row_color='black',
                key='-TABLE-',
                row_height=25)],
        [   sg.Button("Get Records", bind_return_key=True, button_color="Green"),
            sg.Button("Close", button_color="Red"),
                ],
        [   sg.Text("", size=(45, 1), key="-ALLMESSAGE-")]
    ]
    insert_records_layout = [
        [   sg.Text("Insert One Records", size=(45, 1), justification="center")],
        [   sg.Text("pet_id",(45,1)),sg.Input("0")],
        [   sg.Text("name",(45,1)),sg.Input("")],
        [   sg.Text("animal",(45,1)),sg.Input("")],
        [   sg.Text("breed",(45,1)),sg.Input("")],
        [   #sg.Text("Result", size=(38, 1)),
            sg.Text("", size=(38, 1),key="-INSERTED-")],
        [   sg.Button("Insert", bind_return_key=True, button_color="Green"),
            sg.Button("Close", button_color="Red"),
                ],
        [   sg.Text("", size=(45, 1), key="-INSMESSAGE-")]
    ]
    layout = [
        # [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
        [
            sg.Text(
                "Pet Shelter",
                size=(38, 1),
                justification="center",
                font=("Helvetica", 16),
                relief=sg.RELIEF_RIDGE,
                k="-TEXT HEADING-",
                enable_events=True,
            )
        ]
    ]
    layout += [[
        sg.TabGroup([[
            sg.Tab("All Records", display_records_layout),
            sg.Tab("Insert Records", insert_records_layout)
            ]])
    ]]
    window = sg.Window('Shelter', 
                    layout, right_click_menu_tearoff=True, 
                    grab_anywhere=True,
                    resizable=True, margins=(0,0),
                    use_custom_titlebar=True,
                    finalize=True, keep_on_top=True)
    return window

def main():
    window = make_window()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":
            break
        if event == "Get Records":
            all_data = get_requests("all-records")
            if all_data == "Connection Error":
                window["-ALLMESSAGE-"].update("Could not connect to DB")
            else:
                window["-TABLE-"].update(values=pd.DataFrame(all_data["content"]).values.tolist())
        if event == "Insert":
            payload = { "pet_id":int(values[0]),"name":values[1],"animal":values[2],"breed":values[3]}
            insert_data =  get_requests("add-records",payload=payload)
            if insert_data == "ConnectionError":
                window["-INSMESSAGE-"].update("Could not connect to DB")
            else:
                window["-INSMESSAGE-"].update(insert_data["message"])

                

        # if event = "" 
    window.close()

if __name__ == "__main__":
    main()