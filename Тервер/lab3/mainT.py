import PySimpleGUI as sg

def create(table, headings):

    table_layout = [
        [sg.Table(values=table, headings=headings,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Reservations Table',
                    font = 18,
                    auto_size_columns = False,
                    def_col_width = 8
                    )]
    ]

    contact_information_window = sg.Window("Info", 
    table_layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    contact_information_window.close()