# -*- coding: utf8


import matplotlib.pyplot as plt
import requests
import tqdm


def init_matplotlib():
    plt.rcParams['figure.figsize'] = (16, 10)

    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['axes.spines.bottom'] = True
    plt.rcParams['axes.spines.left'] = True
    plt.rcParams['axes.titlesize'] = 20
    plt.rcParams['axes.ymargin'] = 0.1

    plt.rcParams['font.family'] = 'serif'

    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = 'lightgrey'
    plt.rcParams['grid.linewidth'] = .1

    plt.rcParams['xtick.labelsize'] = 20
    plt.rcParams['xtick.bottom'] = True
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['xtick.major.size'] = 5
    plt.rcParams['xtick.major.width'] = 1
    plt.rcParams['xtick.minor.size'] = 3
    plt.rcParams['xtick.minor.width'] = .5
    plt.rcParams['xtick.minor.visible'] = True

    plt.rcParams['ytick.labelsize'] = 20
    plt.rcParams['ytick.left'] = True
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['ytick.major.size'] = 5
    plt.rcParams['ytick.major.width'] = 1
    plt.rcParams['ytick.minor.size'] = 3
    plt.rcParams['ytick.minor.width'] = .5
    plt.rcParams['ytick.minor.visible'] = True

    plt.rcParams['legend.fontsize'] = 20

    plt.rcParams['lines.linewidth'] = 4
    plt.rcParams['lines.markersize'] = 10
    plt.rcParams['lines.markeredgecolor'] = 'black'
    plt.rcParams['patch.edgecolor'] = 'black'

    plt.style.use('tableau-colorblind10')


def download(url, outfpath):
    response = requests.get(url, stream=True)
    
    with open(outfpath, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
