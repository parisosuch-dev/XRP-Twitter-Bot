"""
/ datahandler.py
-----------------------------
/ author: paris osuch
/ website: parisosuch.com
/ git-hub repo: https://github.com/parisosuch-dev/
-----------------------------
/ about: utilizes json, requests, os, pandas, and TimeKeep class from timekeep.py
to get data from nomics api to be stored and handled for later processes in graph.py
-----------------------------
/ dataHandle class
/ / market methods:
/ / / marketData() -> method
/ / / marketPrice() -> method
/ / / marketVol() -> method
/ / / marketCap() -> method
/ / data methods:
/ / / dataWrite() -> method
/ / / dataFind() -> method
/ / / dataDel() -> method
-----------------------------
/ csv data structure
    -------------------------------------------------------------------
    |--------|- index -|- day -  |- hour - |  - date -    | - price - |
    |row1    |   0     |    0    |   1     |   May 15     |     x     |
    |row2    |   1     |    0    |   2     |   May 15     |     x     |
    |row3    |   2     |    0    |   3     |   May 15     |     x     |
    -------------------------------------------------------------------
"""
# / Imports
import json
import requests
import os
from timekeep import TimeKeep
import pandas as pd

# / Data Handle Object
class DataHandle:
    # / constructor
    def __init__(self, marketkey):
        self.key = marketkey
        self.url = "https://api.nomics.com/v1/currencies/ticker?key={self.key}&ids=XRP&interval=1d,30d&convert=USD"
        self.time = TimeKeep()
        self.timeData = self.time.timeData()
        self.weekday = self.timeData[3]
        self.hour = self.timeData[2]
        self.date = self.time.currentDate()

    # / get market data and turn put it in a dictionary
    def marketData(self):
        # / / get response using requests
        r = requests.get(self.url)
        # / / get json from request
        jsonData = json.load(r)

        return jsonData
    # / get market price
    def marketPrice(self):
        # / / get json data
        data = self.marketData()
        # / / get price
        price = data[0]["price"]
        # / / float and round price
        price = float(price)
        price = round(price, 4)

        return price
    # / get market volume
    def marketVol(self):
        # / / get json data
        data = self.marketData()
        # / / get volume on the day and float
        vol = data[0]["1d"]["volume"]
        vol = float(vol)

        return vol
    # / get market cap
    def marketCap(self):
        # / / get json data
        data = self.marketData()
        # / / get market cap from json data
        cap = data[0]["market_cap"]
        cap = float(cap)

    # / write data
    def dataWrite(self, filepath: str):
        # / / create dictionary attribute using DataHandle.price() and self.timeData()
        price = self.marketPrice()

        data = {
            "currentdate":self.date,
            "weekday":self.weekday,
            "hour":self.hour,
            "price":price
        }
        # / / create data frame: read csv file using Pandas.read_csv(file) method
        df = pd.read_csv(filepath)
        # / / append data, the dictionary attribute
        df = df.append(data, ignore_index = True)
        # // write to csv file
        df.to_csv(filepath)

    # / find data row
    def dataFindRow(self, filepath: str, colname: str, row: int):
        df = pd.read_csv(filepath)
        # / / find data
        data = df.iloc[colname][row]

        return data

    # / delete data
    def dataDel(self, filepath: str, index: int):
        # / / read csv file and create data frame
        df = pd.read_csv(filepath)
        # / / drop row at index
        df = df.drop(index)
        # / / write to csv file
        df.to_csv(filepath)


    # / data length
    def dataLen(self, filepath: str):
        # / create a data frame from filepath
        df = pd.read_csv(filepath)
        # / get dimensions
        dimensions = df.shape
        # / return the length of the file
        return (dimensions[0])
