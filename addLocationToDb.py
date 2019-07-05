# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


def addCorrdinates(DATASET_PATH, RESULTSET_PATH, FILENAME_A, FILENAME_B, tablename, isNoRetweet=False):
    print("***** Adding co-ordinates to your DataFrame *****")
    print("¥[*.*]¥ -- > Meh #-o, worse type of operation. It's just copying and pasting")
    print("¥[*.*]¥ -- > Gotta do this cause you are too stupid and cant do this by yourself")
    print("")
    print("")

    cnx = sqlite3.connect(DATASET_PATH + '/' + FILENAME_A +
                          '_' + FILENAME_B + '-REFINEDcombined.db')
    df = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx)
    df.drop("index", axis=1, inplace=True)

    df = df[df.subjectivity != 0]
    df = df[df.polarity != 0]

    if isNoRetweet:
        df = df[df.isRT != 1]
        DATASET_PATH = DATASET_PATH + "/withoutRT"

    user_location = pd.read_csv(
        DATASET_PATH + '/user_location_coordinates.csv')
    user_location.drop('Unnamed: 0', axis=1, inplace=True)

    bigdata = pd.DataFrame()
    for i in user_location.place:
        df_sorted = df[df.user_location == i]
        lat = user_location.lat[user_location.place == i]
        df_sorted['lat'] = float(lat)
        longti = user_location.long[user_location.place == i]
        df_sorted['long'] = float(longti)
        typegg_val = user_location.typegg[user_location.place == i]
        df_sorted['typegg'] = str(typegg_val)
        bigdata = bigdata.append(df_sorted, ignore_index=True)

    RTDB = sqlite3.connect(DATASET_PATH + "/combined_user_location.db")
    bigdata.to_sql(tablename, RTDB)
    print("")
    print("¥[*.*]¥ -- > Your Stupid DataFrame is ready")
    print("¥[*.*]¥ -- > And Eat shit you stupid Human *<:o")
    print("¥[*.*]¥ -- > ~,~")
    print("")
    print("")
