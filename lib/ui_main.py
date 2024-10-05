from nicegui import ui
from lib.data_plot import plot_profile_data


def main_gui(profile_data):

    dark = ui.dark_mode()

    with ui.row().classes('w-full items-center'):
        with ui.button(icon='menu'):
            with ui.menu() as menu:
                ui.menu_item('Dark', on_click=dark.enable)
                ui.menu_item('Light', on_click=dark.disable)

    with ui.pyplot(close=False, figsize=(20, 8)):
        plot_profile_data(profile_data)

    ui.run()
