import numpy as np
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'


def evolve(u, u_previous, a, dt, dx2, dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    # TODO: determine the new temperature field based on previous values
    # and the numerical Laplacian according the explicit time evolution method
    u[1:-1,1:-1] = u_previous[1:-1,1:-1] + \
        a * dt * ( u_previous[2:,1:-1] - 2 * u_previous[1:-1,1:-1] + u_previous[:-2,1:-1] / dx2 + \
        u_previous[1:-1,2:] - 2 * u_previous[1:-1,1:-1] + u_previous[1:-1,:-2] / dy2)
    u_previous[:] = u[:]

def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""
    # TODO: Implement the main iteration loop and write the figure 
    # (to a new) file after each 'image_interval' iteration
    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

def init_fields(filename):
# TODO: Read the initial temperature field from file
# Create also a copy of the field for the previous time step
    field  = np.loadtxt(filename)
    field0 = field.copy()
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))
