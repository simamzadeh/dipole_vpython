from vpython import *
import numpy as np

# Assign constants
charge = 1
distance = 1
k = 8.99 * 10 ** 9

# Making the particles
positive_part = sphere(pos=vector(0, 0, 0), q=1, radius=0.2, color=color.cyan)

negative_part = sphere(pos=vector(1, 0, 0), q=-1, radius=0.2, color=color.yellow)

# # Step 10 - Move y position of dipole particles
# positive_part.pos.y = 2
# negative_part.pos.y = 2

# Steps 3-6
# test_particle = sphere(pos=vector(3,4,0), radius=0.1)
#
# # Calculate distance
# r_pos = test_particle.pos - positive_part.pos
# r_neg = test_particle.pos - negative_part.pos
#
# # Calculate electric field
# elec_field_pos = k * positive_part.q * (r_pos / (mag(r_pos)**3) )
# elec_field_neg = k * negative_part.q * (r_neg / (mag(r_neg)**3) )
#
# total_elec_field = elec_field_pos + elec_field_neg
#
# # Make arrow
# test_arrow = arrow(pos=vector(3,4,0), axis= (1*10**-8)*total_elec_field)


# Define function to plot test particles

def plot_test_particle(test_position):
    sphere(pos=test_position, radius=0.1, color=color.red)

    r_pos = test_position - positive_part.pos
    r_neg = test_position - negative_part.pos

    elec_field_pos = k * positive_part.q * (r_pos / (mag(r_pos) ** 3))
    elec_field_neg = k * negative_part.q * (r_neg / (mag(r_neg) ** 3))

    total_elec_field = elec_field_pos + elec_field_neg

    arrow(pos=test_position, axis=(1 * 10 ** -8) * total_elec_field)


plot_test_particle(vector(3, 4, 0))

# Plot 16 arrows in the xy plane

count = 1
radius = 5
theta = radians(360 / 16)

while count < 16:
    count += 1

    # Plotting test charges in xy plane
    position_xy = radius * vector(np.cos(theta), np.sin(theta), 0)
    position_xy.x = radius * np.cos(theta*count)
    position_xy.y = radius * np.sin(theta*count)

    # Plotting test charges in xz plane
    position_xz = radius * vector(np.cos(theta), 0, np.sin(theta))
    position_xz.x = radius * np.cos(theta*count)
    position_xz.z = radius * np.sin(theta*count)

    plot_test_particle(position_xy)
    plot_test_particle(position_xz)
