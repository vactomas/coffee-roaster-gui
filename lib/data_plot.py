import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib.ticker import FuncFormatter


# Custom formatter for the x-axis
def seconds_to_mmss(x, pos):
    minutes = int(x // 60)
    seconds = int(x % 60)
    return f"{minutes:02d}:{seconds:02d}"


# Data processing
def process_profile_data(
    target,
    time,
):

    # Fit a smooth curve to the data
    spline = UnivariateSpline(time, target, s=0.5)

    # Generate a smooth curve
    time = np.linspace(0, max(time), 1000)
    target = spline(time)

    return time, target


def plot_profile_data(
    profile_data,
):

    ## Extract target_time and target_temperature

    # Extract target_time and target_temperature
    target_time = [row[0] for row in profile_data]
    target_temperature = [row[1] for row in profile_data]
    target_RPM = [row[2] for row in profile_data]
    target_power = [row[3] for row in profile_data]
    target_fan = [row[4] for row in profile_data]

    #
    ## Set up the figure
    #

    # Create a new figure
    plt.figure(figsize=(20, 8))

    # Create subplot 1
    plt.subplot(2, 1, 1)

    # Add labels and title
    plt.ylabel("Temperature (°C)")
    plt.title("Roast Profile Temperature Curve")

    # Set min and max values for axes
    plt.xlim(0, max(target_time) + 60)
    plt.ylim(0, 375)

    # Set custom ticks for x and y axes
    plt.xticks(np.arange(0, max(target_time) + 60, step=15))
    plt.yticks(np.arange(0, 375, step=25))

    # Format x-axis ticks as mm:ss
    formatter = FuncFormatter(seconds_to_mmss)
    plt.gca().xaxis.set_major_formatter(formatter)

    # Add grid
    plt.grid(True)

    #
    ## Begin data processing
    #

    target_time_smooth, target_temperature_smooth = process_profile_data(
        target_temperature,
        target_time,
    )

    target_time_smooth, target_fan_smooth = process_profile_data(
        target_fan,
        target_time,
    )

    target_time_smooth, target_RPM_smooth = process_profile_data(
        target_RPM,
        target_time,
    )

    #
    ## Begin plotting
    #

    # Plot the preset temperature points
    plt.scatter(
        target_time,
        target_temperature,
        color="red",
        label="Data Points",
    )

    # Plot the fitted curve
    plt.plot(
        target_time_smooth,
        target_temperature_smooth,
        label="Predetermined Roast Profile",
        color="blue",
    )

    # Plot the preset fan and RPM values
    plt.subplot(2, 1, 2)

    # Add labels and title
    plt.ylabel("Fan Speed [%] / RPM")

    # Set min and max values for axes
    plt.xlim(0, max(target_time) + 60)
    plt.ylim(0, 100)

    # Set custom ticks for x and y axes
    plt.xticks(np.arange(0, max(target_time) + 60, step=15))
    plt.yticks(np.arange(0, 100, step=25))

    # Format x-axis ticks as mm:ss
    formatter = FuncFormatter(seconds_to_mmss)
    plt.gca().xaxis.set_major_formatter(formatter)

    # Add grid
    plt.grid(True)

    # Plot the preset fan and RPM curves
    plt.plot(
        target_time_smooth,
        target_fan_smooth,
        label="Fan Speed",
        color="green",
    )
    plt.plot(
        target_time_smooth,
        target_RPM_smooth,
        label="RPM",
        color="orange",
    )

    # Add a legend
    plt.legend()

    # Save the figure
    plt.savefig("roast_profile.png")
