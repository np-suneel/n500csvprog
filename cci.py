import pandas as pd
import numpy as np
import talib as tb
import glob
import os
import time
import re

folder_path = 'C:\\Users\\amdge\\Desktop\\origcsvs'
print("Calculating...")



for filename in glob.glob(os.path.join(folder_path, '*.csv')):
    start = time.time()
    x = re.match(r"(C:\\Users\\amdge\\Desktop\\origcsvs)\\(.*).csv", filename)
    datafile = filename
    data = pd.read_csv(datafile, index_col='Date')
    data.index = pd.to_datetime(data.index)

    #SMA, EMA

    smavol20 = data['Volume'].rolling(20).mean()
    ema20 = tb.EMA(np.asarray(data['Close']), timeperiod=20)
    ema50 = tb.EMA(np.asarray(data['Close']), timeperiod=50)
    ema100 = tb.EMA(np.asarray(data['Close']), timeperiod=100)
    ema200 = tb.EMA(np.asarray(data['Close']), timeperiod=200)

    # CCI

    cci10 = tb.CCI(np.asarray(data['High']), np.asarray(data['Low']), np.asarray(data['Close']), timeperiod=10)
    cci20 = tb.CCI(np.asarray(data['High']), np.asarray(data['Low']), np.asarray(data['Close']), timeperiod=20)
    cci30 = tb.CCI(np.asarray(data['High']), np.asarray(data['Low']), np.asarray(data['Close']), timeperiod=30)

    # STOCH

    slowk, slowd = tb.STOCH(np.asarray(data['High']), np.asarray(data['Low']), np.asarray(data['Close']), fastk_period=14,
                            slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

    #MEDPRICE

    medpr = tb.MEDPRICE(np.asarray(data['High']), np.asarray(data['Low']))

    #ADX

    adxpr = tb.ADX(np.asarray(data['High']), np.asarray(data['Low']), np.asarray(data['Close']), timeperiod=14)

    data['MEDPRICE'] = np.round(medpr, decimals=2)
    data['ADX'] = np.round(adxpr, decimals=2)
    data['CCI10'] = np.round(cci10, decimals=2)
    data['CCI20'] = np.round(cci20, decimals=2)
    data['CCI30'] = np.round(cci30, decimals=2)
    data['STOCHK'] = np.round(slowk, decimals=2)
    data['STOCHD'] = np.round(slowd, decimals=2)
    data['EMA20'] = np.round(ema20, decimals=2)
    data['EMA50'] = np.round(ema50, decimals=2)
    data['EMA100'] = np.round(ema100, decimals=2)
    data['EMA200'] = np.round(ema200, decimals=2)
    data['SMA20Vol'] = np.round(smavol20, decimals=2)
    data.to_csv("C:\\Users\\amdge\\Desktop\\CCIstockwise\\" + x.group(2) + ".csv")
    end = time.time()
    print("Calculated indicators for " + x.group(2) + " stock. Execution time: " + str(round((end - start), 2)) + " seconds")
print("Task completed.")
