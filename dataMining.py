# -*- coding: utf-8 -*-
import dataPrep
import GraphingCharts
import bingToCoordinates
import addLocationToDb
import MappingCountry
import MappingWorld
import polarityWITHdate
import settings


try:
    dataPrep.clean(settings.FILENAME_A, settings.FILENAME_B,
                   settings.DATABASEPATH, settings.DBTABLENAME)
except:
    print("Error Occured")
    print("Might be due to the already processed DB")
    pass
GraphingCharts.graphIt(settings.DATABASEPATH, settings.RESULTSAVE_PATH,
                       settings.FILENAME_A, settings.FILENAME_B, settings.DBTABLENAME, isNoRetweet=settings.WITHOUTRT)
bingToCoordinates.findCoordinates(settings.BING_KEY, settings.RESULTSAVE_PATH,
                                  settings.DATABASEPATH, TOP_LIMIT=settings.TOPPLACELIMIT, isNoRetweet=settings.WITHOUTRT)
addLocationToDb.addCorrdinates(settings.DATABASEPATH, settings.RESULTSAVE_PATH,
                               settings.FILENAME_A, settings.FILENAME_B, settings.DBTABLENAME, isNoRetweet=settings.WITHOUTRT)
MappingCountry.mapCountry(
    settings.DATABASEPATH, settings.RESULTSAVE_PATH, settings.DBTABLENAME, isNoRetweet=settings.WITHOUTRT)
MappingWorld.mapWorld(settings.DATABASEPATH,
                      settings.RESULTSAVE_PATH, settings.DBTABLENAME, isNoRetweet=settings.WITHOUTRT)
polarityWITHdate.featureWdate(
    settings.DATABASEPATH, settings.RESULTSAVE_PATH, settings.DBTABLENAME, ["polarity", "subjectivity"])
print("                                __φ(．．)")
print("Hope you gather some new stuff from data")
print("                        --Saksham Sharma")
