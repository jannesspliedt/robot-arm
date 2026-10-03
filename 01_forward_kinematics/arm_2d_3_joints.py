import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter
L1 = 1 # Länge Oberarm in Metern
L2 = 0.7 # Länge Unterarm in Metern
L3 = 0.3 # Länge der Hand in Metern


# Vorwärtskinematik
def forward_kinematics(theta1, theta2, theta3):
    '''berechnet die Ellenbogen-/Handposition/Endeffektorposition aus den Gelenkwinkeln in radiant'''
    elbow = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1)])
    # theta2 ist relativ zum Oberarm, daher theta1 + theta2
    wrist = elbow + np.array([L2 * np.cos(theta2 + theta1), L2 * np.sin(theta2 + theta1)]) 
    # theta3 ist relativ zum Unterarm, daher Summe aller Winkel
    end_effector = wrist + np.array([L3 * np.cos(theta1 + theta2 + theta3), L3 * np.sin(theta1 + theta2 + theta3)])
    return elbow, wrist, end_effector


# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5) # Reichweite max. L1 + L2 + L3 = 2 m, plus Rand
ax.set_ylim(-2.5, 2.5) 
ax.set_aspect("equal")
ax.grid(True)
line, = ax.plot([], [], "o-", lw=4) # Leere Linie, wird in update() pro Bild gefüllt

def update(frame): # wird von FuncAnimation einmal pro Bild aufgerufen
    theta1 = frame * 0.1 # Schulter dreht regelmäßig im Kreis
    theta2 = np.sin(frame * 0.11) # Ellbogen pendelt zwischen -1 und 1 rad (ca. ±57°)
    theta3 = np.cos(frame * 0.1)  # Handgelenk pendelt zwischen -1 und 1 rad (ca. ±57°) aber anderer Rhythmus zum Ellenbogen
    elbow, wrist, end_effector = forward_kinematics(theta1, theta2, theta3)
    xs = [0, elbow[0], wrist[0], end_effector[0]]
    ys = [0, elbow[1], wrist[1], end_effector[1]]
    line.set_data(xs, ys)
    return line,

anim = FuncAnimation(fig, update, frames=300, interval=30) # produziert 300 Bilder, 30 Millisekunden pro Bild (ca. 33 FPS)
plt.show()