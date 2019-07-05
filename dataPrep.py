# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import sqlite3
import threading


def load_tweet_data(filename, data_path, tableName):
    db_path = sqlite3.connect(data_path + "/"+filename + ".db")
    return pd.read_sql_query("SELECT * FROM %s" % tableName, db_path)


def load_tweet_data_merge(name, DATA_PATH, tableName):
    db_path = sqlite3.connect(DATA_PATH + "/Cleaned/" + name + ".db")
    DDFF = pd.read_sql_query("SELECT * FROM %s" % tableName, db_path)
    DDFF.drop("index", axis=1, inplace=True)
    print(name + ".db", " loaded")
    return DDFF


def cleanMethod(FILENAME, DATA_PATH, tableName):
    print("DF '%s' Loading" % FILENAME)
    os.makedirs(DATA_PATH, exist_ok=True)
    df = load_tweet_data(FILENAME, DATA_PATH, tableName)
    print("DF %s Loaded" % FILENAME)
    print("cleaning")
    df.drop("entities", axis=1, inplace=True)
    df.drop("user_created", axis=1, inplace=True)
    df.drop("id_str", axis=1, inplace=True)
    os.makedirs(DATA_PATH + "/Cleaned/", exist_ok=True)
    cleanedDB = sqlite3.connect(DATA_PATH + "/Cleaned/" + FILENAME + ".db")
    df.to_sql(tableName, cleanedDB)
    # print("Later :")
    # print(df.info())


def clean(filename_a, filename_b, data_path, tableName):
    print("")
    print("Welcome To Data Gang!")
    print("(((￣(￣(￣▽￣)￣)￣)))")
    print("")
    print("Author:Saksham Sharma   ＼(≧▽≦)／")
    print("Lets Begin")
    print("ε=ε=ε=ε=┌(;￣▽￣)┘")
    print("")
    print("*****Starting Your Data Journey*****")
    print(" __")
    print("/--|__")
    print("|@   @\\")
    print("")
    print("")
    print("Starting Data Cleaning and Preperation")
    t1 = threading.Thread(target=cleanMethod, name='t1',
                          args=(filename_a, data_path, tableName))
    t1.start()
    if filename_b.strip():
        t2 = threading.Thread(target=cleanMethod, name='t2',
                              args=(filename_b, data_path, tableName))
        t2.start()
        t2.join()
    t1.join()
    df1 = load_tweet_data_merge(filename_a, data_path, tableName)
    if filename_b.strip():
        df2 = load_tweet_data_merge(filename_b, data_path, tableName)
        print("Combining")
        df_row_reindex = pd.concat([df1, df2], ignore_index=True)
    else:
        df_row_reindex = df1

    print("Saving")
    RTDB = sqlite3.connect(data_path + "/" + filename_a +
                           "_" + filename_b + "-REFINEDcombined.db")
    df_row_reindex.to_sql(tableName, RTDB)
    print("")
    print("¥[*.*]¥ -- > Saved :-)")
    print("")
    print("")
