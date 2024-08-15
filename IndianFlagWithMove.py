import matplotlib.pyplot as plt
import matplotlib.patches as pactches
import numpy as np
import io
from PIL import Image
def draw_indian_flag(angle):
    fig,ax = plt.subplots(figsize=(8,5)) #8*5 inches
    #define color
    colors = ['#FF9933', '#FFFFFF', '#138808']

    #draw the reacangles (stripes)

    for i,color in enumerate(colors):
        rect = pactches.Rectangle((0, i*1/3),1,1/3 , linewidth=0,edgecolor='none',facecolor=color)
        ax.add_patch(rect)

    #drwa ashok chakra
    circle = pactches.Circle((0.5, 0.5), 0.1, color='navy', fill=False, linewidth=2)
    ax.add_patch(circle)

    #draw the spokes of the ashok chakra
    num_spokes = 24
    for i in range(num_spokes):
        spoke_angle = angle + i * (360 / num_spokes)
        x = 0.5 + 0.1 * np.cos(np.radians(spoke_angle))
        y = 0.5 + 0.1 * np.sin(np.radians(spoke_angle))
        ax.plot([0.5, x], [0.5, y], color='navy', linewidth=1)

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal')
    ax.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf,format='png',bbox_inches='tight',pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)


def create_gif(filename,num_frames= 30):
    images=[]
    for i in range(num_frames):
        angle = i*(360 / num_frames)
        frame = draw_indian_flag(angle)
        images.append(frame)

    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)


create_gif('indian_flag.gif')