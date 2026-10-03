import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter
L1 = 1 # Länge Oberarm in Metern
L2 = 0.7 # Länge Unterarm in Metern


# Vorwärtskinematik
def forward_kinematics(theta1, theta2):
    '''Berechnung der Ellenbogen-/Handposition aus den Gelenkwinkeln in radiant'''
    elbow = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1)])
    hand = elbow + np.array([L2 * np.cos(theta2 + theta1), L2 * np.sin(theta2 + theta1)]) 
    # theta 2 ist relativ zum ersten glied, daher muss man hier addieren 
    return elbow, hand


# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2) # von -2 bis 2, da der Arm maximal 1.7 Meter lang sein 
ax.set_ylim(-2, 2) # von -2 bis 2, da der Arm maximal 1.7 Meter lang sein 
ax.set_aspect("equal")
ax.grid(True)
line, = ax.plot([], [], "o-", lw=4) # wird später mit update gefüllt

def update(frame):
    theta1 = frame * 0.1 # Schulter dreht sich um 360°
    theta2 = np.sin(frame * 0.11) # Ellenbogen bewegt sich von ca -57° bis 57° (-1 bis 1 in radiant)
    elbow, hand = forward_kinematics(theta1, theta2)
    xs = [0, elbow[0], hand[0]]
    ys = [0, elbow[1], hand[1]]
    line.set_data(xs, ys)
    return line,


anim = FuncAnimation(fig, update, frames=300, interval=30)
plt.show()