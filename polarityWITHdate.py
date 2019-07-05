import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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


def featureWdate(DBPATH, SAVEPATH, tablename,  features, timeperiod='5T', axisInterval=4):

    # Importing the database
    cnx = sqlite3.connect(DBPATH)
    df = pd.read_sql_query("SELECT * FROM %s" % tablename, cnx)

    # Seperating Date and Time
    df['datetime'] = pd.to_datetime(df['tweet_created'])
    df['time'] = df['datetime'].dt.time

    # Taking mean of the values of the feature at specified time-period
    df_reperiod = df.resample(timeperiod, on='datetime').mean()

    df.set_index('time')

    fig, ax = plt.subplots()
    for feature in features:
        ax.plot(df_reperiod.loc[:,
                                feature], marker='o', linestyle='-', label=feature)

    ax.set_ylabel('Feature', fontsize=15)
    ax.set_xlabel('Date - Time', fontsize=15)
    # Set x-axis major ticks to weekly interval, on Mondays
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=axisInterval))
    # Format x-tick labels as 3-letter month name and day number
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
    plt.legend(fontsize=15)
    save_fig("Feature-with-Date", SAVE_PATH)
