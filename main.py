### Coffea Roaster App ###

# imports
import time

from lib.database_handling import db_init, fetch_profile_data
from lib.data_plot import plot_profile_data
from lib.ui_main import main_gui

# from nicegui import ui


def main():

    set_timezone = "Europe/Prague"

    conn, cursor = db_init(set_timezone)

    profile_data = fetch_profile_data(cursor, 1)

    main_gui(profile_data)

    # cursor.execute("SELECT * FROM roast_profiles")
    # print(profile_data)

    # plot_profile_data(profile_data)


if __name__ in {"__main__", "__mp_main__"}:
    main()
