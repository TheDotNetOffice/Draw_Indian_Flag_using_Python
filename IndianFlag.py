import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_indian_flag():
    fig, ax = plt.subplots(figsize=(8, 5))

    # Define the colors
    colors = ['#FF9933', '#FFFFFF', '#138808']

    # Draw the rectangles (stripes)
    for i, color in enumerate(colors):
        rect = patches.Rectangle((0, i * 1/3), 1, 1/3, linewidth=0, edgecolor='none', facecolor=color)
        ax.add_patch(rect)

    # Draw the Ashoka Chakra (wheel) in the center
    circle = patches.Circle((0.5, 0.5), 0.1, color='navy', fill=False, linewidth=2)
    ax.add_patch(circle)

    # Draw the spokes of the Ashoka Chakra
    num_spokes = 24
    for i in range(num_spokes):
        angle = i * (360 / num_spokes)
        x = 0.5 + 0.1 * np.cos(np.radians(angle))
        y = 0.5 + 0.1 * np.sin(np.radians(angle))
        ax.plot([0.5, x], [0.5, y], color='navy', linewidth=1)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.show()

draw_indian_flag()
