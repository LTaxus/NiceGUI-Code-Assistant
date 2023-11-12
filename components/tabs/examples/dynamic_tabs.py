from nicegui import ui

dict_of_tabs = {
    "Tab1": "Content of Tab1",
    "Tab2": "Content of Tab2",
}

# initialize tab_counter with the length of the dict_of_tabs
tab_counter = len(dict_of_tabs)

def add_tab():
    global tab_counter
    # use the tab_counter to create a new tab name
    new_tab_name = f'Tab{tab_counter + 1}'
    tab_counter += 1
    dict_of_tabs[new_tab_name] = f'Content of {new_tab_name}'
    tabs.refresh()

def delete_tab(title):
    if title in dict_of_tabs:
        del dict_of_tabs[title]
        tabs.refresh()

@ui.refreshable
def tabs():
    with ui.tabs().classes('w-full') as tabs:
        for title in dict_of_tabs:
            with ui.tab(name=title, label=''):
                with ui.row().classes('items-center justify-between'):
                    ui.label(title).classes('text-lg')
                    ui.button(icon='close', on_click=lambda t=title: delete_tab(t)).classes('m-0 p-0 text-black dark:text-white text-xs').props('flat')

        with ui.tab(name="+", label='').classes('p-0 m-0'):
            ui.button(icon='add', on_click=add_tab).props('outline').classes('h-full w-full m-0 text-black dark:text-white')

    with ui.tab_panels(tabs):
        for title in dict_of_tabs:
            with ui.tab_panel(title):
                ui.label(dict_of_tabs[title])
        with ui.tab_panel("+"):
            pass

tabs()

ui.run()
