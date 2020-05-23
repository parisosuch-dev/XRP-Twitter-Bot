"""
/ graph.py
-----------------------------
/ author: paris osuch
/ website: parisosuch.com
/ git-hub repo: https://github.com/parisosuch-dev/
-----------------------------
/ about: utilizes matplotlib and the DataHandle class from datahandler.py
to create a 7d graph of market price and delete graph
-----------------------------
/ Graph() class
/ / graphCreate() - method
/ / graphDel() - method
"""
# / Imports

from matplotlib import pyplot as plot
from datahandler import DataHandle
import os

# / Graph Class
class Graph:
    # / constructor
    def __init__(self, filepath: str, imagepath: str, MARKETKEY):
        self.domain = 7
        self.frequency = 24
        self.xAxis = []
        self.yAxis =[]
        self.xLabel = 'date (month/day:hour)'
        self.xLabel = 'price'
        self.filepath = filepath
        self.imagepath = imagepath
        self.key = MARKETKEY
        self.dh = DataHandle(self.key)
    # / make graph from all of the data
    def graphCreate(self):
        # / append data to xAxis and yAxis
        for i in range(self.domain*self.frequency):
            price = self.dh.dataFindRow(self.filepath, "price", i)
            date = self.dh.dataFindRow(self.filepath, "currentdate", i)
            hour = self.dh.dataFindRow(self.filepath, 'hour', i)
            t = date + ':' + hour + 'hr'
            self.xAxis.append(price)
            self.yAxis.append(t)
        plot.plot(self.xAxis, self.yAxis)
        plot.xlabel(self.xLabel)
        plot.ylabel((self.yAxis))
        plot.savefig(self.imagepath)
    # / remove image from path
    def delGraph(self):
        if os.path.exists(self.imagepath):
            os.remove(self.imagepath)
        else:
            print('> image does not exist on path')


