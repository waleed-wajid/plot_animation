#!/home/waleed/anaconda3/bin/python.exe
import os 
import sys

from celluloid import Camera
import pandas as pd
import numpy as np
import matplotlib 
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

proj_dir = os.path.dirname(os.getcwd())
print(proj_dir)
sys.path.append(proj_dir)

from src.plotting import plot_sample

if __name__ == '__main__':
    data = pd.read_csv(os.path.join(proj_dir, 'data', 'raw', '2021-05-01_Scotss-SL-data.csv'))
    
    fig, ax = plt.subplots(figsize=(16,6))
    camera = Camera(fig)

    for i in range(len(data)):
        plot_sample(ax, data.iloc[i])
        plt.legend([f'Q = {data.iloc[i].Q_MI:.2f} m3/s'])
        camera.snap()
    #     sleep(1)
    animation = camera.animate()
    animation.save(os.path.join(proj_dir, 'reports', 'ws_elev.gif'), writer = 'imagemagick')
