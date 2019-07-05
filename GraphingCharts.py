# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import warnings
from pandas.plotting import scatter_matrix
import os


def save_fig(fig_id, IMAGES_PATH, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension,
                dpi=resolution, bbox_inches='tight')
    plt.clf()
    print("Done")
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("")


# Plot Customization
font = {'weight': 'bold',
        'size': 22,
        'family': 'serif'}
plt.rc('font', **font)

# Uncomment this if you want your data to exclude tweets which are retweeted
# df = df[df.isRT != 1]


def graphIt(DBPATH, SAVE_PATH, country1_DB_name, country2_DB_name, tablename, TOP=21, doComprehensive=True, doHash=True, doAndroid=True, doIphone=True, doUserPlace=True, doTweetPlace=True, attributes=["polarity", "subjectivity", "user_followers", "friends_count", "no_tweet_user"], country1_name="IND", country2_name="PAK", isNoRetweet=False):
    print("***** Starting Your Graph Journey *****")
    print("¥[*.*]¥ ---> Minning some awesome graphs for my User")
    print("¥[*.*]¥ ---> All Robots Assemble")
    print("~(o_o)~  ~(o_o)~  ~(o_o)~")
    print("***** All in one Unicode(Unison) say  1 *****")
    print("")
    print("")

    cnx = sqlite3.connect(DBPATH + '/' + country1_DB_name +
                          '_' + country2_DB_name + '-REFINEDcombined.db')
    df = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx)
    df.drop("index", axis=1, inplace=True)
    df = df[df.subjectivity != 0]
    df = df[df.polarity != 0]

    if isNoRetweet:
        df = df[df.isRT != 1]
        SAVE_PATH = SAVE_PATH + "/withoutRT"

    os.makedirs(SAVE_PATH, exist_ok=True)

    if doComprehensive:
        df.hist(bins=50, figsize=(20, 15))
        save_fig("Comprehensive_bargraph", SAVE_PATH)
    if doHash:
        df_hash = df.hashtags.value_counts()
        df_hash.to_csv(SAVE_PATH + "/hashtags.csv", header=True)
        df_hash_top = df_hash[1:TOP]
        df_hash_top.plot(kind="bar", figsize=(40, 30))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            save_fig("Top_Hashtags", SAVE_PATH)

    if doAndroid:
        df_Android = df[df.origin_source == "Twitter for Android"]
        df_Android.hist(bins=50, figsize=(20, 15))
        df_Android.plot(kind="scatter", x="polarity",
                        y="subjectivity", figsize=(30, 20))
        save_fig("PolarityVSSubjectivityANDROID", SAVE_PATH)
        df_Ades = df_Android.describe()
        df_Ades = df_Ades.iloc[[1, 2], :]
        df_Ades.to_csv(SAVE_PATH + "/android.csv", header=True)

    if doIphone:
        df_iPhone = df[df.origin_source == "Twitter for iPhone"]
        df_ides = df_iPhone.describe()
        df_ides = df_ides.iloc[[1, 2], :]
        df_ides.to_csv(SAVE_PATH + "/iPhone.csv", header=True)
        df_iPhone.plot(kind="scatter", x="polarity",
                       y="subjectivity", alpha=1, figsize=(30, 20))
        save_fig("PolarityVSSubjectivityIPHONE", SAVE_PATH)

    if doAndroid & doIphone:
        df_ides = df_ides.T
        df_Ades = df_Ades.T
        df_ides = df_ides.loc[['polarity', 'subjectivity']]
        df_Ades = df_Ades.loc[['polarity', 'subjectivity']]

        w = 0.1
        df_Ades['mean'].plot(kind='bar', position=1, width=w,
                             color='#f39c12', align='center')
        df_ides['mean'].plot(kind='bar', position=0, width=w,
                             color='#3498db', align='center')
        plt.legend(['Android', 'iPhone'])
        save_fig("iphone_with_android", SAVE_PATH)


# sbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    if doUserPlace:
        user_location = df.user_location.value_counts().to_frame()
        user_location.to_csv(SAVE_PATH + "/user_location.csv", header=True)
        user_location_top = user_location[1:TOP]
        user_location_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_user_places", SAVE_PATH)

    if doTweetPlace:
        place_name = df.place_name.value_counts().to_frame()
        place_name.to_csv(SAVE_PATH + "/place_name.csv", header=True)
        place_name_top = place_name[1:TOP]
        place_name_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_tweet_places", SAVE_PATH)

    if country1_DB_name.strip():
        cnx1 = sqlite3.connect(DBPATH + '/Cleaned/' + country1_DB_name + '.db')
        df_country1 = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx1)
        df_country1.drop("index", axis=1, inplace=True)
        df_country1 = df_country1[df_country1.subjectivity != 0]
        df_country1 = df_country1[df_country1.polarity != 0]
        scatter_matrix(df_country1[attributes], figsize=(40, 40))
        save_fig(country1_name + "AttributesScatter", SAVE_PATH)
        df_country1.plot(kind="scatter", x="polarity",
                         y="subjectivity", figsize=(30, 20))
        save_fig('subVSpolarity' + country1_name, SAVE_PATH)
        df_CN1hash = df_country1.hashtags.value_counts()
        df_CN1hash.to_csv(SAVE_PATH + "/" + country1_name +
                          "Hastags.csv", header=True)
        df_CN1hash_top = df_CN1hash[1:TOP]
        df_CN1hash_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country1_name + "_Hastags", SAVE_PATH)
        df_CN1_loc = df_country1.user_location.value_counts()
        df_CN1_loc.to_csv(SAVE_PATH + "/" + country1_name +
                          "UserLocations.csv", header=True)
        df_CN1_loc_top = df_CN1_loc[0:TOP]
        df_CN1_loc_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country1_name + "_user_Locations", SAVE_PATH)
        df_CN1_locT = df_country1.place_name.value_counts()
        df_CN1_locT.to_csv(SAVE_PATH + "/" +
                           country1_name + "TweetLocations.csv", header=True)
        df_CN1_locT_topT = df_CN1_locT[1:TOP]
        df_CN1_locT_topT.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country1_name + "_tweet_Locations", SAVE_PATH)

    if country2_DB_name.strip():
        cnx2 = sqlite3.connect(DBPATH + '/Cleaned/' + country2_DB_name + '.db')
        df_country2 = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx2)
        df_country2.drop("index", axis=1, inplace=True)
        df_country2 = df_country2[df_country2.subjectivity != 0]
        df_country2 = df_country2[df_country2.polarity != 0]
        scatter_matrix(df_country2[attributes], figsize=(40, 40))
        save_fig(country2_name + "AttributesScatter", SAVE_PATH)
        df_country2.plot(kind="scatter", x="polarity",
                         y="subjectivity", figsize=(30, 20))
        save_fig('subVSpolarity' + country2_name, SAVE_PATH)
        df_CN2des = df_country2.hashtags.value_counts()
        df_CN2des.to_csv(SAVE_PATH + "/" + country2_name +
                         "_hashtags.csv", header=True)
        df_CN2des_top = df_CN2des[1:TOP]
        df_CN2des_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country2_name + "_Hashtags", SAVE_PATH)
        df_CN2_loc = df_country2.user_location.value_counts()
        df_CN2_loc.to_csv(SAVE_PATH + "/" + country2_name +
                          "UserLocations.csv", header=True)
        df_CN2_loc_top = df_CN2_loc[0:TOP]
        df_CN2_loc_top.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country2_name + "_user_Locations", SAVE_PATH)
        df_CN2_locT = df_country2.user_location.value_counts()
        df_CN2_locT.to_csv(SAVE_PATH + "/" +
                           country2_name + "TweetLocations.csv", header=True)
        df_CN2_loc_topT = df_CN2_locT[0:TOP]
        df_CN2_loc_topT.plot(kind="bar", figsize=(40, 30))
        save_fig("Top_" + country2_name + "_tweet_Locations", SAVE_PATH)
        print("")
        print("***** All procces, report success *****")
        print("¥[*.*]¥ ---> AHH! Easy Peasy Lemon Squeeze")
        print("¥[*.*]¥ ---> Hope You like it and give me more to churn next time")
        print("")
        print("")
