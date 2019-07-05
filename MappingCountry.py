# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import matplotlib.image as mpimg
import numpy as np
import os


def save_fig(fig_id, IMAGE_PATH, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGE_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


def mapCountry(DATASET_PATH, IMAGE_PATH, tablename, COUNTRY_IMG_PATH='india-pakistan-map.jpg', MAP_EXTENT=[60.6, 97.45, 7.9, 37.6], isNoRetweet=False):
    print("***** Request to process maps recived *****")
    print("¥[*.*]¥ -- > And I ain't gonna do a shit ;-)")
    print("¥[*.*]¥ -- > Just Kidding XD , this is the best way to flex my creative muscles.")
    print("¥[*.*]¥ -- > Get WORKING MY FELLOW MATES")
    print("~(o_o)~  ~(o_o)~  ~(o_o)~")
    print("***** All in one Unicode(Unison) say  1 *****")
    print("")
    print("")

    if isNoRetweet:
        DATASET_PATH = DATASET_PATH + "/withoutRT"
        IMAGE_PATH = IMAGE_PATH + "/withoutRT"

    cnx = sqlite3.connect(DATASET_PATH + '/combined_user_location.db')
    df = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx)
    df.drop("index", axis=1, inplace=True)
    if isNoRetweet:
        df[df.isRT != 1]
    df = df[df.subjectivity != 0]
    df = df[df.polarity != 0]

    # df=df[(df.lat <= 40) & (6 <= df.lat)]
    # df=df[(df.long <= 100) & (25 <= df.long)]

    df.plot(kind="scatter", x="long", y="lat", alpha=0.4,
            label="subjectivity", s=df["subjectivity"] * 1000, figsize=(30, 30),
            c="polarity", cmap=plt.get_cmap("jet_r"), colorbar=False,
            )
    country_img = mpimg.imread(COUNTRY_IMG_PATH)

    plt.ylabel("Latitude", fontsize=45)
    plt.xlabel("Longitude", fontsize=45)
    plt.imshow(country_img, alpha=0.6,
               cmap=plt.get_cmap("jet_r"), extent=MAP_EXTENT)

    polar = df["polarity"]
    tick_values = np.linspace(polar.min(), polar.max(), 6)
    cbar = plt.colorbar()
    cbar.ax.set_yticklabels(["%d" % v for v in tick_values], fontsize=40)
    cbar.set_label('Polarity', fontsize=55)
    plt.legend()
    save_fig("polarity_map_1", IMAGE_PATH)

    df.plot(kind="scatter", x="long", y="lat", alpha=0.4,
            label="subjectivity", s=df["subjectivity"] * 5000, figsize=(30, 30),
            c="polarity", cmap=plt.get_cmap("jet_r"), colorbar=False,
            )
    plt.ylabel("Latitude", fontsize=45)
    plt.xlabel("Longitude", fontsize=45)
    plt.imshow(country_img, alpha=0.6,
               cmap=plt.get_cmap("jet_r"), extent=MAP_EXTENT)

    polar = df["polarity"]
    tick_values = np.linspace(polar.min(), polar.max(), 6)
    cbar = plt.colorbar()
    cbar.ax.set_yticklabels(["%d" % v for v in tick_values], fontsize=40)
    cbar.set_label('Polarity', fontsize=55)
    plt.legend()
    save_fig("polarity_map_2", IMAGE_PATH)

    df.plot(kind="scatter", x="long", y="lat", alpha=0.4,
            label="subjectivity", s=df["subjectivity"] * 10000, figsize=(30, 30),
            c="polarity", cmap=plt.get_cmap("jet_r"), colorbar=False,
            )
    plt.ylabel("Latitude", fontsize=45)
    plt.xlabel("Longitude", fontsize=45)
    plt.imshow(country_img, alpha=0.6,
               cmap=plt.get_cmap("jet_r"), extent=MAP_EXTENT)

    polar = df["polarity"]
    tick_values = np.linspace(polar.min(), polar.max(), 6)
    cbar = plt.colorbar()
    cbar.ax.set_yticklabels(["%d" % v for v in tick_values], fontsize=40)
    cbar.set_label('Polarity', fontsize=55)
    plt.legend()
    save_fig("polarity_map_3", IMAGE_PATH)

    df.plot(kind="scatter", x="long", y="lat", alpha=0.4,
            label="subjectivity", s=df["subjectivity"] * 50000, figsize=(30, 30),
            c="polarity", cmap=plt.get_cmap("jet_r"), colorbar=False,
            )
    plt.ylabel("Latitude", fontsize=45)
    plt.xlabel("Longitude", fontsize=45)
    plt.imshow(country_img, alpha=0.6,
               cmap=plt.get_cmap("jet_r"), extent=MAP_EXTENT)

    polar = df["polarity"]
    tick_values = np.linspace(polar.min(), polar.max(), 6)
    cbar = plt.colorbar()
    cbar.ax.set_yticklabels(["%d" % v for v in tick_values], fontsize=40)
    cbar.set_label('Polarity', fontsize=55)
    plt.legend()
    save_fig("polarity_map_4", IMAGE_PATH)
    print("")
    print("¥[*.*]¥ ---> Tripping HOT country map is prepared")
    print("")
    print("")
