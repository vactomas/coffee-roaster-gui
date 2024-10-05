from nicegui import ui
from lib.data_plot import plot_profile_data
from lib.database_handling import fetch_profile_data


def main_gui(profile_data):

    with ui.pyplot() as plot:
        plot_profile_data(profile_data, plot)

    ui.run()
