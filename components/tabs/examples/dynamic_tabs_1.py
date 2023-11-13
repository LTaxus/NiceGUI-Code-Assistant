from nicegui import ui

dict_of_tabs = {
    "Tab1": "Content of Tab1",
    "Tab2": "Content of Tab2",
}

def get_next_tab_number():
    numbers = [int(name[3:]) for name in dict_of_tabs if name.startswith('Tab') and name[3:].isdigit()]
    return max(numbers) + 1 if numbers else 1

def add_tab():
    new_tab_number = get_next_tab_number()
    new_tab_name = f'Tab{new_tab_number}'
    dict_of_tabs[new_tab_name] = f'Content of {new_tab_name}'
    tabs.refresh()

def delete_tab(title):
    if title in dict_of_tabs:
        del dict_of_tabs[title]
        tabs.refresh()
    else:
        ui.notify(f"Tab '{title}' does not exist")

@ui.refreshable
def tabs():
    with ui.tabs().classes('w-full') as tabs:
        for title in list(dict_of_tabs.keys()):  # Use list to avoid 'RuntimeError: dictionary changed size during iteration'
            with ui.tab(name=title, label=''):
                with ui.row().classes('items-center justify-between p-0 m-0'):
                    ui.label(text=title).classes('text-lg')
                    ui.button(icon='edit').classes('m-0 p-0 text-black dark:text-white text-xs').props('flat').tooltip('Edit tab')
                    ui.button(icon='close', on_click=lambda t=title: delete_tab(t)).classes('m-0 p-0 text-black dark:text-white text-xs').props('flat').tooltip('Delete tab')

        with ui.tab(name="+", label='').classes('p-0 m-0').tooltip('Add new tab'):
            ui.button(icon='add', on_click=add_tab).props('outline').classes('h-full w-full m-0 text-black dark:text-white')

    with ui.tab_panels(tabs):
        for title in dict_of_tabs:
            with ui.tab_panel(title):
                ui.label(dict_of_tabs[title])
        with ui.tab_panel("+"):
            pass

tabs()

ui.run()
