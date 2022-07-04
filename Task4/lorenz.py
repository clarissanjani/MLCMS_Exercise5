import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, sigma, rho, beta):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = sigma * (y - x)
    y_dot = rho * x - y - x * z
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot


def plot_lorenz(sigma, rho, beta, dt, end_Time):
    """
        Plots a 3-dimensional Lorenz System.
        Takes the parameters sigma, rho and beta as well as the time increment dt and the end time end_Time)
        Returns three figures: The simulation results for a run with the initial values 10, 10, 10,
        for a second run with the initial values 10*10^-8, 10, 10,
        and a 2d plot of the difference between the two, plotted over the time.
        It also returns the difference vector for further analysis.
    """

    num_Steps = end_Time / dt
    # setting up the arrays for the results

    xs_1 = np.empty(int(num_Steps) + 1)
    ys_1 = np.empty(int(num_Steps) + 1)
    zs_1 = np.empty(int(num_Steps) + 1)

    # setting up the arrays for time and the difference between the systems

    diff = np.empty(int(num_Steps))
    time_Space = np.linspace(0, end_Time, int(num_Steps))

    # set initial values for both simulations

    xs_1[0], ys_1[0], zs_1[0] = (10.0, 10.0, 10.0)

    for i in range(int(num_Steps)):
        x_dot, y_dot, z_dot = lorenz(xs_1[i], ys_1[i], zs_1[i], sigma, rho, beta)
        xs_1[i + 1] = xs_1[i] + (x_dot * dt)
        ys_1[i + 1] = ys_1[i] + (y_dot * dt)
        zs_1[i + 1] = zs_1[i] + (z_dot * dt)

    # Plot

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(projection='3d')

    ax1.plot(xs_1, ys_1, zs_1, lw="0.5")
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax1.set_zlabel("Z Axis")
    ax1.set_title("Lorenz Attractor derived from x, y, z")
    return xs_1, ys_1, zs_1
