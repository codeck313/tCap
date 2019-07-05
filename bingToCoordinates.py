# -*- coding: utf-8 -*-
from geopy.geocoders import Bing
import pandas as pd
import time
from geopy.exc import GeopyError
import os
# Remove Key


def removeRow(df, name):
    print("Removing", name)
    df = df.set_index("Unnamed: 0")
    if (name in df.index):
        df.drop(name, axis=0, inplace=True)
    df.reset_index(inplace=True)
    return df


def findCoordinates(KEY, DATASET_PATH, SAVELOCATION_PATH, TOP_LIMIT=120, isNoRetweet=False):
    print("*****Outsourcing Work To Get Location's Coordinates*****")
    print("¥[*.*]¥ -- > Gonna Hire A Bangladeshi Guy")
    print("¥[*.*]¥ -- > #metooLAZY")
    print("¥[*.*]¥ -- > Also Trump don't deport my guy !!PLEASE!!")
    print("")
    print("")
    if isNoRetweet:
        DATASET_PATH = DATASET_PATH + "/withoutRT"
        SAVELOCATION_PATH = SAVELOCATION_PATH + "/withoutRT"
    os.makedirs(SAVELOCATION_PATH, exist_ok=True)
    geolocator = Bing(api_key=KEY)
    user_location = pd.read_csv(DATASET_PATH + '/user_location.csv')
    user_location = removeRow(user_location, "Earth")
    user_location = removeRow(user_location, "Worldwide")
    user_location = removeRow(user_location, "Global")
    user_location = removeRow(user_location, "Planet Earth")
    user_location = removeRow(user_location, "Everywhere")
    user_location = removeRow(user_location, ".")
    user_location = removeRow(user_location, "she/her")
    user_location = removeRow(user_location, "In Hearts of")
    user_location = removeRow(user_location, "Mars")
    user_location = removeRow(user_location, "Hogwarts")
    user_location = removeRow(user_location, "worldwide")
    user_location = removeRow(user_location, "Worldwide")
    df = pd.DataFrame(columns=['place', 'lat', 'long', 'type'])
    retryCount = 0
    for i in user_location.iloc[0:TOP_LIMIT, 0]:
        while True:
            try:
                location = geolocator.geocode(i)
                print((i.encode("utf-8"), location.latitude,
                       location.longitude, location.raw['entityType']))
                df = df.append({'place': i, 'lat': location.latitude, 'long': location.longitude,
                                'typegg': location.raw['entityType']}, ignore_index=True)
                time.sleep(0.5)
                retryCount = 0
                break
            except:
                retryCount += 1
                if retryCount > 20:
                    print("Stuck on Error for too long")
                    print("Exiting now")
                    retryCount = 0
                    break
                print("---------------------ERROR----------------")
                continue
    print("")
    print("( ＾◡＾)っ ---> I am done sir,")
    print("")
    print("¥[*.*]¥ -- > Thank you Sayeed")
    print("")
    print("( ＾◡＾)っ ---> Dhonno-baad")
    print("")
    print("")
    df.to_csv(SAVELOCATION_PATH + "/user_location_coordinates.csv")
