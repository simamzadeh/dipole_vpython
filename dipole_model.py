from vpython import *

# Assign constants
charge = 1
distance = 1

# Making the particles
positive = sphere(pos=vector(0,0,0), q = 1, radius=0.2, color=color.cyan)

negative = sphere(pos=vector(1,0,0), q = -1, radius=0.2, color=color.yellow)

test_position = sphere(pos=vector(3,4,0), radius=0.1)